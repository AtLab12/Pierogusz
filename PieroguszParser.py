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
        4,1,19,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,41,8,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,81,8,8,1,8,1,8,1,8,5,8,86,8,8,10,8,12,
        8,89,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,2,2,0,1,1,3,4,1,0,
        10,13,94,0,19,1,0,0,0,2,29,1,0,0,0,4,40,1,0,0,0,6,42,1,0,0,0,8,49,
        1,0,0,0,10,53,1,0,0,0,12,57,1,0,0,0,14,62,1,0,0,0,16,80,1,0,0,0,
        18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,
        0,0,0,22,1,1,0,0,0,23,30,3,4,2,0,24,30,3,6,3,0,25,30,3,8,4,0,26,
        30,3,10,5,0,27,30,3,12,6,0,28,30,3,14,7,0,29,23,1,0,0,0,29,24,1,
        0,0,0,29,25,1,0,0,0,29,26,1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,
        3,1,0,0,0,31,32,5,1,0,0,32,33,5,14,0,0,33,41,5,2,0,0,34,35,5,3,0,
        0,35,36,5,14,0,0,36,41,5,2,0,0,37,38,5,4,0,0,38,39,5,14,0,0,39,41,
        5,2,0,0,40,31,1,0,0,0,40,34,1,0,0,0,40,37,1,0,0,0,41,5,1,0,0,0,42,
        43,7,0,0,0,43,44,5,14,0,0,44,45,5,5,0,0,45,46,5,15,0,0,46,47,5,6,
        0,0,47,48,5,2,0,0,48,7,1,0,0,0,49,50,5,7,0,0,50,51,3,16,8,0,51,52,
        5,2,0,0,52,9,1,0,0,0,53,54,5,8,0,0,54,55,5,14,0,0,55,56,5,2,0,0,
        56,11,1,0,0,0,57,58,5,14,0,0,58,59,5,9,0,0,59,60,3,16,8,0,60,61,
        5,2,0,0,61,13,1,0,0,0,62,63,5,14,0,0,63,64,5,5,0,0,64,65,3,16,8,
        0,65,66,5,6,0,0,66,67,5,9,0,0,67,68,3,16,8,0,68,69,5,2,0,0,69,15,
        1,0,0,0,70,71,6,8,-1,0,71,81,5,14,0,0,72,73,5,14,0,0,73,74,5,5,0,
        0,74,75,3,16,8,0,75,76,5,6,0,0,76,81,1,0,0,0,77,81,5,15,0,0,78,81,
        5,16,0,0,79,81,5,17,0,0,80,70,1,0,0,0,80,72,1,0,0,0,80,77,1,0,0,
        0,80,78,1,0,0,0,80,79,1,0,0,0,81,87,1,0,0,0,82,83,10,6,0,0,83,84,
        7,1,0,0,84,86,3,16,8,7,85,82,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,
        87,88,1,0,0,0,88,17,1,0,0,0,89,87,1,0,0,0,5,21,29,40,80,87
    ]

class PieroguszParser ( Parser ):

    grammarFileName = "Pierogusz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "';'", "'float'", "'string'", 
                     "'['", "']'", "'print'", "'read'", "'='", "'+'", "'-'", 
                     "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "FLOAT", "STRING", 
                      "WS", "COMMENT" ]

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
    ID=14
    INT=15
    FLOAT=16
    STRING=17
    WS=18
    COMMENT=19

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16794) != 0)):
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
            self.state = 40
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
            self.state = 42
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 26) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 43
            self.match(PieroguszParser.ID)
            self.state = 44
            self.match(PieroguszParser.T__4)
            self.state = 45
            self.match(PieroguszParser.INT)
            self.state = 46
            self.match(PieroguszParser.T__5)
            self.state = 47
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
            self.state = 49
            self.match(PieroguszParser.T__6)
            self.state = 50
            self.expr(0)
            self.state = 51
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
            self.state = 53
            self.match(PieroguszParser.T__7)
            self.state = 54
            self.match(PieroguszParser.ID)
            self.state = 55
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
            self.state = 57
            self.match(PieroguszParser.ID)
            self.state = 58
            self.match(PieroguszParser.T__8)
            self.state = 59
            self.expr(0)
            self.state = 60
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
            self.state = 62
            self.match(PieroguszParser.ID)
            self.state = 63
            self.match(PieroguszParser.T__4)
            self.state = 64
            self.expr(0)
            self.state = 65
            self.match(PieroguszParser.T__5)
            self.state = 66
            self.match(PieroguszParser.T__8)
            self.state = 67
            self.expr(0)
            self.state = 68
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
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 71
                self.match(PieroguszParser.ID)
                pass

            elif la_ == 2:
                self.state = 72
                self.match(PieroguszParser.ID)
                self.state = 73
                self.match(PieroguszParser.T__4)
                self.state = 74
                self.expr(0)
                self.state = 75
                self.match(PieroguszParser.T__5)
                pass

            elif la_ == 3:
                self.state = 77
                self.match(PieroguszParser.INT)
                pass

            elif la_ == 4:
                self.state = 78
                self.match(PieroguszParser.FLOAT)
                pass

            elif la_ == 5:
                self.state = 79
                self.match(PieroguszParser.STRING)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PieroguszParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 82
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 83
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 84
                    self.expr(7) 
                self.state = 89
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
                return self.precpred(self._ctx, 6)
         




