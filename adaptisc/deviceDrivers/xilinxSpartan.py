# -*- coding: utf-8 -*-
"""Special thanks to the xilprg project for having configuration
details and device lists for several spartan and virtex
families. Saved me a lot of time.
https://github.com/makestuff/xilprg-nero/blob/d6dfc089db326d71c38cdfce1506b6c7353c374a/xilinx.cpp

"""

from proteusisc.jtagDevice import JTAGDevice
from proteusisc.bittypes import ConstantBitarray, bitarray

from adaptisc.bitparse import BitFile

def bitify(data):
    bits = bitarray()
    bits.frombytes(data)
    return bits

DUMMY     = b"\xFF\xFF\xFF\xFF"
FLUSH     = b"\x00\x00\x00\x00"
SYN       = b"\xAA\x99\x55\x66"
WRITE_CMD = b"\x30\x00\x80\x01"
WRITE_COR = b"\x30\x01\x20\x01"
CMD_AHIGH = b"\x00\x00\x00\x08"
CMD_START = b"\x00\x00\x00\x05"
CMD_RCRC  = b"\x00\x00\x00\x07"

class XilinxSpartan2(JTAGDevice):
    devices = (
        b'\x00\x60\x80\x93', #xc2s15
        b'\x00\x60\xC0\x93', #xc2s30
        b'\x00\x61\x00\x93', #xc2s50
        b'\x00\x61\x40\x93', #xc2s100
        b'\x00\x61\x80\x93', #xc2s150
        b'\x00\x61\xC0\x93', #xc2s200
    )
    def program(self, confpath):
        print("NOTICE! The Spartan 2/E programming has not been tested. "
              "Please report success or errors to the project maintainer.")
        bf = BitFile(confpath)

        # COR data sets SHUTDOWN = 1
        bits = bitify(FLUSH+\
                      SYNC+\
                      WRITE_COR+\
                      b'\xBC\xFD\x05\x00'+\
                      WRITE_CMD+\
                      CMD_START+\
                      WRITE_CMD+\
                      CMD_RCRC+\
                      FLUSH)
        self.run_instruction("CFG_IN", data=bits)
        #prg->reset_tap_state();

        self.run_instruction("JSTART", data=ConstantBitarray(False, 13))
        #prg->reset_tap_state();

        # COR data sets SHUTDOWN = 0
        bits = bitify(FLUSH + SYNC+\
                      WRITE_CMD+\
                      CMD_AHIGH+\
                      WRITE_COR+\
                      b'\xFF\xFC\x05\x00'+\
                      WRITE_CMD+\
                      CMD_START+\
                      WRITE_CMD+\
                      CMD_RCRC+\
                      FLUSH)
        self.run_instruction("CFG_IN", data=bits)
        #prg->reset_tap_state();

        self.run_instruction("JSTART", data=ConstantBitarray(False, 13))
        #prg->reset_tap_state();

        # COR data sets SHUTDOWN = 1
        bits = bitify(FLUSH + SYNC+\
                      WRITE_COR+\
                      b'\xB4\xFD\x05\x00'+\
                      WRITE_CMD+\
                      CMD_START+\
                      WRITE_CMD+\
                      CMD_RCRC+\
                      FLUSH)
        self.run_instruction("CFG_IN", data=bits)
        #prg->reset_tap_state();

        self.run_instruction("JSTART", data=ConstantBitarray(False, 13))
        #prg->reset_tap_state();

        databits = bitarray()
        databits.frombytes(FLUSH)
        self.run_instruction("CFG_IN", data=bf.to_bitarray()+databits)
        #prg->reset_tap_state();

        self.run_instruction("JSTART", data=ConstantBitarray(False, 13))
        #prg->reset_tap_state();

        _, status = self.run_instruction("BYPASS", read_status=True)
        if not status()[2]:
            #attribute INSTRUCTION_CAPTURE : entity is "XXX01";
            #Bit 4 of instruction capture is PROGRAM.
            #Bit 3 is INIT.
            #Bit 2 is DONE.
            raise Exception("DONE bit didn't go high!")


class XilinxSpartan2E(XilinxSpartan2):
    devices = (
        b'\x00\xA1\x00\x93', #xc2s50e
        b'\x00\xA1\x40\x93', #xc2s100e
        b'\x00\xA1\x80\x93', #xc2s150e
        b'\x00\xA1\xC0\x93', #xc2s200e
        b'\x00\xA2\x00\x93', #xc2s300e
        b'\x00\xA2\x80\x93', #xc2s400e
        b'\x00\xA3\x00\x93', #xc2s600e
    )


class XilinxSpartan3(JTAGDevice):
    devices = (
        b'\x01\x40\xD0\x93', #xc3s50
        b'\x01\x41\x40\x93', #xc3s200
        b'\x01\x41\xC0\x93', #xc3s400
        b'\x01\x42\x80\x93', #xc3s1000
        b'\x01\x43\x40\x93', #xc3s1500
        b'\x01\x44\x00\x93', #xc3s2000
        b'\x01\x44\x80\x93', #xc3s4000
        b'\x01\x45\x00\x93', #xc3s5000
    )

    def program(self, confpath):
        """
        Described in https://www.xilinx.com/support/documentation/user_guides/ug012.pdf
        """
        bf = BitFile(confpath);

        self.run_instruction("JPROGRAM", loop=10000)
        resetbits = bitify(DUMMY + SYN +\
                           WRITE_CMD + CMD_RCRC+\
                           FLUSH + FLUSH)
        self.run_instruction("CFG_IN", data=resetbits)
        self.run_instruction("JSHUTDOWN", loop=12)

        self.run_instruction(
            "CFG_IN", data=bitify(WRITE_CMD + CMD_AHIGH + FLUSH + FLUSH));
        self.run_instruction("CFG_IN", data=bf.to_bitarray());
        self.run_instruction("JSTART", loop=12)

        _, status = self.run_instruction("BYPASS", read_status=True)
        if not status()[0]:
            #attribute INSTRUCTION_CAPTURE : entity is "XXXX01";
            #Bit 5 is 1 when DONE is released (part of startup sequence)
            #Bit 4 is 1 if house-cleaning is complete
            #Bit 3 is ISC_Enabled
            #Bit 2 is ISC_Done
            raise Exception("DONE bit didn't go high!")




#resetdata = bitarray('11111111111111111111111111111111')+\
#            bitarray('10101010100110010101010101100110')+\
#            bitarray('00110000000000001000000000000001')+\
#            bitarray('00000000000000000000000000000111')+\
#            bitarray('0'*32)+bitarray('0'*32)


class XilinxSpartan3E(XilinxSpartan3):
    devices = (
        b'\x01\xC1\x00\x93', #xc3s100e
        b'\x01\xC1\xA0\x93', #xc3s250e
        b'\x01\xC2\x20\x93', #xc3s500e
        b'\x01\xC2\xE0\x93', #xc3s1200e
        b'\x01\xC3\xA0\x93', #xc3s1600e
    )



class XilinxSpartan6(JTAGDevice):
    devices = (
        b'\x04\x00\x00\x93', #XC6SLX4
        b'\x04\x00\x10\x93', #XC6SLX9
        b'\x04\x00\x20\x93', #XC6SLX16
        b'\x04\x00\x40\x93', #XC6SLX25
        b'\x04\x02\x40\x93', #XC6SLX25T
        b'\x04\x00\x80\x93', #XC6SLX45
        b'\x04\x02\x80\x93', #XC6SLX45T
        b'\x04\x00\xE0\x93', #XC6SLX75
        b'\x04\x02\xE0\x93', #XC6SLX75T
        b'\x04\x01\x10\x93', #XC6SLX100
        b'\x04\x03\x10\x93', #XC6SLX100T
        b'\x04\x01\xD0\x93', #XC6SLX150
        b'\x04\x03\xD0\x93', #XC6SLX150T
    )

    def program(self, confpath):
        """
        Described in https://www.xilinx.com/support/documentation/user_guides/ug012.pdf
        """
        bf = BitFile(confpath);

        self.run_instruction("JPROGRAM", loop=10000)
        self.run_instruction("JSHUTDOWN", loop=12)

        self.run_instruction(
            "CFG_IN", data=bitify(WRITE_CMD + (CMD_AHIGH + FLUSH + FLUSH)));
        self.run_instruction("CFG_IN", data=bf.to_bitarray());
        self.run_instruction("JSTART", loop=16)

        _, status = self.run_instruction("BYPASS", read_status=True)
        if not status()[0]:
            #attribute INSTRUCTION_CAPTURE : entity is "XXXX01";
            #Bit 5 is 1 when DONE is released (part of startup sequence)
            #Bit 4 is 1 if house-cleaning is complete
            #Bit 3 is ISC_Enabled
            #Bit 2 is ISC_Done
            raise Exception("DONE bit didn't go high!")
