#!/usr/bin/python
import sys
from pprint import pprint
from antlr4.InputStream import InputStream
from antlr4 import CommonTokenStream, RecognitionException, ParseTreeWalker
from bsdlLexer import bsdlLexer
from bsdlParser import bsdlParser
from bsdlListenerImpl import bsdlListenerImpl

try:
    print(sys.argv[1])
    with open(sys.argv[1]) as f:
        data = f.read()
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
    sys.exit()
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit()

try:
    char_stream = InputStream(data)
    lexer = bsdlLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = bsdlParser(tokens);
    tree = parser.evaluate()
    walker = ParseTreeWalker()
    listener = bsdlListenerImpl()
    walker.walk(listener, tree)

    pprint(listener.result)

except RecognitionException:
    traceback.print_stack()
