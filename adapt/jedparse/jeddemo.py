#!/usr/bin/python
import sys
from pprint import pprint

from jedLexer import jedLexer
from jedParser import jedParser
from antlr3 import ANTLRInputStream, CommonTokenStream, RecognitionException

try:
    print sys.argv[1]
    f = open(sys.argv[1])
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit()
except:
    print "Unexpected error:", sys.exc_info()[0]
    sys.exit()

try:
    char_stream = ANTLRInputStream(f)
    lexer = jedLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = jedParser(tokens);
    res = parser.eval()
    bits = res['fuses']
    print "0s", bits.count(0)
    print "1s", bits.count(1)

    import csv
    from bitarray import bitarray
    mapf = open('/media/F02472C324728BFA/Xilinx/14.7/ISE_DS/ISE/xbr/data/xc2c256.map' )
    reader = csv.reader(mapf, delimiter='\t')

    mapdata = [row for row in reader]

    for i in range(len(mapdata[0])):
        outbf = bitarray(1364)
        outbf.setall(False)
        for j in range(len(mapdata)):
            v = mapdata[j][i]
            if v.isdigit():
                #print "[%s][%s]=%s (%s)"%(j,i,v, bits[int(v)])
                outbf[j] = bits[int(v)]
            elif (v != "") and (v != "spare"):
                if v == "done_0":
                    outbf[j] = 1
                if v == "done_1":
                    outbf[j] = 0
                #else:
                #    print "UNK [%s][%s]=%s"%(j,i,v.__repr__())
        print outbf

    f.close()
except RecognitionException:
    traceback.print_stack()
