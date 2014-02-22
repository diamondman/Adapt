.PHONY: all

ANTLRLIBS = "../../lib/ANTLR/antlr-3.1.jar:../../lib/ANTLR/stringtemplate-3.2.jar:../../lib/ANTLR/antlr-runtime-3.1.jar:../../lib/ANTLR/antlr-2.7.7.jar"
ANTLRC = java -cp $(ANTLRLIBS) org.antlr.Tool

all:
	$(ANTLRC) jed.g
