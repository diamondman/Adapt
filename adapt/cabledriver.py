class CableDriver(object):
    def __repr__(self):
        return "<%s>"%self.__class__.__name__

    def execute(self, commands):
        for p in commands:
            print "  Executing", p
            func = getattr(self, p._driver_function_name, None)
            args, kwargs = p._get_args()
            if not getattr(self, 'mock', False):
                func(*args, **kwargs) #TODO pass in stuff
