from bitarray import bitarray

from jtagScanChain import JTAGScanChain

from drivers.digilentdriver import DigilentAdeptController
from drivers.xilinxPC1driver import XilinxPC1Driver
from drivers.openjtagdriver import OpenJtagDriver

if __name__ == '__main__':
    for driver in [DigilentAdeptController, XilinxPC1Driver, OpenJtagDriver]:
        sc = JTAGScanChain(driver(None, True))
        sc.init_chain(True)
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
