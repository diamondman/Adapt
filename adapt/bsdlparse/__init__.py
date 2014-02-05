from bsdlLexer import bsdlLexer
from bsdlParser import bsdlParser
from antlr3 import ANTLRInputStream, CommonTokenStream, RecognitionException

def parse_file(filename):
    f = open(filename)
    char_stream = ANTLRInputStream(f)
    lexer = bsdlLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = bsdlParser(tokens);
    res=parser.eval()
    f.close()
    return res
