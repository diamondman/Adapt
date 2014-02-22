# $ANTLR 3.1 bsdl.g 2014-02-08 13:25:29

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
import os
import sys



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=63
PACKAGE=86
NAND=76
INERTIAL=69
SEVERITY=101
WHILE=117
ROR=99
GENERIC=8
MOD=75
CASE=53
CHAR=121
NEW=77
NOR=79
NOT=80
POSTPONED=87
SUBTYPE=107
EOF=-1
ROL=98
TYPE=110
WORD=30
UNITS=112
DOWNTO=57
BEGIN=50
LOOP=73
RETURN=97
BOTH=22
TRANSPORT=109
IMPURE=68
ICHAR=122
BODY=52
GENERATE=64
LINKAGE=35
COMMENT=40
SELECT=100
REGISTER=93
ARRAY=48
SHARED=102
EXIT=60
RECORD=92
GUARDED=66
SRL=106
SRA=105
NULL=81
XNOR=119
ELSE=58
ON=82
WHITESPACE=39
BUS=36
WAIT=115
OF=17
FILE=61
ASSERT=49
ABS=42
GROUP=65
VARIABLE=114
OUT=32
UNTIL=113
USCORE=41
OR=84
ALIAS=45
ANDSIGN=38
CONSTANT=24
USE=13
ELSIF=59
END=7
FALSE=20
BIT_VECTOR=27
OTHERS=85
REPORT=96
SLA=103
ATTRIBUTE=16
T__124=124
T__123=123
FOR=62
CONFIGURATION=55
LIBRARY=71
SLL=104
ARCHITECTURE=47
AND=46
IF=67
INOUT=33
ENTITY=4
PURE=90
THEN=108
IN=31
COMMA=21
IS=5
REJECT=94
EQUAL=11
ALL=15
SIGNAL=18
ACCESS=43
CPAREN=12
NEXT=78
DIGIT=23
DOT=14
COMPONENT=54
WITH=118
SCOLON=6
FULLCASE_WORD=29
XOR=120
TO=28
OPAREN=9
DISCONNECT=56
RANGE=91
BUFFER=34
PORT=25
LITERAL=72
REM=95
AFTER=44
TRUE=19
PROCEDURE=88
COLON=10
OPEN=83
LABEL=70
WHEN=116
BLOCK=51
MAP=74
BIT=26
PROCESS=89
UNAFFECTED=111
STRING=37

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ENTITY", "IS", "SCOLON", "END", "GENERIC", "OPAREN", "COLON", "EQUAL", 
    "CPAREN", "USE", "DOT", "ALL", "ATTRIBUTE", "OF", "SIGNAL", "TRUE", 
    "FALSE", "COMMA", "BOTH", "DIGIT", "CONSTANT", "PORT", "BIT", "BIT_VECTOR", 
    "TO", "FULLCASE_WORD", "WORD", "IN", "OUT", "INOUT", "BUFFER", "LINKAGE", 
    "BUS", "STRING", "ANDSIGN", "WHITESPACE", "COMMENT", "USCORE", "ABS", 
    "ACCESS", "AFTER", "ALIAS", "AND", "ARCHITECTURE", "ARRAY", "ASSERT", 
    "BEGIN", "BLOCK", "BODY", "CASE", "COMPONENT", "CONFIGURATION", "DISCONNECT", 
    "DOWNTO", "ELSE", "ELSIF", "EXIT", "FILE", "FOR", "FUNCTION", "GENERATE", 
    "GROUP", "GUARDED", "IF", "IMPURE", "INERTIAL", "LABEL", "LIBRARY", 
    "LITERAL", "LOOP", "MAP", "MOD", "NAND", "NEW", "NEXT", "NOR", "NOT", 
    "NULL", "ON", "OPEN", "OR", "OTHERS", "PACKAGE", "POSTPONED", "PROCEDURE", 
    "PROCESS", "PURE", "RANGE", "RECORD", "REGISTER", "REJECT", "REM", "REPORT", 
    "RETURN", "ROL", "ROR", "SELECT", "SEVERITY", "SHARED", "SLA", "SLL", 
    "SRA", "SRL", "SUBTYPE", "THEN", "TRANSPORT", "TYPE", "UNAFFECTED", 
    "UNITS", "UNTIL", "VARIABLE", "WAIT", "WHEN", "WHILE", "WITH", "XNOR", 
    "XOR", "CHAR", "ICHAR", "'e'", "'+'"
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

        self.dfa11 = self.DFA11(
            self, 11,
            eot = self.DFA11_eot,
            eof = self.DFA11_eof,
            min = self.DFA11_min,
            max = self.DFA11_max,
            accept = self.DFA11_accept,
            special = self.DFA11_special,
            transition = self.DFA11_transition
            )



              
        self.attributes = {}
        self.chip_package = None
        self.ports = []




                


        

             




    # $ANTLR start "eval"
    # bsdl.g:24:1: eval returns [value] : ( entity ) EOF ;
    def eval(self, ):

        value = None

        entity1 = None


        try:
            try:
                # bsdl.g:25:5: ( ( entity ) EOF )
                # bsdl.g:25:7: ( entity ) EOF
                pass 
                # bsdl.g:25:7: ( entity )
                # bsdl.g:25:8: entity
                pass 
                self._state.following.append(self.FOLLOW_entity_in_eval61)
                entity1 = self.entity()

                self._state.following.pop()



                #action start
                value=entity1
                #action end
                self.match(self.input, EOF, self.FOLLOW_EOF_in_eval73)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "eval"


    # $ANTLR start "entity"
    # bsdl.g:28:1: entity returns [value] : ENTITY ename= identifier IS (g= generic SCOLON )+ port_list SCOLON ( use SCOLON )* ( ( (i= attribute ) | (i= constant ) ) SCOLON )* END identifier SCOLON ;
    def entity(self, ):

        value = None

        ename = None

        g = None

        i = None

        port_list2 = None


        try:
            try:
                # bsdl.g:29:5: ( ENTITY ename= identifier IS (g= generic SCOLON )+ port_list SCOLON ( use SCOLON )* ( ( (i= attribute ) | (i= constant ) ) SCOLON )* END identifier SCOLON )
                # bsdl.g:29:7: ENTITY ename= identifier IS (g= generic SCOLON )+ port_list SCOLON ( use SCOLON )* ( ( (i= attribute ) | (i= constant ) ) SCOLON )* END identifier SCOLON
                pass 
                #action start
                value = {}
                #action end
                self.match(self.input, ENTITY, self.FOLLOW_ENTITY_in_entity97)
                self._state.following.append(self.FOLLOW_identifier_in_entity101)
                ename = self.identifier()

                self._state.following.pop()
                self.match(self.input, IS, self.FOLLOW_IS_in_entity103)
                #action start
                value['entity_name'] = ((ename is not None) and [ename.value] or [None])[0]
                #action end
                #action start
                value['generics']={}
                #action end
                # bsdl.g:34:5: (g= generic SCOLON )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == GENERIC) :
                        alt1 = 1


                    if alt1 == 1:
                        # bsdl.g:34:6: g= generic SCOLON
                        pass 
                        self._state.following.append(self.FOLLOW_generic_in_entity130)
                        g = self.generic()

                        self._state.following.pop()
                        self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_entity132)
                        #action start
                        value['generics'][((g is not None) and [g.key] or [None])[0]]=((g is not None) and [g.value] or [None])[0]
                        #action end


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                self._state.following.append(self.FOLLOW_port_list_in_entity143)
                port_list2 = self.port_list()

                self._state.following.pop()
                self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_entity145)
                #action start
                value['ports']=port_list2
                #action end
                # bsdl.g:39:5: ( use SCOLON )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == USE) :
                        alt2 = 1


                    if alt2 == 1:
                        # bsdl.g:39:6: use SCOLON
                        pass 
                        self._state.following.append(self.FOLLOW_use_in_entity164)
                        self.use()

                        self._state.following.pop()
                        self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_entity166)


                    else:
                        break #loop2


                #action start
                value['attributes']={}
                #action end
                #action start
                value['constants']={}
                #action end
                # bsdl.g:43:5: ( ( (i= attribute ) | (i= constant ) ) SCOLON )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ATTRIBUTE or LA4_0 == CONSTANT) :
                        alt4 = 1


                    if alt4 == 1:
                        # bsdl.g:44:7: ( (i= attribute ) | (i= constant ) ) SCOLON
                        pass 
                        # bsdl.g:44:7: ( (i= attribute ) | (i= constant ) )
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
                            # bsdl.g:45:9: (i= attribute )
                            pass 
                            # bsdl.g:45:9: (i= attribute )
                            # bsdl.g:45:10: i= attribute
                            pass 
                            self._state.following.append(self.FOLLOW_attribute_in_entity208)
                            i = self.attribute()

                            self._state.following.pop()
                            #action start
                            value['attributes'][((i is not None) and [i.key] or [None])[0]]=((i is not None) and [i.value] or [None])[0]
                            #action end





                        elif alt3 == 2:
                            # bsdl.g:46:10: (i= constant )
                            pass 
                            # bsdl.g:46:10: (i= constant )
                            # bsdl.g:46:11: i= constant
                            pass 
                            self._state.following.append(self.FOLLOW_constant_in_entity225)
                            i = self.constant()

                            self._state.following.pop()
                            #action start
                            value['constants'][((i is not None) and [i.key] or [None])[0]]=((i is not None) and [i.value] or [None])[0]
                            #action end






                        self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_entity238)


                    else:
                        break #loop4


                self.match(self.input, END, self.FOLLOW_END_in_entity253)
                self._state.following.append(self.FOLLOW_identifier_in_entity255)
                self.identifier()

                self._state.following.pop()
                self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_entity257)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "entity"

    class generic_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.key = None
            self.value = None




    # $ANTLR start "generic"
    # bsdl.g:53:1: generic returns [key, value] : GENERIC OPAREN (gk= identifier COLON identifier COLON EQUAL gv= string ) CPAREN ;
    def generic(self, ):

        retval = self.generic_return()
        retval.start = self.input.LT(1)

        gk = None

        gv = None


        try:
            try:
                # bsdl.g:54:5: ( GENERIC OPAREN (gk= identifier COLON identifier COLON EQUAL gv= string ) CPAREN )
                # bsdl.g:54:7: GENERIC OPAREN (gk= identifier COLON identifier COLON EQUAL gv= string ) CPAREN
                pass 
                self.match(self.input, GENERIC, self.FOLLOW_GENERIC_in_generic279)
                self.match(self.input, OPAREN, self.FOLLOW_OPAREN_in_generic281)
                # bsdl.g:55:9: (gk= identifier COLON identifier COLON EQUAL gv= string )
                # bsdl.g:55:10: gk= identifier COLON identifier COLON EQUAL gv= string
                pass 
                self._state.following.append(self.FOLLOW_identifier_in_generic295)
                gk = self.identifier()

                self._state.following.pop()
                self.match(self.input, COLON, self.FOLLOW_COLON_in_generic297)
                self._state.following.append(self.FOLLOW_identifier_in_generic299)
                self.identifier()

                self._state.following.pop()
                self.match(self.input, COLON, self.FOLLOW_COLON_in_generic313)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_generic315)
                self._state.following.append(self.FOLLOW_string_in_generic319)
                gv = self.string()

                self._state.following.pop()



                self.match(self.input, CPAREN, self.FOLLOW_CPAREN_in_generic329)
                #action start
                retval.value=gv
                #action end
                #action start
                retval.key=((gk is not None) and [gk.value] or [None])[0]
                #action end



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "generic"


    # $ANTLR start "use"
    # bsdl.g:60:1: use : USE id1= identifier DOT ALL ;
    def use(self, ):

        id1 = None


        try:
            try:
                # bsdl.g:61:5: ( USE id1= identifier DOT ALL )
                # bsdl.g:61:7: USE id1= identifier DOT ALL
                pass 
                self.match(self.input, USE, self.FOLLOW_USE_in_use349)
                self._state.following.append(self.FOLLOW_identifier_in_use353)
                id1 = self.identifier()

                self._state.following.pop()
                self.match(self.input, DOT, self.FOLLOW_DOT_in_use355)
                self.match(self.input, ALL, self.FOLLOW_ALL_in_use357)
                #action start
                #oprint ((id1 is not None) and [self.input.toString(id1.start,id1.stop)] or [None])[0]+".all"
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "use"

    class attribute_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.key = None
            self.value = None




    # $ANTLR start "attribute"
    # bsdl.g:65:1: attribute returns [key, value] : ATTRIBUTE atn= identifier OF entn= identifier COLON v= general_attribute_assignment ;
    def attribute(self, ):

        retval = self.attribute_return()
        retval.start = self.input.LT(1)

        atn = None

        entn = None

        v = None


        try:
            try:
                # bsdl.g:66:5: ( ATTRIBUTE atn= identifier OF entn= identifier COLON v= general_attribute_assignment )
                # bsdl.g:66:7: ATTRIBUTE atn= identifier OF entn= identifier COLON v= general_attribute_assignment
                pass 
                self.match(self.input, ATTRIBUTE, self.FOLLOW_ATTRIBUTE_in_attribute388)
                self._state.following.append(self.FOLLOW_identifier_in_attribute401)
                atn = self.identifier()

                self._state.following.pop()
                self.match(self.input, OF, self.FOLLOW_OF_in_attribute403)
                self._state.following.append(self.FOLLOW_identifier_in_attribute407)
                entn = self.identifier()

                self._state.following.pop()
                self.match(self.input, COLON, self.FOLLOW_COLON_in_attribute409)
                #action start
                retval.key=((atn is not None) and [atn.value] or [None])[0]
                #action end
                #action start
                #print "ATTRIBUTE CREATION", ((atn is not None) and [atn.value] or [None])[0], ((entn is not None) and [entn.value] or [None])[0]
                #action end
                self._state.following.append(self.FOLLOW_general_attribute_assignment_in_attribute435)
                v = self.general_attribute_assignment()

                self._state.following.pop()
                #action start
                retval.value=v
                #action end



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "attribute"


    # $ANTLR start "general_attribute_assignment"
    # bsdl.g:72:1: general_attribute_assignment returns [value] : ( ( ENTITY IS (i= identifier | s= string | n= number ) ) | ( SIGNAL IS ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) ) ) );
    def general_attribute_assignment(self, ):

        value = None

        i = None

        s = None

        n = None

        scinot_number3 = None


        try:
            try:
                # bsdl.g:73:5: ( ( ENTITY IS (i= identifier | s= string | n= number ) ) | ( SIGNAL IS ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) ) ) )
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
                    # bsdl.g:73:7: ( ENTITY IS (i= identifier | s= string | n= number ) )
                    pass 
                    # bsdl.g:73:7: ( ENTITY IS (i= identifier | s= string | n= number ) )
                    # bsdl.g:73:8: ENTITY IS (i= identifier | s= string | n= number )
                    pass 
                    self.match(self.input, ENTITY, self.FOLLOW_ENTITY_in_general_attribute_assignment459)
                    self.match(self.input, IS, self.FOLLOW_IS_in_general_attribute_assignment461)
                    # bsdl.g:74:13: (i= identifier | s= string | n= number )
                    alt5 = 3
                    LA5 = self.input.LA(1)
                    if LA5 == FULLCASE_WORD or LA5 == WORD:
                        alt5 = 1
                    elif LA5 == STRING:
                        alt5 = 2
                    elif LA5 == DIGIT:
                        alt5 = 3
                    else:
                        nvae = NoViableAltException("", 5, 0, self.input)

                        raise nvae

                    if alt5 == 1:
                        # bsdl.g:75:17: i= identifier
                        pass 
                        self._state.following.append(self.FOLLOW_identifier_in_general_attribute_assignment496)
                        i = self.identifier()

                        self._state.following.pop()
                        #action start
                        value=((i is not None) and [i.value] or [None])[0]
                        #action end


                    elif alt5 == 2:
                        # bsdl.g:76:18: s= string
                        pass 
                        self._state.following.append(self.FOLLOW_string_in_general_attribute_assignment519)
                        s = self.string()

                        self._state.following.pop()
                        #action start
                        value=s
                        #action end


                    elif alt5 == 3:
                        # bsdl.g:77:18: n= number
                        pass 
                        self._state.following.append(self.FOLLOW_number_in_general_attribute_assignment542)
                        n = self.number()

                        self._state.following.pop()
                        #action start
                        value=((n is not None) and [n.value] or [None])[0]
                        #action end








                elif alt8 == 2:
                    # bsdl.g:80:8: ( SIGNAL IS ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) ) )
                    pass 
                    # bsdl.g:80:8: ( SIGNAL IS ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) ) )
                    # bsdl.g:80:9: SIGNAL IS ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) )
                    pass 
                    self.match(self.input, SIGNAL, self.FOLLOW_SIGNAL_in_general_attribute_assignment576)
                    self.match(self.input, IS, self.FOLLOW_IS_in_general_attribute_assignment578)
                    # bsdl.g:81:13: ( ( TRUE | FALSE ) | ( OPAREN scinot_number COMMA BOTH CPAREN ) )
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
                        # bsdl.g:82:17: ( TRUE | FALSE )
                        pass 
                        # bsdl.g:82:17: ( TRUE | FALSE )
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == TRUE) :
                            alt6 = 1
                        elif (LA6_0 == FALSE) :
                            alt6 = 2
                        else:
                            nvae = NoViableAltException("", 6, 0, self.input)

                            raise nvae

                        if alt6 == 1:
                            # bsdl.g:82:18: TRUE
                            pass 
                            self.match(self.input, TRUE, self.FOLLOW_TRUE_in_general_attribute_assignment612)
                            #action start
                            value=True
                            #action end


                        elif alt6 == 2:
                            # bsdl.g:82:37: FALSE
                            pass 
                            self.match(self.input, FALSE, self.FOLLOW_FALSE_in_general_attribute_assignment616)
                            #action start
                            value=False
                            #action end





                    elif alt7 == 2:
                        # bsdl.g:83:17: ( OPAREN scinot_number COMMA BOTH CPAREN )
                        pass 
                        # bsdl.g:83:17: ( OPAREN scinot_number COMMA BOTH CPAREN )
                        # bsdl.g:83:18: OPAREN scinot_number COMMA BOTH CPAREN
                        pass 
                        self.match(self.input, OPAREN, self.FOLLOW_OPAREN_in_general_attribute_assignment639)
                        self._state.following.append(self.FOLLOW_scinot_number_in_general_attribute_assignment641)
                        scinot_number3 = self.scinot_number()

                        self._state.following.pop()
                        #action start
                        value=((scinot_number3 is not None) and [self.input.toString(scinot_number3.start,scinot_number3.stop)] or [None])[0]
                        #action end
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_general_attribute_assignment665)
                        self.match(self.input, BOTH, self.FOLLOW_BOTH_in_general_attribute_assignment667)
                        self.match(self.input, CPAREN, self.FOLLOW_CPAREN_in_general_attribute_assignment669)












            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "general_attribute_assignment"

    class number_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.value = None




    # $ANTLR start "number"
    # bsdl.g:89:1: number returns [value] : ( DIGIT )+ ;
    def number(self, ):

        retval = self.number_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # bsdl.g:90:5: ( ( DIGIT )+ )
                # bsdl.g:90:7: ( DIGIT )+
                pass 
                # bsdl.g:90:7: ( DIGIT )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == DIGIT) :
                        alt9 = 1


                    if alt9 == 1:
                        # bsdl.g:90:7: DIGIT
                        pass 
                        self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_number713)


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1


                #action start
                retval.value=int(self.input.toString(retval.start, self.input.LT(-1)))
                #action end



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "number"

    class constant_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.key = None
            self.value = None




    # $ANTLR start "constant"
    # bsdl.g:93:1: constant returns [key, value] : CONSTANT k= identifier COLON identifier COLON EQUAL v= string ;
    def constant(self, ):

        retval = self.constant_return()
        retval.start = self.input.LT(1)

        k = None

        v = None


        try:
            try:
                # bsdl.g:94:5: ( CONSTANT k= identifier COLON identifier COLON EQUAL v= string )
                # bsdl.g:94:7: CONSTANT k= identifier COLON identifier COLON EQUAL v= string
                pass 
                self.match(self.input, CONSTANT, self.FOLLOW_CONSTANT_in_constant737)
                self._state.following.append(self.FOLLOW_identifier_in_constant741)
                k = self.identifier()

                self._state.following.pop()
                #action start
                retval.key=((k is not None) and [k.value] or [None])[0]
                #action end
                self.match(self.input, COLON, self.FOLLOW_COLON_in_constant745)
                self._state.following.append(self.FOLLOW_identifier_in_constant747)
                self.identifier()

                self._state.following.pop()
                self.match(self.input, COLON, self.FOLLOW_COLON_in_constant758)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_constant760)
                self._state.following.append(self.FOLLOW_string_in_constant764)
                v = self.string()

                self._state.following.pop()
                #action start
                retval.value=v
                #action end



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "constant"


    # $ANTLR start "port_list"
    # bsdl.g:98:1: port_list returns [value] : PORT OPAREN (pd= port_def SCOLON )* (pd= port_def ) CPAREN ;
    def port_list(self, ):

        value = None

        pd = None


        try:
            try:
                # bsdl.g:99:5: ( PORT OPAREN (pd= port_def SCOLON )* (pd= port_def ) CPAREN )
                # bsdl.g:99:7: PORT OPAREN (pd= port_def SCOLON )* (pd= port_def ) CPAREN
                pass 
                #action start
                value = []
                #action end
                self.match(self.input, PORT, self.FOLLOW_PORT_in_port_list797)
                self.match(self.input, OPAREN, self.FOLLOW_OPAREN_in_port_list799)
                # bsdl.g:101:9: (pd= port_def SCOLON )*
                while True: #loop10
                    alt10 = 2
                    alt10 = self.dfa10.predict(self.input)
                    if alt10 == 1:
                        # bsdl.g:101:10: pd= port_def SCOLON
                        pass 
                        self._state.following.append(self.FOLLOW_port_def_in_port_list813)
                        pd = self.port_def()

                        self._state.following.pop()
                        #action start
                        value.extend(pd)
                        #action end
                        self.match(self.input, SCOLON, self.FOLLOW_SCOLON_in_port_list817)


                    else:
                        break #loop10


                # bsdl.g:102:9: (pd= port_def )
                # bsdl.g:102:10: pd= port_def
                pass 
                self._state.following.append(self.FOLLOW_port_def_in_port_list833)
                pd = self.port_def()

                self._state.following.pop()
                #action start
                value.extend(pd)
                #action end



                self.match(self.input, CPAREN, self.FOLLOW_CPAREN_in_port_list846)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "port_list"


    # $ANTLR start "port_def"
    # bsdl.g:105:1: port_def returns [value] : (pname= identifier COMMA )* pname= identifier COLON portmode ( BIT | BIT_VECTOR OPAREN ( DIGIT )+ TO ( DIGIT )+ CPAREN ) ;
    def port_def(self, ):

        value = None

        pname = None


        try:
            try:
                # bsdl.g:106:5: ( (pname= identifier COMMA )* pname= identifier COLON portmode ( BIT | BIT_VECTOR OPAREN ( DIGIT )+ TO ( DIGIT )+ CPAREN ) )
                # bsdl.g:106:7: (pname= identifier COMMA )* pname= identifier COLON portmode ( BIT | BIT_VECTOR OPAREN ( DIGIT )+ TO ( DIGIT )+ CPAREN )
                pass 
                #action start
                value=[]
                #action end
                # bsdl.g:107:8: (pname= identifier COMMA )*
                while True: #loop11
                    alt11 = 2
                    alt11 = self.dfa11.predict(self.input)
                    if alt11 == 1:
                        # bsdl.g:107:9: pname= identifier COMMA
                        pass 
                        self._state.following.append(self.FOLLOW_identifier_in_port_def874)
                        pname = self.identifier()

                        self._state.following.pop()
                        #action start
                        value.append(((pname is not None) and [pname.value] or [None])[0])
                        #action end
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_port_def878)


                    else:
                        break #loop11


                self._state.following.append(self.FOLLOW_identifier_in_port_def892)
                pname = self.identifier()

                self._state.following.pop()
                #action start
                value.append(((pname is not None) and [pname.value] or [None])[0])
                #action end
                self.match(self.input, COLON, self.FOLLOW_COLON_in_port_def896)
                self._state.following.append(self.FOLLOW_portmode_in_port_def898)
                self.portmode()

                self._state.following.pop()
                # bsdl.g:109:9: ( BIT | BIT_VECTOR OPAREN ( DIGIT )+ TO ( DIGIT )+ CPAREN )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == BIT) :
                    alt14 = 1
                elif (LA14_0 == BIT_VECTOR) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # bsdl.g:109:10: BIT
                    pass 
                    self.match(self.input, BIT, self.FOLLOW_BIT_in_port_def911)


                elif alt14 == 2:
                    # bsdl.g:110:10: BIT_VECTOR OPAREN ( DIGIT )+ TO ( DIGIT )+ CPAREN
                    pass 
                    self.match(self.input, BIT_VECTOR, self.FOLLOW_BIT_VECTOR_in_port_def923)
                    self.match(self.input, OPAREN, self.FOLLOW_OPAREN_in_port_def925)
                    # bsdl.g:110:28: ( DIGIT )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == DIGIT) :
                            alt12 = 1


                        if alt12 == 1:
                            # bsdl.g:110:28: DIGIT
                            pass 
                            self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_port_def927)


                        else:
                            if cnt12 >= 1:
                                break #loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1


                    self.match(self.input, TO, self.FOLLOW_TO_in_port_def930)
                    # bsdl.g:110:38: ( DIGIT )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == DIGIT) :
                            alt13 = 1


                        if alt13 == 1:
                            # bsdl.g:110:38: DIGIT
                            pass 
                            self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_port_def932)


                        else:
                            if cnt13 >= 1:
                                break #loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1


                    self.match(self.input, CPAREN, self.FOLLOW_CPAREN_in_port_def935)







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
    # bsdl.g:112:1: identifier returns [value] : ( FULLCASE_WORD | WORD ) ( FULLCASE_WORD | WORD | DIGIT )* ( '_' ( FULLCASE_WORD | WORD | DIGIT )+ )* ;
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # bsdl.g:113:5: ( ( FULLCASE_WORD | WORD ) ( FULLCASE_WORD | WORD | DIGIT )* ( '_' ( FULLCASE_WORD | WORD | DIGIT )+ )* )
                # bsdl.g:113:7: ( FULLCASE_WORD | WORD ) ( FULLCASE_WORD | WORD | DIGIT )* ( '_' ( FULLCASE_WORD | WORD | DIGIT )+ )*
                pass 
                if (FULLCASE_WORD <= self.input.LA(1) <= WORD):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                # bsdl.g:113:28: ( FULLCASE_WORD | WORD | DIGIT )*
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
                        break #loop15


                # bsdl.g:113:56: ( '_' ( FULLCASE_WORD | WORD | DIGIT )+ )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == USCORE) :
                        alt17 = 1


                    if alt17 == 1:
                        # bsdl.g:113:57: '_' ( FULLCASE_WORD | WORD | DIGIT )+
                        pass 
                        self.match(self.input, USCORE, self.FOLLOW_USCORE_in_identifier968)
                        # bsdl.g:113:61: ( FULLCASE_WORD | WORD | DIGIT )+
                        cnt16 = 0
                        while True: #loop16
                            alt16 = 2
                            LA16_0 = self.input.LA(1)

                            if (LA16_0 == DIGIT or (FULLCASE_WORD <= LA16_0 <= WORD)) :
                                alt16 = 1


                            if alt16 == 1:
                                # bsdl.g:
                                pass 
                                if self.input.LA(1) == DIGIT or (FULLCASE_WORD <= self.input.LA(1) <= WORD):
                                    self.input.consume()
                                    self._state.errorRecovery = False

                                else:
                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt16 >= 1:
                                    break #loop16

                                eee = EarlyExitException(16, self.input)
                                raise eee

                            cnt16 += 1




                    else:
                        break #loop17


                #action start
                retval.value = self.input.toString(retval.start, self.input.LT(-1)).upper()
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
    # bsdl.g:116:1: portmode returns [value] : ( IN | OUT | INOUT | BUFFER | LINKAGE | BUS );
    def portmode(self, ):

        value = None

        try:
            try:
                # bsdl.g:117:5: ( IN | OUT | INOUT | BUFFER | LINKAGE | BUS )
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
    # bsdl.g:119:1: string returns [value] : (s= STRING ANDSIGN )* s1= STRING ;
    def string(self, ):

        value = None

        s = None
        s1 = None

        try:
            try:
                # bsdl.g:120:5: ( (s= STRING ANDSIGN )* s1= STRING )
                # bsdl.g:120:7: (s= STRING ANDSIGN )* s1= STRING
                pass 
                #action start
                str_parts = []
                #action end
                # bsdl.g:121:7: (s= STRING ANDSIGN )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == STRING) :
                        LA18_1 = self.input.LA(2)

                        if (LA18_1 == ANDSIGN) :
                            alt18 = 1




                    if alt18 == 1:
                        # bsdl.g:121:8: s= STRING ANDSIGN
                        pass 
                        s=self.match(self.input, STRING, self.FOLLOW_STRING_in_string1039)
                        self.match(self.input, ANDSIGN, self.FOLLOW_ANDSIGN_in_string1041)
                        #action start
                        str_parts.append(s.text[1:-1])
                        #action end


                    else:
                        break #loop18


                s1=self.match(self.input, STRING, self.FOLLOW_STRING_in_string1058)
                #action start
                str_parts.append(s1.text[1:-1])
                #action end
                #action start
                value = "".join(str_parts)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "string"

    class scinot_number_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "scinot_number"
    # bsdl.g:126:1: scinot_number : ( DIGIT )* DOT ( DIGIT )* 'e' ( '+' )? ( DIGIT )* ;
    def scinot_number(self, ):

        retval = self.scinot_number_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # bsdl.g:127:5: ( ( DIGIT )* DOT ( DIGIT )* 'e' ( '+' )? ( DIGIT )* )
                # bsdl.g:127:7: ( DIGIT )* DOT ( DIGIT )* 'e' ( '+' )? ( DIGIT )*
                pass 
                # bsdl.g:127:7: ( DIGIT )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == DIGIT) :
                        alt19 = 1


                    if alt19 == 1:
                        # bsdl.g:127:7: DIGIT
                        pass 
                        self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_scinot_number1087)


                    else:
                        break #loop19


                self.match(self.input, DOT, self.FOLLOW_DOT_in_scinot_number1090)
                # bsdl.g:127:18: ( DIGIT )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == DIGIT) :
                        alt20 = 1


                    if alt20 == 1:
                        # bsdl.g:127:18: DIGIT
                        pass 
                        self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_scinot_number1092)


                    else:
                        break #loop20


                self.match(self.input, 123, self.FOLLOW_123_in_scinot_number1095)
                # bsdl.g:127:29: ( '+' )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == 124) :
                    alt21 = 1
                if alt21 == 1:
                    # bsdl.g:127:29: '+'
                    pass 
                    self.match(self.input, 124, self.FOLLOW_124_in_scinot_number1097)



                # bsdl.g:127:34: ( DIGIT )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == DIGIT) :
                        alt22 = 1


                    if alt22 == 1:
                        # bsdl.g:127:34: DIGIT
                        pass 
                        self.match(self.input, DIGIT, self.FOLLOW_DIGIT_in_scinot_number1100)


                    else:
                        break #loop22





                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "scinot_number"


    # Delegated rules


    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\35\2\12\1\27\1\35\1\37\1\12\1\32\1\6\1\11\2\uffff\3\27\1\14"
        u"\1\6"
        )

    DFA10_max = DFA.unpack(
        u"\1\36\2\51\2\36\1\44\1\51\1\33\1\14\1\11\2\uffff\1\27\1\34\2\27"
        u"\1\14"
        )

    DFA10_accept = DFA.unpack(
        u"\12\uffff\1\2\1\1\5\uffff"
        )

    DFA10_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\2\1"),
        DFA.unpack(u"\1\5\12\uffff\1\4\1\uffff\1\2\5\uffff\2\2\12\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\5\12\uffff\1\4\1\uffff\1\2\5\uffff\2\2\12\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\6\5\uffff\2\6"),
        DFA.unpack(u"\2\1"),
        DFA.unpack(u"\6\7"),
        DFA.unpack(u"\1\5\12\uffff\1\4\1\uffff\1\6\5\uffff\2\6\12\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\10\1\11"),
        DFA.unpack(u"\1\13\5\uffff\1\12"),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\15\4\uffff\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\20\12\uffff\1\17"),
        DFA.unpack(u"\1\13\5\uffff\1\12")
    ]

    # class definition for DFA #10

    DFA10 = DFA
    # lookup tables for DFA #11

    DFA11_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA11_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA11_min = DFA.unpack(
        u"\1\35\2\12\1\27\2\uffff\1\12"
        )

    DFA11_max = DFA.unpack(
        u"\1\36\2\51\1\36\2\uffff\1\51"
        )

    DFA11_accept = DFA.unpack(
        u"\4\uffff\1\2\1\1\1\uffff"
        )

    DFA11_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA11_transition = [
        DFA.unpack(u"\2\1"),
        DFA.unpack(u"\1\4\12\uffff\1\5\1\uffff\1\2\5\uffff\2\2\12\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\4\12\uffff\1\5\1\uffff\1\2\5\uffff\2\2\12\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\6\5\uffff\2\6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\12\uffff\1\5\1\uffff\1\6\5\uffff\2\6\12\uffff"
        u"\1\3")
    ]

    # class definition for DFA #11

    DFA11 = DFA
 

    FOLLOW_entity_in_eval61 = frozenset([])
    FOLLOW_EOF_in_eval73 = frozenset([1])
    FOLLOW_ENTITY_in_entity97 = frozenset([29, 30])
    FOLLOW_identifier_in_entity101 = frozenset([5])
    FOLLOW_IS_in_entity103 = frozenset([8])
    FOLLOW_generic_in_entity130 = frozenset([6])
    FOLLOW_SCOLON_in_entity132 = frozenset([8, 25])
    FOLLOW_port_list_in_entity143 = frozenset([6])
    FOLLOW_SCOLON_in_entity145 = frozenset([7, 13, 16, 24])
    FOLLOW_use_in_entity164 = frozenset([6])
    FOLLOW_SCOLON_in_entity166 = frozenset([7, 13, 16, 24])
    FOLLOW_attribute_in_entity208 = frozenset([6])
    FOLLOW_constant_in_entity225 = frozenset([6])
    FOLLOW_SCOLON_in_entity238 = frozenset([7, 16, 24])
    FOLLOW_END_in_entity253 = frozenset([29, 30])
    FOLLOW_identifier_in_entity255 = frozenset([6])
    FOLLOW_SCOLON_in_entity257 = frozenset([1])
    FOLLOW_GENERIC_in_generic279 = frozenset([9])
    FOLLOW_OPAREN_in_generic281 = frozenset([29, 30])
    FOLLOW_identifier_in_generic295 = frozenset([10])
    FOLLOW_COLON_in_generic297 = frozenset([29, 30])
    FOLLOW_identifier_in_generic299 = frozenset([10])
    FOLLOW_COLON_in_generic313 = frozenset([11])
    FOLLOW_EQUAL_in_generic315 = frozenset([37])
    FOLLOW_string_in_generic319 = frozenset([12])
    FOLLOW_CPAREN_in_generic329 = frozenset([1])
    FOLLOW_USE_in_use349 = frozenset([29, 30])
    FOLLOW_identifier_in_use353 = frozenset([14])
    FOLLOW_DOT_in_use355 = frozenset([15])
    FOLLOW_ALL_in_use357 = frozenset([1])
    FOLLOW_ATTRIBUTE_in_attribute388 = frozenset([29, 30])
    FOLLOW_identifier_in_attribute401 = frozenset([17])
    FOLLOW_OF_in_attribute403 = frozenset([29, 30])
    FOLLOW_identifier_in_attribute407 = frozenset([10])
    FOLLOW_COLON_in_attribute409 = frozenset([4, 18])
    FOLLOW_general_attribute_assignment_in_attribute435 = frozenset([1])
    FOLLOW_ENTITY_in_general_attribute_assignment459 = frozenset([5])
    FOLLOW_IS_in_general_attribute_assignment461 = frozenset([23, 29, 30, 37])
    FOLLOW_identifier_in_general_attribute_assignment496 = frozenset([1])
    FOLLOW_string_in_general_attribute_assignment519 = frozenset([1])
    FOLLOW_number_in_general_attribute_assignment542 = frozenset([1])
    FOLLOW_SIGNAL_in_general_attribute_assignment576 = frozenset([5])
    FOLLOW_IS_in_general_attribute_assignment578 = frozenset([9, 19, 20])
    FOLLOW_TRUE_in_general_attribute_assignment612 = frozenset([1])
    FOLLOW_FALSE_in_general_attribute_assignment616 = frozenset([1])
    FOLLOW_OPAREN_in_general_attribute_assignment639 = frozenset([14, 23])
    FOLLOW_scinot_number_in_general_attribute_assignment641 = frozenset([21])
    FOLLOW_COMMA_in_general_attribute_assignment665 = frozenset([22])
    FOLLOW_BOTH_in_general_attribute_assignment667 = frozenset([12])
    FOLLOW_CPAREN_in_general_attribute_assignment669 = frozenset([1])
    FOLLOW_DIGIT_in_number713 = frozenset([1, 23])
    FOLLOW_CONSTANT_in_constant737 = frozenset([29, 30])
    FOLLOW_identifier_in_constant741 = frozenset([10])
    FOLLOW_COLON_in_constant745 = frozenset([29, 30])
    FOLLOW_identifier_in_constant747 = frozenset([10])
    FOLLOW_COLON_in_constant758 = frozenset([11])
    FOLLOW_EQUAL_in_constant760 = frozenset([37])
    FOLLOW_string_in_constant764 = frozenset([1])
    FOLLOW_PORT_in_port_list797 = frozenset([9])
    FOLLOW_OPAREN_in_port_list799 = frozenset([29, 30])
    FOLLOW_port_def_in_port_list813 = frozenset([6])
    FOLLOW_SCOLON_in_port_list817 = frozenset([29, 30])
    FOLLOW_port_def_in_port_list833 = frozenset([12])
    FOLLOW_CPAREN_in_port_list846 = frozenset([1])
    FOLLOW_identifier_in_port_def874 = frozenset([21])
    FOLLOW_COMMA_in_port_def878 = frozenset([29, 30])
    FOLLOW_identifier_in_port_def892 = frozenset([10])
    FOLLOW_COLON_in_port_def896 = frozenset([31, 32, 33, 34, 35, 36])
    FOLLOW_portmode_in_port_def898 = frozenset([26, 27])
    FOLLOW_BIT_in_port_def911 = frozenset([1])
    FOLLOW_BIT_VECTOR_in_port_def923 = frozenset([9])
    FOLLOW_OPAREN_in_port_def925 = frozenset([23])
    FOLLOW_DIGIT_in_port_def927 = frozenset([23, 28])
    FOLLOW_TO_in_port_def930 = frozenset([23])
    FOLLOW_DIGIT_in_port_def932 = frozenset([12, 23])
    FOLLOW_CPAREN_in_port_def935 = frozenset([1])
    FOLLOW_set_in_identifier952 = frozenset([1, 23, 29, 30, 41])
    FOLLOW_set_in_identifier958 = frozenset([1, 23, 29, 30, 41])
    FOLLOW_USCORE_in_identifier968 = frozenset([23, 29, 30])
    FOLLOW_set_in_identifier970 = frozenset([1, 23, 29, 30, 41])
    FOLLOW_set_in_portmode0 = frozenset([1])
    FOLLOW_STRING_in_string1039 = frozenset([38])
    FOLLOW_ANDSIGN_in_string1041 = frozenset([37])
    FOLLOW_STRING_in_string1058 = frozenset([1])
    FOLLOW_DIGIT_in_scinot_number1087 = frozenset([14, 23])
    FOLLOW_DOT_in_scinot_number1090 = frozenset([23, 123])
    FOLLOW_DIGIT_in_scinot_number1092 = frozenset([23, 123])
    FOLLOW_123_in_scinot_number1095 = frozenset([1, 23, 124])
    FOLLOW_124_in_scinot_number1097 = frozenset([1, 23])
    FOLLOW_DIGIT_in_scinot_number1100 = frozenset([1, 23])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("bsdlLexer", bsdlParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
