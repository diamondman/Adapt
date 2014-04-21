from bitarray import bitarray
from primative import DefaultRunInstructionPrimative
from jtagDeviceDescription import JTAGDeviceDescription

import struct
import sys

class JTAGDevice(object):
    def __init__(self, chain, idcode):
        #if not isinstance(chain, JTAGScanChain):
        #    raise ValueError("JTAGDevice requires an instnace of JTAGScanChain")
        self._chain = chain

        if isinstance(idcode, int):
            self._id = idcode
        elif isinstance(idcode, bitarray):
            if len(idcode) is not 32:
                raise ValueError("JTAGDevice idcode parameter must be an "
                                 "int, a string of length 4, or a bitarray "
                                 "of 32 bits (%s len: %s)"%(idcode,len(idcode)))
            self._id = struct.unpack("<L", idcode.tobytes()[::-1])[0]
        elif isinstance(idcode, str):
            if len(idcode) is not 4:
                raise ValueError("JTAGDevice idcode parameter must be an "
                                 "int, a string of length 4, or a bitarray "
                                 "of 32 bits (%s len: %s)"%(idcode,len(idcode)))
            self._id = struct.unpack("<L", idcode[::-1])[0]
        else:
            raise ValueError("JTAGDevice idcode parameter must be an int or "
                             "string of length 4. (Invalid Type: %s)"%type(idcode))

        self.desc = JTAGDeviceDescription.get_descriptor_for_idcode(self._id)


    def run_tap_instruction(self, *args, **kwargs):
        self._chain._command_queue.append(
            DefaultRunInstructionPrimative(self, *args, **kwargs))

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
