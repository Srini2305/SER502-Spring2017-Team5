# Author: Generated from DevilsCode.g4 by ANTLR 4.7
# Date: April 25, 2017
# Version: 3
# Purpose: To carry out Lexical analysis of the code

# Generated from DevilsCode.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u0081\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21f\n\21\3\22\3\22\7\22j\n\22\f\22\16")
        buf.write("\22m\13\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24y\n\24\3\25\6\25|\n\25\r\25\16\25}\3\25\3\25")
        buf.write("\2\2\26\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26\3\2")
        buf.write("\6\3\2c|\5\2\62;C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2\u0087")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5\61\3\2\2")
        buf.write("\2\7\63\3\2\2\2\t\65\3\2\2\2\13\67\3\2\2\2\r9\3\2\2\2")
        buf.write("\17;\3\2\2\2\21B\3\2\2\2\23D\3\2\2\2\25F\3\2\2\2\27H\3")
        buf.write("\2\2\2\31J\3\2\2\2\33L\3\2\2\2\35S\3\2\2\2\37W\3\2\2\2")
        buf.write("!e\3\2\2\2#g\3\2\2\2%n\3\2\2\2\'x\3\2\2\2){\3\2\2\2+,")
        buf.write("\7o\2\2,-\7c\2\2-.\7k\2\2./\7p\2\2/\60\7\"\2\2\60\4\3")
        buf.write("\2\2\2\61\62\7*\2\2\62\6\3\2\2\2\63\64\7+\2\2\64\b\3\2")
        buf.write("\2\2\65\66\7}\2\2\66\n\3\2\2\2\678\7\177\2\28\f\3\2\2")
        buf.write("\29:\7=\2\2:\16\3\2\2\2;<\7r\2\2<=\7t\2\2=>\7k\2\2>?\7")
        buf.write("p\2\2?@\7v\2\2@A\7\"\2\2A\20\3\2\2\2BC\7?\2\2C\22\3\2")
        buf.write("\2\2DE\7-\2\2E\24\3\2\2\2FG\7/\2\2G\26\3\2\2\2HI\7,\2")
        buf.write("\2I\30\3\2\2\2JK\7\61\2\2K\32\3\2\2\2LM\7y\2\2MN\7j\2")
        buf.write("\2NO\7k\2\2OP\7n\2\2PQ\7g\2\2QR\7\"\2\2R\34\3\2\2\2ST")
        buf.write("\7k\2\2TU\7h\2\2UV\7\"\2\2V\36\3\2\2\2WX\7g\2\2XY\7n\2")
        buf.write("\2YZ\7u\2\2Z[\7g\2\2[ \3\2\2\2\\]\7k\2\2]^\7p\2\2^_\7")
        buf.write("v\2\2_f\7\"\2\2`a\7d\2\2ab\7q\2\2bc\7q\2\2cd\7n\2\2df")
        buf.write("\7\"\2\2e\\\3\2\2\2e`\3\2\2\2f\"\3\2\2\2gk\t\2\2\2hj\t")
        buf.write("\3\2\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2l$\3\2\2")
        buf.write("\2mk\3\2\2\2no\t\4\2\2o&\3\2\2\2py\7>\2\2qr\7>\2\2ry\7")
        buf.write("?\2\2sy\7@\2\2tu\7@\2\2uy\7?\2\2vw\7?\2\2wy\7?\2\2xp\3")
        buf.write("\2\2\2xq\3\2\2\2xs\3\2\2\2xt\3\2\2\2xv\3\2\2\2y(\3\2\2")
        buf.write("\2z|\t\5\2\2{z\3\2\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2\2~")
        buf.write("\177\3\2\2\2\177\u0080\b\25\2\2\u0080*\3\2\2\2\b\2eik")
        buf.write("x}\3\b\2\2")
        return buf.getvalue()


class DevilsCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    DATA_TYPE = 16
    IDENT = 17
    DIGIT = 18
    CPR_SYMBOL = 19
    WS = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main '", "'('", "')'", "'{'", "'}'", "';'", "'print '", "'='", 
            "'+'", "'-'", "'*'", "'/'", "'while '", "'if '", "'else'" ]

    symbolicNames = [ "<INVALID>",
            "DATA_TYPE", "IDENT", "DIGIT", "CPR_SYMBOL", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "DATA_TYPE", "IDENT", "DIGIT", "CPR_SYMBOL", 
                  "WS" ]

    grammarFileName = "DevilsCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

