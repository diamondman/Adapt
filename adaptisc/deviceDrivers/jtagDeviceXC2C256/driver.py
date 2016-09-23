from proteusisc.jtagDevice import JTAGDevice
from proteusisc.bittypes import ConstantBitarray
from bitarray import bitarray

class JTAGDeviceXC2C256(JTAGDevice):
    def erase(self):
        self._chain.jtag_enable()

        self.run_instruction("BYPASS")

        self.run_instruction("ISC_ENABLE", loop=8, delay=0.01)

        self.run_instruction("ISC_ERASE", loop=8, delay=0.01)

        self.run_instruction("ISC_INIT", loop=8,
                             data=ConstantBitarray(True, 1371),
                             delay=0.01) #DISCHARGE

        self.run_instruction("ISC_INIT", loop=8,
                             data=ConstantBitarray(True, 1371),
                             delay=0.01)

        _, status = self.run_instruction("ISC_DISABLE", loop=8, delay=0.01, read_status=True)

        self.run_instruction("BYPASS", delay=0.01)

        print("Post-DISABLE Status:", status())
        self.pstatus(status())

        self._chain.jtag_disable()

    def program(self, configfile):
        from .map import data as mapdata
        #bitstream = configfile.to_bitstream(self.desc)
        bitstream = configfile.to_bitstream("xc2c256", 1371, mapdata)

        self._chain.jtag_enable()

        self.run_instruction("BYPASS", delay=0.01)

        self.run_instruction("ISC_ENABLE", delay=0.8)

        for r in bitstream.segments:
            self.run_instruction("ISC_PROGRAM", data=r, delay=10)

        self.run_instruction("ISC_INIT", delay=0.02) #DISCHARGE

        self.run_instruction("ISC_INIT", data=ConstantBitarray(True, 1371), delay=0.8)

        _, status = self.run_instruction("ISC_DISABLE", read_status=True)

        self.run_instruction("BYPASS")

        print("Post Program Status:", status())
        self.pstatus(status())

        self._chain.jtag_disable()

    @staticmethod
    def pstatus(resflags):
        #print(resflags.__repr__()))
        #if len(resflags)>1:
        #    resflags = resflags[0]
        if not resflags&bitarray('11000011'):
            print(resflags, bitarray('11000011'))
            print(resflags&bitarray('11000011'))
            print()
        print("STATUS: "+("" if (resflags&bitarray('11000011')==bitarray('00000001'))
                          else "INVALID_STATUS ")+\
            ("ISCDIS " if resflags[-6] else "")+("ISCEN " if resflags[-5] else "")+\
            ("SECURE " if resflags[-4] else "")+("DONE " if resflags[-3] else ""))
