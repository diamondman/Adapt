from bitarray import bitarray
import struct

from jtagStateMachine import JTAGStateMachine
from jtagDeviceDescription import JTAGDeviceDescription

class CableDriver(object):
    def __repr__(self):
        return "<%s>"%self.__class__.__name__

class Primative(object):
    _layer = None
    def __init__(self):
        self._staged = False        

    def _stageable(self, trans):
        return True

    def _stage(self, transaction):
        if self._staged:
            raise Exception("Primative already staged")
        self._staged = True

class Level1Primative(Primative):
    _layer = 1
    _effect = [0, 0, 0]
    _executable = True
class Level2Primative(Primative):
    _layer = 2
    _executable = False
class Level3Primative(Primative):
    _layer = 3
    _executable = False

DOESNOTMATTER = 0
ZERO = 1
ONE = 2
CONSTANT = ZERO|ONE
SEQUENCE = CONSTANT|4

styles = {0:'\033[92m', #GREEN
          1:'\033[93m', #YELLO
          2:'\033[91m'} #RED

class CommandQueue(list):
    def __init__(self, sc):
        self._fsm = JTAGStateMachine()
        self._query = []
        self._sc = sc

    def append(self, prim):
        if not prim._stageable(self):
            if not res:
                raise Exception("Failure for testing to prevent stupid errors")
            return
        super(CommandQueue, self).append(prim)
        res = prim._stage(self)
        if not prim._staged:
            raise Exception("Primative not marked as staged after calling _stage.")
        return res

    def flush(self):
        print "FLUSHING", self
        for p in self:
            possible_prims = []
            reqef = p.required_effect
            print ('  \033[95m%s %s %s\033[94m'%tuple(reqef)).replace('0', '-'), p, '\033[0m'
            for p1 in self._sc._controller._primatives:
                #print p1, isinstance(p1, Level1Primative), p1.mro()
                if issubclass(p1, Level1Primative):
                    ef = p1._effect
                    efstyledstr = ''
                    worststyle = 0
                    for i in xrange(3):
                        if reqef[i] is None:
                            reqef[i] = 0
                    
                        curstyle = 0
                        if (ef[i]&reqef[i]) is not reqef[i]:
                            curstyle = 1 if ef[i]==CONSTANT else 2
                        
                        efstyledstr += "%s%s "%(styles.get(curstyle), ef[i])
                        if curstyle > worststyle:
                            worststyle = curstyle
                    
                    if worststyle == 0:
                        possible_prims.append(p1)
                    print " ",efstyledstr, styles.get(worststyle)+p1.__name__+"\033[0m"
                #elif issubclass(p1, Level2Primative):
                #    if p1._executable:

            if not len(possible_prims):
                raise Exception('Unable to match Primative to lower level Primative.')
            best_prim = possible_prims[0]
            for prim in possible_prims[1:]:
                if sum(prim._effect)<sum(best_prim._effect):
                    best_prim = prim
            print "    POSSIBILITIES:", [p.__name__ for p in possible_prims]
            print "    WINNER:", best_prim.__name__

##########################################################################################

class DefaultRunInstructionPrimative(Level3Primative):
    def __init__(self, insname, read=True, execute=True, 
                 loop=0, arg=None, delay=0, expret=None):
        pass

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

    def run_tap_instruction(self, insname, read=True, execute=True, 
                            loop=0, arg=None, delay=0, expret=None):
        prim = RunInstructionPrimative(insname, read, execute, loop, arg, delay, expret)
        self._chain._append_primative(prim)

##########################################################################################

class DefaultLoadReadRegisterPrimative(Level2Primative):
    _function_name = '_load_register'
    def __init__(self, data, read=False):
        super(DefaultLoadReadRegisterPrimative, self).__init__()
        self._data = data
        self._read = read

    def _stage(self, command_queue):
        super(DefaultLoadReadRegisterPrimative, self)._stage(command_queue)
        command_queue._fsm.transition_bit(1)
        return self._read

    @property
    def required_effect(self):
        if not self._staged:
            raise Exception("required_effect is only available after staging")
        return [SEQUENCE, 
                SEQUENCE, 
                ONE if self._read else DOESNOTMATTER] #TMS TDI TDO

    def _stageable(self, trans):
        return trans._fsm.state in ["SHIFTIR", "SHIFTDR"]

    def __repr__(self):
        return "<LOAD/READREGISTER(%s bits, %sRead)>"%(len(self._data), 
                                                       '' if self._read else 'No')

class DefaultChangeTAPStatePrimative(Level2Primative):
    _function_name = 'transition_tap'
    def __init__(self, state):
        super(DefaultChangeTAPStatePrimative, self).__init__()
        self._targetstate = state
        self._startstate = None

    def _stage(self, command_queue):
        super(DefaultChangeTAPStatePrimative, self)._stage(command_queue)
        self._startstate = command_queue._fsm.state
        self._bits = command_queue._fsm.calc_transition_to_state(self._targetstate)
        for b in self._bits[::-1]:
            command_queue._fsm.transition_bit(b)

    @property
    def required_effect(self):
        """TMS, TDI, TDO"""
        if not self._staged:
            raise Exception("required_effect is only available after staging")
        return [SEQUENCE,
                ZERO,
                DOESNOTMATTER]

    def __repr__(self):
        return "<TAPTransition(%s=>%s)>"%(self._startstate if self._startstate 
                                          else '?', self._targetstate)

class DefaultLoadDRPrimative(Level2Primative):
    _function_name = 'load_dr'
    def __init__(self, data, read):
        super(DefaultLoadDRPrimative, self).__init__()
        self._data = data
        self._read = read

    @property
    def required_effect(self):
        """TMS, TDI, TDO"""
        if not self._staged:
            raise Exception("required_effect is only available after staging")
        return [SEQUENCE, 
                SEQUENCE, 
                ONE if self._read else DOESNOTMATTER] #TMS TDI TDO

    def __repr__(self):
        return "<LoadDR(%s bits, %sRead)>"%(len(self._data), 
                                            '' if self._read else 'No')

class DefaultLoadIRPrimative(Level2Primative):
    _function_name = 'load_ir'
    def __init__(self, data, read):
        super(DefaultLoadIRPrimative, self).__init__()
        self._data = data
        self._read = read

    @property
    def required_effect(self):
        """TMS, TDI, TDO"""
        if not self._staged:
            raise Exception("required_effect is only available after staging")
        return [SEQUENCE, 
                SEQUENCE, 
                ONE if self._read else DOESNOTMATTER] #TMS TDI TDO

    def __repr__(self):
        return "<LoadIR(%s bits, %sRead)>"%(len(self._data), 
                                            '' if self._read else 'No')

class ScanChain(object):
    def gen_prim_adder(self, cls_):
        def adder(*args, **kwargs):
            self._append_primative(cls_(*args, **kwargs))
        setattr(self, cls_._function_name, adder)

    def __init__(self, controller):
        print "Starting a scan chain with", controller
 
        self._devices = []
        self._hasinit = False
        self._sm = JTAGStateMachine()
        self._controller = controller
        self._controller._scanchain = self #This might necessitate a factory

        self.__command_queue = None
        for primative in self._controller._primatives:
            pass#print "LAYER %s; Op %s"%(primative._layer, primative.__name__)

        for primative_cls in [DefaultChangeTAPStatePrimative, 
                          DefaultLoadIRPrimative,
                          DefaultLoadDRPrimative,
                          DefaultLoadReadRegisterPrimative]:
            #print primative_cls._function_name
            self.gen_prim_adder(primative_cls)

    def init_chain(self):
        if not self._hasinit:
            self._devices = [JTAGDevice(self, bitarray('00000110110101001000000010010011')),
                             JTAGDevice(self, bitarray('00000110111001011000000010010011'))]

    @property
    def _command_queue(self):
        if not self.__command_queue:
            self.__command_queue = CommandQueue(self)
        return self.__command_queue

    def flush(self):
        self._command_queue.flush()
        self.__command_queue = None

    def _append_primative(self, prim):
        """This can't be the best way to do this..."""
        if self._command_queue.append(prim):
            self.flush()


##########################################################################################
###DIGILENT###
class DigilentWriteTMSPrimative(Level1Primative):
    """TMS, TDI, TDO"""
    _effect = [SEQUENCE, CONSTANT, CONSTANT]

class DigilentWriteTDIPrimative(Level1Primative):
    """TMS, TDI, TDO"""
    _effect = [CONSTANT, SEQUENCE, CONSTANT]

class DigilentWriteTMSTDIPrimative(Level1Primative):
    """TMS, TDI, TDO"""
    _effect = [SEQUENCE, SEQUENCE, CONSTANT]

class DigilentReadTDOPrimative(Level1Primative):
    """TMS, TDI, TDO"""
    _effect = [CONSTANT, CONSTANT, ONE]

class LIESTDIHighPrimative(Level1Primative):
    """TMS, TDI, TDO"""
    _effect = [CONSTANT, ONE, ONE]

class DigilentDriver(CableDriver):
    _primatives = [DigilentWriteTDIPrimative, DigilentWriteTMSPrimative, 
                   DigilentWriteTMSTDIPrimative, DigilentReadTDOPrimative, 
                   LIESTDIHighPrimative]


###XILINX PC1###
class XPC1TransferPrimative(Level1Primative):
    _max_bits = 65536
    """TMS, TDI, TDO"""
    _effect = [SEQUENCE, SEQUENCE, SEQUENCE]

class XilinxPC1Driver(CableDriver):
    _primatives = [XPC1TransferPrimative]

###OpenJTAG###
class OpenJtagChangeTAPStatePrimative(Level2Primative):
    _executable = True

class OpenJtagLoadReadRegisterPrimative(Level2Primative):
    _executable = True

class OpenJtagDriver(CableDriver):
    _primatives = [OpenJtagChangeTAPStatePrimative, OpenJtagLoadReadRegisterPrimative]


##########################################################################################
###MAIN###
if __name__ == '__main__':
    for driver in [DigilentDriver, XilinxPC1Driver, OpenJtagDriver]:
        sc = ScanChain(driver())
        sc.init_chain()
    
        #sc.load_ir(bitarray('11001010'))
        #sc.transition_tap("RTI")
        
        #dev0 = sc._devices[0]
        #dev0.run_tap_instruction("ISC_ENABLE")
        sc.transition_tap("SHIFTIR")
        sc.load_ir(bitarray('11001010'), read=True)
        sc.transition_tap("RTI")
    
        #sc.transition_tap("SHIFTIR")
        #sc.load_ir(bitarray('11001010'))
        #sc.transition_tap("RTI")
    
        sc.flush()
        print
