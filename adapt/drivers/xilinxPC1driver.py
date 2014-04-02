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

PROG = 8
TCK = 4
TMS = 2
TDI = 1
TDO = 1

def xpcu_enable_output(dh, enable):
    dh.controlWrite(0x40, 0xb0, 0x18 if enable else 0x10, 0, '')

def xpcu_unknown_x28_call(dh, enable):
    dh.controlWrite(0x40, 0xb0, 0x28, 0x12 if enable else 0x11, '')

def xpcu_get_GPIO_state(dh):
    return ord(dh.controlRead(0xc0, 0xb0, 0x38, 0, 1))

def xpcu_GPIO_transfer(dh, bit_count, data):
    if bit_count < 0: #TODO Move this to a superclass
        raise ValueError()
    #print "DATALEN:", len(data), "BITCOUNT (0->1):", bit_count
    bits_ret = bin(sum([((ord(data[i*2+1:i*2+2])>>4) & (( 1<< min(4, (bit_count+1)-(i*4)) )-1) )<<4*i 
                        for i in xrange(len(data)/2)])).count('1')

    #bits_ret = bin(sum([(ord(data[i*2+1:i*2+2])>>4)<<4*i 
    #                    for i in xrange(len(data)/2)])).count('1')
    dh.controlWrite(0x40, 0xb0, 0xa6, bit_count, '')
    bytec = dh.bulkWrite(2, data, timeout=1000)
    if bits_ret:
        bytes_wanted = int(math.ceil(bits_ret/8.0))
        bytes_expected = bytes_wanted +(1 if bytes_wanted%2 else 0)

        ret = dh.bulkRead(6, bytes_expected, timeout=1000)

        if not bits_ret%8 and not bytes_wanted%2:
            return ret
        #print ret.__repr__()
        if bytes_wanted != bytes_expected:
            ret = ret[1:]
        #print bits_ret
        if bits_ret%8:
            #print "Trimming bits of ", ret.__repr__()
            ret_ba = bitarray()
            for byte_ in ret:
                ret_ba.extend(bin(ord(byte_))[2:].zfill(8))
            #print "Bits:", ret_ba
            ret_ba = bitarray('0')+ret_ba[:-1]
            #print "post trim:", ret_ba
            ret = ret_ba.tobytes()
            #print ret
        return ret

def bitfieldify(buff, count):
    #bits = bitarray(''.join([bin(ord(i))[2:].zfill(8) for i in buff])[-count:])
    databits = bitarray()
    for byte_ in buff:
        databits.extend(bin(ord(byte_))[2:].zfill(8))
        #databits.fromstring(byte_)
    lendiff = len(databits)-count
    if count:
        databits = databits[lendiff:]
    return databits

class JTAGControlError(Exception):
    pass


class PlatformCable1Driver(object):

    def __init__(self, dev):
        self._dev = dev
        h = self._dev.open()

        self.serialNumber = '000000000000'#h.controlRead(0xC0, 0xE4, 0, 0, 12)
        self.name = 'PC1_'+self.serialNumber[-4:] #h.controlRead(0xC0, 0xE2, 0, 0, 16).replace('\x00', '').replace('\xFF', '')
        #This is probably subtly wrong...
        #pidraw = h.controlRead(0xC0, 0xE9, 0, 0, 4)
        self.productId = 0#(ord(pidraw[0])<<24)|(ord(pidraw[1])<<16)|(ord(pidraw[2])<<8)|ord(pidraw[3]) #%08xo

        self.productName = 'Platform Cable 1'#h.controlRead(0xC0, 0xE1, 0, 0, 28).replace('\x00', '').replace('\xFF', '')
        #firmwareraw = h.controlRead(0xC0, 0xE6, 0, 0, 2)
        self.firmwareVersion = 0#(ord(firmwareraw[1])<<8)|ord(firmwareraw[0])
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

    def jtagEnable(self):
        h = self._handle
        xpcu_enable_output(h, True)
        xpcu_unknown_x28_call(h, False)
        self._jtagon = True

    def jtagDisable(self):
        if not self._jtagon: return
        self._jtagon = False
        xpcu_enable_output(self._handle, False)

    def writeTMSBits(self, buff, count, return_tdo=False, TDI=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        tmsbits = bitfieldify(buff, count)
        if self._scanchain:
            self._scanchain._tapTransition(tmsbits)
        print "TMS bits:", tmsbits

        outbits = bitarray()
        for i in xrange(int(math.ceil(len(tmsbits)/4.0))):
            _start = max(len(tmsbits)-((i+1)*4), 0)
            _end = len(tmsbits)-(i*4)
            outbits.extend(bitarray((4-(_end-_start))*'0')+tmsbits[_start:_end])
            outbits.extend(4*('1' if TDI else '0'))
            outbits.extend(4*('1' if return_tdo else '0'))
            outbits.extend('1111')

        ret = xpcu_GPIO_transfer(self._handle, count-1, outbits.tobytes())
        if ret:
            return ret[::-1]

    def writeTDIBits(self, buff, count, return_tdo=False, TMS=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        tdibits = bitfieldify(buff, count)
        if self._scanchain:
            self._scanchain._tapTransition(bitarray(count*('1' if TMS else '0')))

        outbits = bitarray()
        for i in xrange(int(math.ceil(len(tdibits)/4.0))):
            _start = max(len(tdibits)-((i+1)*4), 0)
            _end = len(tdibits)-(i*4)
            outbits.extend('1111' if TMS else '0000')
            outbits.extend(bitarray((4-(_end-_start))*'0')+tdibits[_start:_end])
            outbits.extend('1111' if return_tdo else '0000')
            outbits.extend('1111')

        ret = xpcu_GPIO_transfer(self._handle, count-1, outbits.tobytes())
        if ret:
            return ret[::-1]


    def readTDOBits(self, count, TMS=False, TDI=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if self._scanchain:
            self._scanchain._tapTransition(bitarray(count*('1' if TMS else '0')))

        outbits = bitarray()
        for i in xrange(int(math.ceil(count/4.0))):
            outbits.extend('1111' if TMS else '0000')
            outbits.extend('1111' if TDI else '0000')
            outbits.extend('1111')
            outbits.extend('1111')

        ret = xpcu_GPIO_transfer(self._handle, count-1, outbits.tobytes())
        if ret:
            return ret[::-1]


    @property
    def _handle(self):
        if not self._dev_handle:
            self._dev_handle = self._dev.open()
        return self._dev_handle

    def close_handle(self):
        if self._dev_handle:
            self._dev_handle.close()



__filter__ = [((0x03FD, 0x0008),PlatformCable1Driver)]
