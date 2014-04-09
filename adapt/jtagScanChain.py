from jtagDeviceDescription import JTAGDeviceDescription

import time
import math
from bitarray import bitarray

NULL_ID_CODES = ['\x00\x00\x00\x00',
                 '\xFF\xFF\xFF\xFF',
                 bitarray('11111111111111111111111111111111'),
                 bitarray('00000000000000000000000000000000')]

def pstatus(resflags):
    #print resflags.__repr__()
    #if len(resflags)>1:
    #    resflags = resflags[0]
    if not resflags&bitarray('11000011'):
        print resflags, bitarray('11000011')
        print resflags&bitarray('11000011')
        print
    print "STATUS: "+("" if (resflags&bitarray('11000011')==bitarray('00000001')) else "INVALID_STATUS ")+\
        ("ISCDIS " if resflags[-6] else "")+("ISCEN " if resflags[-5] else "")+\
        ("SECURE " if resflags[-4] else "")+("DONE " if resflags[-3] else "")

    #print "STATUS: "+("" if (ord(resflags)&0b11000011==1) else "INVALID_STATUS ")+\
    #    ("ISCDIS " if ord(resflags)&32 else "")+("ISCEN " if ord(resflags)&16 else "")+\
    #    ("SECURE " if ord(resflags)&8 else "")+("DONE " if ord(resflags)&4 else "")

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
        if not isinstance(chain, JTAGScanChain):
            raise ValueError("JTAGDevice requires an instnace of JTAGScanChain")
        self._chain = chain

        if isinstance(idcode, int):
            self._id = idcode
        elif isinstance(idcode, bitarray):
            if len(idcode)==32:
                idcode_ = idcode.tobytes()
                self._id = (ord(idcode_[0])<<24)|(ord(idcode_[1])<<16)|\
                    (ord(idcode_[2])<<8)|ord(idcode_[3])
            else:
                raise ValueError("JTAGDevice idcode parameter must be an "
                                 "int, a string of length 4, or a bitarray "
                                 "of 32 bits (%s len: %s)"%(idcode,len(idcode)))
        elif isinstance(idcode, str):
            if len(idcode)==4:
                self._id = (ord(idcode[0])<<24)|(ord(idcode[1])<<16)|\
                    (ord(idcode[2])<<8)|ord(idcode[3])
            else:
                raise ValueError("JTAGDevice idcode parameter must be an "
                                 "int, a string of length 4, or a bitarray "
                                 "of 32 bits (%s len: %s)"%(idcode,len(idcode)))
        else:
            raise ValueError("JTAGDevice idcode parameter must be an int or "
                             "string of length 4. (Invalid Type: %s)"%type(idcode))

        self.desc = JTAGDeviceDescription.get_descriptor_for_idcode(self._id)

    def run_tap_instruction(self, insname, read=True, execute=True, 
                            loop=0, arg=None, delay=0, expret=None):
        ins = self.desc._instructions[insname]
        res = self._chain.write_ir_bits(ins, read=read)

        if arg is not None:
            self._chain.write_dr_bits(arg)
 
        if execute:
            self._chain.run_tap_idle(loop+1)

        if delay:
            time.sleep(delay)

        if read:
            if expret and res != expret:
                print "MISMATCH status on ins %s. Expected %s"%(insname, expret.__repr__())
                print "GOT:", res
                print
                pstatus(res)
            return res

    def erase(self):
        if self._id != 0x16d4c093:
            print "This operation is only supported on the Xilinx XC2C256 for now."
            sys.exit(1)

        self._chain.jtag_enable()

        self.run_tap_instruction("ISC_ENABLE", loop=8, delay=0.01)

        self.run_tap_instruction("ISC_ERASE", loop=8, delay=0.01)

        self.run_tap_instruction("ISC_INIT", loop=8, delay=0.01) #DISCHARGE

        self.run_tap_instruction("ISC_INIT", loop=8, arg=bitarray(), delay=0.01)

        self.run_tap_instruction("ISC_DISABLE", loop=8, delay=0.01, expret=bitarray('00010001'))

        self.run_tap_instruction("BYPASS", delay=0.01, expret=bitarray('00100001'))

        self._chain.transition_tap("TLR")

        self._chain.jtag_disable()

    def program(self, bitstream):
        if self._id != 0x16d4c093:
            print "This operation is only supported on the Xilinx XC2C256 for now."
            sys.exit(1)

        self._chain.jtag_enable()

        self.run_tap_instruction("ISC_ENABLE", loop=8, delay=0.01)

        for i,r in enumerate(bitstream.segments):
            self.run_tap_instruction("ISC_PROGRAM", arg=r, loop=8, delay=0.01)

        self.run_tap_instruction("ISC_INIT", loop=8, delay=0.01)

        self.run_tap_instruction("ISC_INIT", loop=8, arg=bitarray(), delay=0.01)

        self.run_tap_instruction("ISC_DISABLE", loop=8, expret=bitarray('00010101'), delay=0.01)

        self.run_tap_instruction("BYPASS", expret=bitarray('00100101'))

        self._chain.transition_tap("TLR")

        self._chain.jtag_disable()

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

            self.jtag_enable()
            idcode_str = self.read_dr_bits(32)
            while idcode_str not in NULL_ID_CODES:
                Jdev = JTAGDevice(self, idcode_str)
                self._devices.append(Jdev)
                idcode_str = self.read_dr_bits(32)
            self.jtag_disable()

            #The chain comes out last first. Reverse it to get order.
            self._devices.reverse()

    def write_ir_bits(self, data, read=False):
        self.transition_tap("SHIFTIR")
        if len(data) > 1:
            res = self._controller.write_tdi_bits(data[1:], return_tdo=read)[1:]
        else:
            res = bitarray()

        return self._controller.write_tdi_bits(data[0:1], TMS=True, return_tdo=read)[7:]+res
        

    def write_dr_bits(self, data, read=False, finish=True):
        self.transition_tap("SHIFTDR")
        if len(data) == 0:
            return

        if not finish:
            return self._controller.write_tdi_bits(data, return_tdo=read)
        else:
            res = self._controller.write_tdi_bits(data[1:], return_tdo=read)
            self._controller.write_tdi_bits(data[0:1], TMS=True)
            return res #TODO fix return

    def read_dr_bits(self, count):
        self.transition_tap("SHIFTDR")
        return self._controller.read_tdo_bits(count)

    def transition_tap(self, state):
        if state == self._sm.state:
            return

        data = self._sm.calc_transition_to_state(state)
        self._controller.write_tms_bits(data)

    def run_tap_idle(self, cycles):
        self.transition_tap("RTI")
        if cycles>1:
            self._controller.write_tms_bits(bitarray('0'*(cycles-1)))

    def jtag_disable(self):
        self._sm.state = "_PRE5"
        self._controller.jtag_disable()

    def jtag_enable(self):
        self._sm.state = "_PRE5"
        self._controller.jtag_enable()

    def _tap_transition_driver_trigger(self, bits):
        statetrans = [self._sm.state]
        for bit in bits[::-1]:
            self._sm.transition_bit(bit)
            statetrans.append(self._sm.state)

