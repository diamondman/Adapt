from proteusisc.jtagDevice import JTAGDevice

class JTAGUnsupportedDevice(JTAGDevice):
    def erase(self):
        print("Driver for JTAG Device not found. Operation unsupported")
    def program(self):
        print("Driver for JTAG Device not found. Operation unsupported")
