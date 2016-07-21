from .jtagStateMachine import JTAGStateMachine
from .primative import Level1Primative, Level2Primative, Level3Primative, Executable,\
    DOESNOTMATTER, ZERO, ONE, CONSTANT, SEQUENCE,\
    DefaultRunInstructionPrimative

styles = {0:'\033[92m', #GREEN
          1:'\033[93m', #YELLO
          2:'\033[91m'} #RED

class CommandQueue(object):
    def __init__(self, sc):
        self.queue = []
        self.fsm = JTAGStateMachine()
        self.sc = sc
        self._return_queue = []

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
                    #print("Need to render down", item)
                    possible_prims = []
                    reqef = item.required_effect
        
                    #print(('  \033[95m%s %s %s\033[94m'%tuple(reqef)).replace('0', '-'), item,'\033[0m')
                    for p1 in self.sc._lv1_primatives:
                        ef = p1._effect
                        efstyledstr = ''
                        worststyle = 0
                        for i in range(3):
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
                        #print(" ",efstyledstr, styles.get(worststyle)+p1.__name__+"\033[0m")
        
                    if not len(possible_prims):
                        raise Exception('Unable to match Primative to lower level Primative.')
                    best_prim = possible_prims[0]
                    for prim in possible_prims[1:]:
                        if sum(prim._effect)<sum(best_prim._effect):
                            best_prim = prim
                    #print("    POSSIBILITIES:", [p.__name__ for p in possible_prims])
                    #print("    WINNER:", best_prim.__name__)
                    bits = item.get_effect_bits()
                    self.queue.append(best_prim(*bits))

                if not item._committed:
                    raise Exception("Primative not marked as committed after calling _commit.")
                if commit_res:
                    self.flush()

    def flush(self):
        #print("FLUSHING", self.queue)
        #for p in self.queue:
        #    if not isinstance(p, Executable):
        #        print("Need to render down", p)
        self.sc._controller.execute(self.queue)
        self.queue = []

    def get_return(self):
        res = self._return_queue
        self._return_queue = []
        if len(res)==1:
            return res[0]
        elif len(res)>1:
            return res
        return None
