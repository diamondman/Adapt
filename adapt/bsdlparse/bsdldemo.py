#!/usr/bin/python
import sys
from pprint import pprint

from bsdlLexer import bsdlLexer
from bsdlParser import bsdlParser
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
    lexer = bsdlLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = bsdlParser(tokens);
    pprint(parser.eval())
    f.close()
except RecognitionException:
    traceback.print_stack()
