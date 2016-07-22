import csv
import os
import math
from bitarray import bitarray

NULL_ID_CODES = [bitarray('1'*32),
                 bitarray('0'*32)]

manufacturer_lookup = {
    1: 'AMD', 2: 'AMI', 4: 'Fujitsu', 7: 'Hitachi', 8: 'Inmos',
    11: 'Intersil', 13: 'Mostek', 14: 'Freescale (Motorola)',
    16: 'NEC', 19: 'Conexant (Rockwell)', 21: 'NXP (Philips)',
    22: 'Synertek', 25: 'Xicor', 26: 'Zilog', 28: 'Mitsubishi',
    31: 'Atmel', 32: 'SGS/Thomson', 35: 'Wafer Scale Integration',
    37: 'Tristar', 38: 'Visic', 41: 'MicrochipTechnology',
    42: 'Ricoh Ltd.', 44: 'Micron Technology', 47: 'ACTEL',
    49: 'Catalyst', 50: 'Panasonic', 52: 'Cypress',
    55: 'Zarlink(Plessey)', 56: 'UTMC',
    59: 'Integrated CMOS (Vertex)', 61: 'Tektronix',
    62: 'Oracle Corporation', 64: 'ProMos/Mosel Vitelic',
    67: 'Xerox', 69: 'SanDiskCorporation', 70: 'Elan Circuit Tech.',
    73: 'Xilinx', 74: 'Compaq', 76: 'SCI', 79: 'I3 Design System',
    81: 'Crosspoint Solutions', 82: 'Alliance Semiconductor',
    84: 'Hewlett-Packard', 87: 'New Media', 88: 'MHS Electronic',
    91: 'Kawasaki Steel', 93: 'TECMAR', 94: 'Exar',
    97: 'Northern Telecom', 98: 'Sanyo', 100: 'Crystal Semiconductor',
    103: 'Asparix', 104: 'Convex Computer', 107: 'Transwitch',
    109: 'Cannon', 110: 'Altera', 112: 'QUALCOMM',
    115: 'AMS(Austria Micro)', 117: 'Aster Electronics',
    118: 'Bay Networks (Synoptic)', 121: 'Thesys',
    122: 'Solbourne Computer', 124: 'Dialog Semiconductor',
    131: 'Fairchild', 133: 'GTE', 134: 'Harris', 137: 'Intel',
    138: 'I.T.T.', 140: 'Monolithic Memories', 143: 'National',
    145: 'RCA', 146: 'Raytheon', 148: 'Seeq',
    151: 'Texas Instruments', 152: 'Toshiba', 155: 'Eurotechnique',
    157: 'Lucent (AT&T)', 158: 'Exel', 161: 'Lattice Semi.',
    162: 'NCR', 164: 'IBM', 167: 'Intl. CMOS Technology', 168: 'SSSI',
    171: 'VLSI', 173: 'SK Hynix', 174: 'OKI Semiconductor',
    176: 'Sharp', 179: 'IDT', 181: 'DEC', 182: 'LSI Logic',
    185: 'Thinking Machine', 186: 'Thomson CSF', 188: 'Honeywell',
    191: 'Silicon Storage Technology', 193: 'Infineon (Siemens)',
    194: 'Macronix', 196: 'Plus Logic', 199: 'European Silicon Str.',
    200: 'Apple Computer', 203: 'Protocol Engines',
    205: 'Seiko Instruments', 206: 'Samsung', 208: 'Klic',
    211: 'Tandem', 213: 'Integrated Silicon Solutions',
    214: 'Brooktree', 217: 'Performance Semi.',
    218: 'Winbond Electronic', 220: 'Bright Micro', 223: 'PCMCIA',
    224: 'LG Semi (Goldstar)', 227: 'Array Microsystems',
    229: 'Analog Devices', 230: 'PMC-Sierra',
    233: 'Quality Semiconductor', 234: 'Nimbus Technology',
    236: 'Micronas (ITT Intermetall)', 239: 'NEXCOM', 241: 'Sony',
    242: 'Cray Research', 244: 'Vitesse', 247: 'Zentrum/ZMD',
    248: 'TRW', 251: 'Allied-Signal', 253: 'Media Vision',
    254: 'Numonyx Corporation'
}

def bitfieldify(buff, count):
    databits = bitarray()
    for byte_ in buff:
        databits.extend(bin(ord(byte_))[2:].zfill(8))
    lendiff = len(databits)-count
    if count:
        databits = databits[lendiff:]
    return databits

def blen2Blen(bcount):
    """
    Convert a number of bits into the minimum number of bytes to store
    those bits.
    """
    return int(math.ceil(bcount/8.0))

def buff2Blen(buff):
    """
    Shorthand to get the number of bytes required to store a bitarray.
    """
    return blen2Blen(len(buff))

def build_byte_align_buff(buff):
    bitmod = len(buff)%8
    if bitmod == 0:
        rdiff = bitarray()
    else:
        rdiff = bitarray(8-bitmod)
        rdiff.setall(False)
    return rdiff+buff

class JTAGControlError(Exception):
    pass

def pstatus(resflags):
    #print(resflags.__repr__()))
    #if len(resflags)>1:
    #    resflags = resflags[0]
    if not resflags&bitarray('11000011'):
        print(resflags, bitarray('11000011'))
        print(resflags&bitarray('11000011'))
        print()
    print("STATUS: "+("" if (resflags&bitarray('11000011')==bitarray('00000001')) 
                      else "INVALID_STATUS ")+\
        ("ISCDIS " if resflags[-6] else "")+("ISCEN " if resflags[-5] else "")+\
        ("SECURE " if resflags[-4] else "")+("DONE " if resflags[-3] else ""))
