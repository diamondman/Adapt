from proteusisc.jtagDevice import JTAGDevice

class JTAGUnsupportedDevice(JTAGDevice):
    def erase(self, *args, **kwargs):
        print("Driver for JTAG Device not found. Operation unsupported")
    def program(self, *args, **kwargs):
        print("Driver for JTAG Device not found. Operation unsupported")
