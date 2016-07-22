from proteusisc.jtagDevice import JTAGDevice

class JTAGDeviceXC2C256(JTAGDevice):
    def erase(self):
        self._chain.jtag_enable()

        self.run_tap_instruction("BYPASS", delay=0.01)

        self.run_tap_instruction("ISC_ENABLE", loop=8, delay=0.01)

        self.run_tap_instruction("ISC_ERASE", loop=8, delay=0.01)

        self.run_tap_instruction("ISC_INIT", loop=8, delay=0.01) #DISCHARGE

        self.run_tap_instruction("ISC_INIT", loop=8, arg=bitarray(), delay=0.01)

        self.run_tap_instruction("ISC_DISABLE", loop=8, delay=0.01)#, expret=bitarray('00010001'))

        print(self.run_tap_instruction("BYPASS", delay=0.01))#, expret=bitarray('00100001'))

        self._chain.transition_tap("TLR")

        self._chain.jtag_disable()

    def program(self, configfile):
        bitstream = configfile.to_bitstream(self.desc)

        self._chain.jtag_enable()

        self.run_tap_instruction("BYPASS", delay=0.01)

        self.run_tap_instruction("ISC_ENABLE", loop=8, delay=0.01)

        for r in bitstream.segments:
            self.run_tap_instruction("ISC_PROGRAM", arg=r, loop=8, delay=0.01)

        self.run_tap_instruction("ISC_INIT", loop=8, delay=0.01) #DISCHARGE

        self.run_tap_instruction("ISC_INIT", loop=8, arg=bitarray(), delay=0.01)

        self.run_tap_instruction("ISC_DISABLE", loop=8, delay=0.01)#, expret=bitarray('00010101'))

        self.run_tap_instruction("BYPASS")#, expret=bitarray('00100101'))

        self._chain.transition_tap("TLR")

        self._chain.jtag_disable()
