from proteusisc.jtagDevice import JTAGDevice
from proteusisc.bittypes import ConstantBitarray, bitarray

from adaptisc.jedparse import JedecConfigFile

class JTAGDeviceXC2C256(JTAGDevice):
    devices = (
        b'\x06\xd4\xc0\x93', #XC2C256
    )
    def erase(self):
        self.run_instruction("ISC_ENABLE", delay=0.8)

        self.run_instruction("ISC_ERASE", delay=10)

        self.run_instruction("ISC_INIT", delay=0.02, #DISCHARGE
                             data=ConstantBitarray(True, 1371))

        self.run_instruction("ISC_INIT", delay=0.01,
                             data=ConstantBitarray(True, 1371))

        _, status = self.run_instruction("ISC_DISABLE", loop=8,
                                         read_status=True)

        self.run_instruction("BYPASS", delay=0.01)

        print("Post-DISABLE Status:", status())
        self.pstatus(status())

    def program(self, configpath):
        configfile = JedecConfigFile(pargs.file)
        from .map import data as mapdata
        bitstream = configfile.to_bitstream("xc2c256", 1371, mapdata)

        print("Erasing device...")
        self.erase()

        self.run_instruction("ISC_ENABLE", delay=0.8)

        for r in bitstream.segments:
            self.run_instruction("ISC_PROGRAM", data=r, delay=10)

        self.run_instruction("ISC_INIT", delay=0.12) #DISCHARGE

        self.run_instruction("ISC_INIT", delay=0.8,
                             data=ConstantBitarray(True, 1371))

        _, status = self.run_instruction("ISC_DISABLE", read_status=True)

        self.run_instruction("BYPASS")

        print("Post Program Status:", status())
        self.pstatus(status())

    @staticmethod
    def pstatus(resflags):
        if not resflags&bitarray('11000011'):
            print(resflags, bitarray('11000011'))
            print(resflags&bitarray('11000011'))
            print()
        print("STATUS: "+
              ("" if (resflags&bitarray('11000011')==bitarray('00000001'))
               else "INVALID_STATUS ")+\
            ("ISCDIS " if resflags[-6] else "")+\
              ("ISCEN " if resflags[-5] else "")+\
            ("SECURE " if resflags[-4] else "")+\
              ("DONE " if resflags[-3] else ""))
