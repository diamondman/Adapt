from bitarray import bitarray

DOESNOTMATTER = 0
ZERO = 1
ONE = 2
CONSTANT = ZERO|ONE
SEQUENCE = CONSTANT|4

class Primative(object):
    _layer = None
    _is_macro = False
    def __init__(self):
        self._staged = False
        self._committed = False

    def _stage(self, fsm_state):
        if self._staged:
            raise Exception("Primative already staged")
        self._staged = True
        return True

    def _commit(self, trans):
        if not self._staged:
            raise Exception("Primative must be staged before commit.")
        if self._committed:
            raise Exception("Primative already committed.")
        self._committed = True
        return False

class Executable(object):
    def execute(self):
        print "Executing", self.__class__.__name__

class Level1Primative(Primative):
    _layer = 1
    _effect = [0, 0, 0]
    def __repr__(self):
        return "<%s(TMS:%s; TDI:%s; TDO:%s)>"%(self.__class__.__name__, self.tms, self.tdi, self.tdo)
class Level2Primative(Primative):
    _layer = 2
class Level3Primative(Primative):
    _layer = 3
    _is_macro = True




##########################################################################################
#LV3 Primatives

class DefaultRunInstructionPrimative(Level3Primative):
    def __init__(self, device, insname, read=True, execute=True,
                 loop=0, arg=None, delay=0, expret=None):
        super(DefaultRunInstructionPrimative, self).__init__()
        self.insname = insname
        self.inscode = device.desc._instructions[insname]
        self.read = read
        self.execute = execute
        self.arg = arg

    def _expand_macro(self, command_queue):
        macro = [command_queue.sc._lv2_primatives.get('load_ir')(self.inscode, read=self.read)]

        if self.arg is not None:
            macro.append(command_queue.sc._lv2_primatives.get('load_dr')(self.arg, False))

        if self.execute:
            macro.append(command_queue.sc._lv2_primatives.get('transition_tap')("RTI"))

        #TODO ADD DELAY
        #TODO ADD READ
        return macro


##########################################################################################
#LV2 Primatives

class DefaultChangeTAPStatePrimative(Level2Primative):
    _function_name = 'transition_tap'
    def __init__(self, state):
        super(DefaultChangeTAPStatePrimative, self).__init__()
        self._targetstate = state
        self._startstate = None

    def _stage(self, fsm_state):
        super(DefaultChangeTAPStatePrimative, self)._stage(fsm_state)
        self._startstate = fsm_state
        return self._targetstate != fsm_state

    def _commit(self, command_queue):
        super(DefaultChangeTAPStatePrimative, self)._commit(command_queue)
        self._bits = command_queue.fsm.calc_transition_to_state(self._targetstate)
        command_queue.fsm.state = self._targetstate
        return False

    @property
    def required_effect(self):
        if not self._staged:
            raise Exception("required_effect is only available after staging")
        return [SEQUENCE,
                ZERO,
                DOESNOTMATTER]

    def get_effect_bits(self):
        return [len(self._bits), self._bits, 0, 0]

    def __repr__(self):
        return "<TAPTransition(%s=>%s)>"%(self._startstate if self._startstate
                                          else '?', self._targetstate)

class DefaultLoadReadRegisterPrimative(Level2Primative):
    _function_name = '_load_register'
    def __init__(self, data, read=False):
        super(DefaultLoadReadRegisterPrimative, self).__init__()
        self.data = data
        self.read = read

    def _stage(self, fsm_state):
        super(DefaultLoadReadRegisterPrimative, self)._stage(fsm_state)
        return fsm_state in ["SHIFTIR", "SHIFTDR"]

    def _commit(self, command_queue):
        super(DefaultLoadReadRegisterPrimative, self)._commit(command_queue)
        command_queue.fsm.transition_bit(1)
        return self.read

    @property
    def required_effect(self):
        if not self._staged:
            raise Exception("required_effect is only available after staging")
        return [SEQUENCE,
                SEQUENCE,
                ONE if self.read else DOESNOTMATTER] #TMS TDI TDO

    def get_effect_bits(self):
        return [len(self.data),
                self.data,
                bitarray((len(self.data)-1)*'0'+"1"), 
                self.read]

    def __repr__(self):
        return "<LOAD/READREGISTER(%s bits, %sRead)>"%(len(self.data),
                                                       '' if self.read else 'No')

class DefaultLoadDRPrimative(Level2Primative):
    _function_name = 'load_dr'
    _is_macro = True
    def __init__(self, data, read):
        super(DefaultLoadDRPrimative, self).__init__()
        self.data = data
        self.read = read

    def _expand_macro(self, command_queue):
        return [command_queue.sc._lv2_primatives.get('transition_tap')("SHIFTDR"),
                command_queue.sc._lv2_primatives.get('_load_register')(self.data, read=self.read)]

    def __repr__(self):
        return "<LoadDR(%s bits, %sRead)>"%(len(self.data),
                                            '' if self.read else 'No')

class DefaultLoadIRPrimative(Level2Primative):
    _function_name = 'load_ir'
    _is_macro = True
    def __init__(self, data, read):
        super(DefaultLoadIRPrimative, self).__init__()
        self.data = data
        self.read = read

    def _expand_macro(self, command_queue):
        return [command_queue.sc._lv2_primatives.get('transition_tap')("SHIFTIR"),
                command_queue.sc._lv2_primatives.get('_load_register')(self.data, read=self.read)]


    def __repr__(self):
        return "<LoadIR(%s bits, %sRead)>"%(len(self.data),
                                            '' if self.read else 'No')
