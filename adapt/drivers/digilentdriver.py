#-*- coding: utf-8 -*-
"""
    digilentdriver
    ~~~~~~~~~~~~~~

    Digilent driver for Linux USB JTAG controller

    :copyright: (c) 2014 by Jessy Diamond Exum
    :license: Pending, see LICENSE for more details.
"""

from bitarray import bitarray

from adapt.jtagUtils import blen2Blen, buff2Blen, JTAGControlError,\
    build_byte_align_buff
from adapt.cabledriver import CableDriver
from adapt.primative import Level1Primative, Executable,\
    DOESNOTMATTER, ZERO, ONE, CONSTANT, SEQUENCE

def index_or_default(s):
    try:
        s = s[:s.index(b'\x00')]
    except ValueError:
        pass
    try:
        s = s[:s.index(b'\xFF')]
    except ValueError:
        pass
    return s

class DigilentWriteTMSPrimative(Level1Primative, Executable):
    _driver_function_name = 'write_tms_bits'
    """TMS, TDI, TDO"""
    _effect = [SEQUENCE, CONSTANT, CONSTANT]
    def __init__(self, count, tms, tdi, tdo):
        self.count, self.tms, self.tdi, self.tdo = count, tms, tdi, tdo
    def _get_args(self):
        return [self.tms], {'return_tdo':self.tdo, 'TDI': self.tdi}

class DigilentWriteTDIPrimative(Level1Primative, Executable):
    _driver_function_name = 'write_tdi_bits'
    """TMS, TDI, TDO"""
    _effect = [CONSTANT, SEQUENCE, CONSTANT]
    def __init__(self, count, tms, tdi, tdo):
        self.count, self.tms, self.tdi, self.tdo = count, tms, tdi, tdo
    def _get_args(self):
        return [self.tdi], {'return_tdo':self.tdo, 'TMS': self.tms}

class DigilentWriteTMSTDIPrimative(Level1Primative, Executable):
    _driver_function_name = 'write_tms_tdi_bits'
    """TMS, TDI, TDO"""
    _effect = [SEQUENCE, SEQUENCE, CONSTANT]
    def __init__(self, count, tms, tdi, tdo):
        self.count, self.tms, self.tdi, self.tdo = count, tms, tdi, tdo
    def _get_args(self):
        return [self.tms, self.tdi], {'return_tdo':self.tdo}

class DigilentReadTDOPrimative(Level1Primative, Executable):
    _driver_function_name = 'read_tdo_bits'
    """TMS, TDI, TDO"""
    _effect = [CONSTANT, CONSTANT, ONE]
    def __init__(self, count, tms, tdi, tdo):
        self.count, self.tms, self.tdi, self.tdo = count, tms, tdi, tdo
    def _get_args(self):
        return [self.count], {'TMS': self.tms, 'TDI': self.tdi}

class LIESTDIHighPrimative(Level1Primative, Executable):
    _driver_function_name = 'lies_lies'
    """TMS, TDI, TDO"""
    _effect = [CONSTANT, ONE, ONE]
    def __init__(self, count, tms, tdi, tdo):
        self.count, self.tms, self.tdi, self.tdo = count, tms, tdi, tdo
    def _get_args(self):
        return [], {}


class DigilentAdeptController(CableDriver):
    _primatives = [DigilentWriteTDIPrimative, DigilentWriteTMSPrimative,
                   DigilentWriteTMSTDIPrimative, DigilentReadTDOPrimative,
                   LIESTDIHighPrimative]
    def __init__(self, dev, mock=False):
        super(DigilentAdeptController, self).__init__(dev)
        self.mock = mock
        if not mock:
            h = self._dev.open()

            self.serialNumber = h.controlRead(
                0xC0, 0xE4, 0, 0, 12).decode()
            self.name = index_or_default(
                h.controlRead(0xC0, 0xE2, 0, 0, 16)).decode()
            #This is probably subtly wrong...
            pidraw = h.controlRead(0xC0, 0xE9, 0, 0, 4)
            self.productId = (pidraw[3]<<24)|(pidraw[2]<<16)|\
                (pidraw[1]<<8)|pidraw[0] #%08x

            self.productName = index_or_default(
                h.controlRead(0xC0, 0xE1, 0, 0, 28)).decode()
            firmwareraw = h.controlRead(0xC0, 0xE6, 0, 0, 2)
            self.firmwareVersion = (firmwareraw[1]<<8)|firmwareraw[0]
            h.close()

            if (self.productId & 0xFF) <= 0x0F:
                self._cmdout_interface = 1
                self._cmdin_interface = 1
                self._datout_interface = 2
                self._datin_interface = 6
            else:
                self._cmdout_interface = 1
                self._cmdin_interface = 2
                self._datout_interface = 3
                self._datin_interface = 4

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
        h_ = self._handle
        h_.bulkWrite(self._cmdout_interface, b'\x03\x02\x00\x00')
        res = h_.bulkRead(self._cmdin_interface, 2)
        if res[1] != 0:
            raise JTAGControlError("Error enabling JTAG. Error code: %s." %res[1])
        self._jtagon = True

    def jtag_disable(self):
        if not self._jtagon: return
        self._jtagon = False
        h = self._handle
        h.bulkWrite(self._cmdout_interface, b'\x03\x02\x01\x00')
        res = h.bulkRead(self._cmdin_interface, 2)
        if res[1] != 0:
            raise JTAGControlError()

    def write_tms_bits(self, data, return_tdo=False, TDI=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if self._scanchain:
            self._scanchain._tap_transition_driver_trigger(data)


        self._handle.bulkWrite(self._cmdout_interface,
                               b'\x09\x02\x0b\x00'+bytes([return_tdo,
                                                          TDI])+\
                               b"".join([bytes([(len(data)>>(8*i))&0xff])
                                         for i in range(4)]))
        res = self._handle.bulkRead(self._cmdin_interface, 2)
        if res[1] != 0:
            raise JTAGControlError("Uknown Issue writing TMS bits: %s",
                                   res)

        self._handle.bulkWrite(self._datout_interface,
                               build_byte_align_buff(data).tobytes()[::-1])

        tdo_bits = None
        if return_tdo:
            res = self._handle.bulkRead(self._datin_interface,
                                        buff2Blen(data))[::-1]
            tdo_bits = bitarray()
            for byte_ in tdo_bytes:
                tdo_bits.extend(bin(byte_)[2:].zfill(8))

        self._handle.bulkWrite(
            self._cmdout_interface, bytes([0x03, 0x02,
                                           (0x80|0x0b), 0x00]))
        self._handle.bulkRead(self._cmdin_interface, 6) #Not checking for now

        return tdo_bits

    def write_tdi_bits(self, buff, return_tdo=False, TMS=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if self._scanchain:
            tms_bits = bitarray(('1' if TMS else '0')*len(buff))
            self._scanchain._tap_transition_driver_trigger(tms_bits)
            self._handle.bulkWrite(self._cmdout_interface,
                        b'\x09\x02\x08\x00'+bytes([return_tdo, TMS])+\
                        b"".join([bytes([(len(buff)>>(8*i))&0xff]) for
                        i in range(4)]))
        res = self._handle.bulkRead(self._cmdin_interface, 2)
        if res[1] != 0:
            raise JTAGControlError("Uknown Issue writing TDI bits: %s",
                                   res)

        self._handle.bulkWrite(self._datout_interface,
                               build_byte_align_buff(buff).tobytes()[::-1])

        tdo_bits = None
        if return_tdo is True:
            tdo_bytes = self._handle.bulkRead(self._datin_interface,
                                              buff2Blen(buff))[::-1]
            tdo_bits = bitarray()
            for byte_ in tdo_bytes:
                tdo_bits.extend(bin(byte_)[2:].zfill(8))

        self._handle.bulkWrite(self._cmdout_interface,
                               bytes([0x03, 0x02, (0x80|0x08), 0x00]))
        self._handle.bulkRead(self._cmdin_interface, 10) #Not checking this for now.

        return tdo_bits

    def write_tms_tdi_bits(self, tmsdata, tdidata, return_tdo=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if len(tmsdata) != len(tdidata):
            raise Exception("TMSdata and TDIData must be the same length")
        if self._scanchain:
            self._scanchain._tap_transition_driver_trigger(tmsdata)

        self._handle.bulkWrite(self._cmdout_interface,
                               b'\x08\x02\x0A\x00'+bytes([return_tdo])+\
                               b"".join([bytes([(len(tdidata)>>(8*i))&0xff])
                               for i in range(4)]))
        res = self._handle.bulkRead(self._cmdin_interface, 2)
        if res[1] != 0:
            raise JTAGControlError("Uknown Issue writing TMS bits: %s", res)

        data = bitarray([val for pair in zip(tmsdata, tdidata)
                         for val in pair])
        self._handle.bulkWrite(self._datout_interface,
                               build_byte_align_buff(data).tobytes()[::-1])

        tdo_bits = None
        if return_tdo:
            tdo_bytes = self._handle.bulkRead(self._datin_interface,
                                              buff2Blen(data))[::-1]
            tdo_bits = bitarray()
            for byte_ in tdo_bytes:
                tdo_bits.extend(bin(byte_)[2:].zfill(8))

        self._handle.bulkWrite(self._cmdout_interface,
                               bytes([0x03, 0x02, 0x80|0x0A, 0x00]))
        self._handle.bulkRead(self._cmdin_interface, 10) #Not checking for now. Number may be wrong

        return tdo_bits

    def read_tdo_bits(self, count, TMS=False, TDI=False):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        if self._scanchain:
            bits = bitarray(('1' if TMS else '0')*count)
            self._scanchain._tap_transition_driver_trigger(bits)

        #START REQUEST
        self._handle.bulkWrite(self._cmdout_interface,
                               b'\x09\x02\x09\x00'+bytes([TMS, TDI])+\
                               b"".join([bytes([(count>>(8*i))&0xff])
                                         for i in range(4)]))
        res = self._handle.bulkRead(self._cmdin_interface, 2)
        if res[1] != 0:
            raise JTAGControlError("Uknown Issue reading TDO bits: %s", res)

        #READ TDO DATA BACK
        tdo_bytes = self._handle.bulkRead(self._datin_interface,
                                          blen2Blen(count))[::-1]
        tdo_bits = bitarray()
        for byte_ in tdo_bytes:
            tdo_bits.extend(bin(byte_)[2:].zfill(8))

        #GET BACK STATS
        self._handle.bulkWrite(self._cmdout_interface,
                               b'\x03\x02' + bytes([0x0e, 0x02,
                                                    0x80|0x09, 0x00]))
        res = self._handle.bulkRead(self._cmdin_interface, 10)

        return tdo_bits



__filter__ = [((0x1443, None),DigilentAdeptController)]
