from bitarray import bitarray

from cabledriver import CableDriver
from primative import Level2Primative, Executable

class OpenJtagChangeTAPStatePrimative(Level2Primative, Executable):
    _function_name = 'transition_tap'
    _driver_function_name = 'change_TAP_state'
    def __init__(self, state):
        super(OpenJtagChangeTAPStatePrimative, self).__init__()
        self._targetstate = state
        self._startstate = None

    def _stage(self, fsm_state):
        super(OpenJtagChangeTAPStatePrimative, self)._stage(fsm_state)
        self._startstate = fsm_state
        return self._targetstate != fsm_state

    def _commit(self, command_queue):
        super(OpenJtagChangeTAPStatePrimative, self)._commit(command_queue)
        command_queue.fsm.state = self._targetstate
        return False

    def _get_args(self):
        return [self._targetstate], {}

    def __repr__(self):
        return "<OpenJtag TAPTransition(%s=>%s)>"%(self._startstate if self._startstate
                                          else '?', self._targetstate)

class OpenJtagLoadReadRegisterPrimative(Level2Primative, Executable):
    _function_name = '_load_register'
    _driver_function_name = 'loadread_reg'
    def __init__(self, data, read):
        super(OpenJtagLoadReadRegisterPrimative, self).__init__()
        self.data = data
        self.read = read

    def _stage(self, fsm_state):
        super(OpenJtagLoadReadRegisterPrimative, self)._stage(fsm_state)
        return fsm_state in ["SHIFTIR", "SHIFTDR"]

    def _commit(self, command_queue):
        super(OpenJtagLoadReadRegisterPrimative, self)._commit(command_queue)
        command_queue.fsm.transition_bit(1)
        return self.read

    def _get_args(self):
        return [self.data, self.read], {}

    def __repr__(self):
        return "<OpenJtag LOAD/READREGISTER(%s bits, %sRead)>"%(len(self.data),
                                                       '' if self.read else 'No')

class OpenJtagDriver(CableDriver):
    _primatives = [OpenJtagChangeTAPStatePrimative, OpenJtagLoadReadRegisterPrimative]
    def __init__(self, dev, mock=False):
        self.mock = mock
        self._dev = dev
        self.name = "OpenJTAGv1"

    def change_TAP_state(self, state):
        pass

    def loadread_reg(self, data, read):
        pass

    def jtag_enable(self):
        pass

    def jtag_disable(self):
        pass


__filter__ = [((0x0403, 0x6001),OpenJtagDriver)]
