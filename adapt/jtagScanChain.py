import math
import time
import struct
from bitarray import bitarray

from jtagDeviceDescription import JTAGDeviceDescription
from jtagStateMachine import JTAGStateMachine
from jtagUtils import NULL_ID_CODES, pstatus

class JTAGScanChain(object):
    def __init__(self, controller):
        self._controller = controller
        self._controller._scanchain = self #This might necessitate a factory
        self._sm = JTAGStateMachine()
        self._hasinit = False
        self._devices = []

    def init_chain(self):
        if not self._hasinit:
            self._devices = []

            self.jtag_enable()
            idcode_str = self.read_dr_bits(32)
            while idcode_str not in NULL_ID_CODES:
                Jdev = JTAGDevice(self, idcode_str)
                self._devices.append(Jdev)
                idcode_str = self.read_dr_bits(32)
            self.jtag_disable()

            #The chain comes out last first. Reverse it to get order.
            self._devices.reverse()

    def write_ir_bits(self, data, read=False):
        self.transition_tap("SHIFTIR")
        if len(data) > 1:
            res = self._controller.write_tdi_bits(data[1:], return_tdo=read)[1:]
        else:
            res = bitarray()

        return self._controller.write_tdi_bits(data[0:1], TMS=True, return_tdo=read)[7:]+res
        

    def write_dr_bits(self, data, read=False, finish=True):
        self.transition_tap("SHIFTDR")
        if len(data) == 0:
            return

        if not finish:
            return self._controller.write_tdi_bits(data, return_tdo=read)
        else:
            res = self._controller.write_tdi_bits(data[1:], return_tdo=read)
            self._controller.write_tdi_bits(data[0:1], TMS=True)
            return res #TODO fix return

    def read_dr_bits(self, count):
        self.transition_tap("SHIFTDR")
        return self._controller.read_tdo_bits(count)

    def transition_tap(self, state):
        if state == self._sm.state:
            return

        data = self._sm.calc_transition_to_state(state)
        self._controller.write_tms_bits(data)

    def run_tap_idle(self, cycles):
        self.transition_tap("RTI")
        if cycles>1:
            self._controller.write_tms_bits(bitarray('0'*(cycles-1)))

    def jtag_disable(self):
        self._sm.state = "_PRE5"
        self._controller.jtag_disable()

    def jtag_enable(self):
        self._sm.state = "_PRE5"
        self._controller.jtag_enable()

    def _tap_transition_driver_trigger(self, bits):
        statetrans = [self._sm.state]
        for bit in bits[::-1]:
            self._sm.transition_bit(bit)
            statetrans.append(self._sm.state)

class JTAGDevice(object):
    def __init__(self, chain, idcode):
        if not isinstance(chain, JTAGScanChain):
            raise ValueError("JTAGDevice requires an instnace of JTAGScanChain")
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

    def run_tap_instruction(self, insname, read=True, execute=True, 
                            loop=0, arg=None, delay=0, expret=None):
        ins = self.desc._instructions[insname]
        res = self._chain.write_ir_bits(ins, read=read)

        if arg is not None:
            self._chain.write_dr_bits(arg)
 
        if execute:
            self._chain.run_tap_idle(loop+1)

        if delay:
            time.sleep(delay)

        if read:
            if expret and res != expret:
                print "MISMATCH status on ins %s. Expected %s"%(insname, expret.__repr__())
                print "GOT:", res
                print
                pstatus(res)
            return res

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
