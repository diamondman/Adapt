# $ANTLR 3.1 jed.g 2014-02-17 18:49:15

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class jedLexer(Lexer):

    grammarFileName = "jed.g"
    antlr_version = version_str_to_tuple("3.1")
    antlr_version_str = "3.1"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa2 = self.DFA2(
            self, 2,
            eot = self.DFA2_eot,
            eof = self.DFA2_eof,
            min = self.DFA2_min,
            max = self.DFA2_max,
            accept = self.DFA2_accept,
            special = self.DFA2_special,
            transition = self.DFA2_transition
            )






    # $ANTLR start "STX"
    def mSTX(self, ):

        try:
            _type = STX
            _channel = DEFAULT_CHANNEL

            # jed.g:140:8: ( '\\u0002' )
            # jed.g:140:10: '\\u0002'
            pass 
            self.match(2)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STX"



    # $ANTLR start "ETX"
    def mETX(self, ):

        try:
            _type = ETX
            _channel = DEFAULT_CHANNEL

            # jed.g:141:8: ( '\\u0003' )
            # jed.g:141:10: '\\u0003'
            pass 
            self.match(3)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ETX"



    # $ANTLR start "NL"
    def mNL(self, ):

        try:
            _type = NL
            _channel = DEFAULT_CHANNEL

            # jed.g:142:8: ( ( '\\r' | '\\n' )+ )
            # jed.g:142:10: ( '\\r' | '\\n' )+
            pass 
            # jed.g:142:10: ( '\\r' | '\\n' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 10 or LA1_0 == 13) :
                    alt1 = 1


                if alt1 == 1:
                    # jed.g:
                    pass 
                    if self.input.LA(1) == 10 or self.input.LA(1) == 13:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NL"



    # $ANTLR start "C"
    def mC(self, ):

        try:
            _type = C
            _channel = DEFAULT_CHANNEL

            # jed.g:143:8: ( 'C' )
            # jed.g:143:10: 'C'
            pass 
            self.match(67)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "C"



    # $ANTLR start "F"
    def mF(self, ):

        try:
            _type = F
            _channel = DEFAULT_CHANNEL

            # jed.g:144:8: ( 'F' )
            # jed.g:144:10: 'F'
            pass 
            self.match(70)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "F"



    # $ANTLR start "J"
    def mJ(self, ):

        try:
            _type = J
            _channel = DEFAULT_CHANNEL

            # jed.g:145:8: ( 'J' )
            # jed.g:145:10: 'J'
            pass 
            self.match(74)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "J"



    # $ANTLR start "L"
    def mL(self, ):

        try:
            _type = L
            _channel = DEFAULT_CHANNEL

            # jed.g:146:8: ( 'L' )
            # jed.g:146:10: 'L'
            pass 
            self.match(76)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "L"



    # $ANTLR start "N"
    def mN(self, ):

        try:
            _type = N
            _channel = DEFAULT_CHANNEL

            # jed.g:147:8: ( 'N' )
            # jed.g:147:10: 'N'
            pass 
            self.match(78)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "N"



    # $ANTLR start "P"
    def mP(self, ):

        try:
            _type = P
            _channel = DEFAULT_CHANNEL

            # jed.g:148:8: ( 'P' )
            # jed.g:148:10: 'P'
            pass 
            self.match(80)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "P"



    # $ANTLR start "Q"
    def mQ(self, ):

        try:
            _type = Q
            _channel = DEFAULT_CHANNEL

            # jed.g:149:8: ( 'Q' )
            # jed.g:149:10: 'Q'
            pass 
            self.match(81)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Q"



    # $ANTLR start "V"
    def mV(self, ):

        try:
            _type = V
            _channel = DEFAULT_CHANNEL

            # jed.g:150:8: ( 'V' )
            # jed.g:150:10: 'V'
            pass 
            self.match(86)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "V"



    # $ANTLR start "X"
    def mX(self, ):

        try:
            _type = X
            _channel = DEFAULT_CHANNEL

            # jed.g:151:8: ( 'X' )
            # jed.g:151:10: 'X'
            pass 
            self.match(88)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "X"



    # $ANTLR start "ONE"
    def mONE(self, ):

        try:
            _type = ONE
            _channel = DEFAULT_CHANNEL

            # jed.g:153:8: ( '1' )
            # jed.g:153:10: '1'
            pass 
            self.match(49)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ONE"



    # $ANTLR start "ZERO"
    def mZERO(self, ):

        try:
            _type = ZERO
            _channel = DEFAULT_CHANNEL

            # jed.g:154:8: ( '0' )
            # jed.g:154:10: '0'
            pass 
            self.match(48)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ZERO"



    # $ANTLR start "DIG01"
    def mDIG01(self, ):

        try:
            _type = DIG01
            _channel = DEFAULT_CHANNEL

            # jed.g:155:8: ( '2' .. '9' )
            # jed.g:155:10: '2' .. '9'
            pass 
            self.matchRange(50, 57)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIG01"



    # $ANTLR start "STAR"
    def mSTAR(self, ):

        try:
            _type = STAR
            _channel = DEFAULT_CHANNEL

            # jed.g:156:8: ( '*' )
            # jed.g:156:10: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STAR"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # jed.g:157:8: ( ' ' | '\\t' )
            # jed.g:
            pass 
            if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "OTHER"
    def mOTHER(self, ):

        try:
            _type = OTHER
            _channel = DEFAULT_CHANNEL

            # jed.g:159:7: (~ ( '\\u0002' | '\\u0003' ) )
            # jed.g:159:9: ~ ( '\\u0002' | '\\u0003' )
            pass 
            if (0 <= self.input.LA(1) <= 1) or (4 <= self.input.LA(1) <= 65534):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OTHER"



    def mTokens(self):
        # jed.g:1:8: ( STX | ETX | NL | C | F | J | L | N | P | Q | V | X | ONE | ZERO | DIG01 | STAR | WS | OTHER )
        alt2 = 18
        alt2 = self.dfa2.predict(self.input)
        if alt2 == 1:
            # jed.g:1:10: STX
            pass 
            self.mSTX()


        elif alt2 == 2:
            # jed.g:1:14: ETX
            pass 
            self.mETX()


        elif alt2 == 3:
            # jed.g:1:18: NL
            pass 
            self.mNL()


        elif alt2 == 4:
            # jed.g:1:21: C
            pass 
            self.mC()


        elif alt2 == 5:
            # jed.g:1:23: F
            pass 
            self.mF()


        elif alt2 == 6:
            # jed.g:1:25: J
            pass 
            self.mJ()


        elif alt2 == 7:
            # jed.g:1:27: L
            pass 
            self.mL()


        elif alt2 == 8:
            # jed.g:1:29: N
            pass 
            self.mN()


        elif alt2 == 9:
            # jed.g:1:31: P
            pass 
            self.mP()


        elif alt2 == 10:
            # jed.g:1:33: Q
            pass 
            self.mQ()


        elif alt2 == 11:
            # jed.g:1:35: V
            pass 
            self.mV()


        elif alt2 == 12:
            # jed.g:1:37: X
            pass 
            self.mX()


        elif alt2 == 13:
            # jed.g:1:39: ONE
            pass 
            self.mONE()


        elif alt2 == 14:
            # jed.g:1:43: ZERO
            pass 
            self.mZERO()


        elif alt2 == 15:
            # jed.g:1:48: DIG01
            pass 
            self.mDIG01()


        elif alt2 == 16:
            # jed.g:1:54: STAR
            pass 
            self.mSTAR()


        elif alt2 == 17:
            # jed.g:1:59: WS
            pass 
            self.mWS()


        elif alt2 == 18:
            # jed.g:1:62: OTHER
            pass 
            self.mOTHER()







    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\42\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\42\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\0\41\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\ufffe\41\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1\14\1"
        u"\15\1\16\1\17\1\20\1\21\1\22\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12"
        u"\1\13\1\14\1\15\1\16\1\17\1\20\1\21"
        )

    DFA2_special = DFA.unpack(
        u"\42\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\2\22\1\1\1\2\5\22\1\21\1\3\2\22\1\3\22\22\1\21\11\22"
        u"\1\20\5\22\1\16\1\15\10\17\11\22\1\4\2\22\1\5\3\22\1\6\1\22\1\7"
        u"\1\22\1\10\1\22\1\11\1\12\4\22\1\13\1\22\1\14\uffa6\22"),
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

    # class definition for DFA #2

    DFA2 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(jedLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
