#!/usr/bin/python3

import sys
import argparse
from bitarray import bitarray

import proteusisc
from proteusisc.jtagScanChain import JTAGScanChain
from proteusisc.jtagDevice import JTAGDevice

from .jtagUnsupportedDevice import JTAGUnsupportedDevice
from .deviceDrivers.jtagDeviceXC2C256 import JTAGDeviceXC2C256
from .jedparse import JedecConfigFile


def main():
    parser = argparse.ArgumentParser(description='General purpose tool for configuring FPGAs, '\
                                         'CPLDs, and Microcontrollers.', prog='adapt')
    parser.add_argument('--enum', dest='action', action='store_const', const=enum, default=enum,
                        help="Enumerate the attached controllers. Causes no JTAG activity.")
    parser.add_argument('-i','--init', dest='action', action='store_const', const=init,
                        help="Initiate all or a specific JTAG controller to list its chain.")
    parser.add_argument('-e','--erase', dest='action', action='store_const', const=erase,
                        help="Erase the specified device.")
    parser.add_argument('-p','--program', dest='action', action='store_const', const=program,
                        help="Program the specified device. For some devices, this command also erases before programming.")

    parser.add_argument('-cname', '--controllername', dest='cname', type=str,
                        help="Unique identifier for a JTAG controller you want to use. "\
                            "The enum or init commands show these names")
    parser.add_argument('-din', '--deviceindex', dest='din', type=int,
                        help="Index of the JTAG device on the specified controller's chain to run the operation on.")
    parser.add_argument('-f', '--file', dest='file', type=str,
                        help="File path to use for the operation.")

    args = parser.parse_args()
    if args.action in [erase, program]:
        if not args.cname:
            print("Controller ID (-cname) required for operation %s."%args.action.func_name)
            sys.exit(1)
        if args.din is None:
            print("Device Index (-din) required for operation %s."%args.action.func_name)
            sys.exit(1)
    if args.action in [program]:
        if not args.file:
            print("File (-f) required for operation %s."%args.action.func_name)
            sys.exit(1)
    args.action(args)


########################
#      OPERATIONS      #
########################
def enum(pargs):
    print("ADAPT JTAG CONTROLLER DISCOVERY")
    controllers = proteusisc.getAttachedControllers()
    print("USB Controllers:")
    for i, c in enumerate(controllers):
        print("  %d %s"%(i, c))

def init(pargs):
    print("ADAPT JTAG CHAIN SCANNER")
    controllers = proteusisc.getAttachedControllers(pargs.cname)
    print("USB Controllers:")
    for ci, c in enumerate(controllers):
        print("  %d %s=%s"%(ci, c.name, c))
        chain = JTAGScanChain(c, device_initializer=device_initializer)
        chain.init_chain()
        listdevices(chain)

def erase(pargs):
    print("ADAPT JTAG DEVICE ERASER")
    controllers = proteusisc.getAttachedControllers(pargs.cname)
    check_single_controller(controllers)
    c = controllers[0]

    print("Scanning controller %s..." % (controller.productName))
    chain = JTAGScanChain(c, device_initializer=device_initializer)
    chain.init_chain()

    dev = chain._devices[pargs.din]
    print("Preparing to erase (%s)(%s:%s)"%(controller.productName,
                                              dev.desc.manufacturer,
                                              dev.desc._device_name))
    dev.erase()
    print("Finished Erase.")

def program(pargs):
    print("ADAPT JTAG DEVICE PROGRAMMER")
    controllers = proteusisc.getAttachedControllers(pargs.cname)
    check_single_controller(controllers)
    controller = controllers[0]

    print("Scanning controller %s..." % (controller.productName))
    chain = JTAGScanChain(controller)
    chain.init_chain()

    dev = chain._devices[pargs.din]
    print("Preparing to program (%s)(%s:%s)"%(controller.productName,
                                              dev.desc.manufacturer,
                                              dev.desc._device_name))
    print("Parsing programming file...")
    jed = JedecConfigFile(pargs.file)

    print("Erasing device...")
    dev.erase()
    print("Programming device...")
    dev.program(jed)

    print("Finished Programming.")



#########################
#         UTILS         #
#########################
def listdevices(chain, indentspaces=8):
    indent = (" "*indentspaces)
    for di, dev in enumerate(chain._devices):
        if dev._desc:
            print(indent+"%d %s %s %s (%08x)"%(di, dev._desc.manufacturer,
                                         dev._desc._device_name, dev._desc._chip_package,
                                              dev._id))
        else:
            print(indent+"%d UNIDENTIFIED DEVICE. ID: %s."%(di, dev._id))
            print(indent+"    Search for bsdl file: http://bsdl.info/list.htm?search=XXXX%s"%\
                bin(dev._id & 0xFFFFFFF)[2:].zfill(28))

def check_single_controller(controllers):
    if len(controllers)>1:
        print("\033[91mThe ControllerID you provided matches more than one device.\033[0m\n"\
            "\033[93mThis should not happen and may signify an issue with the driver for the controller.\n"\
            "Unplugging the other device(s) that match this ID will allow the operation to continue.\033[0m")
        sys.exit(1)
    if len(controllers)==0:
        print("\033[91mNo Controller match for the ControllerID you provided.\033[0m\n"\
            "\033[93mUse adapt -i to list available controllers.\033[0m\n")
        sys.exit(1)

        
_device_driver_lookup = {
    b'\x16\xd4\xc0\x93': JTAGDeviceXC2C256
}

def device_initializer(sc, idcode):
    if idcode.tobytes() in _device_driver_lookup:
        return _device_driver_lookup[idcode.tobytes()](sc, idcode)
    return JTAGUnsupportedDevice(sc, idcode)


if __name__ == "__main__":
    main()
