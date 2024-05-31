# Generated from Pierogusz.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PieroguszParser import PieroguszParser
else:
    from PieroguszParser import PieroguszParser

# This class defines a complete listener for a parse tree produced by PieroguszParser.
class PieroguszListener(ParseTreeListener):

    # Enter a parse tree produced by PieroguszParser#program.
    def enterProgram(self, ctx:PieroguszParser.ProgramContext):
        pass

    # Exit a parse tree produced by PieroguszParser#program.
    def exitProgram(self, ctx:PieroguszParser.ProgramContext):
        pass


    # Enter a parse tree produced by PieroguszParser#statement.
    def enterStatement(self, ctx:PieroguszParser.StatementContext):
        pass

    # Exit a parse tree produced by PieroguszParser#statement.
    def exitStatement(self, ctx:PieroguszParser.StatementContext):
        pass


    # Enter a parse tree produced by PieroguszParser#varDecl.
    def enterVarDecl(self, ctx:PieroguszParser.VarDeclContext):
        pass

    # Exit a parse tree produced by PieroguszParser#varDecl.
    def exitVarDecl(self, ctx:PieroguszParser.VarDeclContext):
        pass


    # Enter a parse tree produced by PieroguszParser#arrayDecl.
    def enterArrayDecl(self, ctx:PieroguszParser.ArrayDeclContext):
        pass

    # Exit a parse tree produced by PieroguszParser#arrayDecl.
    def exitArrayDecl(self, ctx:PieroguszParser.ArrayDeclContext):
        pass


    # Enter a parse tree produced by PieroguszParser#matrixDecl.
    def enterMatrixDecl(self, ctx:PieroguszParser.MatrixDeclContext):
        pass

    # Exit a parse tree produced by PieroguszParser#matrixDecl.
    def exitMatrixDecl(self, ctx:PieroguszParser.MatrixDeclContext):
        pass


    # Enter a parse tree produced by PieroguszParser#printStmt.
    def enterPrintStmt(self, ctx:PieroguszParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by PieroguszParser#printStmt.
    def exitPrintStmt(self, ctx:PieroguszParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by PieroguszParser#readStmt.
    def enterReadStmt(self, ctx:PieroguszParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by PieroguszParser#readStmt.
    def exitReadStmt(self, ctx:PieroguszParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by PieroguszParser#assignStmt.
    def enterAssignStmt(self, ctx:PieroguszParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by PieroguszParser#assignStmt.
    def exitAssignStmt(self, ctx:PieroguszParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by PieroguszParser#arrayAssignStmt.
    def enterArrayAssignStmt(self, ctx:PieroguszParser.ArrayAssignStmtContext):
        pass

    # Exit a parse tree produced by PieroguszParser#arrayAssignStmt.
    def exitArrayAssignStmt(self, ctx:PieroguszParser.ArrayAssignStmtContext):
        pass


    # Enter a parse tree produced by PieroguszParser#matrixAssignStmt.
    def enterMatrixAssignStmt(self, ctx:PieroguszParser.MatrixAssignStmtContext):
        pass

    # Exit a parse tree produced by PieroguszParser#matrixAssignStmt.
    def exitMatrixAssignStmt(self, ctx:PieroguszParser.MatrixAssignStmtContext):
        pass


    # Enter a parse tree produced by PieroguszParser#expr.
    def enterExpr(self, ctx:PieroguszParser.ExprContext):
        pass

    # Exit a parse tree produced by PieroguszParser#expr.
    def exitExpr(self, ctx:PieroguszParser.ExprContext):
        pass



del PieroguszParser