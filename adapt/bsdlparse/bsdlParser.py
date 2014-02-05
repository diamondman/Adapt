# $ANTLR 3.1 bsdl.g 2014-02-05 02:26:56

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
import os
import sys



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=64
PACKAGE=87
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
BEGIN=51
LOOP=74
RETURN=98
BOTH=23
TRANSPORT=110
IMPURE=69
ICHAR=39
BODY=53
GENERATE=65
LINKAGE=35
COMMENT=41
SELECT=101
REGISTER=94
ARRAY=49
SHARED=103
EXIT=61
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
CPAREN=12
NEXT=79
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
RANGE=92
BUFFER=34
PORT=25
LITERAL=73
REM=96
AFTER=45
TRUE=20
PROCEDURE=89
COLON=10
OPEN=84
LABEL=71
WHEN=117
BLOCK=52
MAP=75
BIT=26
PROCESS=90
UNAFFECTED=112
STRING=37

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ENTITY", "IS", "SCOLON", "END", "GENERIC", "OPAREN", "COLON", "EQUAL", 
    "CPAREN", "USE", "DOT", "ALL", "ATTRIBUTE", "OF", "DIGIT", "SIGNAL", 
    "TRUE", "FALSE", "COMMA", "BOTH", "CONSTANT", "PORT", "BIT", "BIT_VECTOR", 
    "TO", "FULLCASE_WORD", "WORD", "IN", "OUT", "INOUT", "BUFFER", "LINKAGE", 
    "BUS", "STRING", "ANDSIGN", "ICHAR", "WHITESPACE", "COMMENT", "USCORE", 
    "ABS", "ACCESS", "AFTER", "ALIAS", "AND", "ARCHITECTURE", "ARRAY", "ASSERT", 
    "BEGIN", "BLOCK", "BODY", "CASE", "COMPONENT", "CONFIGURATION", "DISCONNECT", 
    "DOWNTO", "ELSE", "ELSIF", "EXIT", "FILE", "FOR", "FUNCTION", "GENERATE", 
    "GROUP", "GUARDED", "IF", "IMPURE", "INERTIAL", "LABEL", "LIBRARY", 
    "LITERAL", "LOOP", "MAP", "MOD", "NAND", "NEW", "NEXT", "NOR", "NOT", 
    "NULL", "ON", "OPEN", "OR", "OTHERS", "PACKAGE", "POSTPONED", "PROCEDURE", 
    "PROCESS", "PURE", "RANGE", "RECORD", "REGISTER", "REJECT", "REM", "REPORT", 
    "RETURN", "ROL", "ROR", "SELECT", "SEVERITY", "SHARED", "SLA", "SLL", 
    "SRA", "SRL", "SUBTYPE", "THEN", "TRANSPORT", "TYPE", "UNAFFECTED", 
    "UNITS", "UNTIL", "VARIABLE", "WAIT", "WHEN", "WHILE", "WITH", "XNOR", 
    "XOR", "CHAR", "'e'"
]




class bsdlParser(Parser):
    grammarFileName = "bsdl.g"
    antlr_version = version_str_to_tuple("3.1")
    antlr_version_str = "3.1"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)


        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )



              
        self.entity_name = ""
        self.attributes = {}
        self.chip_package = None




                


        

             




    # $ANTLR start "eval"
    # bsdl.g:24:1: eval returns [value] : ( entity ) EOF ;
    def eval(self, ):

        value = None

        try:
            try:
                # bsdl.g:25:5: ( ( entity ) EOF )
                # bsdl.g:25:7: ( entity ) EOF
                pass 
                #action start
                value=[]
                #action end
                # bsdl.g:26:9: ( entity )
                # bsdl.g:26:10: entity
                pass 
                self._state.following.append(self.FOLLOW_entity_in_eval71)
                self.entity()

                self._state.following.pop()



                self.match(self.input, EOF, self.FOLLOW_EOF_in_eval82)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "eval"


    # $ANTLR start "entity"
    # bsdl.g:29:1: entity returns [value] : ENTITY ename= identifier IS ( generic SCOLON )+ port_list SCOLON ( use SCOLON )* ( ( attribute | constant ) SCOLON )* END identifier SCOLON ;
    def entity(self, ):

        value = None

        ename = None

        port_list1 = None


        try:
            try:
                # bsdl.g:30:5: ( ENTITY ename= identifier IS ( generic SCOLON )+ port_list SCOLON ( use SCOLON )* ( ( attribute | constant ) SCOLON )* END identifier SCOLON )
                # bsdl.g:30:7: ENTITY ename= identifier IS ( generic SCOLON )+ port_list SCOLON ( use SCOLON )* ( ( attribute | constant ) SCOLON )* END identifier SCOLON
                pass 
                self.match(self.input, ENTITY, self.FOLLOW_ENTITY_in_entity98)
                self._state.following.append(self.FOLLOW_identifier_in_entity102)
                ename = self.identifier()

                self._state.following.pop()
                self.match(self.input, IS, self.FOLLOW_IS_in_entity104)
                #action start
                self.entity_name = ((ename is not None) and [ename.value] or [None])[0]
                #action end
                # bsdl.g:33:5: ( generic SCOLON )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == GENERIC) :
                        alt1 = 1


                    if alt1 == 1:
                        # bsdl.g:33:6: generic SCOLON
                        pass 
                        self._state.following.append(self.FOLLOW_generic_in_entity123)
                        self.generic()

                        self._state.following.pop()
                        self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_entity125)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                self._state.following.append(self.FOLLOW_port_list_in_entity134)
                port_list1 = self.port_list()

                self._state.following.pop()
                self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_entity136)
                #action start
                print "PORTS:", ", ".join(port_list1)
                #action end
                # bsdl.g:38:5: ( use SCOLON )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == USE) :
                        alt2 = 1


                    if alt2 == 1:
                        # bsdl.g:38:6: use SCOLON
                        pass 
                        self._state.following.append(self.FOLLOW_use_in_entity155)
                        self.use()

                        self._state.following.pop()
                        self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_entity157)


                    else:
                        break #loop2


                # bsdl.g:40:5: ( ( attribute | constant ) SCOLON )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ATTRIBUTE or LA4_0 == CONSTANT) :
                        alt4 = 1


                    if alt4 == 1:
                        # bsdl.g:40:6: ( attribute | constant ) SCOLON
                        pass 
                        # bsdl.g:40:6: ( attribute | constant )
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == ATTRIBUTE) :
                            alt3 = 1
                        elif (LA3_0 == CONSTANT) :
                            alt3 = 2
                        else:
                            nvae = NoViableAltException("", 3, 0, self.input)

                            raise nvae

                        if alt3 == 1:
                            # bsdl.g:40:7: attribute
                            pass 
                            self._state.following.append(self.FOLLOW_attribute_in_entity168)
                            self.attribute()

                            self._state.following.pop()


                        elif alt3 == 2:
                            # bsdl.g:40:17: constant
                            pass 
                            self._state.following.append(self.FOLLOW_constant_in_entity170)
                            self.constant()

                            self._state.following.pop()



                        self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_entity173)


                    else:
                        break #loop4


                self.match(self.input, END, self.FOLLOW_END_in_entity182)
                self._state.following.append(self.FOLLOW_identifier_in_entity184)
                self.identifier()

                self._state.following.pop()
                self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_entity186)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "entity"


    # $ANTLR start "generic"
    # bsdl.g:45:1: generic : GENERIC OPAREN ( identifier COLON identifier COLON EQUAL string ) CPAREN ;
    def generic(self, ):

        try:
            try:
                # bsdl.g:46:5: ( GENERIC OPAREN ( identifier COLON identifier COLON EQUAL string ) CPAREN )
                # bsdl.g:46:7: GENERIC OPAREN ( identifier COLON identifier COLON EQUAL string ) CPAREN
                pass 
                self.match(self.input, GENERIC, self.FOLLOW_GENERIC_in_generic203)
                self.match(self.input, OPAREN, self.FOLLOW_OPAREN_in_generic205)
                # bsdl.g:47:9: ( identifier COLON identifier COLON EQUAL string )
                # bsdl.g:47:10: identifier COLON identifier COLON EQUAL string
                pass 
                self._state.following.append(self.FOLLOW_identifier_in_generic217)
                self.identifier()

                self._state.following.pop()
                self.match(self.input, COLON, self.FOLLOW_COLON_in_generic219)
                self._state.following.append(self.FOLLOW_identifier_in_generic221)
                self.identifier()

                self._state.following.pop()
                self.match(self.input, COLON, self.FOLLOW_COLON_in_generic235)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_generic237)
                self._state.following.append(self.FOLLOW_string_in_generic239)
                self.string()

                self._state.following.pop()



                self.match(self.input, CPAREN, self.FOLLOW_CPAREN_in_generic249)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "generic"


    # $ANTLR start "use"
    # bsdl.g:52:1: use : USE id1= identifier DOT ALL ;
    def use(self, ):

        id1 = None


        try:
            try:
                # bsdl.g:53:5: ( USE id1= identifier DOT ALL )
                # bsdl.g:53:7: USE id1= identifier DOT ALL
                pass 
                self.match(self.input, USE, self.FOLLOW_USE_in_use266)
                self._state.following.append(self.FOLLOW_identifier_in_use270)
                id1 = self.identifier()

                self._state.following.pop()
                self.match(self.input, DOT, self.FOLLOW_DOT_in_use272)
                self.match(self.input, ALL, self.FOLLOW_ALL_in_use274)
                #action start
                print ((id1 is not None) and [self.input.toString(id1.start,id1.stop)] or [None])[0]+".all"
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "use"


    # $ANTLR start "attribute"
    # bsdl.g:57:1: attribute : ATTRIBUTE atn= identifier OF entn= identifier COLON general_attribute_assignment ;
    def attribute(self, ):

        atn = None

        entn = None


        try:
            try:
                # bsdl.g:58:5: ( ATTRIBUTE atn= identifier OF entn= identifier COLON general_attribute_assignment )
                # bsdl.g:58:7: ATTRIBUTE atn= identifier OF entn= identifier COLON general_attribute_assignment
                pass 
                self.match(self.input, ATTRIBUTE, self.FOLLOW_ATTRIBUTE_in_attribute301)
                self._state.following.append(self.FOLLOW_identifier_in_attribute314)
                atn = self.identifier()

                self._state.following.pop()
                self.match(self.input, OF, self.FOLLOW_OF_in_attribute316)
                self._state.following.append(self.FOLLOW_identifier_in_attribute320)
                entn = self.identifier()

                self._state.following.pop()
                self.match(self.input, COLON, self.FOLLOW_COLON_in_attribute322)
                #action start
                print "ATTRIBUTE CREATION", ((atn is not None) and [atn.value] or [None])[0], ((entn is not None) and [entn.value] or [None])[0]
                #action end
                self._state.following.append(self.FOLLOW_general_attribute_assignment_in_attribute344)
                self.general_attribute_assignment()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "attribute"


    # $ANTLR start "general_attribute_assignment"
    # bsdl.g:64:1: general_attribute_assignment : ( ( ENTITY IS ( identifier | string | ( DIGIT )+ ) ) | ( SIGNAL IS ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) ) ) );
    def general_attribute_assignment(self, ):

        try:
            try:
                # bsdl.g:65:5: ( ( ENTITY IS ( identifier | string | ( DIGIT )+ ) ) | ( SIGNAL IS ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) ) ) )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == ENTITY) :
                    alt8 = 1
                elif (LA8_0 == SIGNAL) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # bsdl.g:65:7: ( ENTITY IS ( identifier | string | ( DIGIT )+ ) )
                    pass 
                    # bsdl.g:65:7: ( ENTITY IS ( identifier | string | ( DIGIT )+ ) )
                    # bsdl.g:65:8: ENTITY IS ( identifier | string | ( DIGIT )+ )
                    pass 
                    self.match(self.input, ENTITY, self.FOLLOW_ENTITY_in_general_attribute_assignment362)
                    self.match(self.input, IS, self.FOLLOW_IS_in_general_attribute_assignment364)
                    # bsdl.g:66:13: ( identifier | string | ( DIGIT )+ )
                    alt6 = 3
                    LA6 = self.input.LA(1)
                    if LA6 == FULLCASE_WORD or LA6 == WORD:
                        alt6 = 1
                    elif LA6 == STRING:
                        alt6 = 2
                    elif LA6 == DIGIT:
                        alt6 = 3
                    else:
                        nvae = NoViableAltException("", 6, 0, self.input)

                        raise nvae

                    if alt6 == 1:
                        # bsdl.g:67:17: identifier
                        pass 
                        self._state.following.append(self.FOLLOW_identifier_in_general_attribute_assignment397)
                        self.identifier()

                        self._state.following.pop()


                    elif alt6 == 2:
                        # bsdl.g:68:17: string
                        pass 
                        self._state.following.append(self.FOLLOW_string_in_general_attribute_assignment416)
                        self.string()

                        self._state.following.pop()


                    elif alt6 == 3:
                        # bsdl.g:69:17: ( DIGIT )+
                        pass 
                        # bsdl.g:69:17: ( DIGIT )+
                        cnt5 = 0
                        while True: #loop5
                            alt5 = 2
                            LA5_0 = self.input.LA(1)

                            if (LA5_0 == DIGIT) :
                                alt5 = 1


                            if alt5 == 1:
                                # bsdl.g:69:17: DIGIT
                                pass 
                                self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_general_attribute_assignment435)


                            else:
                                if cnt5 >= 1:
                                    break #loop5

                                eee = EarlyExitException(5, self.input)
                                raise eee

                            cnt5 += 1










                elif alt8 == 2:
                    # bsdl.g:72:7: ( SIGNAL IS ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) ) )
                    pass 
                    # bsdl.g:72:7: ( SIGNAL IS ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) ) )
                    # bsdl.g:72:8: SIGNAL IS ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) )
                    pass 
                    self.match(self.input, SIGNAL, self.FOLLOW_SIGNAL_in_general_attribute_assignment468)
                    self.match(self.input, IS, self.FOLLOW_IS_in_general_attribute_assignment470)
                    # bsdl.g:73:13: ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) )
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((TRUE <= LA7_0 <= FALSE)) :
                        alt7 = 1
                    elif (LA7_0 == OPAREN) :
                        alt7 = 2
                    else:
                        nvae = NoViableAltException("", 7, 0, self.input)

                        raise nvae

                    if alt7 == 1:
                        # bsdl.g:74:17: ( TRUE | FALSE )
                        pass 
                        if (TRUE <= self.input.LA(1) <= FALSE):
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    elif alt7 == 2:
                        # bsdl.g:75:17: ( OPAREN scinot_number COMMA BOTH CPAREN )
                        pass 
                        # bsdl.g:75:17: ( OPAREN scinot_number COMMA BOTH CPAREN )
                        # bsdl.g:75:18: OPAREN scinot_number COMMA BOTH CPAREN
                        pass 
                        self.match(self.input, OPAREN, self.FOLLOW_OPAREN_in_general_attribute_assignment527)
                        self._state.following.append(self.FOLLOW_scinot_number_in_general_attribute_assignment529)
                        self.scinot_number()

                        self._state.following.pop()
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_general_attribute_assignment552)
                        self.match(self.input, BOTH, self.FOLLOW_BOTH_in_general_attribute_assignment554)
                        self.match(self.input, CPAREN, self.FOLLOW_CPAREN_in_general_attribute_assignment556)












            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "general_attribute_assignment"


    # $ANTLR start "constant"
    # bsdl.g:81:1: constant : CONSTANT identifier COLON identifier COLON EQUAL string ;
    def constant(self, ):

        try:
            try:
                # bsdl.g:82:5: ( CONSTANT identifier COLON identifier COLON EQUAL string )
                # bsdl.g:82:7: CONSTANT identifier COLON identifier COLON EQUAL string
                pass 
                self.match(self.input, CONSTANT, self.FOLLOW_CONSTANT_in_constant596)
                self._state.following.append(self.FOLLOW_identifier_in_constant598)
                self.identifier()

                self._state.following.pop()
                self.match(self.input, COLON, self.FOLLOW_COLON_in_constant600)
                self._state.following.append(self.FOLLOW_identifier_in_constant602)
                self.identifier()

                self._state.following.pop()
                self.match(self.input, COLON, self.FOLLOW_COLON_in_constant613)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_constant615)
                self._state.following.append(self.FOLLOW_string_in_constant617)
                self.string()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "constant"


    # $ANTLR start "port_list"
    # bsdl.g:86:1: port_list returns [value] : PORT OPAREN (pd= port_def SCOLON )* (pd= port_def ) CPAREN ;
    def port_list(self, ):

        value = None

        pd = None


        try:
            try:
                # bsdl.g:87:5: ( PORT OPAREN (pd= port_def SCOLON )* (pd= port_def ) CPAREN )
                # bsdl.g:87:7: PORT OPAREN (pd= port_def SCOLON )* (pd= port_def ) CPAREN
                pass 
                #action start
                value = []
                #action end
                self.match(self.input, PORT, self.FOLLOW_PORT_in_port_list648)
                self.match(self.input, OPAREN, self.FOLLOW_OPAREN_in_port_list650)
                # bsdl.g:89:9: (pd= port_def SCOLON )*
                while True: #loop9
                    alt9 = 2
                    alt9 = self.dfa9.predict(self.input)
                    if alt9 == 1:
                        # bsdl.g:89:10: pd= port_def SCOLON
                        pass 
                        self._state.following.append(self.FOLLOW_port_def_in_port_list664)
                        pd = self.port_def()

                        self._state.following.pop()
                        #action start
                        value.extend(pd)
                        #action end
                        self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_port_list668)


                    else:
                        break #loop9


                # bsdl.g:90:9: (pd= port_def )
                # bsdl.g:90:10: pd= port_def
                pass 
                self._state.following.append(self.FOLLOW_port_def_in_port_list684)
                pd = self.port_def()

                self._state.following.pop()
                #action start
                value.extend(pd)
                #action end



                self.match(self.input, CPAREN, self.FOLLOW_CPAREN_in_port_list697)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "port_list"


    # $ANTLR start "port_def"
    # bsdl.g:93:1: port_def returns [value] : (pname= identifier COMMA )* pname= identifier COLON portmode ( BIT | BIT_VECTOR OPAREN ( DIGIT )+ TO ( DIGIT )+ CPAREN ) ;
    def port_def(self, ):

        value = None

        pname = None


        try:
            try:
                # bsdl.g:94:5: ( (pname= identifier COMMA )* pname= identifier COLON portmode ( BIT | BIT_VECTOR OPAREN ( DIGIT )+ TO ( DIGIT )+ CPAREN ) )
                # bsdl.g:94:7: (pname= identifier COMMA )* pname= identifier COLON portmode ( BIT | BIT_VECTOR OPAREN ( DIGIT )+ TO ( DIGIT )+ CPAREN )
                pass 
                #action start
                value=[]
                #action end
                # bsdl.g:95:8: (pname= identifier COMMA )*
                while True: #loop10
                    alt10 = 2
                    alt10 = self.dfa10.predict(self.input)
                    if alt10 == 1:
                        # bsdl.g:95:9: pname= identifier COMMA
                        pass 
                        self._state.following.append(self.FOLLOW_identifier_in_port_def725)
                        pname = self.identifier()

                        self._state.following.pop()
                        #action start
                        value.append(((pname is not None) and [pname.value] or [None])[0])
                        #action end
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_port_def729)


                    else:
                        break #loop10


                self._state.following.append(self.FOLLOW_identifier_in_port_def743)
                pname = self.identifier()

                self._state.following.pop()
                #action start
                value.append(((pname is not None) and [pname.value] or [None])[0])
                #action end
                self.match(self.input, COLON, self.FOLLOW_COLON_in_port_def747)
                self._state.following.append(self.FOLLOW_portmode_in_port_def749)
                self.portmode()

                self._state.following.pop()
                # bsdl.g:97:9: ( BIT | BIT_VECTOR OPAREN ( DIGIT )+ TO ( DIGIT )+ CPAREN )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == BIT) :
                    alt13 = 1
                elif (LA13_0 == BIT_VECTOR) :
                    alt13 = 2
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # bsdl.g:97:10: BIT
                    pass 
                    self.match(self.input, BIT, self.FOLLOW_BIT_in_port_def762)


                elif alt13 == 2:
                    # bsdl.g:98:10: BIT_VECTOR OPAREN ( DIGIT )+ TO ( DIGIT )+ CPAREN
                    pass 
                    self.match(self.input, BIT_VECTOR, self.FOLLOW_BIT_VECTOR_in_port_def774)
                    self.match(self.input, OPAREN, self.FOLLOW_OPAREN_in_port_def776)
                    # bsdl.g:98:28: ( DIGIT )+
                    cnt11 = 0
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == DIGIT) :
                            alt11 = 1


                        if alt11 == 1:
                            # bsdl.g:98:28: DIGIT
                            pass 
                            self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_port_def778)


                        else:
                            if cnt11 >= 1:
                                break #loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1


                    self.match(self.input, TO, self.FOLLOW_TO_in_port_def781)
                    # bsdl.g:98:38: ( DIGIT )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == DIGIT) :
                            alt12 = 1


                        if alt12 == 1:
                            # bsdl.g:98:38: DIGIT
                            pass 
                            self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_port_def783)


                        else:
                            if cnt12 >= 1:
                                break #loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1


                    self.match(self.input, CPAREN, self.FOLLOW_CPAREN_in_port_def786)







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "port_def"

    class identifier_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.value = None




    # $ANTLR start "identifier"
    # bsdl.g:100:1: identifier returns [value] : ( FULLCASE_WORD | WORD ) ( FULLCASE_WORD | WORD | DIGIT )* ( '_' ( FULLCASE_WORD | WORD | DIGIT )+ )* ;
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # bsdl.g:101:5: ( ( FULLCASE_WORD | WORD ) ( FULLCASE_WORD | WORD | DIGIT )* ( '_' ( FULLCASE_WORD | WORD | DIGIT )+ )* )
                # bsdl.g:101:7: ( FULLCASE_WORD | WORD ) ( FULLCASE_WORD | WORD | DIGIT )* ( '_' ( FULLCASE_WORD | WORD | DIGIT )+ )*
                pass 
                if (FULLCASE_WORD <= self.input.LA(1) <= WORD):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                # bsdl.g:101:28: ( FULLCASE_WORD | WORD | DIGIT )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == DIGIT or (FULLCASE_WORD <= LA14_0 <= WORD)) :
                        alt14 = 1


                    if alt14 == 1:
                        # bsdl.g:
                        pass 
                        if self.input.LA(1) == DIGIT or (FULLCASE_WORD <= self.input.LA(1) <= WORD):
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        break #loop14


                # bsdl.g:101:56: ( '_' ( FULLCASE_WORD | WORD | DIGIT )+ )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == USCORE) :
                        alt16 = 1


                    if alt16 == 1:
                        # bsdl.g:101:57: '_' ( FULLCASE_WORD | WORD | DIGIT )+
                        pass 
                        self.match(self.input, USCORE, self.FOLLOW_USCORE_in_identifier819)
                        # bsdl.g:101:61: ( FULLCASE_WORD | WORD | DIGIT )+
                        cnt15 = 0
                        while True: #loop15
                            alt15 = 2
                            LA15_0 = self.input.LA(1)

                            if (LA15_0 == DIGIT or (FULLCASE_WORD <= LA15_0 <= WORD)) :
                                alt15 = 1


                            if alt15 == 1:
                                # bsdl.g:
                                pass 
                                if self.input.LA(1) == DIGIT or (FULLCASE_WORD <= self.input.LA(1) <= WORD):
                                    self.input.consume()
                                    self._state.errorRecovery = False

                                else:
                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt15 >= 1:
                                    break #loop15

                                eee = EarlyExitException(15, self.input)
                                raise eee

                            cnt15 += 1




                    else:
                        break #loop16


                #action start
                retval.value = self.input.toString(retval.start, self.input.LT(-1))
                #action end
                #action start
                #print retval.value
                #action end



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "identifier"


    # $ANTLR start "portmode"
    # bsdl.g:104:1: portmode returns [value] : ( IN | OUT | INOUT | BUFFER | LINKAGE | BUS );
    def portmode(self, ):

        value = None

        try:
            try:
                # bsdl.g:105:5: ( IN | OUT | INOUT | BUFFER | LINKAGE | BUS )
                # bsdl.g:
                pass 
                if (IN <= self.input.LA(1) <= BUS):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "portmode"


    # $ANTLR start "string"
    # bsdl.g:107:1: string : ( STRING ANDSIGN )* STRING ;
    def string(self, ):

        try:
            try:
                # bsdl.g:108:5: ( ( STRING ANDSIGN )* STRING )
                # bsdl.g:108:7: ( STRING ANDSIGN )* STRING
                pass 
                # bsdl.g:108:7: ( STRING ANDSIGN )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == STRING) :
                        LA17_1 = self.input.LA(2)

                        if (LA17_1 == ANDSIGN) :
                            alt17 = 1




                    if alt17 == 1:
                        # bsdl.g:108:8: STRING ANDSIGN
                        pass 
                        self.match(self.input, STRING, self.FOLLOW_STRING_in_string902)
                        self.match(self.input, ANDSIGN, self.FOLLOW_ANDSIGN_in_string904)


                    else:
                        break #loop17


                self.match(self.input, STRING, self.FOLLOW_STRING_in_string908)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "string"


    # $ANTLR start "scinot_number"
    # bsdl.g:111:1: scinot_number : ( DIGIT )* DOT ( DIGIT )* 'e' ( DIGIT )* ;
    def scinot_number(self, ):

        try:
            try:
                # bsdl.g:112:5: ( ( DIGIT )* DOT ( DIGIT )* 'e' ( DIGIT )* )
                # bsdl.g:112:7: ( DIGIT )* DOT ( DIGIT )* 'e' ( DIGIT )*
                pass 
                # bsdl.g:112:7: ( DIGIT )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == DIGIT) :
                        alt18 = 1


                    if alt18 == 1:
                        # bsdl.g:112:7: DIGIT
                        pass 
                        self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_scinot_number925)


                    else:
                        break #loop18


                self.match(self.input, DOT, self.FOLLOW_DOT_in_scinot_number928)
                # bsdl.g:112:18: ( DIGIT )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == DIGIT) :
                        alt19 = 1


                    if alt19 == 1:
                        # bsdl.g:112:18: DIGIT
                        pass 
                        self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_scinot_number930)


                    else:
                        break #loop19


                self.match(self.input, 123, self.FOLLOW_123_in_scinot_number933)
                # bsdl.g:112:29: ( DIGIT )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == DIGIT) :
                        alt20 = 1


                    if alt20 == 1:
                        # bsdl.g:112:29: DIGIT
                        pass 
                        self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_scinot_number935)


                    else:
                        break #loop20






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "scinot_number"


    # Delegated rules


    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\35\2\12\1\22\1\35\1\37\1\12\1\32\1\6\1\11\2\uffff\3\22\1\14"
        u"\1\6"
        )

    DFA9_max = DFA.unpack(
        u"\1\36\2\52\2\36\1\44\1\52\1\33\1\14\1\11\2\uffff\1\22\1\34\2\22"
        u"\1\14"
        )

    DFA9_accept = DFA.unpack(
        u"\12\uffff\1\2\1\1\5\uffff"
        )

    DFA9_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\2\1"),
        DFA.unpack(u"\1\5\7\uffff\1\2\3\uffff\1\4\6\uffff\2\2\13\uffff\1"
        u"\3"),
        DFA.unpack(u"\1\5\7\uffff\1\2\3\uffff\1\4\6\uffff\2\2\13\uffff\1"
        u"\3"),
        DFA.unpack(u"\1\6\12\uffff\2\6"),
        DFA.unpack(u"\2\1"),
        DFA.unpack(u"\6\7"),
        DFA.unpack(u"\1\5\7\uffff\1\6\3\uffff\1\4\6\uffff\2\6\13\uffff\1"
        u"\3"),
        DFA.unpack(u"\1\10\1\11"),
        DFA.unpack(u"\1\13\5\uffff\1\12"),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\15\11\uffff\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\20\5\uffff\1\17"),
        DFA.unpack(u"\1\13\5\uffff\1\12")
    ]

    # class definition for DFA #9

    DFA9 = DFA
    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\35\2\12\1\22\2\uffff\1\12"
        )

    DFA10_max = DFA.unpack(
        u"\1\36\2\52\1\36\2\uffff\1\52"
        )

    DFA10_accept = DFA.unpack(
        u"\4\uffff\1\1\1\2\1\uffff"
        )

    DFA10_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\2\1"),
        DFA.unpack(u"\1\5\7\uffff\1\2\3\uffff\1\4\6\uffff\2\2\13\uffff\1"
        u"\3"),
        DFA.unpack(u"\1\5\7\uffff\1\2\3\uffff\1\4\6\uffff\2\2\13\uffff\1"
        u"\3"),
        DFA.unpack(u"\1\6\12\uffff\2\6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\5\7\uffff\1\6\3\uffff\1\4\6\uffff\2\6\13\uffff\1"
        u"\3")
    ]

    # class definition for DFA #10

    DFA10 = DFA
 

    FOLLOW_entity_in_eval71 = frozenset([])
    FOLLOW_EOF_in_eval82 = frozenset([1])
    FOLLOW_ENTITY_in_entity98 = frozenset([29, 30])
    FOLLOW_identifier_in_entity102 = frozenset([5])
    FOLLOW_IS_in_entity104 = frozenset([8])
    FOLLOW_generic_in_entity123 = frozenset([6])
    FOLLOW_SCOLON_in_entity125 = frozenset([8, 25])
    FOLLOW_port_list_in_entity134 = frozenset([6])
    FOLLOW_SCOLON_in_entity136 = frozenset([7, 13, 16, 24])
    FOLLOW_use_in_entity155 = frozenset([6])
    FOLLOW_SCOLON_in_entity157 = frozenset([7, 13, 16, 24])
    FOLLOW_attribute_in_entity168 = frozenset([6])
    FOLLOW_constant_in_entity170 = frozenset([6])
    FOLLOW_SCOLON_in_entity173 = frozenset([7, 16, 24])
    FOLLOW_END_in_entity182 = frozenset([29, 30])
    FOLLOW_identifier_in_entity184 = frozenset([6])
    FOLLOW_SCOLON_in_entity186 = frozenset([1])
    FOLLOW_GENERIC_in_generic203 = frozenset([9])
    FOLLOW_OPAREN_in_generic205 = frozenset([29, 30])
    FOLLOW_identifier_in_generic217 = frozenset([10])
    FOLLOW_COLON_in_generic219 = frozenset([29, 30])
    FOLLOW_identifier_in_generic221 = frozenset([10])
    FOLLOW_COLON_in_generic235 = frozenset([11])
    FOLLOW_EQUAL_in_generic237 = frozenset([37])
    FOLLOW_string_in_generic239 = frozenset([12])
    FOLLOW_CPAREN_in_generic249 = frozenset([1])
    FOLLOW_USE_in_use266 = frozenset([29, 30])
    FOLLOW_identifier_in_use270 = frozenset([14])
    FOLLOW_DOT_in_use272 = frozenset([15])
    FOLLOW_ALL_in_use274 = frozenset([1])
    FOLLOW_ATTRIBUTE_in_attribute301 = frozenset([29, 30])
    FOLLOW_identifier_in_attribute314 = frozenset([17])
    FOLLOW_OF_in_attribute316 = frozenset([29, 30])
    FOLLOW_identifier_in_attribute320 = frozenset([10])
    FOLLOW_COLON_in_attribute322 = frozenset([4, 19])
    FOLLOW_general_attribute_assignment_in_attribute344 = frozenset([1])
    FOLLOW_ENTITY_in_general_attribute_assignment362 = frozenset([5])
    FOLLOW_IS_in_general_attribute_assignment364 = frozenset([18, 29, 30, 37])
    FOLLOW_identifier_in_general_attribute_assignment397 = frozenset([1])
    FOLLOW_string_in_general_attribute_assignment416 = frozenset([1])
    FOLLOW_DIGIT_in_general_attribute_assignment435 = frozenset([1, 18])
    FOLLOW_SIGNAL_in_general_attribute_assignment468 = frozenset([5])
    FOLLOW_IS_in_general_attribute_assignment470 = frozenset([9, 20, 21])
    FOLLOW_set_in_general_attribute_assignment503 = frozenset([1])
    FOLLOW_OPAREN_in_general_attribute_assignment527 = frozenset([14, 18])
    FOLLOW_scinot_number_in_general_attribute_assignment529 = frozenset([22])
    FOLLOW_COMMA_in_general_attribute_assignment552 = frozenset([23])
    FOLLOW_BOTH_in_general_attribute_assignment554 = frozenset([12])
    FOLLOW_CPAREN_in_general_attribute_assignment556 = frozenset([1])
    FOLLOW_CONSTANT_in_constant596 = frozenset([29, 30])
    FOLLOW_identifier_in_constant598 = frozenset([10])
    FOLLOW_COLON_in_constant600 = frozenset([29, 30])
    FOLLOW_identifier_in_constant602 = frozenset([10])
    FOLLOW_COLON_in_constant613 = frozenset([11])
    FOLLOW_EQUAL_in_constant615 = frozenset([37])
    FOLLOW_string_in_constant617 = frozenset([1])
    FOLLOW_PORT_in_port_list648 = frozenset([9])
    FOLLOW_OPAREN_in_port_list650 = frozenset([29, 30])
    FOLLOW_port_def_in_port_list664 = frozenset([6])
    FOLLOW_SCOLON_in_port_list668 = frozenset([29, 30])
    FOLLOW_port_def_in_port_list684 = frozenset([12])
    FOLLOW_CPAREN_in_port_list697 = frozenset([1])
    FOLLOW_identifier_in_port_def725 = frozenset([22])
    FOLLOW_COMMA_in_port_def729 = frozenset([29, 30])
    FOLLOW_identifier_in_port_def743 = frozenset([10])
    FOLLOW_COLON_in_port_def747 = frozenset([31, 32, 33, 34, 35, 36])
    FOLLOW_portmode_in_port_def749 = frozenset([26, 27])
    FOLLOW_BIT_in_port_def762 = frozenset([1])
    FOLLOW_BIT_VECTOR_in_port_def774 = frozenset([9])
    FOLLOW_OPAREN_in_port_def776 = frozenset([18])
    FOLLOW_DIGIT_in_port_def778 = frozenset([18, 28])
    FOLLOW_TO_in_port_def781 = frozenset([18])
    FOLLOW_DIGIT_in_port_def783 = frozenset([12, 18])
    FOLLOW_CPAREN_in_port_def786 = frozenset([1])
    FOLLOW_set_in_identifier803 = frozenset([1, 18, 29, 30, 42])
    FOLLOW_set_in_identifier809 = frozenset([1, 18, 29, 30, 42])
    FOLLOW_USCORE_in_identifier819 = frozenset([18, 29, 30])
    FOLLOW_set_in_identifier821 = frozenset([1, 18, 29, 30, 42])
    FOLLOW_set_in_portmode0 = frozenset([1])
    FOLLOW_STRING_in_string902 = frozenset([38])
    FOLLOW_ANDSIGN_in_string904 = frozenset([37])
    FOLLOW_STRING_in_string908 = frozenset([1])
    FOLLOW_DIGIT_in_scinot_number925 = frozenset([14, 18])
    FOLLOW_DOT_in_scinot_number928 = frozenset([18, 123])
    FOLLOW_DIGIT_in_scinot_number930 = frozenset([18, 123])
    FOLLOW_123_in_scinot_number933 = frozenset([1, 18])
    FOLLOW_DIGIT_in_scinot_number935 = frozenset([1, 18])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("bsdlLexer", bsdlParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
