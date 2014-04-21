import math
import time
import struct
from bitarray import bitarray

from jtagDeviceDescription import JTAGDeviceDescription
from jtagStateMachine import JTAGStateMachine
from primative import Level1Primative, Level2Primative, Level3Primative, Executable,\
    DOESNOTMATTER, ZERO, ONE, CONSTANT, SEQUENCE,\
    DefaultRunInstructionPrimative,\
    DefaultChangeTAPStatePrimative, DefaultLoadIRPrimative, DefaultReadDRPrimative, \
    DefaultLoadDRPrimative, DefaultLoadReadRegisterPrimative
from jtagDevice import JTAGDevice
from command_queue import CommandQueue
from jtagUtils import NULL_ID_CODES, pstatus

class JTAGScanChain(object):
    def gen_prim_adder(self, cls_):
        if not hasattr(self, cls_._function_name):
            def adder(*args, **kwargs):
                self._command_queue.append(cls_(*args, **kwargs))
                return self._command_queue.get_return()
            setattr(self, cls_._function_name, adder)
            self._lv2_primatives[cls_._function_name] = cls_
            #print "Adding %s OK"%cls_
            return True
        #print "Adding %s FAIL"%cls_
        return False

    def __init__(self, controller):
        print "Starting a scan chain with", controller

        self._devices = []
        self._hasinit = False
        self._sm = JTAGStateMachine()

        self._controller = controller
        self._controller._scanchain = self #This might necessitate a factory

        self._command_queue = CommandQueue(self)

        self._lv1_primatives = []
        self._lv2_primatives = {}
        for primative in self._controller._primatives:
            if issubclass(primative, Level2Primative):
                if not self.gen_prim_adder(primative):
                    raise Exception("Failed adding primative %s, primative with name %s "\
                                        "already exists on scanchain"%\
                                        (primative, primative._function_name))
            elif issubclass(primative, Level1Primative):
                self._lv1_primatives.append(primative)
            else:
                print "WTF", primative

        for primative_cls in [DefaultChangeTAPStatePrimative,
                              DefaultLoadIRPrimative,
                              DefaultReadDRPrimative,
                              DefaultLoadDRPrimative,
                              DefaultLoadReadRegisterPrimative]:
            self.gen_prim_adder(primative_cls)

    def init_chain(self, mock=False):
        if not self._hasinit:
            if mock:
                self._devices = [JTAGDevice(self, bitarray('00000110110101001000000010010011')),
                                 JTAGDevice(self, bitarray('00000110111001011000000010010011'))]
                return

            self._devices = []

            self.jtag_enable()
            idcode_str = self.read_dr(32)
            while idcode_str not in NULL_ID_CODES:
                Jdev = JTAGDevice(self, idcode_str)
                self._devices.append(Jdev)
                idcode_str = self.read_dr(32)
            self.jtag_disable()

            #The chain comes out last first. Reverse it to get order.
            self._devices.reverse()

    def flush(self):
        self._command_queue.flush()

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

