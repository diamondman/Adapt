import struct
import time
import sys

from bitarray import bitarray

from .primative import DefaultRunInstructionPrimative
from .jtagDeviceDescription import JTAGDeviceDescription
from .jtagUtils import pstatus

class JTAGDeviceBase(object):
    def __init__(self, chain, idcode):
        self._chain = chain
        self._current_DR = None

        fail = False
        if isinstance(idcode, int):
            if len(bin(idcode)[2:]) > 32:
                fail = True
            else:
                self._id = idcode
        elif isinstance(idcode, bitarray):
            if len(idcode) is not 32:
                fail = True
            else:
                self._id = struct.unpack("<L", idcode.tobytes()[::-1])[0]
        elif isinstance(idcode, str):
            if len(idcode) is not 4:
                fail = True
            else:
                self._id = struct.unpack("<L", idcode[::-1])[0]
        else:
            raise ValueError("JTAGDevice idcode parameter must be an int or "
                             "string of length 4. (Invalid Type: %s)"%type(idcode))
        if fail:
            raise ValueError("JTAGDevice idcode parameter must be a 32 "
                             "bit int, a string of length 4, or a bitarray "
                             "of 32 bits (%s len: %s)"%(idcode,len(idcode)))

        if not self._id & 1:
            raise Exception("Invalid JTAG ID Code: LSB must be 1 (IEEE 1149.1)")

        self._desc = None

    def run_tap_instruction(self, *args, **kwargs):
        expret = kwargs.pop('expret', None)
        self._chain._command_queue.append(
            DefaultRunInstructionPrimative(self, *args, **kwargs))
        res = self._chain._command_queue.get_return()
        if expret and res != expret:
            print("MISMATCH status on ins %s. Expected %s"%\
                  (args[0], expret.__repr__()))
            print("GOT:", res, "\n")
            pstatus(res)
        return res


class JTAGDevice(JTAGDeviceBase):
    def __init__(self, chain, idcode):
        super(JTAGDevice, self).__init__(chain, idcode)
        self._desc = self._chain.get_descriptor_for_idcode(self._id)
