#-*- coding: utf-8 -*-
"""
    digilentdriver
    ~~~~~~~~~~~~~~

    Digilent driver for Linux USB JTAG controller

    :copyright: (c) 2014 by Jessy Diamond Exum
    :license: Pending, see LICENSE for more details.
"""

import usb1
import math

class JTAGControlError(Exception):
    pass

usbcontext = usb1.USBContext()

class JTAGController(object):
    
    def __init__(self, dev):
        self._dev = dev
        h = self._dev.open()

        self.serialNumber = h.controlRead(0xC0, 0xE4, 0, 0, 12)
        self.userName = h.controlRead(0xC0, 0xE2, 0, 0, 16).replace('\x00', '').replace('\xFF', '')
        #This is probably subtly wrong...
        pidraw = h.controlRead(0xC0, 0xE9, 0, 0, 4)
        self.productId = (ord(pidraw[0])<<24)|(ord(pidraw[1])<<16)|(ord(pidraw[2])<<8)|ord(pidraw[3])

        self.productName = h.controlRead(0xC0, 0xE1, 0, 0, 28).replace('\x00', '').replace('\xFF', '')
        firmwareraw = h.controlRead(0xC0, 0xE6, 0, 0, 2)
        self.firmwareVersion = (ord(firmwareraw[1])<<8)|ord(firmwareraw[0])
        h.close()

        self._dev_handle = None
        self._jtagon = False

    def __repr__(self):
        return "%s(%s; uName: %s; SN: %s; FWver: %04x; PID: %08x)"%\
                                         (self.__class__.__name__,
                                          self.productName,
                                          self.userName,
                                          self.serialNumber,
                                          self.firmwareVersion,
                                          self.productId)

    def jtagEnable(self):
        h = self._handle
        h.bulkWrite(1, '\x03\x02\x00\x00')
        res = h.bulkRead(2, 2)
        if ord(res[1]) != 0:
            raise JTAGControlError("Error enabling JTAG. Error code: %s." %ord(res[1]))
        self._jtagon = True

    def jtagDisable(self):
        if not self._jtagon: return
        self._jtagon = False
        h = self._handle
        h.bulkWrite(1, '\x03\x02\x01\x00')
        res = h.bulkRead(2, 2)
        if ord(res[1]) != 0:
            raise JTAGControlError()

    def writeTMSBits(self, buff, count, return_tdo=False, DI=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        h = self._handle
        byte_count = int(math.ceil(count/8.0))
        tdo_bits = None

        h.bulkWrite(1, '\x09\x02\x0b\x00'+chr(return_tdo)+chr(DI)+\
                        "".join([chr(count>>(8*i)) for i in range(4)]))
        res = h.bulkRead(2, 2)
        if ord(res[1]) != 0:
            raise JTAGControlError("Uknown Issue writing TMS bits: %s", res)

        h.bulkWrite(3, buff[::-1])
        if return_tdo is True:
            tdo_bits = h.bulkRead(4, byte_count)[::-1]

        h.bulkWrite(1, '\x03\x02' + chr(0x80|0x0b) + '\x00')
        res = h.bulkRead(2, 6)
        #print res.__repr__() #I may check this later. Do not know how it could fail.

        return tdo_bits

    def readTDOBits(self, count, TMS=False, TDI=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        h = self._handle
        byte_count = int(math.ceil(count/8.0))

        h.bulkWrite(1, '\x09\x02\x09\x00'+chr(TMS)+chr(TDI)+"".join([chr(count>>(8*i)) for i in range(4)]))
        res = h.bulkRead(2, 2)
        if ord(res[1]) != 0:
            raise JTAGControlError("Uknown Issue reading TDO bits: %s", res)

        tdo_bits = h.bulkRead(4, byte_count)[::-1]
        #print "0x"+"".join(["%02x"%ord(b) for b in tdo_bits])

        h.bulkWrite(1, '\x03\x02' + chr(0x80|0x09) + '\x00')
        res = h.bulkRead(2, 10)
        #print res.__repr__() #I may check this later. Do not know how it could fail.

        return tdo_bits
        
        

    @property
    def _handle(self):
        if not self._dev_handle:
            self._dev_handle = self._dev.open()
        return self._dev_handle

    def close_handle(self):
        if self._dev_handle:
            self._dev_handle.close()

    @classmethod
    def getAttachedControllers(cls):
        controllers = []
        for device in usbcontext.getDeviceList(skip_on_error=True):
            if device.getVendorID() == 0x1443:
                controller = cls(device)
                controllers.append(controller)
        return controllers


if __name__ == "__main__":
    controllers = JTAGController.getAttachedControllers()
    print "USB Controllers:"
    for i, c in enumerate(controllers):
        print "  %d %s"%(i, c)
        c.jtagEnable()
        c.writeTMSBits('\x00\x5F', 9) #Transition to SHIFT_DR state.
        idcode = c.readTDOBits(32)
        while idcode != '\x00\x00\x00\x00':
            print("    Device 0x%08x"%sum([(ord(idcode[b])<<(8*b)) for b in range(len(idcode))]))
            idcode = c.readTDOBits(32)
        c.jtagDisable()
