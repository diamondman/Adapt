from digilentdriver import JTAGController
from jtagDeviceDescription import JTAGDeviceDescription

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
        print "STATE:", self.STATE_NAMES[self._state]

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

class JTAGScanChain(object):
    def __init__(self, controller):
        self._controller = controller
        self._sm = JTAGStateMachine()
        self._hasinit = False
        self._devices = []

    def init_chain(self):
        if not self._hasinit:
            #Set state to SHIFT_DR through TLR
            self._controller.jtagEnable()
            self._controller.writeTMSBits('\x00\x5F', 9)

            devices = []
            idcode_str = self._controller.readTDOBits(32)
            while idcode_str != '\x00\x00\x00\x00':
                Jdev = JTAGDevice(self, idcode_str)
                devices.append(Jdev)
                idcode_str = self._controller.readTDOBits(32)
            self._controller.jtagDisable()

            #The chain comes out last first. Reverse it to get order.
            devices.reverse()
            for i, dev in enumerate(devices):
                if dev.desc:
                    print "        %d %s %s %s"%(i, dev.desc.manufacturer, 
                                                 dev.desc._device_name, dev.desc._chip_package)
                else:
                    print "        %d UNIDENTIFIED DEVICE. ID: %s."%(i, dev._id)
                    print "            Search for bsdl file: http://bsdl.info/list.htm?search=XXXX%s"%\
                        bin(dev._id & 0xFFFFFFF)[2:].zfill(28)
            

if __name__ == "__main__":
    controllers = JTAGController.getAttachedControllers()
    print "USB Controllers:"
    for i, c in enumerate(controllers):
        print "  %d %s"%(i, c)
        chain = JTAGScanChain(c)
        chain.init_chain()

