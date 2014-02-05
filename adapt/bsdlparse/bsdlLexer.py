# $ANTLR 3.1 bsdl.g 2014-02-05 02:26:56

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
PACKAGE=87
FUNCTION=64
NAND=77
INERTIAL=70
SEVERITY=102
WHILE=118
ROR=100
GENERIC=8
MOD=76
CASE=54
CHAR=122
NEW=78
NOR=80
NOT=81
POSTPONED=88
SUBTYPE=108
EOF=-1
ROL=99
TYPE=111
WORD=30
UNITS=113
DOWNTO=58
LOOP=74
BEGIN=51
RETURN=98
BOTH=23
TRANSPORT=110
IMPURE=69
BODY=53
ICHAR=39
GENERATE=65
LINKAGE=35
COMMENT=41
REGISTER=94
SELECT=101
ARRAY=49
EXIT=61
SHARED=103
RECORD=93
GUARDED=67
SRL=107
SRA=106
NULL=82
XNOR=120
ELSE=59
ON=83
WHITESPACE=40
BUS=36
WAIT=116
OF=17
FILE=62
ASSERT=50
ABS=43
GROUP=66
VARIABLE=115
OUT=32
UNTIL=114
USCORE=42
OR=85
ALIAS=46
ANDSIGN=38
CONSTANT=24
USE=13
ELSIF=60
END=7
FALSE=21
BIT_VECTOR=27
OTHERS=86
REPORT=97
SLA=104
ATTRIBUTE=16
T__123=123
FOR=63
CONFIGURATION=56
LIBRARY=72
SLL=105
ARCHITECTURE=48
AND=47
IF=68
INOUT=33
ENTITY=4
PURE=91
THEN=109
IN=31
COMMA=22
IS=5
REJECT=95
EQUAL=11
ALL=15
SIGNAL=19
ACCESS=44
NEXT=79
CPAREN=12
DIGIT=18
DOT=14
COMPONENT=55
WITH=119
SCOLON=6
FULLCASE_WORD=29
XOR=121
TO=28
OPAREN=9
DISCONNECT=57
PORT=25
BUFFER=34
RANGE=92
LITERAL=73
AFTER=45
REM=96
TRUE=20
PROCEDURE=89
OPEN=84
COLON=10
LABEL=71
WHEN=117
BLOCK=52
MAP=75
BIT=26
PROCESS=90
UNAFFECTED=112
STRING=37


class bsdlLexer(Lexer):

    grammarFileName = "bsdl.g"
    antlr_version = version_str_to_tuple("3.1")
    antlr_version_str = "3.1"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )






    # $ANTLR start "T__123"
    def mT__123(self, ):

        try:
            _type = T__123
            _channel = DEFAULT_CHANNEL

            # bsdl.g:7:8: ( 'e' )
            # bsdl.g:7:10: 'e'
            pass 
            self.match(101)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__123"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # bsdl.g:118:8: ( '\"' ( ICHAR | DIGIT | '_' | '.' | ',' | ' ' | ':' | ';' | '(' | ')' | '[' | ']' | '*' | '\\t' )* '\"' )
            # bsdl.g:118:12: '\"' ( ICHAR | DIGIT | '_' | '.' | ',' | ' ' | ':' | ';' | '(' | ')' | '[' | ']' | '*' | '\\t' )* '\"'
            pass 
            self.match(34)
            # bsdl.g:118:16: ( ICHAR | DIGIT | '_' | '.' | ',' | ' ' | ':' | ';' | '(' | ')' | '[' | ']' | '*' | '\\t' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 9 or LA1_0 == 32 or (40 <= LA1_0 <= 42) or LA1_0 == 44 or LA1_0 == 46 or (48 <= LA1_0 <= 59) or (65 <= LA1_0 <= 91) or LA1_0 == 93 or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # bsdl.g:
                    pass 
                    if self.input.LA(1) == 9 or self.input.LA(1) == 32 or (40 <= self.input.LA(1) <= 42) or self.input.LA(1) == 44 or self.input.LA(1) == 46 or (48 <= self.input.LA(1) <= 59) or (65 <= self.input.LA(1) <= 91) or self.input.LA(1) == 93 or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop1


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:121:5: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            # bsdl.g:121:7: ( ' ' | '\\t' | '\\r' | '\\n' )+
            pass 
            # bsdl.g:121:7: ( ' ' | '\\t' | '\\r' | '\\n' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((9 <= LA2_0 <= 10) or LA2_0 == 13 or LA2_0 == 32) :
                    alt2 = 1


                if alt2 == 1:
                    # bsdl.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1


            #action start
            _channel = HIDDEN 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:124:5: ( '--' (~ ( '\\r' | '\\n' ) )* )
            # bsdl.g:124:8: '--' (~ ( '\\r' | '\\n' ) )*
            pass 
            self.match("--")
            # bsdl.g:124:13: (~ ( '\\r' | '\\n' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 9) or (11 <= LA3_0 <= 12) or (14 <= LA3_0 <= 65534)) :
                    alt3 = 1


                if alt3 == 1:
                    # bsdl.g:124:13: ~ ( '\\r' | '\\n' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65534):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3


            #action start
            _channel = HIDDEN 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "ANDSIGN"
    def mANDSIGN(self, ):

        try:
            _type = ANDSIGN
            _channel = DEFAULT_CHANNEL

            # bsdl.g:127:17: ( '&' )
            # bsdl.g:127:19: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ANDSIGN"



    # $ANTLR start "USCORE"
    def mUSCORE(self, ):

        try:
            _type = USCORE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:128:17: ( '_' )
            # bsdl.g:128:19: '_'
            pass 
            self.match(95)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "USCORE"



    # $ANTLR start "OPAREN"
    def mOPAREN(self, ):

        try:
            _type = OPAREN
            _channel = DEFAULT_CHANNEL

            # bsdl.g:129:17: ( '(' )
            # bsdl.g:129:19: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPAREN"



    # $ANTLR start "CPAREN"
    def mCPAREN(self, ):

        try:
            _type = CPAREN
            _channel = DEFAULT_CHANNEL

            # bsdl.g:130:17: ( ')' )
            # bsdl.g:130:19: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CPAREN"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # bsdl.g:131:17: ( ':' )
            # bsdl.g:131:19: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "SCOLON"
    def mSCOLON(self, ):

        try:
            _type = SCOLON
            _channel = DEFAULT_CHANNEL

            # bsdl.g:132:17: ( ';' )
            # bsdl.g:132:19: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SCOLON"



    # $ANTLR start "EQUAL"
    def mEQUAL(self, ):

        try:
            _type = EQUAL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:133:17: ( '=' )
            # bsdl.g:133:19: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUAL"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # bsdl.g:134:17: ( ',' )
            # bsdl.g:134:19: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:135:17: ( '.' )
            # bsdl.g:135:19: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "BIT"
    def mBIT(self, ):

        try:
            _type = BIT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:137:17: ( 'bit' )
            # bsdl.g:137:22: 'bit'
            pass 
            self.match("bit")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BIT"



    # $ANTLR start "BIT_VECTOR"
    def mBIT_VECTOR(self, ):

        try:
            _type = BIT_VECTOR
            _channel = DEFAULT_CHANNEL

            # bsdl.g:138:17: ( 'bit_vector' )
            # bsdl.g:138:22: 'bit_vector'
            pass 
            self.match("bit_vector")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BIT_VECTOR"



    # $ANTLR start "ABS"
    def mABS(self, ):

        try:
            _type = ABS
            _channel = DEFAULT_CHANNEL

            # bsdl.g:140:17: ( 'abs' )
            # bsdl.g:140:22: 'abs'
            pass 
            self.match("abs")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ABS"



    # $ANTLR start "ACCESS"
    def mACCESS(self, ):

        try:
            _type = ACCESS
            _channel = DEFAULT_CHANNEL

            # bsdl.g:141:17: ( 'access' )
            # bsdl.g:141:22: 'access'
            pass 
            self.match("access")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ACCESS"



    # $ANTLR start "AFTER"
    def mAFTER(self, ):

        try:
            _type = AFTER
            _channel = DEFAULT_CHANNEL

            # bsdl.g:142:17: ( 'after' )
            # bsdl.g:142:22: 'after'
            pass 
            self.match("after")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AFTER"



    # $ANTLR start "ALIAS"
    def mALIAS(self, ):

        try:
            _type = ALIAS
            _channel = DEFAULT_CHANNEL

            # bsdl.g:143:17: ( 'alias' )
            # bsdl.g:143:22: 'alias'
            pass 
            self.match("alias")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ALIAS"



    # $ANTLR start "ALL"
    def mALL(self, ):

        try:
            _type = ALL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:144:17: ( 'all' )
            # bsdl.g:144:22: 'all'
            pass 
            self.match("all")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ALL"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # bsdl.g:145:17: ( 'and' )
            # bsdl.g:145:22: 'and'
            pass 
            self.match("and")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "ARCHITECTURE"
    def mARCHITECTURE(self, ):

        try:
            _type = ARCHITECTURE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:146:17: ( 'architecture' )
            # bsdl.g:146:22: 'architecture'
            pass 
            self.match("architecture")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ARCHITECTURE"



    # $ANTLR start "ARRAY"
    def mARRAY(self, ):

        try:
            _type = ARRAY
            _channel = DEFAULT_CHANNEL

            # bsdl.g:147:17: ( 'array' )
            # bsdl.g:147:22: 'array'
            pass 
            self.match("array")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ARRAY"



    # $ANTLR start "ASSERT"
    def mASSERT(self, ):

        try:
            _type = ASSERT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:148:17: ( 'assert' )
            # bsdl.g:148:22: 'assert'
            pass 
            self.match("assert")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSERT"



    # $ANTLR start "ATTRIBUTE"
    def mATTRIBUTE(self, ):

        try:
            _type = ATTRIBUTE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:149:17: ( 'attribute' )
            # bsdl.g:149:22: 'attribute'
            pass 
            self.match("attribute")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ATTRIBUTE"



    # $ANTLR start "BEGIN"
    def mBEGIN(self, ):

        try:
            _type = BEGIN
            _channel = DEFAULT_CHANNEL

            # bsdl.g:150:17: ( 'begin' )
            # bsdl.g:150:22: 'begin'
            pass 
            self.match("begin")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BEGIN"



    # $ANTLR start "BLOCK"
    def mBLOCK(self, ):

        try:
            _type = BLOCK
            _channel = DEFAULT_CHANNEL

            # bsdl.g:151:17: ( 'block' )
            # bsdl.g:151:22: 'block'
            pass 
            self.match("block")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BLOCK"



    # $ANTLR start "BODY"
    def mBODY(self, ):

        try:
            _type = BODY
            _channel = DEFAULT_CHANNEL

            # bsdl.g:152:17: ( 'body' )
            # bsdl.g:152:22: 'body'
            pass 
            self.match("body")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BODY"



    # $ANTLR start "BUFFER"
    def mBUFFER(self, ):

        try:
            _type = BUFFER
            _channel = DEFAULT_CHANNEL

            # bsdl.g:153:17: ( 'buffer' )
            # bsdl.g:153:22: 'buffer'
            pass 
            self.match("buffer")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BUFFER"



    # $ANTLR start "BUS"
    def mBUS(self, ):

        try:
            _type = BUS
            _channel = DEFAULT_CHANNEL

            # bsdl.g:154:17: ( 'bus' )
            # bsdl.g:154:22: 'bus'
            pass 
            self.match("bus")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BUS"



    # $ANTLR start "CASE"
    def mCASE(self, ):

        try:
            _type = CASE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:155:17: ( 'case' )
            # bsdl.g:155:22: 'case'
            pass 
            self.match("case")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CASE"



    # $ANTLR start "COMPONENT"
    def mCOMPONENT(self, ):

        try:
            _type = COMPONENT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:156:17: ( 'component' )
            # bsdl.g:156:22: 'component'
            pass 
            self.match("component")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMPONENT"



    # $ANTLR start "CONFIGURATION"
    def mCONFIGURATION(self, ):

        try:
            _type = CONFIGURATION
            _channel = DEFAULT_CHANNEL

            # bsdl.g:157:17: ( 'configuration' )
            # bsdl.g:157:22: 'configuration'
            pass 
            self.match("configuration")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONFIGURATION"



    # $ANTLR start "CONSTANT"
    def mCONSTANT(self, ):

        try:
            _type = CONSTANT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:158:17: ( 'constant' )
            # bsdl.g:158:22: 'constant'
            pass 
            self.match("constant")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONSTANT"



    # $ANTLR start "DISCONNECT"
    def mDISCONNECT(self, ):

        try:
            _type = DISCONNECT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:159:17: ( 'disconnect' )
            # bsdl.g:159:22: 'disconnect'
            pass 
            self.match("disconnect")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DISCONNECT"



    # $ANTLR start "DOWNTO"
    def mDOWNTO(self, ):

        try:
            _type = DOWNTO
            _channel = DEFAULT_CHANNEL

            # bsdl.g:160:17: ( 'downto' )
            # bsdl.g:160:22: 'downto'
            pass 
            self.match("downto")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOWNTO"



    # $ANTLR start "ELSE"
    def mELSE(self, ):

        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:161:17: ( 'else' )
            # bsdl.g:161:22: 'else'
            pass 
            self.match("else")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "ELSIF"
    def mELSIF(self, ):

        try:
            _type = ELSIF
            _channel = DEFAULT_CHANNEL

            # bsdl.g:162:17: ( 'elsif' )
            # bsdl.g:162:22: 'elsif'
            pass 
            self.match("elsif")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ELSIF"



    # $ANTLR start "END"
    def mEND(self, ):

        try:
            _type = END
            _channel = DEFAULT_CHANNEL

            # bsdl.g:163:17: ( 'end' )
            # bsdl.g:163:22: 'end'
            pass 
            self.match("end")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "END"



    # $ANTLR start "ENTITY"
    def mENTITY(self, ):

        try:
            _type = ENTITY
            _channel = DEFAULT_CHANNEL

            # bsdl.g:164:17: ( 'entity' )
            # bsdl.g:164:22: 'entity'
            pass 
            self.match("entity")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ENTITY"



    # $ANTLR start "EXIT"
    def mEXIT(self, ):

        try:
            _type = EXIT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:165:17: ( 'exit' )
            # bsdl.g:165:22: 'exit'
            pass 
            self.match("exit")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXIT"



    # $ANTLR start "FILE"
    def mFILE(self, ):

        try:
            _type = FILE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:166:17: ( 'file' )
            # bsdl.g:166:22: 'file'
            pass 
            self.match("file")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FILE"



    # $ANTLR start "FOR"
    def mFOR(self, ):

        try:
            _type = FOR
            _channel = DEFAULT_CHANNEL

            # bsdl.g:167:17: ( 'for' )
            # bsdl.g:167:22: 'for'
            pass 
            self.match("for")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FOR"



    # $ANTLR start "FUNCTION"
    def mFUNCTION(self, ):

        try:
            _type = FUNCTION
            _channel = DEFAULT_CHANNEL

            # bsdl.g:168:17: ( 'function' )
            # bsdl.g:168:22: 'function'
            pass 
            self.match("function")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FUNCTION"



    # $ANTLR start "GENERATE"
    def mGENERATE(self, ):

        try:
            _type = GENERATE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:169:17: ( 'generate' )
            # bsdl.g:169:22: 'generate'
            pass 
            self.match("generate")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GENERATE"



    # $ANTLR start "GENERIC"
    def mGENERIC(self, ):

        try:
            _type = GENERIC
            _channel = DEFAULT_CHANNEL

            # bsdl.g:170:17: ( 'generic' )
            # bsdl.g:170:22: 'generic'
            pass 
            self.match("generic")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GENERIC"



    # $ANTLR start "GROUP"
    def mGROUP(self, ):

        try:
            _type = GROUP
            _channel = DEFAULT_CHANNEL

            # bsdl.g:171:17: ( 'group' )
            # bsdl.g:171:22: 'group'
            pass 
            self.match("group")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GROUP"



    # $ANTLR start "GUARDED"
    def mGUARDED(self, ):

        try:
            _type = GUARDED
            _channel = DEFAULT_CHANNEL

            # bsdl.g:172:17: ( 'guarded' )
            # bsdl.g:172:22: 'guarded'
            pass 
            self.match("guarded")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GUARDED"



    # $ANTLR start "IF"
    def mIF(self, ):

        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # bsdl.g:173:17: ( 'if' )
            # bsdl.g:173:22: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IF"



    # $ANTLR start "IMPURE"
    def mIMPURE(self, ):

        try:
            _type = IMPURE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:174:17: ( 'impure' )
            # bsdl.g:174:22: 'impure'
            pass 
            self.match("impure")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IMPURE"



    # $ANTLR start "IN"
    def mIN(self, ):

        try:
            _type = IN
            _channel = DEFAULT_CHANNEL

            # bsdl.g:175:17: ( 'in' )
            # bsdl.g:175:22: 'in'
            pass 
            self.match("in")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IN"



    # $ANTLR start "INERTIAL"
    def mINERTIAL(self, ):

        try:
            _type = INERTIAL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:176:17: ( 'inertial' )
            # bsdl.g:176:22: 'inertial'
            pass 
            self.match("inertial")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INERTIAL"



    # $ANTLR start "INOUT"
    def mINOUT(self, ):

        try:
            _type = INOUT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:177:17: ( 'inout' )
            # bsdl.g:177:22: 'inout'
            pass 
            self.match("inout")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INOUT"



    # $ANTLR start "IS"
    def mIS(self, ):

        try:
            _type = IS
            _channel = DEFAULT_CHANNEL

            # bsdl.g:178:17: ( 'is' )
            # bsdl.g:178:22: 'is'
            pass 
            self.match("is")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IS"



    # $ANTLR start "LABEL"
    def mLABEL(self, ):

        try:
            _type = LABEL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:179:17: ( 'label' )
            # bsdl.g:179:22: 'label'
            pass 
            self.match("label")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LABEL"



    # $ANTLR start "LIBRARY"
    def mLIBRARY(self, ):

        try:
            _type = LIBRARY
            _channel = DEFAULT_CHANNEL

            # bsdl.g:180:17: ( 'library' )
            # bsdl.g:180:22: 'library'
            pass 
            self.match("library")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LIBRARY"



    # $ANTLR start "LINKAGE"
    def mLINKAGE(self, ):

        try:
            _type = LINKAGE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:181:17: ( 'linkage' )
            # bsdl.g:181:22: 'linkage'
            pass 
            self.match("linkage")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINKAGE"



    # $ANTLR start "LITERAL"
    def mLITERAL(self, ):

        try:
            _type = LITERAL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:182:17: ( 'literal' )
            # bsdl.g:182:22: 'literal'
            pass 
            self.match("literal")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LITERAL"



    # $ANTLR start "LOOP"
    def mLOOP(self, ):

        try:
            _type = LOOP
            _channel = DEFAULT_CHANNEL

            # bsdl.g:183:17: ( 'loop' )
            # bsdl.g:183:22: 'loop'
            pass 
            self.match("loop")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOOP"



    # $ANTLR start "MAP"
    def mMAP(self, ):

        try:
            _type = MAP
            _channel = DEFAULT_CHANNEL

            # bsdl.g:184:17: ( 'map' )
            # bsdl.g:184:22: 'map'
            pass 
            self.match("map")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MAP"



    # $ANTLR start "MOD"
    def mMOD(self, ):

        try:
            _type = MOD
            _channel = DEFAULT_CHANNEL

            # bsdl.g:185:17: ( 'mod' )
            # bsdl.g:185:22: 'mod'
            pass 
            self.match("mod")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MOD"



    # $ANTLR start "NAND"
    def mNAND(self, ):

        try:
            _type = NAND
            _channel = DEFAULT_CHANNEL

            # bsdl.g:186:17: ( 'nand' )
            # bsdl.g:186:22: 'nand'
            pass 
            self.match("nand")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NAND"



    # $ANTLR start "NEW"
    def mNEW(self, ):

        try:
            _type = NEW
            _channel = DEFAULT_CHANNEL

            # bsdl.g:187:17: ( 'new' )
            # bsdl.g:187:22: 'new'
            pass 
            self.match("new")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEW"



    # $ANTLR start "NEXT"
    def mNEXT(self, ):

        try:
            _type = NEXT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:188:17: ( 'next' )
            # bsdl.g:188:22: 'next'
            pass 
            self.match("next")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEXT"



    # $ANTLR start "NOR"
    def mNOR(self, ):

        try:
            _type = NOR
            _channel = DEFAULT_CHANNEL

            # bsdl.g:189:17: ( 'nor' )
            # bsdl.g:189:22: 'nor'
            pass 
            self.match("nor")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOR"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:190:17: ( 'not' )
            # bsdl.g:190:22: 'not'
            pass 
            self.match("not")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "NULL"
    def mNULL(self, ):

        try:
            _type = NULL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:191:17: ( 'null' )
            # bsdl.g:191:22: 'null'
            pass 
            self.match("null")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NULL"



    # $ANTLR start "OF"
    def mOF(self, ):

        try:
            _type = OF
            _channel = DEFAULT_CHANNEL

            # bsdl.g:192:17: ( 'of' )
            # bsdl.g:192:22: 'of'
            pass 
            self.match("of")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OF"



    # $ANTLR start "ON"
    def mON(self, ):

        try:
            _type = ON
            _channel = DEFAULT_CHANNEL

            # bsdl.g:193:17: ( 'on' )
            # bsdl.g:193:22: 'on'
            pass 
            self.match("on")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ON"



    # $ANTLR start "OPEN"
    def mOPEN(self, ):

        try:
            _type = OPEN
            _channel = DEFAULT_CHANNEL

            # bsdl.g:194:17: ( 'open' )
            # bsdl.g:194:22: 'open'
            pass 
            self.match("open")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPEN"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # bsdl.g:195:17: ( 'or' )
            # bsdl.g:195:22: 'or'
            pass 
            self.match("or")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "OTHERS"
    def mOTHERS(self, ):

        try:
            _type = OTHERS
            _channel = DEFAULT_CHANNEL

            # bsdl.g:196:17: ( 'others' )
            # bsdl.g:196:22: 'others'
            pass 
            self.match("others")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OTHERS"



    # $ANTLR start "OUT"
    def mOUT(self, ):

        try:
            _type = OUT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:197:17: ( 'out' )
            # bsdl.g:197:22: 'out'
            pass 
            self.match("out")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OUT"



    # $ANTLR start "PACKAGE"
    def mPACKAGE(self, ):

        try:
            _type = PACKAGE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:198:17: ( 'package' )
            # bsdl.g:198:22: 'package'
            pass 
            self.match("package")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PACKAGE"



    # $ANTLR start "PORT"
    def mPORT(self, ):

        try:
            _type = PORT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:199:17: ( 'port' )
            # bsdl.g:199:22: 'port'
            pass 
            self.match("port")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PORT"



    # $ANTLR start "POSTPONED"
    def mPOSTPONED(self, ):

        try:
            _type = POSTPONED
            _channel = DEFAULT_CHANNEL

            # bsdl.g:200:17: ( 'postponed' )
            # bsdl.g:200:22: 'postponed'
            pass 
            self.match("postponed")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "POSTPONED"



    # $ANTLR start "PROCEDURE"
    def mPROCEDURE(self, ):

        try:
            _type = PROCEDURE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:201:17: ( 'procedure' )
            # bsdl.g:201:22: 'procedure'
            pass 
            self.match("procedure")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PROCEDURE"



    # $ANTLR start "PROCESS"
    def mPROCESS(self, ):

        try:
            _type = PROCESS
            _channel = DEFAULT_CHANNEL

            # bsdl.g:202:17: ( 'process' )
            # bsdl.g:202:22: 'process'
            pass 
            self.match("process")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PROCESS"



    # $ANTLR start "PURE"
    def mPURE(self, ):

        try:
            _type = PURE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:203:17: ( 'pure' )
            # bsdl.g:203:22: 'pure'
            pass 
            self.match("pure")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PURE"



    # $ANTLR start "RANGE"
    def mRANGE(self, ):

        try:
            _type = RANGE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:204:17: ( 'range' )
            # bsdl.g:204:22: 'range'
            pass 
            self.match("range")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RANGE"



    # $ANTLR start "RECORD"
    def mRECORD(self, ):

        try:
            _type = RECORD
            _channel = DEFAULT_CHANNEL

            # bsdl.g:205:17: ( 'record' )
            # bsdl.g:205:22: 'record'
            pass 
            self.match("record")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RECORD"



    # $ANTLR start "REGISTER"
    def mREGISTER(self, ):

        try:
            _type = REGISTER
            _channel = DEFAULT_CHANNEL

            # bsdl.g:206:17: ( 'register' )
            # bsdl.g:206:22: 'register'
            pass 
            self.match("register")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REGISTER"



    # $ANTLR start "REJECT"
    def mREJECT(self, ):

        try:
            _type = REJECT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:207:17: ( 'reject' )
            # bsdl.g:207:22: 'reject'
            pass 
            self.match("reject")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REJECT"



    # $ANTLR start "REM"
    def mREM(self, ):

        try:
            _type = REM
            _channel = DEFAULT_CHANNEL

            # bsdl.g:208:17: ( 'rem' )
            # bsdl.g:208:22: 'rem'
            pass 
            self.match("rem")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REM"



    # $ANTLR start "REPORT"
    def mREPORT(self, ):

        try:
            _type = REPORT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:209:17: ( 'report' )
            # bsdl.g:209:22: 'report'
            pass 
            self.match("report")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REPORT"



    # $ANTLR start "RETURN"
    def mRETURN(self, ):

        try:
            _type = RETURN
            _channel = DEFAULT_CHANNEL

            # bsdl.g:210:17: ( 'return' )
            # bsdl.g:210:22: 'return'
            pass 
            self.match("return")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RETURN"



    # $ANTLR start "ROL"
    def mROL(self, ):

        try:
            _type = ROL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:211:17: ( 'rol' )
            # bsdl.g:211:22: 'rol'
            pass 
            self.match("rol")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROL"



    # $ANTLR start "ROR"
    def mROR(self, ):

        try:
            _type = ROR
            _channel = DEFAULT_CHANNEL

            # bsdl.g:212:17: ( 'ror' )
            # bsdl.g:212:22: 'ror'
            pass 
            self.match("ror")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROR"



    # $ANTLR start "SELECT"
    def mSELECT(self, ):

        try:
            _type = SELECT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:213:17: ( 'select' )
            # bsdl.g:213:22: 'select'
            pass 
            self.match("select")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SELECT"



    # $ANTLR start "SEVERITY"
    def mSEVERITY(self, ):

        try:
            _type = SEVERITY
            _channel = DEFAULT_CHANNEL

            # bsdl.g:214:17: ( 'severity' )
            # bsdl.g:214:22: 'severity'
            pass 
            self.match("severity")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEVERITY"



    # $ANTLR start "SIGNAL"
    def mSIGNAL(self, ):

        try:
            _type = SIGNAL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:215:17: ( 'signal' )
            # bsdl.g:215:22: 'signal'
            pass 
            self.match("signal")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SIGNAL"



    # $ANTLR start "SHARED"
    def mSHARED(self, ):

        try:
            _type = SHARED
            _channel = DEFAULT_CHANNEL

            # bsdl.g:216:17: ( 'shared' )
            # bsdl.g:216:22: 'shared'
            pass 
            self.match("shared")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SHARED"



    # $ANTLR start "SLA"
    def mSLA(self, ):

        try:
            _type = SLA
            _channel = DEFAULT_CHANNEL

            # bsdl.g:217:17: ( 'sla' )
            # bsdl.g:217:22: 'sla'
            pass 
            self.match("sla")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SLA"



    # $ANTLR start "SLL"
    def mSLL(self, ):

        try:
            _type = SLL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:218:17: ( 'sll' )
            # bsdl.g:218:22: 'sll'
            pass 
            self.match("sll")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SLL"



    # $ANTLR start "SRA"
    def mSRA(self, ):

        try:
            _type = SRA
            _channel = DEFAULT_CHANNEL

            # bsdl.g:219:17: ( 'sra' )
            # bsdl.g:219:22: 'sra'
            pass 
            self.match("sra")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SRA"



    # $ANTLR start "SRL"
    def mSRL(self, ):

        try:
            _type = SRL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:220:17: ( 'srl' )
            # bsdl.g:220:22: 'srl'
            pass 
            self.match("srl")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SRL"



    # $ANTLR start "SUBTYPE"
    def mSUBTYPE(self, ):

        try:
            _type = SUBTYPE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:221:17: ( 'subtype' )
            # bsdl.g:221:22: 'subtype'
            pass 
            self.match("subtype")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SUBTYPE"



    # $ANTLR start "THEN"
    def mTHEN(self, ):

        try:
            _type = THEN
            _channel = DEFAULT_CHANNEL

            # bsdl.g:222:17: ( 'then' )
            # bsdl.g:222:22: 'then'
            pass 
            self.match("then")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THEN"



    # $ANTLR start "TO"
    def mTO(self, ):

        try:
            _type = TO
            _channel = DEFAULT_CHANNEL

            # bsdl.g:223:17: ( 'to' )
            # bsdl.g:223:22: 'to'
            pass 
            self.match("to")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TO"



    # $ANTLR start "TRANSPORT"
    def mTRANSPORT(self, ):

        try:
            _type = TRANSPORT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:224:17: ( 'transport' )
            # bsdl.g:224:22: 'transport'
            pass 
            self.match("transport")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TRANSPORT"



    # $ANTLR start "TYPE"
    def mTYPE(self, ):

        try:
            _type = TYPE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:225:17: ( 'type' )
            # bsdl.g:225:22: 'type'
            pass 
            self.match("type")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TYPE"



    # $ANTLR start "UNAFFECTED"
    def mUNAFFECTED(self, ):

        try:
            _type = UNAFFECTED
            _channel = DEFAULT_CHANNEL

            # bsdl.g:226:17: ( 'unaffected' )
            # bsdl.g:226:22: 'unaffected'
            pass 
            self.match("unaffected")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNAFFECTED"



    # $ANTLR start "UNITS"
    def mUNITS(self, ):

        try:
            _type = UNITS
            _channel = DEFAULT_CHANNEL

            # bsdl.g:227:17: ( 'units' )
            # bsdl.g:227:22: 'units'
            pass 
            self.match("units")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNITS"



    # $ANTLR start "UNTIL"
    def mUNTIL(self, ):

        try:
            _type = UNTIL
            _channel = DEFAULT_CHANNEL

            # bsdl.g:228:17: ( 'until' )
            # bsdl.g:228:22: 'until'
            pass 
            self.match("until")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNTIL"



    # $ANTLR start "USE"
    def mUSE(self, ):

        try:
            _type = USE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:229:17: ( 'use' )
            # bsdl.g:229:22: 'use'
            pass 
            self.match("use")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "USE"



    # $ANTLR start "VARIABLE"
    def mVARIABLE(self, ):

        try:
            _type = VARIABLE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:230:17: ( 'variable' )
            # bsdl.g:230:22: 'variable'
            pass 
            self.match("variable")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VARIABLE"



    # $ANTLR start "WAIT"
    def mWAIT(self, ):

        try:
            _type = WAIT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:231:17: ( 'wait' )
            # bsdl.g:231:22: 'wait'
            pass 
            self.match("wait")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WAIT"



    # $ANTLR start "WHEN"
    def mWHEN(self, ):

        try:
            _type = WHEN
            _channel = DEFAULT_CHANNEL

            # bsdl.g:232:17: ( 'when' )
            # bsdl.g:232:22: 'when'
            pass 
            self.match("when")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHEN"



    # $ANTLR start "WHILE"
    def mWHILE(self, ):

        try:
            _type = WHILE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:233:17: ( 'while' )
            # bsdl.g:233:22: 'while'
            pass 
            self.match("while")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHILE"



    # $ANTLR start "WITH"
    def mWITH(self, ):

        try:
            _type = WITH
            _channel = DEFAULT_CHANNEL

            # bsdl.g:234:17: ( 'with' )
            # bsdl.g:234:22: 'with'
            pass 
            self.match("with")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WITH"



    # $ANTLR start "XNOR"
    def mXNOR(self, ):

        try:
            _type = XNOR
            _channel = DEFAULT_CHANNEL

            # bsdl.g:235:17: ( 'xnor' )
            # bsdl.g:235:22: 'xnor'
            pass 
            self.match("xnor")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "XNOR"



    # $ANTLR start "XOR"
    def mXOR(self, ):

        try:
            _type = XOR
            _channel = DEFAULT_CHANNEL

            # bsdl.g:236:17: ( 'xor' )
            # bsdl.g:236:22: 'xor'
            pass 
            self.match("xor")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "XOR"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):

        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:238:17: ( 'true' )
            # bsdl.g:238:22: 'true'
            pass 
            self.match("true")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):

        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # bsdl.g:239:17: ( 'false' )
            # bsdl.g:239:22: 'false'
            pass 
            self.match("false")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "BOTH"
    def mBOTH(self, ):

        try:
            _type = BOTH
            _channel = DEFAULT_CHANNEL

            # bsdl.g:240:17: ( 'BOTH' | 'both' )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 66) :
                alt4 = 1
            elif (LA4_0 == 98) :
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae

            if alt4 == 1:
                # bsdl.g:240:22: 'BOTH'
                pass 
                self.match("BOTH")


            elif alt4 == 2:
                # bsdl.g:240:29: 'both'
                pass 
                self.match("both")


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BOTH"



    # $ANTLR start "WORD"
    def mWORD(self, ):

        try:
            _type = WORD
            _channel = DEFAULT_CHANNEL

            # bsdl.g:248:17: ( ( CHAR )+ )
            # bsdl.g:248:19: ( CHAR )+
            pass 
            # bsdl.g:248:19: ( CHAR )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((97 <= LA5_0 <= 122)) :
                    alt5 = 1


                if alt5 == 1:
                    # bsdl.g:248:19: CHAR
                    pass 
                    self.mCHAR()


                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WORD"



    # $ANTLR start "FULLCASE_WORD"
    def mFULLCASE_WORD(self, ):

        try:
            _type = FULLCASE_WORD
            _channel = DEFAULT_CHANNEL

            # bsdl.g:249:17: ( ( ICHAR )+ )
            # bsdl.g:249:19: ( ICHAR )+
            pass 
            # bsdl.g:249:19: ( ICHAR )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((65 <= LA6_0 <= 90) or (97 <= LA6_0 <= 122)) :
                    alt6 = 1


                if alt6 == 1:
                    # bsdl.g:249:19: ICHAR
                    pass 
                    self.mICHAR()


                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FULLCASE_WORD"



    # $ANTLR start "CHAR"
    def mCHAR(self, ):

        try:
            # bsdl.g:250:17: ( 'a' .. 'z' )
            # bsdl.g:250:19: 'a' .. 'z'
            pass 
            self.matchRange(97, 122)




        finally:

            pass

    # $ANTLR end "CHAR"



    # $ANTLR start "ICHAR"
    def mICHAR(self, ):

        try:
            # bsdl.g:251:17: ( ( CHAR | 'A' .. 'Z' ) )
            # bsdl.g:251:19: ( CHAR | 'A' .. 'Z' )
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ICHAR"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            _type = DIGIT
            _channel = DEFAULT_CHANNEL

            # bsdl.g:252:17: ( '0' .. '9' )
            # bsdl.g:252:19: '0' .. '9'
            pass 
            self.matchRange(48, 57)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIGIT"



    def mTokens(self):
        # bsdl.g:1:8: ( T__123 | STRING | WHITESPACE | COMMENT | ANDSIGN | USCORE | OPAREN | CPAREN | COLON | SCOLON | EQUAL | COMMA | DOT | BIT | BIT_VECTOR | ABS | ACCESS | AFTER | ALIAS | ALL | AND | ARCHITECTURE | ARRAY | ASSERT | ATTRIBUTE | BEGIN | BLOCK | BODY | BUFFER | BUS | CASE | COMPONENT | CONFIGURATION | CONSTANT | DISCONNECT | DOWNTO | ELSE | ELSIF | END | ENTITY | EXIT | FILE | FOR | FUNCTION | GENERATE | GENERIC | GROUP | GUARDED | IF | IMPURE | IN | INERTIAL | INOUT | IS | LABEL | LIBRARY | LINKAGE | LITERAL | LOOP | MAP | MOD | NAND | NEW | NEXT | NOR | NOT | NULL | OF | ON | OPEN | OR | OTHERS | OUT | PACKAGE | PORT | POSTPONED | PROCEDURE | PROCESS | PURE | RANGE | RECORD | REGISTER | REJECT | REM | REPORT | RETURN | ROL | ROR | SELECT | SEVERITY | SIGNAL | SHARED | SLA | SLL | SRA | SRL | SUBTYPE | THEN | TO | TRANSPORT | TYPE | UNAFFECTED | UNITS | UNTIL | USE | VARIABLE | WAIT | WHEN | WHILE | WITH | XNOR | XOR | TRUE | FALSE | BOTH | WORD | FULLCASE_WORD | DIGIT )
        alt7 = 118
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # bsdl.g:1:10: T__123
            pass 
            self.mT__123()


        elif alt7 == 2:
            # bsdl.g:1:17: STRING
            pass 
            self.mSTRING()


        elif alt7 == 3:
            # bsdl.g:1:24: WHITESPACE
            pass 
            self.mWHITESPACE()


        elif alt7 == 4:
            # bsdl.g:1:35: COMMENT
            pass 
            self.mCOMMENT()


        elif alt7 == 5:
            # bsdl.g:1:43: ANDSIGN
            pass 
            self.mANDSIGN()


        elif alt7 == 6:
            # bsdl.g:1:51: USCORE
            pass 
            self.mUSCORE()


        elif alt7 == 7:
            # bsdl.g:1:58: OPAREN
            pass 
            self.mOPAREN()


        elif alt7 == 8:
            # bsdl.g:1:65: CPAREN
            pass 
            self.mCPAREN()


        elif alt7 == 9:
            # bsdl.g:1:72: COLON
            pass 
            self.mCOLON()


        elif alt7 == 10:
            # bsdl.g:1:78: SCOLON
            pass 
            self.mSCOLON()


        elif alt7 == 11:
            # bsdl.g:1:85: EQUAL
            pass 
            self.mEQUAL()


        elif alt7 == 12:
            # bsdl.g:1:91: COMMA
            pass 
            self.mCOMMA()


        elif alt7 == 13:
            # bsdl.g:1:97: DOT
            pass 
            self.mDOT()


        elif alt7 == 14:
            # bsdl.g:1:101: BIT
            pass 
            self.mBIT()


        elif alt7 == 15:
            # bsdl.g:1:105: BIT_VECTOR
            pass 
            self.mBIT_VECTOR()


        elif alt7 == 16:
            # bsdl.g:1:116: ABS
            pass 
            self.mABS()


        elif alt7 == 17:
            # bsdl.g:1:120: ACCESS
            pass 
            self.mACCESS()


        elif alt7 == 18:
            # bsdl.g:1:127: AFTER
            pass 
            self.mAFTER()


        elif alt7 == 19:
            # bsdl.g:1:133: ALIAS
            pass 
            self.mALIAS()


        elif alt7 == 20:
            # bsdl.g:1:139: ALL
            pass 
            self.mALL()


        elif alt7 == 21:
            # bsdl.g:1:143: AND
            pass 
            self.mAND()


        elif alt7 == 22:
            # bsdl.g:1:147: ARCHITECTURE
            pass 
            self.mARCHITECTURE()


        elif alt7 == 23:
            # bsdl.g:1:160: ARRAY
            pass 
            self.mARRAY()


        elif alt7 == 24:
            # bsdl.g:1:166: ASSERT
            pass 
            self.mASSERT()


        elif alt7 == 25:
            # bsdl.g:1:173: ATTRIBUTE
            pass 
            self.mATTRIBUTE()


        elif alt7 == 26:
            # bsdl.g:1:183: BEGIN
            pass 
            self.mBEGIN()


        elif alt7 == 27:
            # bsdl.g:1:189: BLOCK
            pass 
            self.mBLOCK()


        elif alt7 == 28:
            # bsdl.g:1:195: BODY
            pass 
            self.mBODY()


        elif alt7 == 29:
            # bsdl.g:1:200: BUFFER
            pass 
            self.mBUFFER()


        elif alt7 == 30:
            # bsdl.g:1:207: BUS
            pass 
            self.mBUS()


        elif alt7 == 31:
            # bsdl.g:1:211: CASE
            pass 
            self.mCASE()


        elif alt7 == 32:
            # bsdl.g:1:216: COMPONENT
            pass 
            self.mCOMPONENT()


        elif alt7 == 33:
            # bsdl.g:1:226: CONFIGURATION
            pass 
            self.mCONFIGURATION()


        elif alt7 == 34:
            # bsdl.g:1:240: CONSTANT
            pass 
            self.mCONSTANT()


        elif alt7 == 35:
            # bsdl.g:1:249: DISCONNECT
            pass 
            self.mDISCONNECT()


        elif alt7 == 36:
            # bsdl.g:1:260: DOWNTO
            pass 
            self.mDOWNTO()


        elif alt7 == 37:
            # bsdl.g:1:267: ELSE
            pass 
            self.mELSE()


        elif alt7 == 38:
            # bsdl.g:1:272: ELSIF
            pass 
            self.mELSIF()


        elif alt7 == 39:
            # bsdl.g:1:278: END
            pass 
            self.mEND()


        elif alt7 == 40:
            # bsdl.g:1:282: ENTITY
            pass 
            self.mENTITY()


        elif alt7 == 41:
            # bsdl.g:1:289: EXIT
            pass 
            self.mEXIT()


        elif alt7 == 42:
            # bsdl.g:1:294: FILE
            pass 
            self.mFILE()


        elif alt7 == 43:
            # bsdl.g:1:299: FOR
            pass 
            self.mFOR()


        elif alt7 == 44:
            # bsdl.g:1:303: FUNCTION
            pass 
            self.mFUNCTION()


        elif alt7 == 45:
            # bsdl.g:1:312: GENERATE
            pass 
            self.mGENERATE()


        elif alt7 == 46:
            # bsdl.g:1:321: GENERIC
            pass 
            self.mGENERIC()


        elif alt7 == 47:
            # bsdl.g:1:329: GROUP
            pass 
            self.mGROUP()


        elif alt7 == 48:
            # bsdl.g:1:335: GUARDED
            pass 
            self.mGUARDED()


        elif alt7 == 49:
            # bsdl.g:1:343: IF
            pass 
            self.mIF()


        elif alt7 == 50:
            # bsdl.g:1:346: IMPURE
            pass 
            self.mIMPURE()


        elif alt7 == 51:
            # bsdl.g:1:353: IN
            pass 
            self.mIN()


        elif alt7 == 52:
            # bsdl.g:1:356: INERTIAL
            pass 
            self.mINERTIAL()


        elif alt7 == 53:
            # bsdl.g:1:365: INOUT
            pass 
            self.mINOUT()


        elif alt7 == 54:
            # bsdl.g:1:371: IS
            pass 
            self.mIS()


        elif alt7 == 55:
            # bsdl.g:1:374: LABEL
            pass 
            self.mLABEL()


        elif alt7 == 56:
            # bsdl.g:1:380: LIBRARY
            pass 
            self.mLIBRARY()


        elif alt7 == 57:
            # bsdl.g:1:388: LINKAGE
            pass 
            self.mLINKAGE()


        elif alt7 == 58:
            # bsdl.g:1:396: LITERAL
            pass 
            self.mLITERAL()


        elif alt7 == 59:
            # bsdl.g:1:404: LOOP
            pass 
            self.mLOOP()


        elif alt7 == 60:
            # bsdl.g:1:409: MAP
            pass 
            self.mMAP()


        elif alt7 == 61:
            # bsdl.g:1:413: MOD
            pass 
            self.mMOD()


        elif alt7 == 62:
            # bsdl.g:1:417: NAND
            pass 
            self.mNAND()


        elif alt7 == 63:
            # bsdl.g:1:422: NEW
            pass 
            self.mNEW()


        elif alt7 == 64:
            # bsdl.g:1:426: NEXT
            pass 
            self.mNEXT()


        elif alt7 == 65:
            # bsdl.g:1:431: NOR
            pass 
            self.mNOR()


        elif alt7 == 66:
            # bsdl.g:1:435: NOT
            pass 
            self.mNOT()


        elif alt7 == 67:
            # bsdl.g:1:439: NULL
            pass 
            self.mNULL()


        elif alt7 == 68:
            # bsdl.g:1:444: OF
            pass 
            self.mOF()


        elif alt7 == 69:
            # bsdl.g:1:447: ON
            pass 
            self.mON()


        elif alt7 == 70:
            # bsdl.g:1:450: OPEN
            pass 
            self.mOPEN()


        elif alt7 == 71:
            # bsdl.g:1:455: OR
            pass 
            self.mOR()


        elif alt7 == 72:
            # bsdl.g:1:458: OTHERS
            pass 
            self.mOTHERS()


        elif alt7 == 73:
            # bsdl.g:1:465: OUT
            pass 
            self.mOUT()


        elif alt7 == 74:
            # bsdl.g:1:469: PACKAGE
            pass 
            self.mPACKAGE()


        elif alt7 == 75:
            # bsdl.g:1:477: PORT
            pass 
            self.mPORT()


        elif alt7 == 76:
            # bsdl.g:1:482: POSTPONED
            pass 
            self.mPOSTPONED()


        elif alt7 == 77:
            # bsdl.g:1:492: PROCEDURE
            pass 
            self.mPROCEDURE()


        elif alt7 == 78:
            # bsdl.g:1:502: PROCESS
            pass 
            self.mPROCESS()


        elif alt7 == 79:
            # bsdl.g:1:510: PURE
            pass 
            self.mPURE()


        elif alt7 == 80:
            # bsdl.g:1:515: RANGE
            pass 
            self.mRANGE()


        elif alt7 == 81:
            # bsdl.g:1:521: RECORD
            pass 
            self.mRECORD()


        elif alt7 == 82:
            # bsdl.g:1:528: REGISTER
            pass 
            self.mREGISTER()


        elif alt7 == 83:
            # bsdl.g:1:537: REJECT
            pass 
            self.mREJECT()


        elif alt7 == 84:
            # bsdl.g:1:544: REM
            pass 
            self.mREM()


        elif alt7 == 85:
            # bsdl.g:1:548: REPORT
            pass 
            self.mREPORT()


        elif alt7 == 86:
            # bsdl.g:1:555: RETURN
            pass 
            self.mRETURN()


        elif alt7 == 87:
            # bsdl.g:1:562: ROL
            pass 
            self.mROL()


        elif alt7 == 88:
            # bsdl.g:1:566: ROR
            pass 
            self.mROR()


        elif alt7 == 89:
            # bsdl.g:1:570: SELECT
            pass 
            self.mSELECT()


        elif alt7 == 90:
            # bsdl.g:1:577: SEVERITY
            pass 
            self.mSEVERITY()


        elif alt7 == 91:
            # bsdl.g:1:586: SIGNAL
            pass 
            self.mSIGNAL()


        elif alt7 == 92:
            # bsdl.g:1:593: SHARED
            pass 
            self.mSHARED()


        elif alt7 == 93:
            # bsdl.g:1:600: SLA
            pass 
            self.mSLA()


        elif alt7 == 94:
            # bsdl.g:1:604: SLL
            pass 
            self.mSLL()


        elif alt7 == 95:
            # bsdl.g:1:608: SRA
            pass 
            self.mSRA()


        elif alt7 == 96:
            # bsdl.g:1:612: SRL
            pass 
            self.mSRL()


        elif alt7 == 97:
            # bsdl.g:1:616: SUBTYPE
            pass 
            self.mSUBTYPE()


        elif alt7 == 98:
            # bsdl.g:1:624: THEN
            pass 
            self.mTHEN()


        elif alt7 == 99:
            # bsdl.g:1:629: TO
            pass 
            self.mTO()


        elif alt7 == 100:
            # bsdl.g:1:632: TRANSPORT
            pass 
            self.mTRANSPORT()


        elif alt7 == 101:
            # bsdl.g:1:642: TYPE
            pass 
            self.mTYPE()


        elif alt7 == 102:
            # bsdl.g:1:647: UNAFFECTED
            pass 
            self.mUNAFFECTED()


        elif alt7 == 103:
            # bsdl.g:1:658: UNITS
            pass 
            self.mUNITS()


        elif alt7 == 104:
            # bsdl.g:1:664: UNTIL
            pass 
            self.mUNTIL()


        elif alt7 == 105:
            # bsdl.g:1:670: USE
            pass 
            self.mUSE()


        elif alt7 == 106:
            # bsdl.g:1:674: VARIABLE
            pass 
            self.mVARIABLE()


        elif alt7 == 107:
            # bsdl.g:1:683: WAIT
            pass 
            self.mWAIT()


        elif alt7 == 108:
            # bsdl.g:1:688: WHEN
            pass 
            self.mWHEN()


        elif alt7 == 109:
            # bsdl.g:1:693: WHILE
            pass 
            self.mWHILE()


        elif alt7 == 110:
            # bsdl.g:1:699: WITH
            pass 
            self.mWITH()


        elif alt7 == 111:
            # bsdl.g:1:704: XNOR
            pass 
            self.mXNOR()


        elif alt7 == 112:
            # bsdl.g:1:709: XOR
            pass 
            self.mXOR()


        elif alt7 == 113:
            # bsdl.g:1:713: TRUE
            pass 
            self.mTRUE()


        elif alt7 == 114:
            # bsdl.g:1:718: FALSE
            pass 
            self.mFALSE()


        elif alt7 == 115:
            # bsdl.g:1:724: BOTH
            pass 
            self.mBOTH()


        elif alt7 == 116:
            # bsdl.g:1:729: WORD
            pass 
            self.mWORD()


        elif alt7 == 117:
            # bsdl.g:1:734: FULLCASE_WORD
            pass 
            self.mFULLCASE_WORD()


        elif alt7 == 118:
            # bsdl.g:1:748: DIGIT
            pass 
            self.mDIGIT()







    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\1\uffff\1\50\14\uffff\23\56\1\43\1\56\2\uffff\3\56\1\uffff\5\56"
        u"\1\uffff\23\56\1\u0090\1\56\1\u0094\1\u0095\11\56\1\u00a3\1\u00a4"
        u"\1\56\1\u00a6\20\56\1\u00c1\12\56\1\43\1\56\1\u00d3\2\56\1\u00d7"
        u"\5\56\1\u00dd\1\u00de\3\56\1\u00e2\1\u00e3\12\56\1\u00ef\5\56\1"
        u"\uffff\3\56\2\uffff\5\56\1\u00fd\1\u00fe\1\56\1\u0100\1\56\1\u0102"
        u"\1\u0103\1\56\2\uffff\1\56\1\uffff\1\56\1\u0107\11\56\1\u0111\2"
        u"\56\1\u0114\1\u0115\4\56\1\u011a\1\u011b\1\u011c\1\u011d\2\56\1"
        u"\uffff\6\56\1\u0126\6\56\1\u012d\1\43\1\u012f\1\56\1\uffff\1\56"
        u"\1\u0132\2\uffff\2\56\1\u0135\1\u0136\1\56\2\uffff\3\56\2\uffff"
        u"\4\56\1\u013f\5\56\1\u0145\1\uffff\14\56\1\u0152\2\uffff\1\u0153"
        u"\1\uffff\1\u0154\2\uffff\1\u0155\1\u0156\1\56\1\uffff\1\56\1\u0159"
        u"\2\56\1\u015c\4\56\1\uffff\2\56\2\uffff\4\56\4\uffff\1\56\1\u0168"
        u"\1\56\1\u016a\1\u016b\3\56\1\uffff\1\56\1\u0170\1\u0171\1\56\1"
        u"\u0173\1\u0174\1\uffff\1\u0136\1\uffff\1\u0175\1\56\1\uffff\1\u0177"
        u"\1\u0178\2\uffff\2\56\1\u017b\1\u017c\1\56\1\u017e\2\56\1\uffff"
        u"\5\56\1\uffff\1\56\1\u0187\1\56\1\u018a\3\56\1\u018e\1\u018f\3"
        u"\56\5\uffff\2\56\1\uffff\2\56\1\uffff\1\u0198\12\56\1\uffff\1\56"
        u"\2\uffff\1\56\1\u01a5\1\u01a6\1\56\2\uffff\1\u01a8\3\uffff\1\u01a9"
        u"\2\uffff\1\u01aa\1\u01ab\2\uffff\1\56\1\uffff\1\u01ad\5\56\1\u01b3"
        u"\1\56\1\uffff\2\56\1\uffff\1\56\1\u01b8\1\56\2\uffff\3\56\1\u01bd"
        u"\4\56\1\uffff\1\u01c2\1\56\1\u01c4\1\u01c5\1\u01c6\1\u01c7\1\56"
        u"\1\u01c9\1\u01ca\3\56\2\uffff\1\56\4\uffff\1\56\1\uffff\5\56\1"
        u"\uffff\2\56\1\u01d7\1\u01d8\1\uffff\1\56\1\u01da\1\u01db\1\u01dc"
        u"\1\uffff\1\u01dd\2\56\1\u01e0\1\uffff\1\56\4\uffff\1\56\2\uffff"
        u"\1\u01e3\7\56\1\u01eb\1\56\1\u01ed\1\u01ee\2\uffff\1\u01ef\4\uffff"
        u"\2\56\1\uffff\1\u01f2\1\u01f3\1\uffff\2\56\1\u01f6\1\56\1\u01f8"
        u"\1\u01f9\1\56\1\uffff\1\56\3\uffff\1\u01fc\1\u01fd\2\uffff\1\u01fe"
        u"\1\56\1\uffff\1\56\2\uffff\1\56\1\u0202\3\uffff\1\u0203\2\56\2"
        u"\uffff\1\u0206\1\56\1\uffff\1\u0208\1\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\u0209\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\11\1\101\14\uffff\23\101\1\117\1\101\2\uffff\3\101\1\uffff\5"
        u"\101\1\uffff\77\101\1\124\41\101\1\uffff\3\101\2\uffff\15\101\2"
        u"\uffff\1\101\1\uffff\32\101\1\uffff\16\101\1\110\2\101\1\uffff"
        u"\2\101\2\uffff\5\101\2\uffff\3\101\2\uffff\13\101\1\uffff\15\101"
        u"\2\uffff\1\101\1\uffff\1\101\2\uffff\3\101\1\uffff\11\101\1\uffff"
        u"\2\101\2\uffff\4\101\4\uffff\10\101\1\uffff\6\101\1\uffff\1\101"
        u"\1\uffff\2\101\1\uffff\2\101\2\uffff\10\101\1\uffff\5\101\1\uffff"
        u"\14\101\5\uffff\2\101\1\uffff\2\101\1\uffff\13\101\1\uffff\1\101"
        u"\2\uffff\4\101\2\uffff\1\101\3\uffff\1\101\2\uffff\2\101\2\uffff"
        u"\1\101\1\uffff\10\101\1\uffff\2\101\1\uffff\3\101\2\uffff\10\101"
        u"\1\uffff\14\101\2\uffff\1\101\4\uffff\1\101\1\uffff\5\101\1\uffff"
        u"\4\101\1\uffff\4\101\1\uffff\4\101\1\uffff\1\101\4\uffff\1\101"
        u"\2\uffff\14\101\2\uffff\1\101\4\uffff\2\101\1\uffff\2\101\1\uffff"
        u"\7\101\1\uffff\1\101\3\uffff\2\101\2\uffff\2\101\1\uffff\1\101"
        u"\2\uffff\2\101\3\uffff\3\101\2\uffff\2\101\1\uffff\1\101\1\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\2\172\14\uffff\23\172\1\117\1\172\2\uffff\3\172\1\uffff\5\172"
        u"\1\uffff\77\172\1\124\41\172\1\uffff\3\172\2\uffff\15\172\2\uffff"
        u"\1\172\1\uffff\32\172\1\uffff\16\172\1\110\2\172\1\uffff\2\172"
        u"\2\uffff\5\172\2\uffff\3\172\2\uffff\13\172\1\uffff\15\172\2\uffff"
        u"\1\172\1\uffff\1\172\2\uffff\3\172\1\uffff\11\172\1\uffff\2\172"
        u"\2\uffff\4\172\4\uffff\10\172\1\uffff\6\172\1\uffff\1\172\1\uffff"
        u"\2\172\1\uffff\2\172\2\uffff\10\172\1\uffff\5\172\1\uffff\14\172"
        u"\5\uffff\2\172\1\uffff\2\172\1\uffff\13\172\1\uffff\1\172\2\uffff"
        u"\4\172\2\uffff\1\172\3\uffff\1\172\2\uffff\2\172\2\uffff\1\172"
        u"\1\uffff\10\172\1\uffff\2\172\1\uffff\3\172\2\uffff\10\172\1\uffff"
        u"\14\172\2\uffff\1\172\4\uffff\1\172\1\uffff\5\172\1\uffff\4\172"
        u"\1\uffff\4\172\1\uffff\4\172\1\uffff\1\172\4\uffff\1\172\2\uffff"
        u"\14\172\2\uffff\1\172\4\uffff\2\172\1\uffff\2\172\1\uffff\7\172"
        u"\1\uffff\1\172\3\uffff\2\172\2\uffff\2\172\1\uffff\1\172\2\uffff"
        u"\2\172\3\uffff\3\172\2\uffff\2\172\1\uffff\1\172\1\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1\14\1\15"
        u"\25\uffff\1\165\1\166\3\uffff\1\1\5\uffff\1\164\141\uffff\1\61"
        u"\3\uffff\1\63\1\66\15\uffff\1\104\1\105\1\uffff\1\107\32\uffff"
        u"\1\143\21\uffff\1\47\2\uffff\1\17\1\16\5\uffff\1\36\1\20\3\uffff"
        u"\1\24\1\25\13\uffff\1\53\15\uffff\1\74\1\75\1\uffff\1\77\1\uffff"
        u"\1\101\1\102\3\uffff\1\111\11\uffff\1\124\2\uffff\1\127\1\130\4"
        u"\uffff\1\135\1\136\1\137\1\140\10\uffff\1\151\6\uffff\1\160\1\uffff"
        u"\1\45\2\uffff\1\51\2\uffff\1\34\1\163\10\uffff\1\37\5\uffff\1\52"
        u"\14\uffff\1\73\1\76\1\100\1\103\1\106\2\uffff\1\113\2\uffff\1\117"
        u"\13\uffff\1\142\1\uffff\1\161\1\145\4\uffff\1\153\1\154\1\uffff"
        u"\1\156\1\157\1\46\1\uffff\1\32\1\33\2\uffff\1\22\1\23\1\uffff\1"
        u"\27\10\uffff\1\162\2\uffff\1\57\3\uffff\1\65\1\67\10\uffff\1\120"
        u"\14\uffff\1\147\1\150\1\uffff\1\155\1\50\1\35\1\21\1\uffff\1\30"
        u"\5\uffff\1\44\4\uffff\1\62\4\uffff\1\110\4\uffff\1\121\1\uffff"
        u"\1\123\1\125\1\126\1\131\1\uffff\1\133\1\134\14\uffff\1\56\1\60"
        u"\1\uffff\1\70\1\71\1\72\1\112\2\uffff\1\116\2\uffff\1\141\7\uffff"
        u"\1\42\1\uffff\1\54\1\55\1\64\2\uffff\1\122\1\132\2\uffff\1\152"
        u"\1\uffff\1\31\1\40\2\uffff\1\114\1\115\1\144\3\uffff\1\43\1\146"
        u"\2\uffff\1\26\1\uffff\1\41"
        )

    DFA7_special = DFA.unpack(
        u"\u0209\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\2\3\2\uffff\1\3\22\uffff\1\3\1\uffff\1\2\3\uffff\1"
        u"\5\1\uffff\1\7\1\10\2\uffff\1\14\1\4\1\15\1\uffff\12\44\1\11\1"
        u"\12\1\uffff\1\13\3\uffff\1\43\1\41\30\43\4\uffff\1\6\1\uffff\1"
        u"\17\1\16\1\20\1\21\1\1\1\22\1\23\1\42\1\24\2\42\1\25\1\26\1\27"
        u"\1\30\1\31\1\42\1\32\1\33\1\34\1\35\1\36\1\37\1\40\2\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\45\1\42\1\46\11\42\1\47\2\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\52\3\42\1\51\2\42\1\53\2\42\1"
        u"\54\5\42\1\55\5\42"),
        DFA.unpack(u"\32\43\6\uffff\1\42\1\57\1\60\2\42\1\61\5\42\1\62\1"
        u"\42\1\63\3\42\1\64\1\65\1\66\6\42"),
        DFA.unpack(u"\32\43\6\uffff\1\67\15\42\1\70\13\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\71\5\42\1\72\13\42"),
        DFA.unpack(u"\32\43\6\uffff\1\76\7\42\1\73\5\42\1\74\5\42\1\75\5"
        u"\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\77\14\42\1\100\2\42\1\101\5\42"),
        DFA.unpack(u"\32\43\6\uffff\5\42\1\102\6\42\1\103\1\104\4\42\1\105"
        u"\7\42"),
        DFA.unpack(u"\32\43\6\uffff\1\106\7\42\1\107\5\42\1\110\13\42"),
        DFA.unpack(u"\32\43\6\uffff\1\111\15\42\1\112\13\42"),
        DFA.unpack(u"\32\43\6\uffff\1\113\3\42\1\114\11\42\1\115\5\42\1"
        u"\116\5\42"),
        DFA.unpack(u"\32\43\6\uffff\5\42\1\117\7\42\1\120\1\42\1\121\1\42"
        u"\1\122\1\42\1\123\1\124\5\42"),
        DFA.unpack(u"\32\43\6\uffff\1\125\15\42\1\126\2\42\1\127\2\42\1"
        u"\130\5\42"),
        DFA.unpack(u"\32\43\6\uffff\1\131\3\42\1\132\11\42\1\133\13\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\134\2\42\1\136\1\135\2\42\1\137"
        u"\5\42\1\140\2\42\1\141\5\42"),
        DFA.unpack(u"\32\43\6\uffff\7\42\1\142\6\42\1\143\2\42\1\144\6\42"
        u"\1\145\1\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\146\4\42\1\147\7\42"),
        DFA.unpack(u"\32\43\6\uffff\1\150\31\42"),
        DFA.unpack(u"\32\43\6\uffff\1\151\6\42\1\152\1\153\21\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\154\1\155\13\42"),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\157\7\42"),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\160\17\42\1\161\6\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\162\21\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\163\6\42"),
        DFA.unpack(u"\32\43\6\uffff\6\42\1\164\23\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\165\13\42"),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\166\17\42\1\167\6\42"),
        DFA.unpack(u"\32\43\6\uffff\5\42\1\170\14\42\1\171\7\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\172\7\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\173\27\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\174\6\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\175\2\42\1\176\16\42"),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\177\26\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u0080\16\42\1\u0081\10\42"),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u0082\7\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u0083\6\42"),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u0084\7\42"),
        DFA.unpack(u"\32\43\6\uffff\14\42\1\u0085\1\u0086\14\42"),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u0087\7\42"),
        DFA.unpack(u"\32\43\6\uffff\26\42\1\u0088\3\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u0089\16\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u008a\10\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u008b\14\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u008c\16\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u008d\14\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u008e\13\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u008f\31\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\17\42\1\u0091\12\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0092\11\42\1\u0093\13\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\1\42\1\u0096\30\42"),
        DFA.unpack(u"\32\43\6\uffff\1\42\1\u0097\13\42\1\u0098\5\42\1\u0099"
        u"\6\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u009a\13\42"),
        DFA.unpack(u"\32\43\6\uffff\17\42\1\u009b\12\42"),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\u009c\26\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u009d\14\42"),
        DFA.unpack(u"\32\43\6\uffff\26\42\1\u009e\1\u009f\2\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u00a0\1\42\1\u00a1\6\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u00a2\16\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00a5\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\7\42\1\u00a7\22\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u00a8\6\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u00a9\27\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u00aa\1\u00ab\7\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u00ac\13\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u00ad\10\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u00ae\14\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u00af\3\42\1\u00b0\2\42\1\u00b1"
        u"\2\42\1\u00b2\2\42\1\u00b3\3\42\1\u00b4\6\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u00b5\5\42\1\u00b6\10\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u00b7\11\42\1\u00b8\4\42"),
        DFA.unpack(u"\32\43\6\uffff\6\42\1\u00b9\23\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u00ba\31\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u00bb\12\42\1\u00bc\16\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u00bd\12\42\1\u00be\16\42"),
        DFA.unpack(u"\32\43\6\uffff\1\42\1\u00bf\30\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00c0\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u00c2\23\42\1\u00c3\5\42"),
        DFA.unpack(u"\32\43\6\uffff\17\42\1\u00c4\12\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u00c5\7\42\1\u00c6\12\42\1\u00c7\6"
        u"\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00c8\25\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u00c9\10\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u00ca\21\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00cb\3\42\1\u00cc\21\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u00cd\6\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u00ce\13\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u00cf\10\42"),
        DFA.unpack(u"\1\u00d0"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00d1\3\42\1\u00d2\21\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u00d4\21\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u00d5\6\42"),
        DFA.unpack(u"\32\43\4\uffff\1\u00d6\1\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u00d8\21\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u00d9\27\42"),
        DFA.unpack(u"\32\43\6\uffff\30\42\1\u00da\1\42"),
        DFA.unpack(u"\32\43\6\uffff\7\42\1\u00db\22\42"),
        DFA.unpack(u"\32\43\6\uffff\5\42\1\u00dc\24\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00df\25\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00e0\25\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u00e1\31\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\7\42\1\u00e4\22\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u00e5\31\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00e6\25\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u00e7\10\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00e8\25\42"),
        DFA.unpack(u"\32\43\6\uffff\17\42\1\u00e9\12\42"),
        DFA.unpack(u"\32\43\6\uffff\5\42\1\u00ea\14\42\1\u00eb\7\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u00ec\27\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u00ed\14\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00ee\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u00f0\27\42"),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u00f1\7\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00f2\25\42"),
        DFA.unpack(u"\32\43\6\uffff\24\42\1\u00f3\5\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u00f4\10\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\24\42\1\u00f5\5\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u00f6\10\42"),
        DFA.unpack(u"\32\43\6\uffff\24\42\1\u00f7\5\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00f8\25\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u00f9\10\42"),
        DFA.unpack(u"\32\43\6\uffff\12\42\1\u00fa\17\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u00fb\25\42"),
        DFA.unpack(u"\32\43\6\uffff\17\42\1\u00fc\12\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\u00ff\26\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u0101\6\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u0104\16\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u0105\14\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0106\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\12\42\1\u0108\17\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u0109\6\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u010a\6\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u010b\27\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u010c\25\42"),
        DFA.unpack(u"\32\43\6\uffff\6\42\1\u010d\23\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u010e\13\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u010f\21\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0110\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u0112\13\42"),
        DFA.unpack(u"\32\43\6\uffff\24\42\1\u0113\5\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0116\25\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0117\25\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u0118\14\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0119\10\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u011e\6\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u011f\14\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u0120\14\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0121\25\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0122\25\42"),
        DFA.unpack(u"\32\43\6\uffff\5\42\1\u0123\24\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u0124\6\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u0125\21\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u0127\21\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u0128\6\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u0129\14\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u012a\16\42"),
        DFA.unpack(u"\32\43\6\uffff\7\42\1\u012b\22\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u012c\10\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\1\u012e"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\5\42\1\u0130\24\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u0131\6\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u0133\14\42"),
        DFA.unpack(u"\32\43\6\uffff\12\42\1\u0134\17\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0137\25\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u0138\7\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0139\10\42"),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u013a\7\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u013b\21\42"),
        DFA.unpack(u"\32\43\6\uffff\30\42\1\u013c\1\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u013d\10\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u013e\21\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u0140\13\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u0141\21\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u0142\6\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u0143\13\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u0144\6\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u0146\6\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0147\25\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0148\10\42"),
        DFA.unpack(u"\32\43\6\uffff\17\42\1\u0149\12\42"),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\u014a\26\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u014b\10\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u014c\6\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u014d\6\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u014e\16\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u014f\31\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u0150\31\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0151\10\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0157\10\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\1\u0158\31\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\17\42\1\u015a\12\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u015b\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u015d\25\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u015e\10\42"),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u015f\7\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u0160\27\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0161\10\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0162\10\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u0163\27\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0164\10\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u0165\31\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0166\25\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\30\42\1\u0167\1\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u0169\7\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\5\42\1\u016c\24\42"),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u016d\7\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u016e\16\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\1\u016f\31\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0172\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\43"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\30\42\1\u0176\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0179\10\42"),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u017a\7\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u017d\6\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u017f\6\42"),
        DFA.unpack(u"\32\43\6\uffff\1\42\1\u0180\30\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u0181\14\42"),
        DFA.unpack(u"\32\43\6\uffff\6\42\1\u0182\23\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u0183\31\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u0184\14\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u0185\13\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u0186\21\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u0188\7\42\1\u0189\21\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u018b\25\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u018c\25\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u018d\21\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0190\10\42"),
        DFA.unpack(u"\32\43\6\uffff\6\42\1\u0191\23\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u0192\31\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u0193\7\42"),
        DFA.unpack(u"\32\43\6\uffff\6\42\1\u0194\23\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u0195\13\42"),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\u0196\16\42\1\u0197\7\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\u0199\26\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u019a\6\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u019b\6\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u019c\6\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u019d\14\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u019e\6\42"),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u019f\21\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u01a0\16\42"),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\u01a1\26\42"),
        DFA.unpack(u"\32\43\6\uffff\17\42\1\u01a2\12\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\17\42\1\u01a3\12\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01a4\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\1\42\1\u01a7\30\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01ac\25\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\24\42\1\u01ae\5\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01af\25\42"),
        DFA.unpack(u"\32\43\6\uffff\24\42\1\u01b0\5\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u01b1\14\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u01b2\14\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u01b4\13\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u01b5\6\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u01b6\27\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\u01b7\26\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u01b9\31\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\30\42\1\u01ba\1\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01bb\25\42"),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u01bc\16\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01be\25\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u01bf\14\42"),
        DFA.unpack(u"\32\43\6\uffff\24\42\1\u01c0\5\42"),
        DFA.unpack(u"\32\43\6\uffff\22\42\1\u01c1\7\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01c3\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u01c8\6\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01cb\25\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u01cc\13\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u01cd\27\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u01ce\16\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u01cf\27\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u01d0\6\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u01d1\14\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u01d2\10\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u01d3\6\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01d4\25\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u01d5\14\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01d6\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\13\42\1\u01d9\16\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01de\25\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u01df\10\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u01e1\10\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\30\42\1\u01e2\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u01e4\10\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u01e5\6\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01e6\25\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u01e7\6\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01e8\25\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u01e9\6\42"),
        DFA.unpack(u"\32\43\6\uffff\1\u01ea\31\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\2\42\1\u01ec\27\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\u01f0\26\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01f1\25\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u01f4\6\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u01f5\25\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\24\42\1\u01f7\5\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u01fa\6\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\23\42\1\u01fb\6\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\3\42\1\u01ff\26\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\21\42\1\u0200\10\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\10\42\1\u0201\21\42"),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\4\42\1\u0204\25\42"),
        DFA.unpack(u"\32\43\6\uffff\16\42\1\u0205\13\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"\32\43\6\uffff\15\42\1\u0207\14\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\43\6\uffff\32\42"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    DFA7 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(bsdlLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
