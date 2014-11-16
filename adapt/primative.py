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
        print("Executing", self.__class__.__name__)

class Level1Primative(Primative):
    _layer = 1
    _effect = [0, 0, 0]
    def __repr__(self):
        tms = self.tms
        tdi = self.tdi
        tdo = self.tdo
        if isinstance(self.tdi, bitarray):
            if len(self.tdi)>30:
                tdi = "%s...(%s bits)"%(tdi[0:30], len(tdi))
        if isinstance(self.tms, bitarray):
            if len(self.tms)>30:
                tms = "%s...(%s bits)"%(tms[0:30], len(tms))
        return "<%s(TMS:%s; TDI:%s; TDO:%s)>"%(self.__class__.__name__, tms, tdi, tdo)
class Level2Primative(Primative):
    _layer = 2
class Level3Primative(Primative):
    _layer = 3
    _is_macro = True




##########################################################################################
#LV3 Primatives

class DefaultRunInstructionPrimative(Level3Primative):
    def __init__(self, device, insname, read=True, execute=True,
                 loop=0, arg=None, delay=0):
        super(DefaultRunInstructionPrimative, self).__init__()
        self.insname = insname
        self.read = read
        self.execute = execute
        self.arg = arg
        self.delay = delay
        self.target_device = device

    def _expand_macro(self, command_queue):
        devices = command_queue.sc._devices

        out_ir = bitarray()
        for i, dev in enumerate(devices):
            if dev is self.target_device:
                instruction = self.insname
            else:
                instruction = 'BYPASS'
            dev._current_DR = dev.desc._ins_reg_map[instruction]
            #print("Dev %s DR: %s"%(i, dev._current_DR))
            inscode = dev.desc._instructions[instruction]
            out_ir.extend(inscode)

        #print("OUTIR:", out_ir)
        #print()

        macro = [command_queue.sc._lv2_primatives.get('load_ir')(out_ir, read=self.read)]

        if self.arg is not None:
            out_dr = bitarray()
            if self.arg != bitarray():
                for dev in devices:
                    if dev is self.target_device:
                        out_dr.extend(self.arg)
                    else:
                        out_dr.extend('0')
            macro.append(command_queue.sc._lv2_primatives.get('load_dr')(out_dr, False))

        if self.execute:
            macro.append(command_queue.sc._lv2_primatives.get('transition_tap')("RTI"))

        if self.delay:
            macro.append(command_queue.sc._lv2_primatives.get('sleep')(self.delay))
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
    def __init__(self, data, read=False, TMSLast=True, bitcount=None):
        super(DefaultLoadReadRegisterPrimative, self).__init__()
        self.data = data
        self.read = read
        self.TMSLast = TMSLast
        self.bitcount=bitcount

    def _stage(self, fsm_state):
        super(DefaultLoadReadRegisterPrimative, self)._stage(fsm_state)
        if fsm_state not in ["SHIFTIR", "SHIFTDR"]:
            return False

        if not ((self.bitcount if self.bitcount else len(self.data))>0):
            return False
        return True

    def _commit(self, command_queue):
        super(DefaultLoadReadRegisterPrimative, self)._commit(command_queue)
        if self.TMSLast:
            command_queue.fsm.transition_bit(1)
        return self.read

    @property
    def required_effect(self):
        if not self._staged:
            raise Exception("required_effect is only available after staging")
        return [SEQUENCE if self.TMSLast else ZERO,
                CONSTANT if self.bitcount else SEQUENCE,
                ONE if self.read else DOESNOTMATTER] #TMS TDI TDO

    def get_effect_bits(self):
        TMS = 0
        if self.TMSLast:
            TMS = bitarray("1"+(len(self.data)-1)*'0')
        return [self.bitcount if self.bitcount else len(self.data),
                TMS, #TMS
                self.data, #TDI
                self.read] #TDO

    def __repr__(self):
        return "<LOAD/READREGISTER(%s bits, %sRead)>"%(
            self.bitcount if self.bitcount else len(self.data),
            '' if self.read else 'No')

class DefaultReadDRPrimative(Level2Primative):
    _function_name = 'read_dr'
    _is_macro = True
    def __init__(self, bitcount):
        super(DefaultReadDRPrimative, self).__init__()
        self.bitcount = bitcount

    def _expand_macro(self, command_queue):
        return [command_queue.sc._lv2_primatives.get('transition_tap')("SHIFTDR"),
                command_queue.sc._lv2_primatives.get('_load_register')(
                    False, read=True, TMSLast=False, bitcount=self.bitcount)]

    def __repr__(self):
        return "<ReadDR(%s bits)>"%(len(self.data))

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


class DefaultSleepPrimative(Level2Primative, Executable):
    _function_name = 'sleep'
    _driver_function_name = 'sleep'
    def __init__(self, delay):
        super(DefaultSleepPrimative, self).__init__()
        self.delay = delay

    def _stage(self, fsm_state):
        super(DefaultSleepPrimative, self)._stage(fsm_state)
        return self.delay>0

    def _get_args(self):
        return [self.delay], {}

    def __repr__(self):
        return "<SLEEP(%s seconds)>"%(self.delay)
