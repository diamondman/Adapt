from bitarray import bitarray
import csv

from jedLexer import jedLexer
from jedParser import jedParser
from antlr3 import ANTLRInputStream, CommonTokenStream, RecognitionException

def gc(addr):
    return (addr>>1)^addr

def graycode_buff(num, fillcount):
    buff = bitarray(bin(gc(num))[2:].zfill(fillcount))
    buff.reverse()
    return buff

def parse_file(filename):
    f = open(filename)
    char_stream = ANTLRInputStream(f)
    lexer = jedLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = jedParser(tokens);
    res=parser.eval()
    f.close()
    return res

class BitStream(object):
    def __init__(self, segments):
        self.segments = segments

class JedecConfigFile(object):
    def __init__(self, path):
        self._path = path
        jeddata = parse_file(path)
        self.bits = jeddata['fuses']

    def to_bitstream(self, mappath):
        print "Loading map file..."
        mapf = open(mappath)
        reader = csv.reader(mapf, delimiter='\t')
        mapdata = [row for row in reader]
        
        f = open('/home/diamondman/CPLDTest/lastadaptprog.dat', 'w')
        print len(mapdata)
        outbuffers = []
        for i in range(len(mapdata[0])):
            outbf = bitarray(1364)
            outbf.setall(False)
            for j in range(len(mapdata)):
                v = mapdata[j][i]
                if v.isdigit():
                    outbf[j] = self.bits[int(v)]
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
            f.write(outbf.to01()+"\n")
            outbuffers.append(graycode_buff(i, 7)+outbf)

        f.close()
        return BitStream(outbuffers)
