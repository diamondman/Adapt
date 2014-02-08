from jtagScanChain import JTAGScanChain
from digilentdriver import JTAGController

if __name__ == "__main__":
    print "ADAPT JTAG CHAIN SCANNER"
    controllers = JTAGController.getAttachedControllers()
    print "USB Controllers:"
    for i, c in enumerate(controllers):
        print "  %d %s"%(i, c)
        chain = JTAGScanChain(c)
        chain.init_chain()

