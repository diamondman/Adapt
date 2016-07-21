import time

from .jtagUtils import JTAGControlError

class CableDriver(object):
    def __init__(self, dev):
        self._dev = dev
        self._dev_handle = None

    def __repr__(self):
        return "<%s>"%self.__class__.__name__

    def execute(self, commands):
        for p in commands:
            #print("  Executing", p)
            func = getattr(self, p._driver_function_name, None)
            args, kwargs = p._get_args()
            if not func:
                raise Exception("Registered function %s not found on class %s"%
                                (p._driver_function_name, p.__class__))
            if not getattr(self, 'mock', False):
                res = func(*args, **kwargs) #TODO pass in stuff
                if res:
                    #print("RES", res)
                    self._scanchain._command_queue._return_queue.append(res)

    def sleep(self, delay):
        if not self._jtagon:
            raise JTAGControlError('JTAG Must be enabled first')
        time.sleep(delay)

    @property
    def _handle(self):
        if not self._dev_handle:
            self._dev_handle = self._dev.open()
        return self._dev_handle

    def close_handle(self):
        if self._dev_handle:
            self._dev_handle.close()
