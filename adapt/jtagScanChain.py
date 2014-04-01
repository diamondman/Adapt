from jtagDeviceDescription import JTAGDeviceDescription

import time
import math
from bitarray import bitarray

def gc(addr):
    return (addr>>1)^addr

def pstatus(resflags):
    print resflags.__repr__()
    if len(resflags)>1:
        resflags = resflags[0]
    print "STATUS: "+("" if (ord(resflags)&0b11000011==1) else "INVALID_STATUS ")+\
        ("ISCDIS " if ord(resflags)&32 else "")+("ISCEN " if ord(resflags)&16 else "")+\
        ("SECURE " if ord(resflags)&8 else "")+("DONE " if ord(resflags)&4 else "")

def build_byte_align_buff(bit_count):
    bitmod = bit_count%8
    if bitmod == 0: 
        rdiff = bitarray()
        print "NO BUFF NEEDED", rdiff
    else:
        rdiff = bitarray(8-bitmod)
        rdiff.setall(False)
    return rdiff

class JTAGStateMachine(object):
    states = {
        "_PRE5": ["_PRE5", "_PRE4"],
        "_PRE4": ["_PRE5", "_PRE3"],
        "_PRE3": ["_PRE5", "_PRE2"],
        "_PRE2": ["_PRE5", "_PRE1"],
        "_PRE1": ["_PRE5", "TLR"],
        "TLR": ["RTI", "TLR"], 
        "RTI": ["RTI", "DRSCAN"], 
        "DRSCAN": ["CAPTUREDR", "IRSCAN"], 
        "CAPTUREDR": ["SHIFTDR","EXIT1DR"], 
        "SHIFTDR": ["SHIFTDR","EXIT1DR"], 
        "EXIT1DR": ["PAUSEDR","UPDATEDR"], 
        "PAUSEDR": ["PAUSEDR","EXIT2DR"], 
        "EXIT2DR": ["SHIFTDR","UPDATEDR"], 
        "UPDATEDR": ["RTI","DRSCAN"], 
        "IRSCAN": ["CAPTUREIR","TLR"], 
        "CAPTUREIR": ["SHIFTIR","EXIT1IR"], 
        "SHIFTIR": ["SHIFTIR","EXIT1IR"], 
        "EXIT1IR": ["PAUSEIR","UPDATEIR"], 
        "PAUSEIR": ["PAUSEIR","EXIT2IR"], 
        "EXIT2IR": ["SHIFTIR","UPDATEIR"], 
        "UPDATEIR": ["RTI","DRSCAN"]
        }

    def __init__(self):
        self._statestr = "_PRE5"

    def transition_bit(self, bit):
        choice = self.states.get(self._statestr, None)
        if choice is not None:
            self._statestr = choice[bit]

    @property
    def state(self):
        return self._statestr

    @state.setter
    def state(self, value):
        if value in self.states:
            self._statestr = value
        else:
            raise ValueError("%s is not a valid state for this state machine"%value)

    @classmethod
    def find_shortest_path(cls, start, end, path=None):
        path = (path or []) + [start]
        if start == end:
            return path
        if not cls.states.has_key(start):
            return None
        shortest = None
        for node in cls.states[start]:
            if node not in path:
                newpath = cls.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
    
    @classmethod
    def get_steps_from_nodes_path(cls, path):
        steps = []
        last_node = path[0]
        for node in path[1:]:
            steps.append(cls.states.get(last_node).index(node))
            last_node = node
        return bitarray(steps)

    def calc_transition_to_state(self, newstate):
        if newstate not in self.states:
            raise ValueError("%s is not a valid state for this state machine"%newstate)

        path = self.find_shortest_path(self._statestr, newstate)
        if not path:
            raise ValueError("No path to the requested state.")
        res = self.get_steps_from_nodes_path(path)
        res.reverse()
        return res

    def __repr__(self):
        return "<%s (State: %s)>"%(self.__class__.__name__, self.state)

class JTAGDevice(object):
    def __init__(self, chain, idcode):
        #print "IDCODE", idcode.__repr__()
        if not isinstance(chain, JTAGScanChain):
            raise ValueError("JTAGDevice requires an instnace of JTAGScanChain")
        self._chain = chain

        if isinstance(idcode, int):
            self._id = idcode
        elif isinstance(idcode, str):
            if len(idcode)==4:
                self._id = (ord(idcode[0])<<24)|(ord(idcode[1])<<16)|\
                    (ord(idcode[2])<<8)|ord(idcode[3])
            else:
                raise ValueError("JTAGDevice idcode parameter must be an "
                                 "int or string of length 4. (%s)"%self._id)
        else:
            raise ValueError("JTAGDevice idcode parameter must be an int or "
                             "string of length 4. (Invalid Type: %s)"%type(idcode))

        self.desc = JTAGDeviceDescription.get_descriptor_for_idcode(self._id)

    def run_TAP_instruction(self, insname, readback=False, execute=True, extraruncycles=0):
        self._chain.transition_TAP("SHIFTIR")
        ins = self.desc._instructions[insname]
        res = self._chain.write_IR_bits(ins.tobytes(), 
                                        self.desc._instruction_length, 
                                        readback=readback)
        if execute:
            self._chain.run_TAP_idle(extraruncycles+1)
        if readback:
            return res

    def erase(self):
        if self._id != 0x16d4c093:
            print "This operation is only supported on the Xilinx XC2C256 for now."
            sys.exit(1)
        
        self._chain.jtagEnable()

        pstatus(self.run_TAP_instruction("ISC_ENABLE", readback=True, extraruncycles=8))
    
        pstatus(self.run_TAP_instruction("ISC_ERASE", readback=True, extraruncycles=8))

        pstatus(self.run_TAP_instruction("ISC_INIT", readback=True, extraruncycles=8))
        
        pstatus(self.run_TAP_instruction("ISC_INIT", readback=True, execute=False))
        self._chain.transition_TAP("UPDATEDR")
        self._chain.run_TAP_idle(8)

        pstatus(self.run_TAP_instruction("ISC_DISABLE", readback=True, extraruncycles=8))

        pstatus(self.run_TAP_instruction("BYPASS", readback=True))
        self._chain.transition_TAP("TLR")
        
        self._chain.jtagDisable()

    def program(self, data_array):
        if self._id != 0x16d4c093:
            print "This operation is only supported on the Xilinx XC2C256 for now."
            sys.exit(1)
        
        chain = self._chain
        con = chain._controller
        chain.jtagEnable()
        
        chain.transition_TAP("SHIFTIR")
        pstatus(con.writeTDIBits('\x68', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_ENABLE
        con.writeTMSBits('\x01', 8) #RUN
        time.sleep(0.01)
    
        for i,r in enumerate(data_array):
            addr = bitarray(bin(gc(i))[2:].zfill(7))
            addr.reverse()
    
            #print "\nLOADING(%s:%s) ="%(i,addr), r
            con.writeTMSBits('\x03', 4) #Get to ShiftIR
            pstatus(con.writeTDIBits('\x6A', 7, return_tdo=True))#first ins bits
            con.writeTDIBits('\x01', 1, TMS=True) #ISC_PROGRAM
            con.writeTMSBits('\x03', 4) #Get to ShiftDR without running
            
            buffered_r = build_byte_align_buff(len(r)) + r
            buffered_addr = build_byte_align_buff(len(addr)) + addr
    
            con.writeTDIBits(buffered_r.tobytes(), len(r), return_tdo=True).__repr__()
            con.writeTDIBits(buffered_addr.tobytes(), len(addr)-1, return_tdo=True) #ISC_PROGRAM
            con.writeTDIBits(chr(addr[0]), 1, TMS=True, return_tdo=True) #ISC_PROGRAM
            
            con.writeTMSBits('\x01', 8) #RUN
            time.sleep(0.01)
        
        chain.transition_TAP("SHIFTIR")
        pstatus(con.writeTDIBits('\xF0', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_DISCHARGE
        con.writeTMSBits('\x01', 8) #RUN
        time.sleep(0.01)
        
        chain.transition_TAP("SHIFTIR")
        pstatus(con.writeTDIBits('\xF0', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_INIT
        con.writeTMSBits('\x1b', 5) #init pulse
        con.writeTMSBits('\x00', 8) #RUN
        time.sleep(0.01)
    
        chain.transition_TAP("SHIFTIR")
        con.writeTDIBits('\x40', 7, return_tdo=True).__repr__()
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_DISABLE
        con.writeTMSBits('\x01', 8) #RUN
        time.sleep(0.01)
    
        chain.transition_TAP("SHIFTIR")
        pstatus(con.writeTDIBits('\xff', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #BYPASS
        con.writeTMSBits('\xFF', 8) #RUN
        time.sleep(0.01)
        
        self._chain.jtagDisable()

class JTAGScanChain(object):
    def __init__(self, controller):
        self._controller = controller
        self._controller._scanchain = self #This might necessitate a factory
        self._sm = JTAGStateMachine()
        self._hasinit = False
        self._devices = []

    def init_chain(self):
        if not self._hasinit:
            self._devices = []

            self.jtagEnable()
            idcode_str = self.read_DR_bits(32)
            while idcode_str not in ('\x00\x00\x00\x00', '\xff\xff\xff\xff'):
                Jdev = JTAGDevice(self, idcode_str)
                self._devices.append(Jdev)
                idcode_str = self.read_DR_bits(32)
            self.jtagDisable()

            #The chain comes out last first. Reverse it to get order.
            self._devices.reverse()

    def write_IR_bits(self, data, count, readback=False):
        self.transition_TAP("SHIFTIR")

        res = self._controller.writeTDIBits(data, count-1, return_tdo=readback)
        rbit = 7 if count%8 == 0 else count%8-1
        remainder = (ord(data[0])&(pow(2,rbit)))>>rbit
        self._controller.writeTDIBits(chr(remainder), 1, TMS=True)
        return res

    def read_DR_bits(self, count):
        if self._sm.state != "SHIFTDR":
            self.transition_TAP("SHIFTDR")
        return self._controller.readTDOBits(count)

    def transition_TAP(self, state):
        data = self._sm.calc_transition_to_state(state)
        bufferz = bitarray('0'*(8-(len(data)%8)))
        datastr = (bufferz+data).tobytes()

        self._controller.writeTMSBits(datastr, len(data))

        #print data
        #print data.tobytes().__repr__()
        #print bufferz.__repr__()
        #print datastr.__repr__()

    def run_TAP_idle(self, cycles):
        self.transition_TAP("RTI")
        if cycles>1:
            self._controller.writeTMSBits('\x00'*int(math.ceil(cycles/8.0)), 
                                                 cycles-1)

    def jtagDisable(self):
        self._sm.state = "_PRE5"
        self._controller.jtagDisable()

    def jtagEnable(self):
        self._sm.state = "_PRE5"
        self._controller.jtagEnable()

    def _tapTransition(self, bits):
        #print "Bits:", bits
        statetrans = [self._sm.state]
        for bit in bits[::-1]:
            #print "Transitioning TMS->%s"%bit
            self._sm.transition_bit(bit)
            #if statetrans[-1]!=self._sm.state:
            statetrans.append(self._sm.state)
        #print "TAP:",self._sm.state
        #print "TAP State Change:", "->".join(statetrans)
