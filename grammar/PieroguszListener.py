# Generated from Pierogusz.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PieroguszParser import PieroguszParser
else:
    from PieroguszParser import PieroguszParser

# This class defines a complete listener for a parse tree produced by PieroguszParser.
class PieroguszListener(ParseTreeListener):

    # Enter a parse tree produced by PieroguszParser#prog.
    def enterProg(self, ctx:PieroguszParser.ProgContext):
        pass

    # Exit a parse tree produced by PieroguszParser#prog.
    def exitProg(self, ctx:PieroguszParser.ProgContext):
        pass


    # Enter a parse tree produced by PieroguszParser#block.
    def enterBlock(self, ctx:PieroguszParser.BlockContext):
        pass

    # Exit a parse tree produced by PieroguszParser#block.
    def exitBlock(self, ctx:PieroguszParser.BlockContext):
        pass


    # Enter a parse tree produced by PieroguszParser#statement.
    def enterStatement(self, ctx:PieroguszParser.StatementContext):
        pass

    # Exit a parse tree produced by PieroguszParser#statement.
    def exitStatement(self, ctx:PieroguszParser.StatementContext):
        pass


    # Enter a parse tree produced by PieroguszParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:PieroguszParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by PieroguszParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:PieroguszParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by PieroguszParser#assignment.
    def enterAssignment(self, ctx:PieroguszParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PieroguszParser#assignment.
    def exitAssignment(self, ctx:PieroguszParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PieroguszParser#printCall.
    def enterPrintCall(self, ctx:PieroguszParser.PrintCallContext):
        pass

    # Exit a parse tree produced by PieroguszParser#printCall.
    def exitPrintCall(self, ctx:PieroguszParser.PrintCallContext):
        pass


    # Enter a parse tree produced by PieroguszParser#readCall.
    def enterReadCall(self, ctx:PieroguszParser.ReadCallContext):
        pass

    # Exit a parse tree produced by PieroguszParser#readCall.
    def exitReadCall(self, ctx:PieroguszParser.ReadCallContext):
        pass


    # Enter a parse tree produced by PieroguszParser#expression.
    def enterExpression(self, ctx:PieroguszParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PieroguszParser#expression.
    def exitExpression(self, ctx:PieroguszParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PieroguszParser#or.
    def enterOr(self, ctx:PieroguszParser.OrContext):
        pass

    # Exit a parse tree produced by PieroguszParser#or.
    def exitOr(self, ctx:PieroguszParser.OrContext):
        pass


    # Enter a parse tree produced by PieroguszParser#xor.
    def enterXor(self, ctx:PieroguszParser.XorContext):
        pass

    # Exit a parse tree produced by PieroguszParser#xor.
    def exitXor(self, ctx:PieroguszParser.XorContext):
        pass


    # Enter a parse tree produced by PieroguszParser#and.
    def enterAnd(self, ctx:PieroguszParser.AndContext):
        pass

    # Exit a parse tree produced by PieroguszParser#and.
    def exitAnd(self, ctx:PieroguszParser.AndContext):
        pass


    # Enter a parse tree produced by PieroguszParser#equal.
    def enterEqual(self, ctx:PieroguszParser.EqualContext):
        pass

    # Exit a parse tree produced by PieroguszParser#equal.
    def exitEqual(self, ctx:PieroguszParser.EqualContext):
        pass


    # Enter a parse tree produced by PieroguszParser#negation.
    def enterNegation(self, ctx:PieroguszParser.NegationContext):
        pass

    # Exit a parse tree produced by PieroguszParser#negation.
    def exitNegation(self, ctx:PieroguszParser.NegationContext):
        pass


    # Enter a parse tree produced by PieroguszParser#simpleBoolValue.
    def enterSimpleBoolValue(self, ctx:PieroguszParser.SimpleBoolValueContext):
        pass

    # Exit a parse tree produced by PieroguszParser#simpleBoolValue.
    def exitSimpleBoolValue(self, ctx:PieroguszParser.SimpleBoolValueContext):
        pass


    # Enter a parse tree produced by PieroguszParser#bool.
    def enterBool(self, ctx:PieroguszParser.BoolContext):
        pass

    # Exit a parse tree produced by PieroguszParser#bool.
    def exitBool(self, ctx:PieroguszParser.BoolContext):
        pass


    # Enter a parse tree produced by PieroguszParser#simpleLogicalExpression.
    def enterSimpleLogicalExpression(self, ctx:PieroguszParser.SimpleLogicalExpressionContext):
        pass

    # Exit a parse tree produced by PieroguszParser#simpleLogicalExpression.
    def exitSimpleLogicalExpression(self, ctx:PieroguszParser.SimpleLogicalExpressionContext):
        pass


    # Enter a parse tree produced by PieroguszParser#add.
    def enterAdd(self, ctx:PieroguszParser.AddContext):
        pass

    # Exit a parse tree produced by PieroguszParser#add.
    def exitAdd(self, ctx:PieroguszParser.AddContext):
        pass


    # Enter a parse tree produced by PieroguszParser#singleValue3.
    def enterSingleValue3(self, ctx:PieroguszParser.SingleValue3Context):
        pass

    # Exit a parse tree produced by PieroguszParser#singleValue3.
    def exitSingleValue3(self, ctx:PieroguszParser.SingleValue3Context):
        pass


    # Enter a parse tree produced by PieroguszParser#substract.
    def enterSubstract(self, ctx:PieroguszParser.SubstractContext):
        pass

    # Exit a parse tree produced by PieroguszParser#substract.
    def exitSubstract(self, ctx:PieroguszParser.SubstractContext):
        pass


    # Enter a parse tree produced by PieroguszParser#singleValue2.
    def enterSingleValue2(self, ctx:PieroguszParser.SingleValue2Context):
        pass

    # Exit a parse tree produced by PieroguszParser#singleValue2.
    def exitSingleValue2(self, ctx:PieroguszParser.SingleValue2Context):
        pass


    # Enter a parse tree produced by PieroguszParser#divide.
    def enterDivide(self, ctx:PieroguszParser.DivideContext):
        pass

    # Exit a parse tree produced by PieroguszParser#divide.
    def exitDivide(self, ctx:PieroguszParser.DivideContext):
        pass


    # Enter a parse tree produced by PieroguszParser#multiply.
    def enterMultiply(self, ctx:PieroguszParser.MultiplyContext):
        pass

    # Exit a parse tree produced by PieroguszParser#multiply.
    def exitMultiply(self, ctx:PieroguszParser.MultiplyContext):
        pass


    # Enter a parse tree produced by PieroguszParser#singleValue1.
    def enterSingleValue1(self, ctx:PieroguszParser.SingleValue1Context):
        pass

    # Exit a parse tree produced by PieroguszParser#singleValue1.
    def exitSingleValue1(self, ctx:PieroguszParser.SingleValue1Context):
        pass


    # Enter a parse tree produced by PieroguszParser#positive.
    def enterPositive(self, ctx:PieroguszParser.PositiveContext):
        pass

    # Exit a parse tree produced by PieroguszParser#positive.
    def exitPositive(self, ctx:PieroguszParser.PositiveContext):
        pass


    # Enter a parse tree produced by PieroguszParser#negative.
    def enterNegative(self, ctx:PieroguszParser.NegativeContext):
        pass

    # Exit a parse tree produced by PieroguszParser#negative.
    def exitNegative(self, ctx:PieroguszParser.NegativeContext):
        pass


    # Enter a parse tree produced by PieroguszParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:PieroguszParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by PieroguszParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:PieroguszParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by PieroguszParser#ifElseStatement.
    def enterIfElseStatement(self, ctx:PieroguszParser.IfElseStatementContext):
        pass

    # Exit a parse tree produced by PieroguszParser#ifElseStatement.
    def exitIfElseStatement(self, ctx:PieroguszParser.IfElseStatementContext):
        pass


    # Enter a parse tree produced by PieroguszParser#ifStatement.
    def enterIfStatement(self, ctx:PieroguszParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PieroguszParser#ifStatement.
    def exitIfStatement(self, ctx:PieroguszParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PieroguszParser#ifBlock.
    def enterIfBlock(self, ctx:PieroguszParser.IfBlockContext):
        pass

    # Exit a parse tree produced by PieroguszParser#ifBlock.
    def exitIfBlock(self, ctx:PieroguszParser.IfBlockContext):
        pass


    # Enter a parse tree produced by PieroguszParser#elseBlock.
    def enterElseBlock(self, ctx:PieroguszParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by PieroguszParser#elseBlock.
    def exitElseBlock(self, ctx:PieroguszParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by PieroguszParser#condition.
    def enterCondition(self, ctx:PieroguszParser.ConditionContext):
        pass

    # Exit a parse tree produced by PieroguszParser#condition.
    def exitCondition(self, ctx:PieroguszParser.ConditionContext):
        pass


    # Enter a parse tree produced by PieroguszParser#lesserThan.
    def enterLesserThan(self, ctx:PieroguszParser.LesserThanContext):
        pass

    # Exit a parse tree produced by PieroguszParser#lesserThan.
    def exitLesserThan(self, ctx:PieroguszParser.LesserThanContext):
        pass


    # Enter a parse tree produced by PieroguszParser#lesserThanEqual.
    def enterLesserThanEqual(self, ctx:PieroguszParser.LesserThanEqualContext):
        pass

    # Exit a parse tree produced by PieroguszParser#lesserThanEqual.
    def exitLesserThanEqual(self, ctx:PieroguszParser.LesserThanEqualContext):
        pass


    # Enter a parse tree produced by PieroguszParser#greaterThan.
    def enterGreaterThan(self, ctx:PieroguszParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by PieroguszParser#greaterThan.
    def exitGreaterThan(self, ctx:PieroguszParser.GreaterThanContext):
        pass


    # Enter a parse tree produced by PieroguszParser#greaterThanEqual.
    def enterGreaterThanEqual(self, ctx:PieroguszParser.GreaterThanEqualContext):
        pass

    # Exit a parse tree produced by PieroguszParser#greaterThanEqual.
    def exitGreaterThanEqual(self, ctx:PieroguszParser.GreaterThanEqualContext):
        pass


    # Enter a parse tree produced by PieroguszParser#isEqual.
    def enterIsEqual(self, ctx:PieroguszParser.IsEqualContext):
        pass

    # Exit a parse tree produced by PieroguszParser#isEqual.
    def exitIsEqual(self, ctx:PieroguszParser.IsEqualContext):
        pass


    # Enter a parse tree produced by PieroguszParser#notEqual.
    def enterNotEqual(self, ctx:PieroguszParser.NotEqualContext):
        pass

    # Exit a parse tree produced by PieroguszParser#notEqual.
    def exitNotEqual(self, ctx:PieroguszParser.NotEqualContext):
        pass


    # Enter a parse tree produced by PieroguszParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:PieroguszParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by PieroguszParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:PieroguszParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by PieroguszParser#functionName.
    def enterFunctionName(self, ctx:PieroguszParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by PieroguszParser#functionName.
    def exitFunctionName(self, ctx:PieroguszParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by PieroguszParser#functionParams.
    def enterFunctionParams(self, ctx:PieroguszParser.FunctionParamsContext):
        pass

    # Exit a parse tree produced by PieroguszParser#functionParams.
    def exitFunctionParams(self, ctx:PieroguszParser.FunctionParamsContext):
        pass


    # Enter a parse tree produced by PieroguszParser#functionBlock.
    def enterFunctionBlock(self, ctx:PieroguszParser.FunctionBlockContext):
        pass

    # Exit a parse tree produced by PieroguszParser#functionBlock.
    def exitFunctionBlock(self, ctx:PieroguszParser.FunctionBlockContext):
        pass


    # Enter a parse tree produced by PieroguszParser#functionCall.
    def enterFunctionCall(self, ctx:PieroguszParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PieroguszParser#functionCall.
    def exitFunctionCall(self, ctx:PieroguszParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PieroguszParser#functionArguments.
    def enterFunctionArguments(self, ctx:PieroguszParser.FunctionArgumentsContext):
        pass

    # Exit a parse tree produced by PieroguszParser#functionArguments.
    def exitFunctionArguments(self, ctx:PieroguszParser.FunctionArgumentsContext):
        pass


    # Enter a parse tree produced by PieroguszParser#loopTimes.
    def enterLoopTimes(self, ctx:PieroguszParser.LoopTimesContext):
        pass

    # Exit a parse tree produced by PieroguszParser#loopTimes.
    def exitLoopTimes(self, ctx:PieroguszParser.LoopTimesContext):
        pass


    # Enter a parse tree produced by PieroguszParser#repetitions.
    def enterRepetitions(self, ctx:PieroguszParser.RepetitionsContext):
        pass

    # Exit a parse tree produced by PieroguszParser#repetitions.
    def exitRepetitions(self, ctx:PieroguszParser.RepetitionsContext):
        pass


    # Enter a parse tree produced by PieroguszParser#loopBlock.
    def enterLoopBlock(self, ctx:PieroguszParser.LoopBlockContext):
        pass

    # Exit a parse tree produced by PieroguszParser#loopBlock.
    def exitLoopBlock(self, ctx:PieroguszParser.LoopBlockContext):
        pass


    # Enter a parse tree produced by PieroguszParser#structureDefinition.
    def enterStructureDefinition(self, ctx:PieroguszParser.StructureDefinitionContext):
        pass

    # Exit a parse tree produced by PieroguszParser#structureDefinition.
    def exitStructureDefinition(self, ctx:PieroguszParser.StructureDefinitionContext):
        pass


    # Enter a parse tree produced by PieroguszParser#structureDeclaration.
    def enterStructureDeclaration(self, ctx:PieroguszParser.StructureDeclarationContext):
        pass

    # Exit a parse tree produced by PieroguszParser#structureDeclaration.
    def exitStructureDeclaration(self, ctx:PieroguszParser.StructureDeclarationContext):
        pass


    # Enter a parse tree produced by PieroguszParser#structFieldDef.
    def enterStructFieldDef(self, ctx:PieroguszParser.StructFieldDefContext):
        pass

    # Exit a parse tree produced by PieroguszParser#structFieldDef.
    def exitStructFieldDef(self, ctx:PieroguszParser.StructFieldDefContext):
        pass


    # Enter a parse tree produced by PieroguszParser#structureInstantiation.
    def enterStructureInstantiation(self, ctx:PieroguszParser.StructureInstantiationContext):
        pass

    # Exit a parse tree produced by PieroguszParser#structureInstantiation.
    def exitStructureInstantiation(self, ctx:PieroguszParser.StructureInstantiationContext):
        pass


    # Enter a parse tree produced by PieroguszParser#fieldInitializationList.
    def enterFieldInitializationList(self, ctx:PieroguszParser.FieldInitializationListContext):
        pass

    # Exit a parse tree produced by PieroguszParser#fieldInitializationList.
    def exitFieldInitializationList(self, ctx:PieroguszParser.FieldInitializationListContext):
        pass


    # Enter a parse tree produced by PieroguszParser#fieldInitialization.
    def enterFieldInitialization(self, ctx:PieroguszParser.FieldInitializationContext):
        pass

    # Exit a parse tree produced by PieroguszParser#fieldInitialization.
    def exitFieldInitialization(self, ctx:PieroguszParser.FieldInitializationContext):
        pass


    # Enter a parse tree produced by PieroguszParser#fieldAccess.
    def enterFieldAccess(self, ctx:PieroguszParser.FieldAccessContext):
        pass

    # Exit a parse tree produced by PieroguszParser#fieldAccess.
    def exitFieldAccess(self, ctx:PieroguszParser.FieldAccessContext):
        pass


    # Enter a parse tree produced by PieroguszParser#toIntExpression.
    def enterToIntExpression(self, ctx:PieroguszParser.ToIntExpressionContext):
        pass

    # Exit a parse tree produced by PieroguszParser#toIntExpression.
    def exitToIntExpression(self, ctx:PieroguszParser.ToIntExpressionContext):
        pass


    # Enter a parse tree produced by PieroguszParser#toFloatExpression.
    def enterToFloatExpression(self, ctx:PieroguszParser.ToFloatExpressionContext):
        pass

    # Exit a parse tree produced by PieroguszParser#toFloatExpression.
    def exitToFloatExpression(self, ctx:PieroguszParser.ToFloatExpressionContext):
        pass


    # Enter a parse tree produced by PieroguszParser#toStringExpression.
    def enterToStringExpression(self, ctx:PieroguszParser.ToStringExpressionContext):
        pass

    # Exit a parse tree produced by PieroguszParser#toStringExpression.
    def exitToStringExpression(self, ctx:PieroguszParser.ToStringExpressionContext):
        pass


    # Enter a parse tree produced by PieroguszParser#value.
    def enterValue(self, ctx:PieroguszParser.ValueContext):
        pass

    # Exit a parse tree produced by PieroguszParser#value.
    def exitValue(self, ctx:PieroguszParser.ValueContext):
        pass


    # Enter a parse tree produced by PieroguszParser#dataType.
    def enterDataType(self, ctx:PieroguszParser.DataTypeContext):
        pass

    # Exit a parse tree produced by PieroguszParser#dataType.
    def exitDataType(self, ctx:PieroguszParser.DataTypeContext):
        pass


    # Enter a parse tree produced by PieroguszParser#structureType.
    def enterStructureType(self, ctx:PieroguszParser.StructureTypeContext):
        pass

    # Exit a parse tree produced by PieroguszParser#structureType.
    def exitStructureType(self, ctx:PieroguszParser.StructureTypeContext):
        pass



del PieroguszParser