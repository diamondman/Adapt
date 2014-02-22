import sys
import csv
import time
from bitarray import bitarray

from jtagScanChain import JTAGScanChain
from digilentdriver import JTAGController
import jedparse

def gc(addr):
    return (addr>>1)^addr

def build_byte_align_buff(bit_count):
    bitmod = bit_count%8
    if bitmod == 0: 
        rdiff = bitarray()
        print "NO BUFF NEEDED", rdiff
    else:
        rdiff = bitarray(8-bitmod)
        rdiff.setall(False)
    return rdiff

def pstatus(resflags):
    print "STATUS: "+("" if (ord(resflags)&0b11000011==1) else "INVALID_STATUS ")+\
        ("ISCDIS " if ord(resflags)&32 else "")+("ISCEN " if ord(resflags)&16 else "")+\
        ("SECURE " if ord(resflags)&8 else "")+("DONE " if ord(resflags)&4 else "")


def program_device(chain, device, data_array):
    import ipdb
    con = chain._controller
    chain._jtagEnable()
    
    #ipdb.set_trace()
    con.writeTMSBits('\x00\xDF', 10) #Get to ShiftIR
    pstatus(con.writeTDIBits('\x68', 7, return_tdo=True))
    con.writeTDIBits('\x01', 1, TMS=True) #ISC_ENABLE
    con.writeTMSBits('\x01', 8) #RUN
    time.sleep(0.01)

    for i,r in enumerate(data_array):
        addr = bitarray(bin(gc(i))[2:].zfill(7))
        addr.reverse()

        print "\nLOADING(%s:%s) ="%(i,addr), r
        con.writeTMSBits('\x03', 4) #Get to ShiftIR
        pstatus(con.writeTDIBits('\x6A', 7, return_tdo=True))#first ins bits
        con.writeTDIBits('\x01', 1, TMS=True) #ISC_PROGRAM
        con.writeTMSBits('\x03', 4) #Get to ShiftDR without running
        
        buffered_r = build_byte_align_buff(len(r)) + r
        buffered_addr = build_byte_align_buff(len(addr)) + addr

        con.writeTDIBits(buffered_r.tobytes(), len(r), return_tdo=True).__repr__()
        con.writeTDIBits(buffered_addr.tobytes(), len(addr)-1, return_tdo=True) #ISC_PROGRAM
        con.writeTDIBits(chr(addr[0]), 1, TMS=True, return_tdo=True) #ISC_PROGRAM
        
        con.writeTMSBits('\x01', 8) #RUN
        time.sleep(0.01)
    
    #ipdb.set_trace()
    con.writeTMSBits('\x03', 4) #Get to ShiftIR
    pstatus(con.writeTDIBits('\xF0', 7, return_tdo=True))
    con.writeTDIBits('\x01', 1, TMS=True) #ISC_DISCHARGE
    con.writeTMSBits('\x01', 8) #RUN
    time.sleep(0.01)
    
    #ipdb.set_trace()
    con.writeTMSBits('\x03', 4) #Get to ShiftIR
    pstatus(con.writeTDIBits('\xF0', 7, return_tdo=True))
    con.writeTDIBits('\x01', 1, TMS=True) #ISC_INIT
    con.writeTMSBits('\x1b', 5) #init pulse
    con.writeTMSBits('\x00', 8) #RUN
    time.sleep(0.01)

    #ipdb.set_trace()
    con.writeTMSBits('\x03', 4) #Get to ShiftIR
    con.writeTDIBits('\x40', 7, return_tdo=True).__repr__()
    con.writeTDIBits('\x01', 1, TMS=True) #ISC_DISABLE
    con.writeTMSBits('\x01', 8) #RUN
    time.sleep(0.01)

    #ipdb.set_trace()
    con.writeTMSBits('\x03', 4) #Get to ShiftIR
    pstatus(con.writeTDIBits('\xff', 7, return_tdo=True))
    con.writeTDIBits('\x01', 1, TMS=True) #BYPASS
    con.writeTMSBits('\xFF', 8) #RUN
    time.sleep(0.01)
    
    chain._jtagDisable()

def erase_device(chain, device):
    import ipdb
    con = chain._controller
    chain._jtagEnable()
    #print device.desc._instructions
    
    cmd_isce = device.desc._instructions['ISC_ENABLE']
    cmd_iscd = device.desc._instructions['ISC_DISABLE']
    cmd_iscerase = device.desc._instructions['ISC_ERASE']
    print cmd_isce, cmd_iscd, cmd_iscerase
    
    #ipdb.set_trace()
    con.writeTMSBits('\x00\xDF', 10) #Get to ShiftIR
    pstatus(con.writeTDIBits('\x68', 7, return_tdo=True))
    con.writeTDIBits('\x01', 1, TMS=True) #ISC_ENABLE
    con.writeTMSBits('\x01', 8) #RUN
    time.sleep(0.01)

    #ipdb.set_trace()
    con.writeTMSBits('\x03', 4) #Get to ShiftIR
    pstatus(con.writeTDIBits('\x6D', 7, return_tdo=True))
    con.writeTDIBits('\x01', 1, TMS=True) #ISC_ERASE
    con.writeTMSBits('\x01', 8) #RUN
    time.sleep(0.01)
    
    #ipdb.set_trace()
    con.writeTMSBits('\x03', 4) #Get to ShiftIR
    pstatus(con.writeTDIBits('\xF0', 7, return_tdo=True))
    con.writeTDIBits('\x01', 1, TMS=True) #ISC_DISCHARGE
    con.writeTMSBits('\x01', 8) #RUN
    time.sleep(0.01)
    
    #ipdb.set_trace()
    con.writeTMSBits('\x03', 4) #Get to ShiftIR
    pstatus(con.writeTDIBits('\xF0', 7, return_tdo=True))
    con.writeTDIBits('\x01', 1, TMS=True) #ISC_INIT
    con.writeTMSBits('\x1b', 5) #init pulse
    con.writeTMSBits('\x00', 8) #RUN
    time.sleep(0.01)

    #ipdb.set_trace()
    con.writeTMSBits('\x03', 4) #Get to ShiftIR
    pstatus(con.writeTDIBits('\x40', 7, return_tdo=True))
    con.writeTDIBits('\x01', 1, TMS=True) #ISC_DISABLE
    con.writeTMSBits('\x01', 8) #RUN
    time.sleep(0.01)

    #ipdb.set_trace()
    con.writeTMSBits('\x03', 4) #Get to ShiftIR
    pstatus(con.writeTDIBits('\xff', 7, return_tdo=True))
    con.writeTDIBits('\x01', 1, TMS=True) #BYPASS
    con.writeTMSBits('\xFF', 8) #RUN
    time.sleep(0.01)

    #time.sleep(2)
    chain._jtagDisable()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "ADAPT JTAG CHAIN SCANNER"
        controllers = JTAGController.getAttachedControllers()
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
        controllers = JTAGController.getAttachedControllers()
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
        erase_device(chain, dev)

    elif sys.argv[1] == '-p':
        print "Detecting controllers..."
        controllers = JTAGController.getAttachedControllers()
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
                #else:
                #    print "UNK [%s][%s]=%s"%(j,i,v.__repr__())
            #outbf[0] = 0
            #outbf[681] = 0
            #outbf[682] = 0
            #outbf[1363] = 0
            outbuffers.append(outbf)
        #for b in outbuffers:
        #    print b, len(b)
        print "Loads required", len(outbuffers)
        
        dev = chain._devices[0]
        print "Erasing device..."
        erase_device(chain, dev)
        print "Programming device..."
        program_device(chain, dev, outbuffers)

    else:
        print "Unknown command %s" % sys.argv[1]
