#!/usr/bin/python
from bitarray import bitarray
import csv

from jtagUtils import graycode_buff

class JedecConfigFile(object):
    def __init__(self, path):
        self.entity_started = False
        self.entity_finished = False
        
        self.device_name = None
        self.default_test = None
        self.default_fuse = None
        self.fuse_count = None
        self.checksum = None
        self.pin_count = None
        self.dev_id = None
        self.fuses = bitarray()

        with open(path) as f:
            last_addr = 0
            for line in f:
                line = line.replace('\n', '').replace('\r','')
        
                if not self.entity_started:
                    if '\x02' in line:
                        stx_index = line.index('\x02')
                        line = line[stx_index+1:]
                        self.entity_started = True
                    else:
                        continue
                
                if self.entity_finished:
                    break
        
                if '\x03' in line:
                    etx_index = line.index('\x03')
                    line = line[:etx_index]
                    self.entity_finished = True
        
                if len(line)==0:
                    continue
        
                if line[-1] != '*':
                    raise Exception("FUCK")
                else:
                    line = line[:-1]
        
                term = line[0].upper()
                if term == 'L':
                    space_index = line.index(' ')
                    addr = int(line[1:space_index])
                    addr_diff = addr-len(self.fuses)
                    if addr_diff<0:
                        raise Exception("Addresses for fuse bits must monotonically increase")
                    if addr_diff:
                        self.fuses += bitarray(('1' if self.default_fuse else '0')*addr_diff)
                    data = bitarray(line[space_index+1:])
                    self.fuses += data
                elif term == 'N':
                    if "DEVICE" in line:
                        term_index = line.index("DEVICE")
                        self.device_name = line[term_index+7:].replace(' ', '')
                elif term == 'C':
                    self.checksum = int(line[1:].replace(' ', ''), 16)
                elif term == 'J':
                    self.dev_id = line[1:]
                elif term == 'F':
                    default_fuse_str = line[1:].replace(' ', '')
                    if len(default_fuse_str) is not 1:
                        raise Exception("F term can only have one bit")
                    self.default_fuse = int(default_fuse_str, 2)
                elif term == 'X':
                    default_test_str = line[1:].replace(' ', '')
                    if len(default_test_str) is not 1:
                        raise Exception("X term can only have one bit")
                    self.default_test = int(default_test_str, 2)
        
                elif term == 'Q' and len(line)>1:
                    term2 = line[1].upper()
                    if term2 == 'F':
                        self.fuse_count = int(line[2:].replace(' ', ''))
                    elif term2 == 'P': #PINCOUNT
                        self.pin_count = int(line[2:].replace(' ', ''))
                    elif term2 == 'V': #TESTVECMAX
                        self.test_vec_max = int(line[2:].replace(' ', ''))
                else:
                    raise NotImplementedError

        fuselen_diff = self.fuse_count-len(self.fuses)
        if fuselen_diff>0:
            print "ADDING", fuselen_diff
            self.fuses += bitarray(('1' if self.default_fuse else '0')*fuselen_diff)
        if fuselen_diff<0:
            raise Exception("Too many bits provided in jed file fuses")


    def to_bitstream(self, mappath):
        print "Loading map file..."
        mapf = open(mappath)
        reader = csv.reader(mapf, delimiter='\t')
        mapdata = [row for row in reader]
        

        print "Translating programming file to bitstream..."
        outbuffers = []
        for i in range(len(mapdata[0])):
            outbf = bitarray(1364)
            outbf.setall(False)
            for j in range(len(mapdata)):
                v = mapdata[j][i]
                if v.isdigit():
                    outbf[j] = self.fuses[int(v)]
                elif i in (0,681,682,1363):
                    outbf[j] = 1
                elif v == "done_0":
                    outbf[j] = 1
                    outbf[0] = 1
                elif v == "done_1":
                    outbf[j] = 0
                    outbf[j+1:] = 1
                elif "sec_" in v:
                    outbf[j] = 1
                elif v == "":
                    outbf[j] = 1
            outbuffers.append(graycode_buff(i, 7)+outbf)

        return BitStream(outbuffers)


class BitStream(object):
    def __init__(self, segments):
        self.segments = segments

if __name__ == "__main__":
    import sys
    j = JedecConfigFile(sys.argv[1])
    print "DEVICE:     ", j.device_name
    print "FUSECOUNT:  ", j.fuse_count
    print "DEFAULTTEST:", j.default_test
    print "DEFAULTFUSE:", j.default_fuse
    print "CHECKSUM:   ", j.checksum
    print "PINCOUNT:   ", j.pin_count
    print "TESTVECMAX: ", j.test_vec_max
    print "DEVID:      ", j.dev_id
    print "FUSES:      ", j.fuses
