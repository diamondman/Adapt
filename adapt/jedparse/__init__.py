from jedLexer import jedLexer
from jedParser import jedParser
from antlr3 import ANTLRInputStream, CommonTokenStream, RecognitionException

def parse_file(filename):
    f = open(filename)
    char_stream = ANTLRInputStream(f)
    lexer = jedLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = jedParser(tokens);
    res=parser.eval()
    f.close()
    return res
