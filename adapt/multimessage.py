from bitarray import bitarray
import struct

from jtagStateMachine import JTAGStateMachine
from jtagDeviceDescription import JTAGDeviceDescription

DOESNOTMATTER = 0
ZERO = 1
ONE = 2
CONSTANT = ZERO|ONE
SEQUENCE = CONSTANT|4

styles = {0:'\033[92m', #GREEN
          1:'\033[93m', #YELLO
          2:'\033[91m'} #RED

class CableDriver(object):
    def __repr__(self):
        return "<%s>"%self.__class__.__name__

    def execute(self, commands):
        for p in commands:
            print "  Executing", p

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

class CommandQueue(object):
    def __init__(self, sc):
        self.queue = []
        self.fsm = JTAGStateMachine()
        self.sc = sc

    def flatten_macro(self, item):
        if not item._is_macro:
            return [item]
        else:
            queue = []
            for subitem in item._expand_macro(self):
                queue += self.flatten_macro(subitem)
            return queue

    def append(self, prim):
        for item in self.flatten_macro(prim):
            if item._stage(self.fsm.state):
                if not item._staged:
                    raise Exception("Primative not marked as staged after calling _stage.")

                commit_res = item._commit(self)
                if isinstance(item, Executable):
                    self.queue.append(item)
                else:
                    print "Need to render down", item
                    possible_prims = []
                    reqef = item.required_effect
        
                    #print ('  \033[95m%s %s %s\033[94m'%tuple(reqef)).replace('0', '-'), item,'\033[0m'
                    for p1 in self.sc._lv1_primatives:
                        ef = p1._effect
                        efstyledstr = ''
                        worststyle = 0
                        for i in xrange(3):
                            if reqef[i] is None:
                                reqef[i] = 0
    
                            curstyle = 0
                            if (ef[i]&reqef[i]) is not reqef[i]:
                                curstyle = 1 if ef[i]==CONSTANT else 2
    
                            #efstyledstr += "%s%s "%(styles.get(curstyle), ef[i])
                            if curstyle > worststyle:
                                worststyle = curstyle
    
                        if worststyle == 0:
                            possible_prims.append(p1)
                        #print " ",efstyledstr, styles.get(worststyle)+p1.__name__+"\033[0m"
        
                    if not len(possible_prims):
                        raise Exception('Unable to match Primative to lower level Primative.')
                    best_prim = possible_prims[0]
                    for prim in possible_prims[1:]:
                        if sum(prim._effect)<sum(best_prim._effect):
                            best_prim = prim
                    #print "    POSSIBILITIES:", [p.__name__ for p in possible_prims]
                    print "    WINNER:", best_prim.__name__
                    bits = item.get_effect_bits()
                    self.queue.append(best_prim(*bits))

                if not item._committed:
                    raise Exception("Primative not marked as committed after calling _commit.")
                if commit_res:
                    self.flush()

    def flush(self):
        print "FLUSHING", self.queue
        #for p in self.queue:
        #    if not isinstance(p, Executable):
        #        print "Need to render down", p
        self.sc._controller.execute(self.queue)
        self.queue = []

##########################################################################################

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


class JTAGDevice(object):
    def __init__(self, chain, idcode):
        if not isinstance(chain, ScanChain):
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

    def run_tap_instruction(self, *args, **kwargs):
        self._chain._command_queue.append(
            DefaultRunInstructionPrimative(self, *args, **kwargs))

##########################################################################################

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
        return [self._bits, 0, 0]

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
        return [self.data,
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

class ScanChain(object):
    def gen_prim_adder(self, cls_):
        if not hasattr(self, cls_._function_name):
            def adder(*args, **kwargs):
                self._command_queue.append(cls_(*args, **kwargs))
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
                          DefaultLoadDRPrimative,
                          DefaultLoadReadRegisterPrimative]:
            self.gen_prim_adder(primative_cls)

    def init_chain(self):
        if not self._hasinit:
            self._devices = [JTAGDevice(self, bitarray('00000110110101001000000010010011')),
                             JTAGDevice(self, bitarray('00000110111001011000000010010011'))]

    def flush(self):
        self._command_queue.flush()


##########################################################################################
###DIGILENT###
class DigilentWriteTMSPrimative(Level1Primative, Executable):
    """TMS, TDI, TDO"""
    _effect = [SEQUENCE, CONSTANT, CONSTANT]
    def __init__(self, tms, tdi, tdo):
        self.tms, self.tdi, self.tdo = tms, tdi, tdo

class DigilentWriteTDIPrimative(Level1Primative, Executable):
    """TMS, TDI, TDO"""
    _effect = [CONSTANT, SEQUENCE, CONSTANT]
    def __init__(self, tms, tdi, tdo):
        self.tms, self.tdi, self.tdo = tms, tdi, tdo

class DigilentWriteTMSTDIPrimative(Level1Primative, Executable):
    """TMS, TDI, TDO"""
    _effect = [SEQUENCE, SEQUENCE, CONSTANT]
    def __init__(self, tms, tdi, tdo):
        self.tms, self.tdi, self.tdo = tms, tdi, tdo

class DigilentReadTDOPrimative(Level1Primative, Executable):
    """TMS, TDI, TDO"""
    _effect = [CONSTANT, CONSTANT, ONE]
    def __init__(self, tms, tdi, tdo):
        self.tms, self.tdi, self.tdo = tms, tdi, tdo

class LIESTDIHighPrimative(Level1Primative, Executable):
    """TMS, TDI, TDO"""
    _effect = [CONSTANT, ONE, ONE]
    def __init__(self, tms, tdi, tdo):
        self.tms, self.tdi, self.tdo = tms, tdi, tdo

class DigilentDriver(CableDriver):
    _primatives = [DigilentWriteTDIPrimative, DigilentWriteTMSPrimative,
                   DigilentWriteTMSTDIPrimative, DigilentReadTDOPrimative,
                   LIESTDIHighPrimative]


###XILINX PC1###
class XPC1TransferPrimative(Level1Primative, Executable):
    _max_bits = 65536
    """TMS, TDI, TDO"""
    _effect = [SEQUENCE, SEQUENCE, SEQUENCE]
    def __init__(self, tms, tdi, tdo):
        self.tms, self.tdi, self.tdo = tms, tdi, tdo

class XilinxPC1Driver(CableDriver):
    _primatives = [XPC1TransferPrimative]

###OpenJTAG###
class OpenJtagChangeTAPStatePrimative(Level2Primative, Executable):
    _function_name = 'transition_tap'
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

    def __repr__(self):
        return "<OpenJtag TAPTransition(%s=>%s)>"%(self._startstate if self._startstate
                                          else '?', self._targetstate)

class OpenJtagLoadReadRegisterPrimative(Level2Primative, Executable):
    _function_name = '_load_register'
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

    def __repr__(self):
        return "<OpenJtag LOAD/READREGISTER(%s bits, %sRead)>"%(len(self.data),
                                                       '' if self.read else 'No')

class OpenJtagDriver(CableDriver):
    _primatives = [OpenJtagChangeTAPStatePrimative, OpenJtagLoadReadRegisterPrimative]


##########################################################################################
###MAIN###
if __name__ == '__main__':
    for driver in [DigilentDriver, XilinxPC1Driver, OpenJtagDriver]:
        sc = ScanChain(driver())
        sc.init_chain()
        dev0 = sc._devices[0]

        #dev0.run_tap_instruction("ISC_ENABLE", loop=8, delay=0.01, read=False)
        #dev0.run_tap_instruction("ISC_ERASE", loop=8, delay=0.01, read=False)
        dev0.run_tap_instruction("ISC_INIT", loop=8, delay=0.01, read=False) #DISCHARGE
        dev0.run_tap_instruction("ISC_INIT", loop=8, arg=bitarray(), delay=0.01, read=False)
        #dev0.run_tap_instruction("ISC_DISABLE", loop=8, delay=0.01, expret=bitarray('00010001'))
        #dev0.run_tap_instruction("BYPASS", delay=0.01, expret=bitarray('00100001'))
        #sc.transition_tap("TLR")

        sc.flush()
        print
