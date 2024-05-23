# Generated from Pierogusz.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,44,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,85,8,8,1,8,1,8,1,8,5,8,
        90,8,8,10,8,12,8,93,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,2,2,
        0,1,1,3,5,1,0,11,14,100,0,19,1,0,0,0,2,29,1,0,0,0,4,43,1,0,0,0,6,
        45,1,0,0,0,8,52,1,0,0,0,10,56,1,0,0,0,12,60,1,0,0,0,14,65,1,0,0,
        0,16,84,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,30,3,4,2,0,24,30,3,6,3,0,25,
        30,3,8,4,0,26,30,3,10,5,0,27,30,3,12,6,0,28,30,3,14,7,0,29,23,1,
        0,0,0,29,24,1,0,0,0,29,25,1,0,0,0,29,26,1,0,0,0,29,27,1,0,0,0,29,
        28,1,0,0,0,30,3,1,0,0,0,31,32,5,1,0,0,32,33,5,15,0,0,33,44,5,2,0,
        0,34,35,5,3,0,0,35,36,5,15,0,0,36,44,5,2,0,0,37,38,5,4,0,0,38,39,
        5,15,0,0,39,44,5,2,0,0,40,41,5,5,0,0,41,42,5,15,0,0,42,44,5,2,0,
        0,43,31,1,0,0,0,43,34,1,0,0,0,43,37,1,0,0,0,43,40,1,0,0,0,44,5,1,
        0,0,0,45,46,7,0,0,0,46,47,5,15,0,0,47,48,5,6,0,0,48,49,5,16,0,0,
        49,50,5,7,0,0,50,51,5,2,0,0,51,7,1,0,0,0,52,53,5,8,0,0,53,54,3,16,
        8,0,54,55,5,2,0,0,55,9,1,0,0,0,56,57,5,9,0,0,57,58,5,15,0,0,58,59,
        5,2,0,0,59,11,1,0,0,0,60,61,5,15,0,0,61,62,5,10,0,0,62,63,3,16,8,
        0,63,64,5,2,0,0,64,13,1,0,0,0,65,66,5,15,0,0,66,67,5,6,0,0,67,68,
        3,16,8,0,68,69,5,7,0,0,69,70,5,10,0,0,70,71,3,16,8,0,71,72,5,2,0,
        0,72,15,1,0,0,0,73,74,6,8,-1,0,74,85,5,15,0,0,75,76,5,15,0,0,76,
        77,5,6,0,0,77,78,3,16,8,0,78,79,5,7,0,0,79,85,1,0,0,0,80,85,5,16,
        0,0,81,85,5,17,0,0,82,85,5,18,0,0,83,85,5,19,0,0,84,73,1,0,0,0,84,
        75,1,0,0,0,84,80,1,0,0,0,84,81,1,0,0,0,84,82,1,0,0,0,84,83,1,0,0,
        0,85,91,1,0,0,0,86,87,10,7,0,0,87,88,7,1,0,0,88,90,3,16,8,8,89,86,
        1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,17,1,0,0,0,
        93,91,1,0,0,0,5,21,29,43,84,91
    ]

class PieroguszParser ( Parser ):

    grammarFileName = "Pierogusz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "';'", "'float32'", "'float64'", 
                     "'string'", "'['", "']'", "'print'", "'read'", "'='", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "FLOAT", "SCIENTIFIC_FLOAT", "STRING", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_arrayDecl = 3
    RULE_printStmt = 4
    RULE_readStmt = 5
    RULE_assignStmt = 6
    RULE_arrayAssignStmt = 7
    RULE_expr = 8

    ruleNames =  [ "program", "statement", "varDecl", "arrayDecl", "printStmt", 
                   "readStmt", "assignStmt", "arrayAssignStmt", "expr" ]

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
    ID=15
    INT=16
    FLOAT=17
    SCIENTIFIC_FLOAT=18
    STRING=19
    WS=20
    COMMENT=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PieroguszParser.StatementContext)
            else:
                return self.getTypedRuleContext(PieroguszParser.StatementContext,i)


        def getRuleIndex(self):
            return PieroguszParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PieroguszParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33594) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(PieroguszParser.VarDeclContext,0)


        def arrayDecl(self):
            return self.getTypedRuleContext(PieroguszParser.ArrayDeclContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(PieroguszParser.PrintStmtContext,0)


        def readStmt(self):
            return self.getTypedRuleContext(PieroguszParser.ReadStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(PieroguszParser.AssignStmtContext,0)


        def arrayAssignStmt(self):
            return self.getTypedRuleContext(PieroguszParser.ArrayAssignStmtContext,0)


        def getRuleIndex(self):
            return PieroguszParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PieroguszParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.arrayDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.printStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.readStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.assignStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 28
                self.arrayAssignStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PieroguszParser.ID, 0)

        def getRuleIndex(self):
            return PieroguszParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = PieroguszParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(PieroguszParser.T__0)
                self.state = 32
                self.match(PieroguszParser.ID)
                self.state = 33
                self.match(PieroguszParser.T__1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(PieroguszParser.T__2)
                self.state = 35
                self.match(PieroguszParser.ID)
                self.state = 36
                self.match(PieroguszParser.T__1)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(PieroguszParser.T__3)
                self.state = 38
                self.match(PieroguszParser.ID)
                self.state = 39
                self.match(PieroguszParser.T__1)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.match(PieroguszParser.T__4)
                self.state = 41
                self.match(PieroguszParser.ID)
                self.state = 42
                self.match(PieroguszParser.T__1)
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


    class ArrayDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PieroguszParser.ID, 0)

        def INT(self):
            return self.getToken(PieroguszParser.INT, 0)

        def getRuleIndex(self):
            return PieroguszParser.RULE_arrayDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDecl" ):
                listener.enterArrayDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDecl" ):
                listener.exitArrayDecl(self)




    def arrayDecl(self):

        localctx = PieroguszParser.ArrayDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrayDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 46
            self.match(PieroguszParser.ID)
            self.state = 47
            self.match(PieroguszParser.T__5)
            self.state = 48
            self.match(PieroguszParser.INT)
            self.state = 49
            self.match(PieroguszParser.T__6)
            self.state = 50
            self.match(PieroguszParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PieroguszParser.ExprContext,0)


        def getRuleIndex(self):
            return PieroguszParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)




    def printStmt(self):

        localctx = PieroguszParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(PieroguszParser.T__7)
            self.state = 53
            self.expr(0)
            self.state = 54
            self.match(PieroguszParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PieroguszParser.ID, 0)

        def getRuleIndex(self):
            return PieroguszParser.RULE_readStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)




    def readStmt(self):

        localctx = PieroguszParser.ReadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_readStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(PieroguszParser.T__8)
            self.state = 57
            self.match(PieroguszParser.ID)
            self.state = 58
            self.match(PieroguszParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PieroguszParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(PieroguszParser.ExprContext,0)


        def getRuleIndex(self):
            return PieroguszParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)




    def assignStmt(self):

        localctx = PieroguszParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(PieroguszParser.ID)
            self.state = 61
            self.match(PieroguszParser.T__9)
            self.state = 62
            self.expr(0)
            self.state = 63
            self.match(PieroguszParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PieroguszParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PieroguszParser.ExprContext)
            else:
                return self.getTypedRuleContext(PieroguszParser.ExprContext,i)


        def getRuleIndex(self):
            return PieroguszParser.RULE_arrayAssignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAssignStmt" ):
                listener.enterArrayAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAssignStmt" ):
                listener.exitArrayAssignStmt(self)




    def arrayAssignStmt(self):

        localctx = PieroguszParser.ArrayAssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrayAssignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(PieroguszParser.ID)
            self.state = 66
            self.match(PieroguszParser.T__5)
            self.state = 67
            self.expr(0)
            self.state = 68
            self.match(PieroguszParser.T__6)
            self.state = 69
            self.match(PieroguszParser.T__9)
            self.state = 70
            self.expr(0)
            self.state = 71
            self.match(PieroguszParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PieroguszParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PieroguszParser.ExprContext)
            else:
                return self.getTypedRuleContext(PieroguszParser.ExprContext,i)


        def INT(self):
            return self.getToken(PieroguszParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PieroguszParser.FLOAT, 0)

        def SCIENTIFIC_FLOAT(self):
            return self.getToken(PieroguszParser.SCIENTIFIC_FLOAT, 0)

        def STRING(self):
            return self.getToken(PieroguszParser.STRING, 0)

        def getRuleIndex(self):
            return PieroguszParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PieroguszParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 74
                self.match(PieroguszParser.ID)
                pass

            elif la_ == 2:
                self.state = 75
                self.match(PieroguszParser.ID)
                self.state = 76
                self.match(PieroguszParser.T__5)
                self.state = 77
                self.expr(0)
                self.state = 78
                self.match(PieroguszParser.T__6)
                pass

            elif la_ == 3:
                self.state = 80
                self.match(PieroguszParser.INT)
                pass

            elif la_ == 4:
                self.state = 81
                self.match(PieroguszParser.FLOAT)
                pass

            elif la_ == 5:
                self.state = 82
                self.match(PieroguszParser.SCIENTIFIC_FLOAT)
                pass

            elif la_ == 6:
                self.state = 83
                self.match(PieroguszParser.STRING)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PieroguszParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 86
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 87
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 88
                    self.expr(8) 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         




