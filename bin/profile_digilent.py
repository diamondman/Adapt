#!/usr/bin/python3
import usb1
import binascii
import bitarray
import math

DCAP_i2a = {
    0x00000001: "dcapJtg", # Jtag....
    0x00000002: "dcapPio", # Pin I/O
    0x00000004: "dcapEpp", # Async Parallel Interface
    0x00000008: "dcapStm", # Sync Parallel Interface (High Speed Stream)
    0x00000010: "dcapSpi", # Serial Peripheral Interface
    0x00000020: "dcapTwi", # Two Wire (Serial) Interface (i2c)
    0x00000040: "dcapAci", # Async Comm Interface (UART)
    0x00000080: "dcapAio", # Analog IN/OUT
    0x00000100: "dcapEmc", # Electro-Mechanical Control
    0x00000200: "dcapDci", # 
    0x00000400: "dcapGio", # General Sensor & User I/O Libraries
    0x00000800: "dcapPti", # 
}

c = usb1.USBContext()

iter = c.getDeviceIterator()

digilent_devs = []
for dev in iter:
    if dev.getVendorID() == 0x1443:
        digilent_devs.append(dev)

def index_or_default(s):
    try:
        s = s[:s.index(b'\x00')]
    except ValueError:
        pass
    try:
        s = s[:s.index(b'\xFF')]
    except ValueError:
        pass
    return s
                                
def cread(h, req, l, bin_data=False, flip=False):
    try:
        d = h.controlRead(0xC0, req, 0, 0, l)
        if flip:
            d = d[::-1]
        if bin_data:
            return "0x"+(binascii.hexlify(d).decode('utf8').upper().zfill(l*2))
        else:
            return index_or_default(d).decode('utf8')
    except usb1.USBErrorPipe as e:
        return "NOT SUPPORTED"
    except Exception as e:
        return str(d) + " (FAILED " + str(e) + ")"

def FX2ReadPROM(h, addr, l, raw=False):
    d = h.controlRead(0xc0, 0xA2, addr, 0, l)
    if raw:
        return d
    return "0x"+(binascii.hexlify(d).decode('utf8').upper().zfill(l*2))

def FX2ReadRAM(h, addr, l, raw=False):
    d = h.controlRead(0xc0, 0xA3, addr, 0, l)
    if raw:
        return d
    return "0x"+(binascii.hexlify(d).decode('utf8').upper().zfill(l*2))

def CheckIsFX2(h):
    try:
        h.controlRead(0xc0, 0xA2, 0xE60A, 0, 1)
        return True
    except usb1.USBErrorPipe:
        return False

def ListCapabilities(handle):
    print("    DCAP:            ", cread(handle, 0xE7, 8, True, True))
    try:
        d = handle.controlRead(0xC0, 0xE7, 0, 0, 8)
        bits = bitarray.bitarray(bin(int.from_bytes(d, 'little'))[2:]
                                 .zfill(8*len(d))[::-1])
        for b in range(16):
            if bits[b]:
                print("        ("+str(b)+") "+DCAP_i2a.get(1<<b, "UNKNOWN FEATURE BIT"))
    except usb1.USBErrorPipe as e:
        pass
    except Exception as e:
        print("        Subfeature list FAILED (" + str(e) + ")")

        
def printDeviceInfo(handle):
    print("        Device Info:")
    d = FX2ReadPROM(handle, 0x3FF0, 4+2, True)[2::-1]
    print("            ??:      ",
          "0x"+(binascii.hexlify(d).decode('utf8').upper().zfill(len(d)*2)))
    d = FX2ReadPROM(handle, 0x3FE0, 12+2, True)[2:]
    print("            SN:      ",
          d.replace(b'\xFF',b'').replace(b'\x00',b'').decode('utf8'))
    d = FX2ReadPROM(handle, 0x3FC0, 16+2, True)[2:]
    print("            UserName:",
          d.replace(b'\xFF',b'').replace(b'\x00',b'').decode('utf8'))
    d = FX2ReadPROM(handle, 0x3FA0, 28+2, True)[2:]
    print("            ProdName:",
          d.replace(b'\xFF',b'').replace(b'\x00',b'').decode('utf8'))
    d = FX2ReadPROM(handle, 0x3FF8, 2+2, True)[2:]
    print("            UNKN:    ",
          d.replace(b'\xFF',b'').replace(b'\x00',b'').decode('utf8'))

print(str(len(digilent_devs))+" devices found")
for i, dev in enumerate(digilent_devs):
    print("(DEV "+str(i).zfill(2)+")", hex(dev.getVendorID())[2:].zfill(4)+":"+hex(dev.getProductID())[2:].zfill(4),)
    handle = dev.open()
    print("    Product Name:    ", cread(handle, 0xE1, 28))
    print("    User Name:       ", cread(handle, 0xE2, 16))
    print("    Serial Number:   ", cread(handle, 0xE4, 12))
    print("    Firmware Version:", cread(handle, 0xE6, 4, True, True))
    print("    Product ID:      ", cread(handle, 0xE9, 4, True, True))
    isfx2 = CheckIsFX2(handle)
    print("    Chip:            ", "FX2" if isfx2 else "AVR")
    if isfx2:
        print("        ChipID (wat):", FX2ReadRAM(handle, 0xE60A, 1))
        #printDeviceInfo(handle)
    ListCapabilities(handle)
    handle.close()
    print()
