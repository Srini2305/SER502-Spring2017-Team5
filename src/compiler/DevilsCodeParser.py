# Generated from DevilsCode.g4 by ANTLR 4.7
# encoding: utf-8
# Modified by Hari Iyer
# Date: 26 April, 2017
# Version: 3
# Purpose: Parsing the DevilsCode program to generate the Parse Tree

from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys
import os

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("\u00a0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\7\3+\n\3\f\3\16\3.\13\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4C\n\4\3\5\3\5\3\5\3\5\5\5I\n\5\3\6\3\6\3\6\3\6")
        buf.write("\5\6O\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\7\b^\n\b\f\b\16\ba\13\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\7\tl\n\t\f\t\16\to\13\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\5\nw\n\n\3\13\3\13\3\13\3\13\3\13\7\13~\n\13")
        buf.write("\f\13\16\13\u0081\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u008f\n\r\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u009e")
        buf.write("\n\20\3\20\2\6\4\16\20\24\21\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36\2\2\2\u00a5\2 \3\2\2\2\4\'\3\2\2\2\6B\3\2")
        buf.write("\2\2\bH\3\2\2\2\nN\3\2\2\2\fP\3\2\2\2\16T\3\2\2\2\20b")
        buf.write("\3\2\2\2\22v\3\2\2\2\24x\3\2\2\2\26\u0082\3\2\2\2\30\u0088")
        buf.write("\3\2\2\2\32\u0090\3\2\2\2\34\u0093\3\2\2\2\36\u009d\3")
        buf.write("\2\2\2 !\7\3\2\2!\"\7\4\2\2\"#\7\5\2\2#$\7\6\2\2$%\5\4")
        buf.write("\3\2%&\7\7\2\2&\3\3\2\2\2\',\b\3\1\2()\f\4\2\2)+\5\6\4")
        buf.write("\2*(\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\5\3\2\2\2")
        buf.write(".,\3\2\2\2/\60\5\b\5\2\60\61\7\b\2\2\61C\3\2\2\2\62\63")
        buf.write("\5\n\6\2\63\64\7\b\2\2\64C\3\2\2\2\65C\5\26\f\2\66C\5")
        buf.write("\30\r\2\678\7\6\2\289\5\4\3\29:\7\7\2\2:C\3\2\2\2;<\7")
        buf.write("\t\2\2<=\7\23\2\2=C\7\b\2\2>?\7\t\2\2?@\5\24\13\2@A\7")
        buf.write("\b\2\2AC\3\2\2\2B/\3\2\2\2B\62\3\2\2\2B\65\3\2\2\2B\66")
        buf.write("\3\2\2\2B\67\3\2\2\2B;\3\2\2\2B>\3\2\2\2C\7\3\2\2\2DI")
        buf.write("\7\23\2\2EI\5\f\7\2FI\5\16\b\2GI\5\34\17\2HD\3\2\2\2H")
        buf.write("E\3\2\2\2HF\3\2\2\2HG\3\2\2\2I\t\3\2\2\2JK\7\22\2\2KO")
        buf.write("\7\23\2\2LM\7\22\2\2MO\5\f\7\2NJ\3\2\2\2NL\3\2\2\2O\13")
        buf.write("\3\2\2\2PQ\7\23\2\2QR\7\n\2\2RS\5\b\5\2S\r\3\2\2\2TU\b")
        buf.write("\b\1\2UV\5\20\t\2V_\3\2\2\2WX\f\5\2\2XY\7\13\2\2Y^\5\20")
        buf.write("\t\2Z[\f\4\2\2[\\\7\f\2\2\\^\5\20\t\2]W\3\2\2\2]Z\3\2")
        buf.write("\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\17\3\2\2\2a_\3\2\2")
        buf.write("\2bc\b\t\1\2cd\5\22\n\2dm\3\2\2\2ef\f\5\2\2fg\7\r\2\2")
        buf.write("gl\5\22\n\2hi\f\4\2\2ij\7\16\2\2jl\5\22\n\2ke\3\2\2\2")
        buf.write("kh\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2n\21\3\2\2\2o")
        buf.write("m\3\2\2\2pw\5\24\13\2qr\7\4\2\2rs\5\16\b\2st\7\5\2\2t")
        buf.write("w\3\2\2\2uw\7\23\2\2vp\3\2\2\2vq\3\2\2\2vu\3\2\2\2w\23")
        buf.write("\3\2\2\2xy\b\13\1\2yz\7\24\2\2z\177\3\2\2\2{|\f\4\2\2")
        buf.write("|~\7\24\2\2}{\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177")
        buf.write("\u0080\3\2\2\2\u0080\25\3\2\2\2\u0081\177\3\2\2\2\u0082")
        buf.write("\u0083\7\17\2\2\u0083\u0084\7\4\2\2\u0084\u0085\5\b\5")
        buf.write("\2\u0085\u0086\7\5\2\2\u0086\u0087\5\6\4\2\u0087\27\3")
        buf.write("\2\2\2\u0088\u0089\7\20\2\2\u0089\u008a\7\4\2\2\u008a")
        buf.write("\u008b\5\b\5\2\u008b\u008c\7\5\2\2\u008c\u008e\5\6\4\2")
        buf.write("\u008d\u008f\5\32\16\2\u008e\u008d\3\2\2\2\u008e\u008f")
        buf.write("\3\2\2\2\u008f\31\3\2\2\2\u0090\u0091\7\21\2\2\u0091\u0092")
        buf.write("\5\6\4\2\u0092\33\3\2\2\2\u0093\u0094\5\36\20\2\u0094")
        buf.write("\u0095\7\25\2\2\u0095\u0096\5\36\20\2\u0096\35\3\2\2\2")
        buf.write("\u0097\u009e\7\23\2\2\u0098\u009e\5\24\13\2\u0099\u009a")
        buf.write("\7\4\2\2\u009a\u009b\5\16\b\2\u009b\u009c\7\5\2\2\u009c")
        buf.write("\u009e\3\2\2\2\u009d\u0097\3\2\2\2\u009d\u0098\3\2\2\2")
        buf.write("\u009d\u0099\3\2\2\2\u009e\37\3\2\2\2\16,BHN]_kmv\177")
        buf.write("\u008e\u009d")
        return buf.getvalue()


class DevilsCodeParser(Parser):


    grammarFileName = "DevilsCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main '", "'('", "')'", "'{'", "'}'", 
                     "';'", "'print '", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'while '", "'if '", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DATA_TYPE", "IDENT", "DIGIT", "CPR_SYMBOL", "WS" ]

    RULE_program = 0
    RULE_stmtlists = 1
    RULE_stmt = 2
    RULE_expr = 3
    RULE_dec_stmt = 4
    RULE_assign_expr = 5
    RULE_math_expr = 6
    RULE_math_term = 7
    RULE_math_factor = 8
    RULE_number = 9
    RULE_while_stmt = 10
    RULE_if_stmt = 11
    RULE_else_stmt = 12
    RULE_cpr_expr = 13
    RULE_cpr_term = 14

    ruleNames =  [ "program", "stmtlists", "stmt", "expr", "dec_stmt", "assign_expr", 
                   "math_expr", "math_term", "math_factor", "number", "while_stmt", 
                   "if_stmt", "else_stmt", "cpr_expr", "cpr_term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    DATA_TYPE=16
    IDENT=17
    DIGIT=18
    CPR_SYMBOL=19
    WS=20

    def __init__(self, input:TokenStream, file_name, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.file_name = file_name + '.ic'
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtlists(self):
            return self.getTypedRuleContext(DevilsCodeParser.StmtlistsContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):
        localctx = DevilsCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(DevilsCodeParser.T__0)
            self.state = 31
            self.match(DevilsCodeParser.T__1)
            self.state = 32
            self.match(DevilsCodeParser.T__2)
            self.state = 33
            self.match(DevilsCodeParser.T__3)
            self.state = 34
            self.stmtlists(0)
            self.state = 35
            self.match(DevilsCodeParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            try:
                os.remove(self.file_name)
                quit()
            except OSError:
                pass
        finally:
            self.exitRule()
        return localctx

    class StmtlistsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtlists(self):
            return self.getTypedRuleContext(DevilsCodeParser.StmtlistsContext,0)


        def stmt(self):
            return self.getTypedRuleContext(DevilsCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_stmtlists

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtlists" ):
                listener.enterStmtlists(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtlists" ):
                listener.exitStmtlists(self)



    def stmtlists(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DevilsCodeParser.StmtlistsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_stmtlists, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DevilsCodeParser.StmtlistsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stmtlists)
                    self.state = 38
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 39
                    self.stmt() 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            	     
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.ExprContext,0)


        def dec_stmt(self):
            return self.getTypedRuleContext(DevilsCodeParser.Dec_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(DevilsCodeParser.While_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(DevilsCodeParser.If_stmtContext,0)


        def stmtlists(self):
            return self.getTypedRuleContext(DevilsCodeParser.StmtlistsContext,0)


        def IDENT(self):
            return self.getToken(DevilsCodeParser.IDENT, 0)

        def number(self):
            return self.getTypedRuleContext(DevilsCodeParser.NumberContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = DevilsCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.expr()
                self.state = 46
                self.match(DevilsCodeParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.dec_stmt()
                self.state = 49
                self.match(DevilsCodeParser.T__5)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.while_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.match(DevilsCodeParser.T__3)
                self.state = 54
                self.stmtlists(0)
                self.state = 55
                self.match(DevilsCodeParser.T__4)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.match(DevilsCodeParser.T__6)
                self.state = 58
                self.match(DevilsCodeParser.IDENT)
                self.state = 59
                self.match(DevilsCodeParser.T__5)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.match(DevilsCodeParser.T__6)
                self.state = 61
                self.number(0)
                self.state = 62
                self.match(DevilsCodeParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(DevilsCodeParser.IDENT, 0)

        def assign_expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.Assign_exprContext,0)


        def math_expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.Math_exprContext,0)


        def cpr_expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.Cpr_exprContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = DevilsCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(DevilsCodeParser.IDENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.assign_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.math_expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.cpr_expr()
                pass


        except RecognitionException as re:
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.exitRule()
        return localctx

    class Dec_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_TYPE(self):
            return self.getToken(DevilsCodeParser.DATA_TYPE, 0)

        def IDENT(self):
            return self.getToken(DevilsCodeParser.IDENT, 0)

        def assign_expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.Assign_exprContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_dec_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec_stmt" ):
                listener.enterDec_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec_stmt" ):
                listener.exitDec_stmt(self)




    def dec_stmt(self):

        localctx = DevilsCodeParser.Dec_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dec_stmt)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(DevilsCodeParser.DATA_TYPE)
                self.state = 73
                self.match(DevilsCodeParser.IDENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(DevilsCodeParser.DATA_TYPE)
                self.state = 75
                self.assign_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.exitRule()
        return localctx

    class Assign_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(DevilsCodeParser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_assign_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_expr" ):
                listener.enterAssign_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_expr" ):
                listener.exitAssign_expr(self)




    def assign_expr(self):

        localctx = DevilsCodeParser.Assign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(DevilsCodeParser.IDENT)
            self.state = 79
            self.match(DevilsCodeParser.T__7)
            self.state = 80
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.exitRule()
        return localctx

    class Math_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def math_term(self):
            return self.getTypedRuleContext(DevilsCodeParser.Math_termContext,0)


        def math_expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.Math_exprContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_math_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_expr" ):
                listener.enterMath_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_expr" ):
                listener.exitMath_expr(self)



    def math_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DevilsCodeParser.Math_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_math_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.math_term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 91
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = DevilsCodeParser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 86
                        self.match(DevilsCodeParser.T__8)
                        self.state = 87
                        self.math_term(0)
                        pass

                    elif la_ == 2:
                        localctx = DevilsCodeParser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 89
                        self.match(DevilsCodeParser.T__9)
                        self.state = 90
                        self.math_term(0)
                        pass

             
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Math_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def math_factor(self):
            return self.getTypedRuleContext(DevilsCodeParser.Math_factorContext,0)


        def math_term(self):
            return self.getTypedRuleContext(DevilsCodeParser.Math_termContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_math_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_term" ):
                listener.enterMath_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_term" ):
                listener.exitMath_term(self)



    def math_term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DevilsCodeParser.Math_termContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_math_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.math_factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 105
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = DevilsCodeParser.Math_termContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_term)
                        self.state = 99
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 100
                        self.match(DevilsCodeParser.T__10)
                        self.state = 101
                        self.math_factor()
                        pass

                    elif la_ == 2:
                        localctx = DevilsCodeParser.Math_termContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_term)
                        self.state = 102
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 103
                        self.match(DevilsCodeParser.T__11)
                        self.state = 104
                        self.math_factor()
                        pass

             
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Math_factorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(DevilsCodeParser.NumberContext,0)


        def math_expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.Math_exprContext,0)


        def IDENT(self):
            return self.getToken(DevilsCodeParser.IDENT, 0)

        def getRuleIndex(self):
            return DevilsCodeParser.RULE_math_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_factor" ):
                listener.enterMath_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_factor" ):
                listener.exitMath_factor(self)




    def math_factor(self):

        localctx = DevilsCodeParser.Math_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_math_factor)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DevilsCodeParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.number(0)
                pass
            elif token in [DevilsCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(DevilsCodeParser.T__1)
                self.state = 112
                self.math_expr(0)
                self.state = 113
                self.match(DevilsCodeParser.T__2)
                pass
            elif token in [DevilsCodeParser.IDENT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.match(DevilsCodeParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(DevilsCodeParser.DIGIT, 0)

        def number(self):
            return self.getTypedRuleContext(DevilsCodeParser.NumberContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)



    def number(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DevilsCodeParser.NumberContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_number, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(DevilsCodeParser.DIGIT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DevilsCodeParser.NumberContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_number)
                    self.state = 121
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 122
                    self.match(DevilsCodeParser.DIGIT) 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(DevilsCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)




    def while_stmt(self):

        localctx = DevilsCodeParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(DevilsCodeParser.T__12)
            self.state = 129
            self.match(DevilsCodeParser.T__1)
            self.state = 130
            self.expr()
            self.state = 131
            self.match(DevilsCodeParser.T__2)
            self.state = 132
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.exitRule()
        return localctx

    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(DevilsCodeParser.StmtContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(DevilsCodeParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = DevilsCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(DevilsCodeParser.T__13)
            self.state = 135
            self.match(DevilsCodeParser.T__1)
            self.state = 136
            self.expr()
            self.state = 137
            self.match(DevilsCodeParser.T__2)
            self.state = 138
            self.stmt()
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 139
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.exitRule()
        return localctx

    class Else_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(DevilsCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_else_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_stmt" ):
                listener.enterElse_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_stmt" ):
                listener.exitElse_stmt(self)




    def else_stmt(self):

        localctx = DevilsCodeParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(DevilsCodeParser.T__14)
            self.state = 143
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.exitRule()
        return localctx

    class Cpr_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cpr_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DevilsCodeParser.Cpr_termContext)
            else:
                return self.getTypedRuleContext(DevilsCodeParser.Cpr_termContext,i)


        def CPR_SYMBOL(self):
            return self.getToken(DevilsCodeParser.CPR_SYMBOL, 0)

        def getRuleIndex(self):
            return DevilsCodeParser.RULE_cpr_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCpr_expr" ):
                listener.enterCpr_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCpr_expr" ):
                listener.exitCpr_expr(self)




    def cpr_expr(self):

        localctx = DevilsCodeParser.Cpr_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_cpr_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.cpr_term()
            self.state = 146
            self.match(DevilsCodeParser.CPR_SYMBOL)
            self.state = 147
            self.cpr_term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.exitRule()
        return localctx

    class Cpr_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(DevilsCodeParser.IDENT, 0)

        def number(self):
            return self.getTypedRuleContext(DevilsCodeParser.NumberContext,0)


        def math_expr(self):
            return self.getTypedRuleContext(DevilsCodeParser.Math_exprContext,0)


        def getRuleIndex(self):
            return DevilsCodeParser.RULE_cpr_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCpr_term" ):
                listener.enterCpr_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCpr_term" ):
                listener.exitCpr_term(self)




    def cpr_term(self):

        localctx = DevilsCodeParser.Cpr_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cpr_term)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DevilsCodeParser.IDENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(DevilsCodeParser.IDENT)
                pass
            elif token in [DevilsCodeParser.DIGIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.number(0)
                pass
            elif token in [DevilsCodeParser.T__1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.match(DevilsCodeParser.T__1)
                self.state = 152
                self.math_expr(0)
                self.state = 153
                self.match(DevilsCodeParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
            
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.stmtlists_sempred
        self._predicates[6] = self.math_expr_sempred
        self._predicates[7] = self.math_term_sempred
        self._predicates[9] = self.number_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def stmtlists_sempred(self, localctx:StmtlistsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def math_expr_sempred(self, localctx:Math_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def math_term_sempred(self, localctx:Math_termContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def number_sempred(self, localctx:NumberContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         



