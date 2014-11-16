import csv
import os
import math
from bitarray import bitarray

NULL_ID_CODES = [bitarray('1'*32),
                 bitarray('0'*32)]

adapt_base_dir = os.path.abspath(os.path.split(os.path.split(__file__)[0])[0]) 

manufacturer_lookup = {}
try:
    with open(os.path.join(adapt_base_dir, 'res', 'jtagmanufacturers.txt')) as f:
        reader = csv.reader(f,delimiter=';')
        manufacturer_lookup={int(r[0],16):r[1] for r in reader}
except IOError as e:
    with open(os.path.join(adapt_base_dir, '..', 'res', 'jtagmanufacturers.txt')) as f:
        reader = csv.reader(f,delimiter=';')
        manufacturer_lookup={int(r[0],16):r[1] for r in reader}

def bitfieldify(buff, count):
    #bits = bitarray(''.join([bin(ord(i))[2:].zfill(8) for i in buff])[-count:])
    databits = bitarray()
    for byte_ in buff:
        databits.extend(bin(ord(byte_))[2:].zfill(8))
        #databits.fromstring(byte_)
    lendiff = len(databits)-count
    if count:
        databits = databits[lendiff:]
    return databits


def gc(addr):
    return (addr>>1)^addr

def graycode_buff(num, fillcount):
    buff = bitarray(bin(gc(num))[2:].zfill(fillcount))
    buff.reverse()
    return buff

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
        #print("NO BUFF NEEDED", rdiff)
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
