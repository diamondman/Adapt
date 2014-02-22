# $ANTLR 3.1 jed.g 2014-02-17 18:49:15

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
import os
import sys
from bitarray import bitarray



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
F=9
STAR=19
OTHER=5
C=18
L=11
N=12
J=10
V=15
ONE=7
Q=14
P=13
EOF=-1
ETX=21
X=16
ZERO=6
DIG01=8
WS=17
STX=20
NL=4

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "NL", "OTHER", "ZERO", "ONE", "DIG01", "F", "J", "L", "N", "P", "Q", 
    "V", "X", "WS", "C", "STAR", "STX", "ETX"
]




class jedParser(Parser):
    grammarFileName = "jed.g"
    antlr_version = version_str_to_tuple("3.1")
    antlr_version_str = "3.1"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)


        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )



              
        self._fuse_count = 0
        self._fuses = bitarray()
        self._fuse_default = False
        self._pin_count = 0




                


        

             




    # $ANTLR start "eval"
    # jed.g:26:1: eval returns [value] : ( otherstar | NL )* ( entity ) ( otherstar | NL )* EOF ;
    def eval(self, ):

        value = None

        entity1 = None


        try:
            try:
                # jed.g:27:5: ( ( otherstar | NL )* ( entity ) ( otherstar | NL )* EOF )
                # jed.g:27:7: ( otherstar | NL )* ( entity ) ( otherstar | NL )* EOF
                pass 
                # jed.g:27:7: ( otherstar | NL )*
                while True: #loop1
                    alt1 = 3
                    LA1_0 = self.input.LA(1)

                    if ((OTHER <= LA1_0 <= STAR)) :
                        alt1 = 1
                    elif (LA1_0 == NL) :
                        alt1 = 2


                    if alt1 == 1:
                        # jed.g:27:8: otherstar
                        pass 
                        self._state.following.append(self.FOLLOW_otherstar_in_eval61)
                        self.otherstar()

                        self._state.following.pop()


                    elif alt1 == 2:
                        # jed.g:27:18: NL
                        pass 
                        self.match(self.input, NL, self.FOLLOW_NL_in_eval63)


                    else:
                        break #loop1


                # jed.g:28:9: ( entity )
                # jed.g:28:10: entity
                pass 
                self._state.following.append(self.FOLLOW_entity_in_eval76)
                entity1 = self.entity()

                self._state.following.pop()
                #action start
                value = entity1
                #action end



                # jed.g:29:9: ( otherstar | NL )*
                while True: #loop2
                    alt2 = 3
                    LA2_0 = self.input.LA(1)

                    if ((OTHER <= LA2_0 <= STAR)) :
                        alt2 = 1
                    elif (LA2_0 == NL) :
                        alt2 = 2


                    if alt2 == 1:
                        # jed.g:29:10: otherstar
                        pass 
                        self._state.following.append(self.FOLLOW_otherstar_in_eval90)
                        self.otherstar()

                        self._state.following.pop()


                    elif alt2 == 2:
                        # jed.g:29:20: NL
                        pass 
                        self.match(self.input, NL, self.FOLLOW_NL_in_eval92)


                    else:
                        break #loop2


                self.match(self.input, EOF, self.FOLLOW_EOF_in_eval104)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "eval"


    # $ANTLR start "other"
    # jed.g:32:1: other : ( OTHER | ZERO | ONE | DIG01 | F | J | L | N | P | Q | V | X | WS | C ) ;
    def other(self, ):

        try:
            try:
                # jed.g:33:5: ( ( OTHER | ZERO | ONE | DIG01 | F | J | L | N | P | Q | V | X | WS | C ) )
                # jed.g:33:7: ( OTHER | ZERO | ONE | DIG01 | F | J | L | N | P | Q | V | X | WS | C )
                pass 
                if (OTHER <= self.input.LA(1) <= C):
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

        return 

    # $ANTLR end "other"


    # $ANTLR start "otherstar"
    # jed.g:36:1: otherstar : ( other | STAR ) ;
    def otherstar(self, ):

        try:
            try:
                # jed.g:37:5: ( ( other | STAR ) )
                # jed.g:37:7: ( other | STAR )
                pass 
                # jed.g:37:7: ( other | STAR )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((OTHER <= LA3_0 <= C)) :
                    alt3 = 1
                elif (LA3_0 == STAR) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # jed.g:37:8: other
                    pass 
                    self._state.following.append(self.FOLLOW_other_in_otherstar162)
                    self.other()

                    self._state.following.pop()


                elif alt3 == 2:
                    # jed.g:37:14: STAR
                    pass 
                    self.match(self.input, STAR, self.FOLLOW_STAR_in_otherstar164)







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "otherstar"

    class string_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "string"
    # jed.g:40:1: string : ( other )+ ;
    def string(self, ):

        retval = self.string_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # jed.g:41:5: ( ( other )+ )
                # jed.g:41:7: ( other )+
                pass 
                # jed.g:41:7: ( other )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((OTHER <= LA4_0 <= C)) :
                        alt4 = 1


                    if alt4 == 1:
                        # jed.g:41:7: other
                        pass 
                        self._state.following.append(self.FOLLOW_other_in_string183)
                        self.other()

                        self._state.following.pop()


                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1





                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "string"


    # $ANTLR start "entity"
    # jed.g:44:1: entity returns [value] : STX lines ETX ;
    def entity(self, ):

        value = None

        lines2 = None


        try:
            try:
                # jed.g:45:5: ( STX lines ETX )
                # jed.g:45:7: STX lines ETX
                pass 
                self.match(self.input, STX, self.FOLLOW_STX_in_entity205)
                self._state.following.append(self.FOLLOW_lines_in_entity207)
                lines2 = self.lines()

                self._state.following.pop()
                self.match(self.input, ETX, self.FOLLOW_ETX_in_entity209)
                #action start
                value=lines2
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "entity"


    # $ANTLR start "lines"
    # jed.g:48:1: lines returns [value] : ( fuse_count | pin_count | default_fuse | default_test | test_vec_max | fuses | note | dev_id | checksum )+ ;
    def lines(self, ):

        value = None

        fuse_count3 = None

        pin_count4 = None

        checksum5 = None


        try:
            try:
                # jed.g:49:5: ( ( fuse_count | pin_count | default_fuse | default_test | test_vec_max | fuses | note | dev_id | checksum )+ )
                # jed.g:49:7: ( fuse_count | pin_count | default_fuse | default_test | test_vec_max | fuses | note | dev_id | checksum )+
                pass 
                # jed.g:49:7: ( fuse_count | pin_count | default_fuse | default_test | test_vec_max | fuses | note | dev_id | checksum )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 10
                    alt5 = self.dfa5.predict(self.input)
                    if alt5 == 1:
                        # jed.g:49:10: fuse_count
                        pass 
                        self._state.following.append(self.FOLLOW_fuse_count_in_lines235)
                        fuse_count3 = self.fuse_count()

                        self._state.following.pop()
                        #action start
                        self._fuse_count = fuse_count3
                        #action end


                    elif alt5 == 2:
                        # jed.g:50:10: pin_count
                        pass 
                        self._state.following.append(self.FOLLOW_pin_count_in_lines252)
                        pin_count4 = self.pin_count()

                        self._state.following.pop()
                        #action start
                        self._pin_count = pin_count4
                        #action end


                    elif alt5 == 3:
                        # jed.g:51:10: default_fuse
                        pass 
                        self._state.following.append(self.FOLLOW_default_fuse_in_lines270)
                        self.default_fuse()

                        self._state.following.pop()


                    elif alt5 == 4:
                        # jed.g:52:10: default_test
                        pass 
                        self._state.following.append(self.FOLLOW_default_test_in_lines281)
                        self.default_test()

                        self._state.following.pop()


                    elif alt5 == 5:
                        # jed.g:53:10: test_vec_max
                        pass 
                        self._state.following.append(self.FOLLOW_test_vec_max_in_lines292)
                        self.test_vec_max()

                        self._state.following.pop()


                    elif alt5 == 6:
                        # jed.g:54:10: fuses
                        pass 
                        self._state.following.append(self.FOLLOW_fuses_in_lines303)
                        self.fuses()

                        self._state.following.pop()


                    elif alt5 == 7:
                        # jed.g:55:10: note
                        pass 
                        self._state.following.append(self.FOLLOW_note_in_lines314)
                        self.note()

                        self._state.following.pop()


                    elif alt5 == 8:
                        # jed.g:56:10: dev_id
                        pass 
                        self._state.following.append(self.FOLLOW_dev_id_in_lines325)
                        self.dev_id()

                        self._state.following.pop()


                    elif alt5 == 9:
                        # jed.g:57:10: checksum
                        pass 
                        self._state.following.append(self.FOLLOW_checksum_in_lines336)
                        checksum5 = self.checksum()

                        self._state.following.pop()
                        #action start
                        self._checksum = checksum5
                        #action end


                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1


                #action start
                       
                addr_diff = self._fuse_count-len(self._fuses)
                if addr_diff < 0:
                    raise Exception("JEDEC File has more bits than the F field specifies. Actual: %s; F: %s."%\
                                    (len(self._fuses), self._fuse_count))
                if addr_diff:
                    buff = bitarray(addr_diff)
                    buff.setall(self._fuse_default)
                    self._fuses += buff
                value = {'fuses': self._fuses, 
                          'checksum': self._checksum, 
                          'fusecount': self._fuse_count,
                          'pincount': self._pin_count}
                      
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "lines"

    class fuses_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.address = None
            self.length = None




    # $ANTLR start "fuses"
    # jed.g:74:1: fuses returns [address, length] : L digits ( WS )+ bit_field STAR NL ;
    def fuses(self, ):

        retval = self.fuses_return()
        retval.start = self.input.LT(1)

        digits6 = None

        bit_field7 = None


        try:
            try:
                # jed.g:75:5: ( L digits ( WS )+ bit_field STAR NL )
                # jed.g:75:7: L digits ( WS )+ bit_field STAR NL
                pass 
                self.match(self.input, L, self.FOLLOW_L_in_fuses382)
                self._state.following.append(self.FOLLOW_digits_in_fuses384)
                digits6 = self.digits()

                self._state.following.pop()
                # jed.g:75:16: ( WS )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == WS) :
                        alt6 = 1


                    if alt6 == 1:
                        # jed.g:75:16: WS
                        pass 
                        self.match(self.input, WS, self.FOLLOW_WS_in_fuses386)


                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                self._state.following.append(self.FOLLOW_bit_field_in_fuses389)
                bit_field7 = self.bit_field()

                self._state.following.pop()
                self.match(self.input, STAR, self.FOLLOW_STAR_in_fuses391)
                self.match(self.input, NL, self.FOLLOW_NL_in_fuses393)
                #action start
                retval.address=((digits6 is not None) and [digits6.value] or [None])[0]
                #action end
                #action start
                retval.length=len(((bit_field7 is not None) and [self.input.toString(bit_field7.start,bit_field7.stop)] or [None])[0])
                #action end
                #action start
                         
                addr_diff = retval.address-len(self._fuses)
                if addr_diff<0:
                    raise Exception("JED FILE CAN NOT HAVE OUT OF ORDER ADDRESSES!")
                if addr_diff:
                    buff = bitarray(addr_diff)
                    buff.setall(self._fuse_default)
                    self._fuses += buff
                self._fuses += ((bit_field7 is not None) and [bit_field7.value] or [None])[0]
                        
                #action end



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "fuses"

    class bit_field_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.value = None




    # $ANTLR start "bit_field"
    # jed.g:88:1: bit_field returns [value] : ( ZERO | ONE )+ ;
    def bit_field(self, ):

        retval = self.bit_field_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # jed.g:89:5: ( ( ZERO | ONE )+ )
                # jed.g:89:7: ( ZERO | ONE )+
                pass 
                # jed.g:89:7: ( ZERO | ONE )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((ZERO <= LA7_0 <= ONE)) :
                        alt7 = 1


                    if alt7 == 1:
                        # jed.g:
                        pass 
                        if (ZERO <= self.input.LA(1) <= ONE):
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1


                #action start
                retval.value=bitarray(str(self.input.toString(retval.start, self.input.LT(-1))))
                #action end



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "bit_field"


    # $ANTLR start "note"
    # jed.g:92:1: note returns [value] : N string STAR NL ;
    def note(self, ):

        value = None

        string8 = None


        try:
            try:
                # jed.g:93:5: ( N string STAR NL )
                # jed.g:93:7: N string STAR NL
                pass 
                self.match(self.input, N, self.FOLLOW_N_in_note455)
                self._state.following.append(self.FOLLOW_string_in_note457)
                string8 = self.string()

                self._state.following.pop()
                self.match(self.input, STAR, self.FOLLOW_STAR_in_note459)
                self.match(self.input, NL, self.FOLLOW_NL_in_note461)
                #action start
                value=((string8 is not None) and [self.input.toString(string8.start,string8.stop)] or [None])[0]
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "note"


    # $ANTLR start "checksum"
    # jed.g:97:1: checksum returns [value] : C string STAR NL ;
    def checksum(self, ):

        value = None

        string9 = None


        try:
            try:
                # jed.g:98:5: ( C string STAR NL )
                # jed.g:98:7: C string STAR NL
                pass 
                self.match(self.input, C, self.FOLLOW_C_in_checksum492)
                self._state.following.append(self.FOLLOW_string_in_checksum494)
                string9 = self.string()

                self._state.following.pop()
                self.match(self.input, STAR, self.FOLLOW_STAR_in_checksum496)
                self.match(self.input, NL, self.FOLLOW_NL_in_checksum498)
                #action start
                value=((string9 is not None) and [self.input.toString(string9.start,string9.stop)] or [None])[0]
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "checksum"


    # $ANTLR start "dev_id"
    # jed.g:102:1: dev_id returns [value] : J string STAR NL ;
    def dev_id(self, ):

        value = None

        string10 = None


        try:
            try:
                # jed.g:103:5: ( J string STAR NL )
                # jed.g:103:7: J string STAR NL
                pass 
                self.match(self.input, J, self.FOLLOW_J_in_dev_id529)
                self._state.following.append(self.FOLLOW_string_in_dev_id531)
                string10 = self.string()

                self._state.following.pop()
                self.match(self.input, STAR, self.FOLLOW_STAR_in_dev_id533)
                self.match(self.input, NL, self.FOLLOW_NL_in_dev_id535)
                #action start
                value=((string10 is not None) and [self.input.toString(string10.start,string10.stop)] or [None])[0]
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "dev_id"


    # $ANTLR start "fuse_count"
    # jed.g:107:1: fuse_count returns [value] : Q F digits STAR NL ;
    def fuse_count(self, ):

        value = None

        digits11 = None


        try:
            try:
                # jed.g:108:5: ( Q F digits STAR NL )
                # jed.g:108:7: Q F digits STAR NL
                pass 
                self.match(self.input, Q, self.FOLLOW_Q_in_fuse_count567)
                self.match(self.input, F, self.FOLLOW_F_in_fuse_count569)
                self._state.following.append(self.FOLLOW_digits_in_fuse_count571)
                digits11 = self.digits()

                self._state.following.pop()
                self.match(self.input, STAR, self.FOLLOW_STAR_in_fuse_count573)
                self.match(self.input, NL, self.FOLLOW_NL_in_fuse_count575)
                #action start
                value=((digits11 is not None) and [digits11.value] or [None])[0]
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "fuse_count"


    # $ANTLR start "pin_count"
    # jed.g:111:1: pin_count returns [value] : Q P digits STAR NL ;
    def pin_count(self, ):

        value = None

        digits12 = None


        try:
            try:
                # jed.g:112:5: ( Q P digits STAR NL )
                # jed.g:112:7: Q P digits STAR NL
                pass 
                self.match(self.input, Q, self.FOLLOW_Q_in_pin_count598)
                self.match(self.input, P, self.FOLLOW_P_in_pin_count600)
                self._state.following.append(self.FOLLOW_digits_in_pin_count602)
                digits12 = self.digits()

                self._state.following.pop()
                self.match(self.input, STAR, self.FOLLOW_STAR_in_pin_count604)
                self.match(self.input, NL, self.FOLLOW_NL_in_pin_count606)
                #action start
                value=((digits12 is not None) and [digits12.value] or [None])[0]
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "pin_count"


    # $ANTLR start "default_fuse"
    # jed.g:115:1: default_fuse returns [value] : F bool STAR NL ;
    def default_fuse(self, ):

        value = None

        bool13 = None


        try:
            try:
                # jed.g:116:5: ( F bool STAR NL )
                # jed.g:116:7: F bool STAR NL
                pass 
                self.match(self.input, F, self.FOLLOW_F_in_default_fuse629)
                self._state.following.append(self.FOLLOW_bool_in_default_fuse631)
                bool13 = self.bool()

                self._state.following.pop()
                self.match(self.input, STAR, self.FOLLOW_STAR_in_default_fuse633)
                self.match(self.input, NL, self.FOLLOW_NL_in_default_fuse635)
                #action start
                value=bool13
                #action end
                #action start
                self._fuse_default=bool13
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "default_fuse"


    # $ANTLR start "default_test"
    # jed.g:120:1: default_test returns [value] : X bool STAR NL ;
    def default_test(self, ):

        value = None

        bool14 = None


        try:
            try:
                # jed.g:121:5: ( X bool STAR NL )
                # jed.g:121:7: X bool STAR NL
                pass 
                self.match(self.input, X, self.FOLLOW_X_in_default_test668)
                self._state.following.append(self.FOLLOW_bool_in_default_test670)
                bool14 = self.bool()

                self._state.following.pop()
                self.match(self.input, STAR, self.FOLLOW_STAR_in_default_test672)
                self.match(self.input, NL, self.FOLLOW_NL_in_default_test674)
                #action start
                value=bool14
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "default_test"


    # $ANTLR start "test_vec_max"
    # jed.g:124:1: test_vec_max returns [value] : Q V bool STAR NL ;
    def test_vec_max(self, ):

        value = None

        bool15 = None


        try:
            try:
                # jed.g:125:5: ( Q V bool STAR NL )
                # jed.g:125:7: Q V bool STAR NL
                pass 
                self.match(self.input, Q, self.FOLLOW_Q_in_test_vec_max697)
                self.match(self.input, V, self.FOLLOW_V_in_test_vec_max699)
                self._state.following.append(self.FOLLOW_bool_in_test_vec_max701)
                bool15 = self.bool()

                self._state.following.pop()
                self.match(self.input, STAR, self.FOLLOW_STAR_in_test_vec_max703)
                self.match(self.input, NL, self.FOLLOW_NL_in_test_vec_max705)
                #action start
                value=bool15
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "test_vec_max"


    # $ANTLR start "bool"
    # jed.g:128:1: bool returns [value] : ( ZERO | ONE ) ;
    def bool(self, ):

        value = None

        try:
            try:
                # jed.g:129:5: ( ( ZERO | ONE ) )
                # jed.g:129:7: ( ZERO | ONE )
                pass 
                # jed.g:129:7: ( ZERO | ONE )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == ZERO) :
                    alt8 = 1
                elif (LA8_0 == ONE) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # jed.g:129:8: ZERO
                    pass 
                    self.match(self.input, ZERO, self.FOLLOW_ZERO_in_bool729)
                    #action start
                    value=False
                    #action end


                elif alt8 == 2:
                    # jed.g:129:28: ONE
                    pass 
                    self.match(self.input, ONE, self.FOLLOW_ONE_in_bool733)
                    #action start
                    value=True
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "bool"

    class digits_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.value = None




    # $ANTLR start "digits"
    # jed.g:132:1: digits returns [value] : ( digit )+ ;
    def digits(self, ):

        retval = self.digits_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # jed.g:133:5: ( ( digit )+ )
                # jed.g:133:7: ( digit )+
                pass 
                # jed.g:133:7: ( digit )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((ZERO <= LA9_0 <= DIG01)) :
                        alt9 = 1


                    if alt9 == 1:
                        # jed.g:133:7: digit
                        pass 
                        self._state.following.append(self.FOLLOW_digit_in_digits757)
                        self.digit()

                        self._state.following.pop()


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1


                #action start
                retval.value = int(self.input.toString(retval.start, self.input.LT(-1)))
                #action end



                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "digits"


    # $ANTLR start "digit"
    # jed.g:136:1: digit : ( ZERO | ONE | DIG01 );
    def digit(self, ):

        try:
            try:
                # jed.g:137:5: ( ZERO | ONE | DIG01 )
                # jed.g:
                pass 
                if (ZERO <= self.input.LA(1) <= DIG01):
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

        return 

    # $ANTLR end "digit"


    # Delegated rules


    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\11\1\uffff\1\11\11\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\25\1\uffff\1\17\11\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\1\uffff\1\12\1\uffff\1\3\1\4\1\6\1\7\1\10\1\11\1\1\1\2\1\5"
        )

    DFA5_special = DFA.unpack(
        u"\14\uffff"
        )

            
    DFA5_transition = [
        DFA.unpack(u"\1\3\1\7\1\5\1\6\1\uffff\1\2\1\uffff\1\4\1\uffff\1\10"
        u"\2\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11\3\uffff\1\12\1\uffff\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    DFA5 = DFA
 

    FOLLOW_otherstar_in_eval61 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    FOLLOW_NL_in_eval63 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    FOLLOW_entity_in_eval76 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    FOLLOW_otherstar_in_eval90 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    FOLLOW_NL_in_eval92 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    FOLLOW_EOF_in_eval104 = frozenset([1])
    FOLLOW_set_in_other116 = frozenset([1])
    FOLLOW_other_in_otherstar162 = frozenset([1])
    FOLLOW_STAR_in_otherstar164 = frozenset([1])
    FOLLOW_other_in_string183 = frozenset([1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    FOLLOW_STX_in_entity205 = frozenset([9, 10, 11, 12, 14, 16, 18])
    FOLLOW_lines_in_entity207 = frozenset([21])
    FOLLOW_ETX_in_entity209 = frozenset([1])
    FOLLOW_fuse_count_in_lines235 = frozenset([1, 9, 10, 11, 12, 14, 16, 18])
    FOLLOW_pin_count_in_lines252 = frozenset([1, 9, 10, 11, 12, 14, 16, 18])
    FOLLOW_default_fuse_in_lines270 = frozenset([1, 9, 10, 11, 12, 14, 16, 18])
    FOLLOW_default_test_in_lines281 = frozenset([1, 9, 10, 11, 12, 14, 16, 18])
    FOLLOW_test_vec_max_in_lines292 = frozenset([1, 9, 10, 11, 12, 14, 16, 18])
    FOLLOW_fuses_in_lines303 = frozenset([1, 9, 10, 11, 12, 14, 16, 18])
    FOLLOW_note_in_lines314 = frozenset([1, 9, 10, 11, 12, 14, 16, 18])
    FOLLOW_dev_id_in_lines325 = frozenset([1, 9, 10, 11, 12, 14, 16, 18])
    FOLLOW_checksum_in_lines336 = frozenset([1, 9, 10, 11, 12, 14, 16, 18])
    FOLLOW_L_in_fuses382 = frozenset([6, 7, 8])
    FOLLOW_digits_in_fuses384 = frozenset([17])
    FOLLOW_WS_in_fuses386 = frozenset([6, 7, 17])
    FOLLOW_bit_field_in_fuses389 = frozenset([19])
    FOLLOW_STAR_in_fuses391 = frozenset([4])
    FOLLOW_NL_in_fuses393 = frozenset([1])
    FOLLOW_set_in_bit_field427 = frozenset([1, 6, 7])
    FOLLOW_N_in_note455 = frozenset([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    FOLLOW_string_in_note457 = frozenset([19])
    FOLLOW_STAR_in_note459 = frozenset([4])
    FOLLOW_NL_in_note461 = frozenset([1])
    FOLLOW_C_in_checksum492 = frozenset([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    FOLLOW_string_in_checksum494 = frozenset([19])
    FOLLOW_STAR_in_checksum496 = frozenset([4])
    FOLLOW_NL_in_checksum498 = frozenset([1])
    FOLLOW_J_in_dev_id529 = frozenset([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    FOLLOW_string_in_dev_id531 = frozenset([19])
    FOLLOW_STAR_in_dev_id533 = frozenset([4])
    FOLLOW_NL_in_dev_id535 = frozenset([1])
    FOLLOW_Q_in_fuse_count567 = frozenset([9])
    FOLLOW_F_in_fuse_count569 = frozenset([6, 7, 8])
    FOLLOW_digits_in_fuse_count571 = frozenset([19])
    FOLLOW_STAR_in_fuse_count573 = frozenset([4])
    FOLLOW_NL_in_fuse_count575 = frozenset([1])
    FOLLOW_Q_in_pin_count598 = frozenset([13])
    FOLLOW_P_in_pin_count600 = frozenset([6, 7, 8])
    FOLLOW_digits_in_pin_count602 = frozenset([19])
    FOLLOW_STAR_in_pin_count604 = frozenset([4])
    FOLLOW_NL_in_pin_count606 = frozenset([1])
    FOLLOW_F_in_default_fuse629 = frozenset([6, 7])
    FOLLOW_bool_in_default_fuse631 = frozenset([19])
    FOLLOW_STAR_in_default_fuse633 = frozenset([4])
    FOLLOW_NL_in_default_fuse635 = frozenset([1])
    FOLLOW_X_in_default_test668 = frozenset([6, 7])
    FOLLOW_bool_in_default_test670 = frozenset([19])
    FOLLOW_STAR_in_default_test672 = frozenset([4])
    FOLLOW_NL_in_default_test674 = frozenset([1])
    FOLLOW_Q_in_test_vec_max697 = frozenset([15])
    FOLLOW_V_in_test_vec_max699 = frozenset([6, 7])
    FOLLOW_bool_in_test_vec_max701 = frozenset([19])
    FOLLOW_STAR_in_test_vec_max703 = frozenset([4])
    FOLLOW_NL_in_test_vec_max705 = frozenset([1])
    FOLLOW_ZERO_in_bool729 = frozenset([1])
    FOLLOW_ONE_in_bool733 = frozenset([1])
    FOLLOW_digit_in_digits757 = frozenset([1, 6, 7, 8])
    FOLLOW_set_in_digit0 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("jedLexer", jedParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
