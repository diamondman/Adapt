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

class JTAGControlError(Exception):
    pass


class PlatformCable1Driver(object):

    def __init__(self, dev):
        self._dev = dev
        h = self._dev.open()

        self.serialNumber = '000000000000'
        self.name = 'PC1_'+self.serialNumber[-4:]
        self.productId = 0#(ord(pidraw[0])<<24)|(ord(pidraw[1])<<16)|(ord(pidraw[2])<<8)|ord(pidraw[3]) #%08xo

        self.productName = 'Platform Cable 1'#h.controlRead(0xC0, 0xE1, 0, 0, 28).replace('\x00', '').replace('\xFF', '')
        self.firmwareVersion = 0
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
        self.xpcu_enable_output(True)
        self.xpcu_unknown_x28_call(False)
        self._jtagon = True

    def jtag_disable(self):
        if not self._jtagon: return
        self._jtagon = False
        self.xpcu_enable_output(False)

    def write_tms_bits(self, buff, return_tdo=False, TDI=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if self._scanchain:
            self._scanchain._tap_transition_driver_trigger(buff)

        outbits = bitarray()
        for i in xrange(int(math.ceil(len(buff)/4.0))):
            _start = max(len(buff)-((i+1)*4), 0)
            _end = len(buff)-(i*4)
            outbits.extend(bitarray((4-(_end-_start))*'0')+buff[_start:_end])
            outbits.extend(4*('1' if TDI else '0'))
            outbits.extend(4*('1' if return_tdo else '0'))
            outbits.extend('1111')

        tdo_bytes = self.xpcu_GPIO_transfer(len(buff)-1, outbits.tobytes())
        if tdo_bytes:
            tdo_bytes = tdo_bytes[::-1]
            tdo_bits = bitarray()
            for byte_ in tdo_bytes:
                tdo_bits.extend(bin(ord(byte_))[2:].zfill(8))
            return tdo_bits

    def write_tdi_bits(self, buff, return_tdo=False, TMS=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if self._scanchain:
            self._scanchain._tap_transition_driver_trigger(bitarray(len(buff)*('1' if TMS else '0')))

        outbits = bitarray()
        for i in xrange(int(math.ceil(len(buff)/4.0))):
            _start = max(len(buff)-((i+1)*4), 0)
            _end = len(buff)-(i*4)
            outbits.extend('1111' if TMS else '0000')
            outbits.extend(bitarray((4-(_end-_start))*'0')+buff[_start:_end])
            outbits.extend('1111' if return_tdo else '0000')
            outbits.extend('1111')

        tdo_bytes = self.xpcu_GPIO_transfer(len(buff)-1, outbits.tobytes())

        if tdo_bytes:
            tdo_bytes = tdo_bytes[::-1]
            tdo_bits = bitarray()
            for byte_ in tdo_bytes:
                tdo_bits.extend(bin(ord(byte_))[2:].zfill(8))
            return tdo_bits


    def read_tdo_bits(self, count, TMS=False, TDI=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if self._scanchain:
            self._scanchain._tap_transition_driver_trigger(bitarray(count*('1' if TMS else '0')))

        outbits = bitarray()
        for i in xrange(int(math.ceil(count/4.0))):
            outbits.extend('1111' if TMS else '0000')
            outbits.extend('1111' if TDI else '0000')
            outbits.extend('1111')
            outbits.extend('1111')

        tdo_bytes = self.xpcu_GPIO_transfer(count-1, outbits.tobytes())
        if tdo_bytes:
            tdo_bytes = tdo_bytes[::-1]
            tdo_bits = bitarray()
            for byte_ in tdo_bytes:
                tdo_bits.extend(bin(ord(byte_))[2:].zfill(8))
            return tdo_bits


    @property
    def _handle(self):
        if not self._dev_handle:
            self._dev_handle = self._dev.open()
        return self._dev_handle

    def close_handle(self):
        if self._dev_handle:
            self._dev_handle.close()


    def xpcu_enable_output(self, enable):
        self._handle.controlWrite(0x40, 0xb0, 0x18 if enable else 0x10, 0, '')

    def xpcu_unknown_x28_call(self, enable):
        self._handle.controlWrite(0x40, 0xb0, 0x28, 0x12 if enable else 0x11, '')

    def xpcu_get_GPIO_state(self):
        return ord(self._handle.controlRead(0xc0, 0xb0, 0x38, 0, 1))

    def xpcu_GPIO_transfer(self, bit_count, data):
        if bit_count < 0: #TODO Move this to a superclass
            raise ValueError()
        #print "DATALEN:", len(data), "BITCOUNT (0->1):", bit_count
        bits_ret = bin(sum([((ord(data[i*2+1:i*2+2])>>4) &
                             (( 1<< min(4, (bit_count+1)-(i*4)) )-1) )<<4*i
                            for i in xrange(len(data)/2)])).count('1')

        #bits_ret = bin(sum([(ord(data[i*2+1:i*2+2])>>4)<<4*i
        #                    for i in xrange(len(data)/2)])).count('1')
        self._handle.controlWrite(0x40, 0xb0, 0xa6, bit_count, '')
        bytec = self._handle.bulkWrite(2, data, timeout=1000)
        if bits_ret:
            bytes_wanted = int(math.ceil(bits_ret/8.0))
            bytes_expected = bytes_wanted +(1 if bytes_wanted%2 else 0)

            ret = self._handle.bulkRead(6, bytes_expected, timeout=1000)

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



__filter__ = [((0x03FD, 0x0008),PlatformCable1Driver)]
