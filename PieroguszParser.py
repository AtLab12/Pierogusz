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
        4,1,27,136,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,53,8,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,126,8,10,1,10,1,10,1,10,5,
        10,131,8,10,10,10,12,10,134,9,10,1,10,0,1,20,11,0,2,4,6,8,10,12,
        14,16,18,20,0,2,2,0,1,1,3,6,1,0,12,18,145,0,23,1,0,0,0,2,35,1,0,
        0,0,4,52,1,0,0,0,6,54,1,0,0,0,8,61,1,0,0,0,10,71,1,0,0,0,12,75,1,
        0,0,0,14,79,1,0,0,0,16,84,1,0,0,0,18,92,1,0,0,0,20,125,1,0,0,0,22,
        24,3,2,1,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,
        0,26,1,1,0,0,0,27,36,3,4,2,0,28,36,3,6,3,0,29,36,3,8,4,0,30,36,3,
        10,5,0,31,36,3,12,6,0,32,36,3,14,7,0,33,36,3,16,8,0,34,36,3,18,9,
        0,35,27,1,0,0,0,35,28,1,0,0,0,35,29,1,0,0,0,35,30,1,0,0,0,35,31,
        1,0,0,0,35,32,1,0,0,0,35,33,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,
        38,5,1,0,0,38,39,5,20,0,0,39,53,5,2,0,0,40,41,5,3,0,0,41,42,5,20,
        0,0,42,53,5,2,0,0,43,44,5,4,0,0,44,45,5,20,0,0,45,53,5,2,0,0,46,
        47,5,5,0,0,47,48,5,20,0,0,48,53,5,2,0,0,49,50,5,6,0,0,50,51,5,20,
        0,0,51,53,5,2,0,0,52,37,1,0,0,0,52,40,1,0,0,0,52,43,1,0,0,0,52,46,
        1,0,0,0,52,49,1,0,0,0,53,5,1,0,0,0,54,55,7,0,0,0,55,56,5,20,0,0,
        56,57,5,7,0,0,57,58,5,21,0,0,58,59,5,8,0,0,59,60,5,2,0,0,60,7,1,
        0,0,0,61,62,7,0,0,0,62,63,5,20,0,0,63,64,5,7,0,0,64,65,5,21,0,0,
        65,66,5,8,0,0,66,67,5,7,0,0,67,68,5,21,0,0,68,69,5,8,0,0,69,70,5,
        2,0,0,70,9,1,0,0,0,71,72,5,9,0,0,72,73,3,20,10,0,73,74,5,2,0,0,74,
        11,1,0,0,0,75,76,5,10,0,0,76,77,5,20,0,0,77,78,5,2,0,0,78,13,1,0,
        0,0,79,80,5,20,0,0,80,81,5,11,0,0,81,82,3,20,10,0,82,83,5,2,0,0,
        83,15,1,0,0,0,84,85,5,20,0,0,85,86,5,7,0,0,86,87,3,20,10,0,87,88,
        5,8,0,0,88,89,5,11,0,0,89,90,3,20,10,0,90,91,5,2,0,0,91,17,1,0,0,
        0,92,93,5,20,0,0,93,94,5,7,0,0,94,95,3,20,10,0,95,96,5,8,0,0,96,
        97,5,7,0,0,97,98,3,20,10,0,98,99,5,8,0,0,99,100,5,11,0,0,100,101,
        3,20,10,0,101,102,5,2,0,0,102,19,1,0,0,0,103,104,6,10,-1,0,104,105,
        5,19,0,0,105,126,3,20,10,9,106,126,5,20,0,0,107,108,5,20,0,0,108,
        109,5,7,0,0,109,110,3,20,10,0,110,111,5,8,0,0,111,126,1,0,0,0,112,
        113,5,20,0,0,113,114,5,7,0,0,114,115,3,20,10,0,115,116,5,8,0,0,116,
        117,5,7,0,0,117,118,3,20,10,0,118,119,5,8,0,0,119,126,1,0,0,0,120,
        126,5,21,0,0,121,126,5,22,0,0,122,126,5,23,0,0,123,126,5,24,0,0,
        124,126,5,25,0,0,125,103,1,0,0,0,125,106,1,0,0,0,125,107,1,0,0,0,
        125,112,1,0,0,0,125,120,1,0,0,0,125,121,1,0,0,0,125,122,1,0,0,0,
        125,123,1,0,0,0,125,124,1,0,0,0,126,132,1,0,0,0,127,128,10,10,0,
        0,128,129,7,1,0,0,129,131,3,20,10,11,130,127,1,0,0,0,131,134,1,0,
        0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,21,1,0,0,0,134,132,1,0,0,
        0,5,25,35,52,125,132
    ]

class PieroguszParser ( Parser ):

    grammarFileName = "Pierogusz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "';'", "'float32'", "'float64'", 
                     "'string'", "'bool'", "'['", "']'", "'print'", "'read'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'AND'", "'OR'", 
                     "'XOR'", "'NEG'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "FLOAT", "SCIENTIFIC_FLOAT", "STRING", 
                      "BOOL", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_arrayDecl = 3
    RULE_matrixDecl = 4
    RULE_printStmt = 5
    RULE_readStmt = 6
    RULE_assignStmt = 7
    RULE_arrayAssignStmt = 8
    RULE_matrixAssignStmt = 9
    RULE_expr = 10

    ruleNames =  [ "program", "statement", "varDecl", "arrayDecl", "matrixDecl", 
                   "printStmt", "readStmt", "assignStmt", "arrayAssignStmt", 
                   "matrixAssignStmt", "expr" ]

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
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ID=20
    INT=21
    FLOAT=22
    SCIENTIFIC_FLOAT=23
    STRING=24
    BOOL=25
    WS=26
    COMMENT=27

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
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1050234) != 0)):
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


        def matrixDecl(self):
            return self.getTypedRuleContext(PieroguszParser.MatrixDeclContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(PieroguszParser.PrintStmtContext,0)


        def readStmt(self):
            return self.getTypedRuleContext(PieroguszParser.ReadStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(PieroguszParser.AssignStmtContext,0)


        def arrayAssignStmt(self):
            return self.getTypedRuleContext(PieroguszParser.ArrayAssignStmtContext,0)


        def matrixAssignStmt(self):
            return self.getTypedRuleContext(PieroguszParser.MatrixAssignStmtContext,0)


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
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.arrayDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.matrixDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.printStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.readStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 32
                self.assignStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 33
                self.arrayAssignStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 34
                self.matrixAssignStmt()
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
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(PieroguszParser.T__0)
                self.state = 38
                self.match(PieroguszParser.ID)
                self.state = 39
                self.match(PieroguszParser.T__1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(PieroguszParser.T__2)
                self.state = 41
                self.match(PieroguszParser.ID)
                self.state = 42
                self.match(PieroguszParser.T__1)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(PieroguszParser.T__3)
                self.state = 44
                self.match(PieroguszParser.ID)
                self.state = 45
                self.match(PieroguszParser.T__1)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(PieroguszParser.T__4)
                self.state = 47
                self.match(PieroguszParser.ID)
                self.state = 48
                self.match(PieroguszParser.T__1)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.match(PieroguszParser.T__5)
                self.state = 50
                self.match(PieroguszParser.ID)
                self.state = 51
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
            self.state = 54
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 55
            self.match(PieroguszParser.ID)
            self.state = 56
            self.match(PieroguszParser.T__6)
            self.state = 57
            self.match(PieroguszParser.INT)
            self.state = 58
            self.match(PieroguszParser.T__7)
            self.state = 59
            self.match(PieroguszParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PieroguszParser.ID, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(PieroguszParser.INT)
            else:
                return self.getToken(PieroguszParser.INT, i)

        def getRuleIndex(self):
            return PieroguszParser.RULE_matrixDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixDecl" ):
                listener.enterMatrixDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixDecl" ):
                listener.exitMatrixDecl(self)




    def matrixDecl(self):

        localctx = PieroguszParser.MatrixDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_matrixDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 62
            self.match(PieroguszParser.ID)
            self.state = 63
            self.match(PieroguszParser.T__6)
            self.state = 64
            self.match(PieroguszParser.INT)
            self.state = 65
            self.match(PieroguszParser.T__7)
            self.state = 66
            self.match(PieroguszParser.T__6)
            self.state = 67
            self.match(PieroguszParser.INT)
            self.state = 68
            self.match(PieroguszParser.T__7)
            self.state = 69
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
        self.enterRule(localctx, 10, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(PieroguszParser.T__8)
            self.state = 72
            self.expr(0)
            self.state = 73
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
        self.enterRule(localctx, 12, self.RULE_readStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(PieroguszParser.T__9)
            self.state = 76
            self.match(PieroguszParser.ID)
            self.state = 77
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
        self.enterRule(localctx, 14, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(PieroguszParser.ID)
            self.state = 80
            self.match(PieroguszParser.T__10)
            self.state = 81
            self.expr(0)
            self.state = 82
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
        self.enterRule(localctx, 16, self.RULE_arrayAssignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(PieroguszParser.ID)
            self.state = 85
            self.match(PieroguszParser.T__6)
            self.state = 86
            self.expr(0)
            self.state = 87
            self.match(PieroguszParser.T__7)
            self.state = 88
            self.match(PieroguszParser.T__10)
            self.state = 89
            self.expr(0)
            self.state = 90
            self.match(PieroguszParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixAssignStmtContext(ParserRuleContext):
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
            return PieroguszParser.RULE_matrixAssignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixAssignStmt" ):
                listener.enterMatrixAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixAssignStmt" ):
                listener.exitMatrixAssignStmt(self)




    def matrixAssignStmt(self):

        localctx = PieroguszParser.MatrixAssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_matrixAssignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(PieroguszParser.ID)
            self.state = 93
            self.match(PieroguszParser.T__6)
            self.state = 94
            self.expr(0)
            self.state = 95
            self.match(PieroguszParser.T__7)
            self.state = 96
            self.match(PieroguszParser.T__6)
            self.state = 97
            self.expr(0)
            self.state = 98
            self.match(PieroguszParser.T__7)
            self.state = 99
            self.match(PieroguszParser.T__10)
            self.state = 100
            self.expr(0)
            self.state = 101
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PieroguszParser.ExprContext)
            else:
                return self.getTypedRuleContext(PieroguszParser.ExprContext,i)


        def ID(self):
            return self.getToken(PieroguszParser.ID, 0)

        def INT(self):
            return self.getToken(PieroguszParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PieroguszParser.FLOAT, 0)

        def SCIENTIFIC_FLOAT(self):
            return self.getToken(PieroguszParser.SCIENTIFIC_FLOAT, 0)

        def STRING(self):
            return self.getToken(PieroguszParser.STRING, 0)

        def BOOL(self):
            return self.getToken(PieroguszParser.BOOL, 0)

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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 104
                self.match(PieroguszParser.T__18)
                self.state = 105
                self.expr(9)
                pass

            elif la_ == 2:
                self.state = 106
                self.match(PieroguszParser.ID)
                pass

            elif la_ == 3:
                self.state = 107
                self.match(PieroguszParser.ID)
                self.state = 108
                self.match(PieroguszParser.T__6)
                self.state = 109
                self.expr(0)
                self.state = 110
                self.match(PieroguszParser.T__7)
                pass

            elif la_ == 4:
                self.state = 112
                self.match(PieroguszParser.ID)
                self.state = 113
                self.match(PieroguszParser.T__6)
                self.state = 114
                self.expr(0)
                self.state = 115
                self.match(PieroguszParser.T__7)
                self.state = 116
                self.match(PieroguszParser.T__6)
                self.state = 117
                self.expr(0)
                self.state = 118
                self.match(PieroguszParser.T__7)
                pass

            elif la_ == 5:
                self.state = 120
                self.match(PieroguszParser.INT)
                pass

            elif la_ == 6:
                self.state = 121
                self.match(PieroguszParser.FLOAT)
                pass

            elif la_ == 7:
                self.state = 122
                self.match(PieroguszParser.SCIENTIFIC_FLOAT)
                pass

            elif la_ == 8:
                self.state = 123
                self.match(PieroguszParser.STRING)
                pass

            elif la_ == 9:
                self.state = 124
                self.match(PieroguszParser.BOOL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PieroguszParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 127
                    if not self.precpred(self._ctx, 10):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                    self.state = 128
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 520192) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 129
                    self.expr(11) 
                self.state = 134
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
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         




