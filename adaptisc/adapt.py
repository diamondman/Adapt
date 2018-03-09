#!/usr/bin/env python3

import os
import sys
import argparse

import proteusisc
from proteusisc import JTAGScanChain, bitarray
from proteusisc import errors as proteusiscerrors
from proteusisc.jtagDevice import JTAGDevice

from .jtagUnsupportedDevice import JTAGUnsupportedDevice
from . import deviceDrivers

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

    parser.add_argument('-v','--verbose', dest='verbose', action='store_true',
                        help="Show additional information from proteusisc.")

    parser.add_argument('-cname', '--controllername', dest='cname', type=str,
                        help="Unique identifier for a JTAG controller you want to use. "\
                            "The enum or init commands show these names")
    parser.add_argument('-din', '--deviceindex', dest='din', type=int,
                        help="Index of the JTAG device on the specified controller's chain to run the operation on.")
    parser.add_argument('-f', '--file', dest='file', type=str,
                        help="File path to use for the operation.")
    parser.add_argument('-noerr', '--skip-jtag-error', dest='skipjtagerr', action='store_true',
                        default=False, help="File path to use for the operation.")

    args = parser.parse_args()
    if args.action in [erase, program]:
        if not args.cname:
            print("Controller ID (-cname) required for operation '%s'."%args.action.__name__.upper())
            sys.exit(1)
        if args.din is None:
            print("Device Index (-din) required for operation '%s'."%args.action.__name__.upper())
            sys.exit(1)
    if args.action in [program]:
        if not args.file:
            print("File (-f) required for operation '%s'."%args.action.__name__.upper())
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
        try:

            print("  %d %s=%s"%(ci, c.name, c))
            chain = JTAGScanChain(c,
                                  device_initializer=device_initializer,
                                  ignore_jtag_enabled=pargs.skipjtagerr,
                                  print_statistics=pargs.verbose)
            chain.init_chain()
            listdevices(chain)
        except proteusiscerrors.DevicePermissionDeniedError:
            print("\033[91m"
"    **********************************************************\n"
"    *    Controller Inaccessible: Permission Denied Error    *\n"
"    * http://proteusisc.org/help/ControllerInaccessibleError *\n"
"    **********************************************************"
        "\033[0m")
        except proteusiscerrors.JTAGAlreadyEnabledError:
            print("\033[91m"
"    **********************************************************\n"
"    *       Error: JTAG Already Enabled on Controller!       *\n"
"    *  Controller is either in use or left in invalid state. *\n"
"    *   Use -noerr flag to ignore this error or powercycle   *\n"
"    *         your controller. Use at your own fish.         *\n"
"    *   http://proteusisc.org/help/JTAGAlreadyEnabledError   *\n"
"    **********************************************************"
        "\033[0m")

def erase(pargs):
    print("ADAPT JTAG DEVICE ERASER")
    controllers = proteusisc.getAttachedControllers(pargs.cname)
    check_single_controller(controllers)
    c = controllers[0]

    print("Scanning controller %s..." % (c.productName))
    try:
        chain = JTAGScanChain(c,
                              device_initializer=device_initializer,
                              ignore_jtag_enabled=pargs.skipjtagerr,
                              print_statistics=pargs.verbose)
        chain.init_chain()
        print("Found (%d) devices..."%len(chain._devices))

        chain.jtag_enable()
        print("Controller Speed: %s bps"% chain.speed)

        dev = chain._devices[pargs.din]
        dev.erase()
        print("Preparing to erase (%s)(%s:%s)"%(c.productName,
                                              dev._desc.manufacturer,
                                              dev._desc._device_name))
        chain.flush()
        chain.jtag_disable()
        print("Finished Erase.")
    except proteusiscerrors.JTAGAlreadyEnabledError:
        print("\033[91m"
"    **********************************************************\n"
"    *       Error: JTAG Already Enabled on Controller!       *\n"
"    *  Controller is either in use or left in invalid state. *\n"
"    *   Use -noerr flag to ignore this error or powercycle   *\n"
"    *         your controller. Use at your own fish.         *\n"
"    *   http://proteusisc.org/help/JTAGAlreadyEnabledError   *\n"
"    **********************************************************"
"\033[0m")

def program(pargs):
    print("ADAPT JTAG DEVICE PROGRAMMER")
    controllers = proteusisc.getAttachedControllers(pargs.cname)
    check_single_controller(controllers)
    c = controllers[0]

    print("Scanning controller %s..." % (c.productName))
    try:
        chain = JTAGScanChain(c,
                              device_initializer=device_initializer,
                              ignore_jtag_enabled=pargs.skipjtagerr,
                              print_statistics=pargs.verbose)
        chain.init_chain()
        print("Found (%d) device%s..."%
              (len(chain._devices), 's'if len(chain._devices)>1 else ''))

        chain.jtag_enable()
        print("Controller Speed: %s bps"% chain.speed)

        dev = chain._devices[pargs.din]
        print("Preparing to program (%s)(%s:%s)"%(c.productName,
                                                  dev._desc.manufacturer,
                                                  dev._desc._device_name))

        dev.program(pargs.file)
        print("Programming device...")
        chain.flush()
        chain.jtag_disable()

        print("Finished Programming.")

    except proteusiscerrors.JTAGAlreadyEnabledError:
        print("\033[91m"
"    **********************************************************\n"
"    *       Error: JTAG Already Enabled on Controller!       *\n"
"    *  Controller is either in use or left in invalid state. *\n"
"    *   Use -noerr flag to ignore this error or powercycle   *\n"
"    *         your controller. Use at your own fish.         *\n"
"    *   http://proteusisc.org/help/JTAGAlreadyEnabledError   *\n"
"    **********************************************************"
"\033[0m")


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


def device_initializer(sc, idcode):
    maskedidcode = (idcode&bitarray('00001111111111111111111111111111'))\
       .tobytes()
    if maskedidcode in deviceDrivers.device_driver_lookup:
        return deviceDrivers.device_driver_lookup[maskedidcode]\
            (sc, idcode)
    return JTAGUnsupportedDevice(sc, idcode)

if __name__ == "__main__":
    main()
