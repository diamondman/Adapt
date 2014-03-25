from jtagDeviceDescription import JTAGDeviceDescription

import time
from bitarray import bitarray

def gc(addr):
    return (addr>>1)^addr

def pstatus(resflags):
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
    STATE_TLR = 0
    STATE_IDLE = 1
    STATE_SELECT_DR = 2
    STATE_CAPTURE_DR = 3
    STATE_SHIFT_DR = 4
    STATE_EXIT1_DR = 5
    STATE_PAUSE_DR = 6
    STATE_EXIT2_DR = 7
    STATE_UPDATE_DR = 8
    STATE_SELECT_IR = 9
    STATE_CAPTURE_IR = 10
    STATE_SHIFT_IR = 11
    STATE_EXIT1_IR = 12
    STATE_PAUSE_IR = 13
    STATE_EXIT2_IR = 14
    STATE_UPDATE_IR = 15

    STATE_NAMES = {0:'TLR',
                   1:'IDLE',
                   2:'SELECT_DR',
                   3:'CAPTURE_DR',
                   4:'SHIFT_DR',
                   5:'EXIT1_DR',
                   6:'PAUSE_DR',
                   7:'EXIT2_DR',
                   8:'UPDATE_DR' ,
                   9:'SELECT_IR' ,
                   10:'CAPTURE_IR',
                   11:'SHIFT_IR',
                   12:'EXIT1_IR',
                   13:'PAUSE_IR',
                   14:'EXIT2_IR',
                   15:'UPDATE_IR'}

    def __init__(self):
        self._state = self.STATE_TLR

    def transition(self, bit):
        if self._state == self.STATE_TLR:
            if not bit: self._state = self.STATE_IDLE
        elif self._state == self.STATE_IDLE:
            if bit:     self._state = self.STATE_SELECT_DR
        elif self._state == self.STATE_SELECT_DR:
            if bit:     self._state = self.STATE_SELECT_IR
            else:       self._state = self.STATE_CAPTURE_DR
        elif self._state == self.STATE_CAPTURE_DR:
            if bit:     self._state = self.STATE_EXIT1_DR
            else:       self._state = self.STATE_SHIFT_DR
        elif self._state == self.STATE_SHIFT_DR:
            if bit:     self._state = self.STATE_EXIT1_DR
        elif self._state == self.STATE_EXIT1_DR:
            if bit:     self._state = self.STATE_UPDATE_DR
            else:       self._state = self.STATE_PAUSE_DR
        elif self._state == self.STATE_PAUSE_DR:
            if bit:     self._state = self.STATE_EXIT2_DR
        elif self._state == self.STATE_EXIT2_DR:
            if bit:     self._state = self.STATE_UPDATE_DR
            else:       self._state = self.STATE_SHIFT_DR
        elif self._state == self.STATE_UPDATE_DR:
            if bit:     self._state = self.STATE_SELECT_DR
            else:       self._state = self.STATE_IDLE
        elif self._state == self.STATE_SELECT_IR:
            if bit:     self._state = self.STATE_TLR
            else:       self._state = self.STATE_CAPTURE_IR
        elif self._state == self.STATE_CAPTURE_IR:
            if bit:     self._state = self.STATE_EXIT1_IR
            else:       self._state = self.STATE_SHIFT_IR
        elif self._state == self.STATE_SHIFT_IR:
            if bit:     self._state = self.STATE_EXIT1_IR
        elif self._state == self.STATE_EXIT1_IR:
            if bit:     self._state = self.STATE_UPDATE_IR
            else:       self._state = self.STATE_PAUSE_IR
        elif self._state == self.STATE_PAUSE_IR:
            if bit:     self._state = self.STATE_EXIT2_IR
        elif self._state == self.STATE_EXIT2_IR:
            if bit:     self._state = self.UPDATE_IR
            else:       self._state = self.SHIFT_IR
        elif self._state == self.STATE_UPDATE_IR:
            if bit:     self._state = self.STATE_SELECT_DR
            else:       self._state = self.STATE_IDLE
        #print "STATE:", self.state

    @property
    def state(self):
        return self.STATE_NAMES.get(self._state, "UNKNOWN STATE!")

class JTAGDevice(object):
    def __init__(self, chain, idcode):
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

    def erase(self):
        #import ipdb
        con = self._chain._controller
        self._chain._jtagEnable()
        #print self.desc._instructions
        
        cmd_isce = self.desc._instructions['ISC_ENABLE']
        cmd_iscd = self.desc._instructions['ISC_DISABLE']
        cmd_iscerase = self.desc._instructions['ISC_ERASE']
        print cmd_isce, cmd_iscd, cmd_iscerase
        
        #ipdb.set_trace()
        con.writeTMSBits('\x00\xDF', 10) #Get to ShiftIR
        pstatus(con.writeTDIBits('\x68', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_ENABLE
        con.writeTMSBits('\x01', 8) #RUN
        time.sleep(0.01)
    
        #ipdb.set_trace()
        con.writeTMSBits('\x03', 4) #Get to ShiftIR
        pstatus(con.writeTDIBits('\x6D', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_ERASE
        con.writeTMSBits('\x01', 8) #RUN
        time.sleep(0.01)
        
        #ipdb.set_trace()
        con.writeTMSBits('\x03', 4) #Get to ShiftIR
        pstatus(con.writeTDIBits('\xF0', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_DISCHARGE
        con.writeTMSBits('\x01', 8) #RUN
        time.sleep(0.01)
        
        #ipdb.set_trace()
        con.writeTMSBits('\x03', 4) #Get to ShiftIR
        pstatus(con.writeTDIBits('\xF0', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_INIT
        con.writeTMSBits('\x1b', 5) #init pulse
        con.writeTMSBits('\x00', 8) #RUN
        time.sleep(0.01)
    
        #ipdb.set_trace()
        con.writeTMSBits('\x03', 4) #Get to ShiftIR
        pstatus(con.writeTDIBits('\x40', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_DISABLE
        con.writeTMSBits('\x01', 8) #RUN
        time.sleep(0.01)
    
        #ipdb.set_trace()
        con.writeTMSBits('\x03', 4) #Get to ShiftIR
        pstatus(con.writeTDIBits('\xff', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #BYPASS
        con.writeTMSBits('\xFF', 8) #RUN
        time.sleep(0.01)
    
        #time.sleep(2)
        self._chain._jtagDisable()

    def program(self, data_array):
        import ipdb
        con = self._chain._controller
        self._chain._jtagEnable()
        
        #ipdb.set_trace()
        con.writeTMSBits('\x00\xDF', 10) #Get to ShiftIR
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
        
        #ipdb.set_trace()
        con.writeTMSBits('\x03', 4) #Get to ShiftIR
        pstatus(con.writeTDIBits('\xF0', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_DISCHARGE
        con.writeTMSBits('\x01', 8) #RUN
        time.sleep(0.01)
        
        #ipdb.set_trace()
        con.writeTMSBits('\x03', 4) #Get to ShiftIR
        pstatus(con.writeTDIBits('\xF0', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_INIT
        con.writeTMSBits('\x1b', 5) #init pulse
        con.writeTMSBits('\x00', 8) #RUN
        time.sleep(0.01)
    
        #ipdb.set_trace()
        con.writeTMSBits('\x03', 4) #Get to ShiftIR
        con.writeTDIBits('\x40', 7, return_tdo=True).__repr__()
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_DISABLE
        con.writeTMSBits('\x01', 8) #RUN
        time.sleep(0.01)
    
        #ipdb.set_trace()
        con.writeTMSBits('\x03', 4) #Get to ShiftIR
        pstatus(con.writeTDIBits('\xff', 7, return_tdo=True))
        con.writeTDIBits('\x01', 1, TMS=True) #BYPASS
        con.writeTMSBits('\xFF', 8) #RUN
        time.sleep(0.01)
        
        self._chain._jtagDisable()

class JTAGScanChain(object):
    def __init__(self, controller):
        self._controller = controller
        self._controller._scanchain = self #This might necessitate a factory
        self._sm = JTAGStateMachine()
        self._hasinit = False
        self._devices = []

    def init_chain(self):
        if not self._hasinit:
            #Set state to SHIFT_DR through TLR
            self._controller.jtagEnable()
            self._controller.writeTMSBits('\x00\x5F', 9)

            self._devices = []
            idcode_str = self._controller.readTDOBits(32)
            while idcode_str != '\x00\x00\x00\x00':
                Jdev = JTAGDevice(self, idcode_str)
                self._devices.append(Jdev)
                idcode_str = self._controller.readTDOBits(32)
            self._controller.jtagDisable()

            #The chain comes out last first. Reverse it to get order.
            self._devices.reverse()

    def _jtagDisable(self):
        self._controller.jtagDisable()

    def _jtagEnable(self):
        self._controller.jtagEnable()

    def _tapTransition(self, bits):
        #print "Bits:", bits
        statetrans = [self._sm.state]
        for bit in bits[::-1]:
            #print "Transitioning TMS->%s"%bit
            self._sm.transition(bit)
            #if statetrans[-1]!=self._sm.state:
            statetrans.append(self._sm.state)
        #print "TAP:",self._sm.state
        #print "TAP State Change:", "->".join(statetrans)

if __name__ == "__main__":
    from digilentdriver import JTAGController
    controllers = JTAGController.getAttachedControllers()
    print "USB Controllers:"
    for i, c in enumerate(controllers):
        print "  %d %s"%(i, c)
        chain = JTAGScanChain(c)
        chain.init_chain()

