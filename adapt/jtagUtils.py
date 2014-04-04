import csv
import os
from bitarray import bitarray

adapt_base_dir = os.path.abspath(os.path.split(os.path.split(__file__)[0])[0])

manufacturer_lookup = {}
with open(os.path.join(adapt_base_dir, 'res', 'jtagmanufacturers.txt')) as f:
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
