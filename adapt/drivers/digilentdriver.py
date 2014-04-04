#-*- coding: utf-8 -*-
"""
    digilentdriver
    ~~~~~~~~~~~~~~

    Digilent driver for Linux USB JTAG controller

    :copyright: (c) 2014 by Jessy Diamond Exum
    :license: Pending, see LICENSE for more details.
"""

import math

from bitarray import bitarray

def build_byte_align_buff(buff):
    bitmod = len(buff)%8
    if bitmod == 0:
        rdiff = bitarray()
        #print "NO BUFF NEEDED", rdiff
    else:
        rdiff = bitarray(8-bitmod)
        rdiff.setall(False)
    return rdiff+buff

class JTAGControlError(Exception):
    pass


class DigilentAdeptController(object):

    def __init__(self, dev):
        self._dev = dev
        h = self._dev.open()

        self.serialNumber = h.controlRead(0xC0, 0xE4, 0, 0, 12)
        self.name = h.controlRead(0xC0, 0xE2, 0, 0, 16).replace('\x00', '').replace('\xFF', '')
        #This is probably subtly wrong...
        pidraw = h.controlRead(0xC0, 0xE9, 0, 0, 4)
        self.productId = (ord(pidraw[0])<<24)|(ord(pidraw[1])<<16)|(ord(pidraw[2])<<8)|ord(pidraw[3]) #%08x

        self.productName = h.controlRead(0xC0, 0xE1, 0, 0, 28).replace('\x00', '').replace('\xFF', '')
        firmwareraw = h.controlRead(0xC0, 0xE6, 0, 0, 2)
        self.firmwareVersion = (ord(firmwareraw[1])<<8)|ord(firmwareraw[0])
        h.close()

        self._dev_handle = None
        self._jtagon = False

        self._scanchain = None


    def __repr__(self):
        return "%s(%s; Name: %s; SN: %s; FWver: %04x)"%\
                                         (self.__class__.__name__,
                                          self.productName,
                                          self.name,
                                          self.serialNumber,
                                          self.firmwareVersion)

    def jtag_enable(self):
        h = self._handle
        h.bulkWrite(1, '\x03\x02\x00\x00')
        res = h.bulkRead(2, 2)
        if ord(res[1]) != 0:
            raise JTAGControlError("Error enabling JTAG. Error code: %s." %ord(res[1]))
        self._jtagon = True

    def jtag_disable(self):
        if not self._jtagon: return
        self._jtagon = False
        h = self._handle
        h.bulkWrite(1, '\x03\x02\x01\x00')
        res = h.bulkRead(2, 2)
        if ord(res[1]) != 0:
            raise JTAGControlError()

    def write_tms_bits(self, data, return_tdo=False, TDI=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if self._scanchain:
            self._scanchain._tap_transition_driver_trigger(data)

        h = self._handle

        h.bulkWrite(1, '\x09\x02\x0b\x00'+chr(return_tdo)+chr(TDI)+\
                        "".join([chr((len(data)>>(8*i))&0xff) for i in range(4)]))
        res = h.bulkRead(2, 2)
        if ord(res[1]) != 0:
            raise JTAGControlError("Uknown Issue writing TMS bits: %s", res)

        h.bulkWrite(3, build_byte_align_buff(data).tobytes()[::-1])

        tdo_bits = None
        if return_tdo:
            tdo_bits = h.bulkRead(4, int(math.ceil(len(data)/8.0)))[::-1]

        h.bulkWrite(1, '\x03\x02' + chr(0x80|0x0b) + '\x00')
        h.bulkRead(2, 6) #Not checking for now

        return tdo_bits

    def write_tdi_bits(self, buff, return_tdo=False, TMS=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if self._scanchain:
            bits = bitarray(('1' if TMS else '0')*len(buff))
            self._scanchain._tap_transition_driver_trigger(bits)

        self._handle.bulkWrite(1, '\x09\x02\x08\x00'+chr(return_tdo)+chr(TMS)+\
                        "".join([chr((len(buff)>>(8*i))&0xff) for i in range(4)]))
        res = self._handle.bulkRead(2, 2)
        if ord(res[1]) != 0:
            raise JTAGControlError("Uknown Issue writing TDI bits: %s", res)

        #WRITE DATA
        bbuff = build_byte_align_buff(buff).tobytes()
        self._handle.bulkWrite(3, bbuff[::-1])

        #GET DATA BACK
        tdo_bits = None
        if return_tdo is True:
            byte_count = int(math.ceil(len(buff)/8.0))
            tdo_bits = self._handle.bulkRead(4, byte_count)[::-1]

        #GET BACK STATS
        self._handle.bulkWrite(1, '\x03\x02' + chr(0x80|0x08) + '\x00')
        self._handle.bulkRead(2, 10) #Not checking this for now.

        return tdo_bits

    def read_tdo_bits(self, count, TMS=False, TDI=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if self._scanchain:
            bits = bitarray(('1' if TMS else '0')*count)
            self._scanchain._tap_transition_driver_trigger(bits)
        h = self._handle
        byte_count = int(math.ceil(count/8.0))
        tdo_bits = None

        h.bulkWrite(1, '\x09\x02\x09\x00'+chr(TMS)+chr(TDI)+\
                        "".join([chr((count>>(8*i))&0xff) for i in range(4)]))
        res = h.bulkRead(2, 2)
        if ord(res[1]) != 0:
            raise JTAGControlError("Uknown Issue reading TDO bits: %s", res)

        tdo_bits = h.bulkRead(4, byte_count)[::-1]
        #print "0x"+"".join(["%02x"%ord(b) for b in tdo_bits])

        #GET BACK STATS
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



__filter__ = [((0x1443, None),DigilentAdeptController)]
