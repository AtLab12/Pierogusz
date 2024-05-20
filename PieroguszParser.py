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
        4,1,16,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,35,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,55,8,6,1,6,1,6,
        1,6,5,6,60,8,6,10,6,12,6,63,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,1,
        1,0,8,11,67,0,15,1,0,0,0,2,23,1,0,0,0,4,34,1,0,0,0,6,36,1,0,0,0,
        8,40,1,0,0,0,10,44,1,0,0,0,12,54,1,0,0,0,14,16,3,2,1,0,15,14,1,0,
        0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,24,
        3,4,2,0,20,24,3,6,3,0,21,24,3,8,4,0,22,24,3,10,5,0,23,19,1,0,0,0,
        23,20,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,1,
        0,0,26,27,5,12,0,0,27,35,5,2,0,0,28,29,5,3,0,0,29,30,5,12,0,0,30,
        35,5,2,0,0,31,32,5,4,0,0,32,33,5,12,0,0,33,35,5,2,0,0,34,25,1,0,
        0,0,34,28,1,0,0,0,34,31,1,0,0,0,35,5,1,0,0,0,36,37,5,5,0,0,37,38,
        3,12,6,0,38,39,5,2,0,0,39,7,1,0,0,0,40,41,5,6,0,0,41,42,5,12,0,0,
        42,43,5,2,0,0,43,9,1,0,0,0,44,45,5,12,0,0,45,46,5,7,0,0,46,47,3,
        12,6,0,47,48,5,2,0,0,48,11,1,0,0,0,49,50,6,6,-1,0,50,55,5,12,0,0,
        51,55,5,13,0,0,52,55,5,14,0,0,53,55,5,15,0,0,54,49,1,0,0,0,54,51,
        1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,0,55,61,1,0,0,0,56,57,10,5,0,0,
        57,58,7,0,0,0,58,60,3,12,6,6,59,56,1,0,0,0,60,63,1,0,0,0,61,59,1,
        0,0,0,61,62,1,0,0,0,62,13,1,0,0,0,63,61,1,0,0,0,5,17,23,34,54,61
    ]

class PieroguszParser ( Parser ):

    grammarFileName = "Pierogusz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "';'", "'float'", "'string'", 
                     "'print'", "'read'", "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "FLOAT", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_printStmt = 3
    RULE_readStmt = 4
    RULE_assignStmt = 5
    RULE_expr = 6

    ruleNames =  [ "program", "statement", "varDecl", "printStmt", "readStmt", 
                   "assignStmt", "expr" ]

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
    ID=12
    INT=13
    FLOAT=14
    STRING=15
    WS=16

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
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4218) != 0)):
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


        def printStmt(self):
            return self.getTypedRuleContext(PieroguszParser.PrintStmtContext,0)


        def readStmt(self):
            return self.getTypedRuleContext(PieroguszParser.ReadStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(PieroguszParser.AssignStmtContext,0)


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
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.varDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.printStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.readStmt()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.assignStmt()
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
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(PieroguszParser.T__0)
                self.state = 26
                self.match(PieroguszParser.ID)
                self.state = 27
                self.match(PieroguszParser.T__1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(PieroguszParser.T__2)
                self.state = 29
                self.match(PieroguszParser.ID)
                self.state = 30
                self.match(PieroguszParser.T__1)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(PieroguszParser.T__3)
                self.state = 32
                self.match(PieroguszParser.ID)
                self.state = 33
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
        self.enterRule(localctx, 6, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(PieroguszParser.T__4)
            self.state = 37
            self.expr(0)
            self.state = 38
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
        self.enterRule(localctx, 8, self.RULE_readStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(PieroguszParser.T__5)
            self.state = 41
            self.match(PieroguszParser.ID)
            self.state = 42
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
        self.enterRule(localctx, 10, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(PieroguszParser.ID)
            self.state = 45
            self.match(PieroguszParser.T__6)
            self.state = 46
            self.expr(0)
            self.state = 47
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

        def INT(self):
            return self.getToken(PieroguszParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PieroguszParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(PieroguszParser.STRING, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PieroguszParser.ExprContext)
            else:
                return self.getTypedRuleContext(PieroguszParser.ExprContext,i)


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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 50
                self.match(PieroguszParser.ID)
                pass
            elif token in [13]:
                self.state = 51
                self.match(PieroguszParser.INT)
                pass
            elif token in [14]:
                self.state = 52
                self.match(PieroguszParser.FLOAT)
                pass
            elif token in [15]:
                self.state = 53
                self.match(PieroguszParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PieroguszParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 56
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 57
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 58
                    self.expr(6) 
                self.state = 63
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
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         



