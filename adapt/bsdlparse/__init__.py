from antlr4.InputStream import InputStream
from antlr4 import CommonTokenStream, RecognitionException, ParseTreeWalker
from .bsdlLexer import bsdlLexer
from .bsdlParser import bsdlParser
from .bsdlListenerImpl import bsdlListenerImpl

def parse_file(filename):
    with open(filename) as f:
        data = f.read()
    char_stream = InputStream(data)
    lexer = bsdlLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = bsdlParser(tokens);
    tree = parser.evaluate()
    walker = ParseTreeWalker()
    listener = bsdlListenerImpl()
    walker.walk(listener, tree)
    return listener.result
