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
import numbers

from cabledriver import CableDriver
from primative import Level1Primative, Level2Primative, Level3Primative,\
    Executable, DefaultRunInstructionPrimative,\
    DOESNOTMATTER, ZERO, ONE, CONSTANT, SEQUENCE
from jtagUtils import JTAGControlError

#PROG = 8
#TCK = 4
#TMS = 2
#TDI = 1
#TDO = 1

class XPC1TransferPrimative(Level1Primative, Executable):
    #transfer_bits_single can be used for single bit jtag transfers.
    #This will be necessary for firmware upgrade.
    _driver_function_name = 'transfer_bits'#_single'#_cpld_upgrade'
    _max_bits = 65536
    """TMS, TDI, TDO"""
    _effect = [SEQUENCE, SEQUENCE, SEQUENCE]
    def __init__(self, count, tms, tdi, tdo):
        self.count, self.tms, self.tdi, self.tdo = count, tms, tdi, tdo
    def _get_args(self):
        return [self.count, self.tms, self.tdi], {'TDO': self.tdo}

class XilinxPC1Driver(CableDriver):
    _primatives = [XPC1TransferPrimative]
    def __init__(self, dev, mock=False):
        super(XilinxPC1Driver, self).__init__(dev)
        self.mock = mock
        if not mock:
            h = self._dev.open()
    
            self.serialNumber = '000000000000'
            self.name = 'PC1_'+self.serialNumber[-4:]
            self.productId = 0
    
            self.productName = 'Platform Cable 1'
            self.firmwareVersion = 0
            h.close()

        self._jtagon = False
        self._scanchain = None

    def __repr__(self):
        if self.mock:
            return "%s(MOCK)"%self.__class__.__name__
        return "%s(%s; Name: %s; SN: %s; FWver: %04x)"%\
                                         (self.__class__.__name__,
                                          self.productName,
                                          self.name,
                                          self.serialNumber,
                                          self.firmwareVersion)

    def jtag_enable(self):
        self.xpcu_enable_output(True)
        self.xpcu_set_jtag_speed(False)
        self._jtagon = True
        #self.xpcu_enable_cpld_upgrade_mode(True)

    def jtag_disable(self):
        if not self._jtagon: return
        self._jtagon = False
        self.xpcu_enable_output(False)
        #self.xpcu_enable_cpld_upgrade_mode(False)

    def transfer_bits(self, count, TMS, TDI, TDO=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if isinstance(TMS, (numbers.Number, bool)):
            TMS = bitarray(count*('1' if TMS else '0'))
        if isinstance(TDI, (numbers.Number, bool)):
            TDI = bitarray(count*('1' if TDI else '0'))
        #if isinstance(TDO, (numbers.Number, bool)):
        #    TDO = bitarray(count*('1' if TDO else '0'))
        if self._scanchain:
            self._scanchain._tap_transition_driver_trigger(TMS)

        outbits = bitarray()
        for i in range(int(math.ceil(count/4.0))):
            _start = max(count-((i+1)*4), 0)
            _end = count-(i*4)
            outbits.extend(bitarray((4-(_end-_start))*'0')+TMS[_start:_end])
            outbits.extend(bitarray((4-(_end-_start))*'0')+TDI[_start:_end])
            outbits.extend(4*('1' if TDO else '0'))
            outbits.extend('1111')

        tdo_bytes = self.xpcu_GPIO_transfer(count-1, outbits.tobytes())
        if tdo_bytes:
            tdo_bytes = tdo_bytes[::-1]
            tdo_bits = bitarray()
            for byte_ in tdo_bytes:
                tdo_bits.extend(bin(byte_)[2:].zfill(8)) #TODO make modern
            return tdo_bits

    def transfer_bits_single(self, count, TMS, TDI, TDO=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if isinstance(TMS, (numbers.Number, bool)):
            TMS = bitarray(count*('1' if TMS else '0'))
        if isinstance(TDI, (numbers.Number, bool)):
            TDI = bitarray(count*('1' if TDI else '0'))
        #if isinstance(TDO, (numbers.Number, bool)):
        #    TDO = bitarray(count*('1' if TDO else '0'))
        if self._scanchain:
            self._scanchain._tap_transition_driver_trigger(TMS)
        #self.xpcu_single_read()
        outbits = bitarray()
        TMS.reverse()
        TDI.reverse()

        for bit_num in range(count):
            self.xpcu_single_write(TMS[bit_num], TDI[bit_num])
            if TDO:
                b = self.xpcu_single_read()
                outbits.append(b)

        if outbits:
            outbits.reverse()
            #print(outbits, len(outbits))
            return outbits

    def transfer_bits_single_cpld_upgrade(self, count, TMS, TDI, TDO=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if isinstance(TMS, (numbers.Number, bool)):
            TMS = bitarray(count*('1' if TMS else '0'))
        if isinstance(TDI, (numbers.Number, bool)):
            TDI = bitarray(count*('1' if TDI else '0'))
        #if isinstance(TDO, (numbers.Number, bool)):
        #    TDO = bitarray(count*('1' if TDO else '0'))
        if self._scanchain:
            self._scanchain._tap_transition_driver_trigger(TMS)
        #self.xpcu_single_read()
        outbits = bitarray()
        TMS.reverse()
        TDI.reverse()

        for bit_num in range(count):
            if TDO:
                b = self.xpcu_single_read()
                outbits.append(b)
            self.xpcu_single_write(TMS[bit_num], TDI[bit_num])

        if outbits:
            outbits.reverse()
            print(outbits, len(outbits))
            return outbits



    def xpcu_enable_output(self, enable):
        self._handle.controlWrite(0x40, 0xb0, 0x18 if enable else 0x10, 0, b'')

    def xpcu_enable_cpld_upgrade_mode(self, enable):
        self._handle.controlWrite(0x40, 0xb0, 0x52, 1 if enable else 0, b'')

    def xpcu_set_jtag_speed(self, speed_mode=1):
        self._handle.controlWrite(0x40, 0xb0, 0x28, 0x10|speed_mode, b'')

    def xpcu_get_GPIO_state(self):
        return ord(self._handle.controlRead(0xc0, 0xb0, 0x38, 0, 1))

    def xpcu_single_write(self, TMS, TDI):
        val = 0b100|(TMS<<1)|TDI
        self._handle.controlWrite(0x40, 0xb0, 0x30, val, b'')
        val = (TMS<<1)|TDI
        self._handle.controlWrite(0x40, 0xb0, 0x30, val, b'')

    def xpcu_single_read(self):
        b = self._handle.controlRead(0xC0, 0xb0, 0x38, 0, 1)
        #print(bin(ord(b)))
        return bool(ord(b)&1)

    def xpcu_GPIO_transfer(self, bit_count, data):
        if bit_count < 0:
            raise ValueError()
        bits_ret = bin(sum([((ord(data[i*2+1:i*2+2])>>4) &
                             (( 1<< min(4, (bit_count+1)-(i*4)) )-1) )<<4*i
                            for i in range(int(len(data)/2))])).count('1')

        self._handle.controlWrite(0x40, 0xb0, 0xa6, bit_count, b'')

        bytec = self._handle.bulkWrite(2, data, timeout=5000)
        if bits_ret:
            bytes_wanted = int(math.ceil(bits_ret/8.0))
            bytes_expected = bytes_wanted +(1 if bytes_wanted%2 else 0)

            ret = self._handle.bulkRead(6, bytes_expected, timeout=5000)

            if not bits_ret%8 and not bytes_wanted%2:
                return ret

            if bytes_wanted != bytes_expected: #Forgot what this does
                ret = ret[1:]

            if bits_ret%8:
                ret_ba = bitarray()
                for byte_ in ret:
                    ret_ba.extend(bin(ord(byte_))[2:].zfill(8))
                ret_ba = bitarray('0')+ret_ba[:-1]
                ret = ret_ba.tobytes()
            return ret



__filter__ = [((0x03FD, 0x0008),XilinxPC1Driver)]
