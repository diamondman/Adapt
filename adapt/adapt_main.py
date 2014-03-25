import sys
import csv
from bitarray import bitarray

from jtagScanChain import JTAGScanChain
import jtagControllerManager
import jedparse

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "ADAPT JTAG CHAIN SCANNER"
        controllers = jtagControllerManager.getAttachedControllers()
        print "USB Controllers:"
        for i, c in enumerate(controllers):
            print "  %d %s"%(i, c)
            chain = JTAGScanChain(c)
            chain.init_chain()
            for i, dev in enumerate(chain._devices):
                if dev.desc:
                    print "        %d %s %s %s (%08x)"%(i, dev.desc.manufacturer, 
                                                 dev.desc._device_name, dev.desc._chip_package,
                                                      dev._id)
                else:
                    print "        %d UNIDENTIFIED DEVICE. ID: %s."%(i, dev._id)
                    print "            Search for bsdl file: http://bsdl.info/list.htm?search=XXXX%s"%\
                        bin(dev._id & 0xFFFFFFF)[2:].zfill(28)
    
    elif sys.argv[1] == '-e':
        print "Detecting controllers..."
        controllers = jtagControllerManager.getAttachedControllers()
        if len(controllers)>1:
            print "Can not Erase target. Multiple JTAG cables present. This will be supported later."
            sys.exit(1)

        print "Scanning controller %s..." % (controllers[0].productName)
        chain = JTAGScanChain(controllers[0])
        chain.init_chain()

        print "Preparing to erase (%s)(%s:%s)"%(controllers[0].productName, 
                                                  chain._devices[0].desc.manufacturer,
                                                  chain._devices[0].desc._device_name)
        if controllers[0].productName != "CoolRunner 2 Starter 2":
            print """This only works with the CoolRunner 2 Starter 2 at the moment. """
            """You are about to screw something up"""
            sys.exit(2)

        dev = chain._devices[0]
        dev.erase()

    elif sys.argv[1] == '-p':
        print "Detecting controllers..."
        controllers = jtagControllerManager.getAttachedControllers()
        if len(controllers)>1:
            print "Can not program targe. Multiple JTAG cables present. This will be supported later."
            sys.exit(1)

        print "Scanning controller %s..." % (controllers[0].productName)
        chain = JTAGScanChain(controllers[0])
        chain.init_chain()

        print "Preparing to program (%s)(%s:%s)"%(controllers[0].productName, 
                                                  chain._devices[0].desc.manufacturer,
                                                  chain._devices[0].desc._device_name)
        if controllers[0].productName != "CoolRunner 2 Starter 2":
            print """This only works with the CoolRunner 2 Starter 2 at the moment. """
            """You are about to screw something up"""
            sys.exit(2)
        if len(sys.argv) < 3:
            print "You need to provide a programming file."
            sys.exit(1)
            print "Parsing programming file..."
        jeddata = jedparse.parse_file(sys.argv[2])
        bits = jeddata['fuses']

        mapf = open('/media/F02472C324728BFA/Xilinx/14.7/ISE_DS/ISE/xbr/data/xc2c256.map' )
        reader = csv.reader(mapf, delimiter='\t')
        mapdata = [row for row in reader]

        outbuffers = []
        for i in range(len(mapdata[0])):
            outbf = bitarray(1364)
            outbf.setall(False)
            for j in range(len(mapdata)):
                v = mapdata[j][i]
                if v.isdigit():
                    #if int(v) not in [0,681,682,1363]:
                    outbf[j] = bits[int(v)]
                elif v == "done_0":
                    outbf[j] = 1
                    outbf[0] = 1
                elif v == "done_1":
                    outbf[j] = 0
                    outbf[j+1:] = 1
                elif "sec_" in v:
                    outbf[j] = 1
            outbuffers.append(outbf)
        print "Loads required", len(outbuffers)
        
        dev = chain._devices[0]
        print "Erasing device..."
        dev.erase()
        print "Programming device..."
        dev.program(outbuffers)

    else:
        print "Unknown command %s" % sys.argv[1]
