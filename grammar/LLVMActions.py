import sys
from collections import deque
from LLVMGenerator import LLVMGenerator
from PieroguszListener import PieroguszListener
from PieroguszParser import PieroguszParser
from ScopeManager import scope_manager
from Models import VarType, Value

BUFFER_SIZE = 16


class LLVMActions(PieroguszListener):
    def __init__(self):
#         self.local_vars = {}
        self.stack = deque()
        self.reg_counter = 0
        self.functions = {}
        self.current_function_name = None
        self.skip_variableDeclaration = False

    # Enter a parse tree produced by PieroguszParser#prog.
#     def enterProg(self, ctx: PieroguszParser.ProgContext):

    # Exit a parse tree produced by PieroguszParser#prog.
    def exitProg(self, ctx):
        LLVMGenerator.close_main()
        with open("output.ll", "w") as file:
            file.write(LLVMGenerator.generate())

    #         print(LLVMGenerator.generate())

    # Enter a parse tree produced by PieroguszParser#block.
    def enterBlock(self, ctx: PieroguszParser.BlockContext):
        scope_manager.enter_scope()

    # Exit a parse tree produced by PieroguszParser#block.
    def exitBlock(self, ctx: PieroguszParser.BlockContext):
        scope_manager.exit_scope()
        pass

    # Exit a parse tree produced by PieroguszParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx: PieroguszParser.VariableDeclarationContext):
        ID = ctx.ID().getText()
        type_key = ctx.dataType()
        var_type = VarType.UNKNOWN

        if type_key.INT_KEY() is not None:
            var_type = VarType.INT
        elif type_key.FLOAT_KEY() is not None:
            var_type = VarType.FLOAT
        elif type_key.STRING_KEY() is not None:
            var_type = VarType.STRING
        elif type_key.BOOL_KEY() is not None:
            var_type = VarType.BOOLEAN

        scoped_id = scope_manager.declare_variable(ID, Value(ID, var_type, 0))
        self.declare_type(var_type, scoped_id, scope_manager.is_global())

    def declare_type(self, type: VarType, scoped_id, is_global):
        if type == VarType.INT:
            LLVMGenerator.declare_i32(scoped_id, is_global)
        if type == VarType.FLOAT:
            LLVMGenerator.declare_double(scoped_id, is_global)
        if type == VarType.STRING:
            LLVMGenerator.declare_string(scoped_id, is_global)
        if type == VarType.BOOLEAN:
            LLVMGenerator.declare_bool(scoped_id, is_global)

    # Exit a parse tree produced by PieroguszParser#assignment.
    def exitAssignment(self, ctx: PieroguszParser.AssignmentContext):
        ID = ctx.ID().getText()
        v = self.stack.pop()
        variable = scope_manager.lookup_variable(ID)
        if variable:
            scoped_id = scope_manager.assign_value_to_variable(ID, v)
            self.assign_value(scoped_id, v)
        else:
            error(ctx.getRuleIndex(), f"unknown variable {ID}")

    def assign_value(self, scoped_id, v: Value):
        if v.type == VarType.INT:
            LLVMGenerator.assign_i32(scoped_id, v.name)
        if v.type == VarType.FLOAT:
            LLVMGenerator.assign_double(scoped_id, v.name)
        if v.type == VarType.STRING:
            LLVMGenerator.assign_string(scoped_id)
        if v.type == VarType.BOOLEAN:
            LLVMGenerator.assign_bool(scoped_id, v.name)

    def exitValue(self, ctx: PieroguszParser.ValueContext):
        if ctx.ID() is not None:
            ID = ctx.ID().getText()
            print(ID)
            try:
                current_fparams = self.functions[self.current_function_name]["params"]
                if ID in current_fparams:
                    print("ID in params", current_fparams[ID])
                    current_fparams[ID].name = f"%{ID}"
                    self.stack.append(current_fparams[ID])
                    return
            except:
                print('Not a function param inside function')

            try:
                v = scope_manager.lookup_variable(ID)
                scoped_id = scope_manager.get_scoped_id(ID)
                self.load_variable_value(scoped_id, v.type)
                print('exitValue ID', scoped_id)
            except KeyError as e:
                error(ctx.start.line, f"Undefined variable {ID}")

        if ctx.INT() is not None:
            self.stack.append(Value(ctx.INT().getText(), VarType.INT, 0))

        if ctx.FLOAT() is not None:
            self.stack.append(Value(ctx.FLOAT().getText(), VarType.FLOAT, 0))

        if ctx.STRING() is not None:
            # tmp = ctx.STRING().getText()
            # content = tmp[1:len(tmp) - 1]
            # LLVMGenerator.constant_string(content)
            # n = "%ptrstr" + str(LLVMGenerator.str - 1)
            # self.stack.append(Value(n, VarType.STRING, len(content)))
            str_content = ctx.STRING().getText()[1:-1]  # Remove quotes
            self.handle_string_literal(str_content)

        if ctx.BOOL() is not None:
            # self.stack.append(Value(ctx.BOOL().getText(), VarType.BOOLEAN, 0))
            bool_value = True if ctx.BOOL().getText() == 'true' else False
            self.stack.append(Value(bool_value, VarType.BOOLEAN, 0))

    def load_variable_value(self, scoped_id, value_type):
        print("load_variable_value scoped_id", scoped_id)
        LLVMGenerator.load_variable(scoped_id, value_type)
        self.stack.append(Value(scoped_id, value_type, None))

    def handle_string_literal(self, content):
        # Directly use the method to create a global string and load it
        global_string_id = LLVMGenerator.constant_string(content)
#         loaded_string_ptr = LLVMGenerator.load_string(global_string_id)
        self.stack.append(Value(global_string_id, VarType.STRING, len(content)))
#
#     def handle_string_literal(self, content):
#         # Create a unique global string constant in LLVM
#         global_string_id = LLVMGenerator.create_global_string(content)
#         self.stack.append(Value(global_string_id, VarType.STRING, len(content)))

    # Exit a parse tree produced by PieroguszParser#printCall.
    def exitPrintCall(self, ctx: PieroguszParser.PrintCallContext):
        ID = ctx.ID().getText()
        variable = scope_manager.lookup_variable(ID)
        if variable:
            self.print_value(variable, scope_manager.get_scoped_id(ID))  # Assuming a generalized print function
        else:
            error(ctx.getRuleIndex(), f"unknown variable {ID}")

    def print_value(self, v, scoped_id):
        print("print_value", scoped_id, "is function param",self.is_function_param(scoped_id))
        if not self.is_function_param(scoped_id):
            LLVMGenerator.load_variable(scoped_id, v.type)
            tmp = f"%tmp.{LLVMGenerator.reg-1}"
            scoped_id = tmp
        else:
            scoped_id = scoped_id[0] + self.extract_substring(scoped_id)

        print("print_value", scoped_id)

        if v.type == VarType.INT:
            LLVMGenerator.printf_i32(scoped_id)
        if v.type == VarType.FLOAT:
            LLVMGenerator.printf_double(scoped_id)
        if v.type == VarType.STRING:
            LLVMGenerator.printf_string(scoped_id)
        if v.type == VarType.BOOLEAN:
            LLVMGenerator.printf_boolean(scoped_id)

    # Exit a parse tree produced by PieroguszParser#readCall.
    def exitReadCall(self, ctx: PieroguszParser.ReadCallContext):
        ID = ctx.ID().getText()
        variable = scope_manager.lookup_variable(ID)
        scoped_id = scope_manager.get_scoped_id(ID)
        if variable:
            self.read_value(scoped_id, variable)  # Assuming a generalized print function
        else:
            error(ctx.getRuleIndex(), f"unknown variable {ID}")

    def read_value(self, scoped_id, v: Value):
        if v.type == VarType.INT:
            LLVMGenerator.scanf_i32(scoped_id)
        if v.type == VarType.FLOAT:
            LLVMGenerator.scanf_double(scoped_id)
        if v.type == VarType.STRING:
            LLVMGenerator.scanf_string(scoped_id, v.length or BUFFER_SIZE)
        if v.type == VarType.BOOLEAN:
            LLVMGenerator.scanf_boolean(scoped_id)

    # Exit a parse tree produced by PieroguszParser#add.
    def exitAdd(self, ctx: PieroguszParser.AddContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if v1.type == VarType.INT and v2.type == VarType.INT:
            LLVMGenerator.add_i32(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.INT, 0))
        elif v1.type == VarType.FLOAT and v2.type == VarType.FLOAT:
            LLVMGenerator.add_double(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        elif ((v1.type == VarType.INT and v2.type == VarType.FLOAT) or
              (v1.type == VarType.FLOAT and v2.type == VarType.INT)):
            # For the case when one value is an integer and the other is a float,
            # we will convert the integer to float and then add
            if v1.type == VarType.INT:
                LLVMGenerator.int_to_float(v1.name)  # convert int to float
                v1.name = f"%tmp.{LLVMGenerator.reg - 1}"
                v1.type = VarType.FLOAT
            else:
                LLVMGenerator.int_to_float(v2.name)  # convert int to float
                v2.name = f"%tmp.{LLVMGenerator.reg - 1}"
                v2.type = VarType.FLOAT
            LLVMGenerator.add_double(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        elif v1.type == VarType.STRING and v2.type == VarType.STRING:
            tmp_string_id = "%tmp." + str(LLVMGenerator.reg - 3)
            LLVMGenerator.add_string(v1.name, v2.name, tmp_string_id, v1.length, v2.length)
            self.stack.append(Value(tmp_string_id, VarType.STRING, v1.length + v2.length))

        else:
            error(ctx.getRuleIndex(), "invalid operand types for addition operation")

    # Exit a parse tree produced by PieroguszParser#substract.
    def exitSubstract(self, ctx: PieroguszParser.SubstractContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()

        if v1.type == VarType.INT and v2.type == VarType.INT:
            LLVMGenerator.sub_i32(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.INT, 0))
        elif v1.type == VarType.FLOAT and v2.type == VarType.FLOAT:
            LLVMGenerator.sub_double(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        elif ((v1.type == VarType.INT and v2.type == VarType.FLOAT) or
              (v1.type == VarType.FLOAT and v2.type == VarType.INT)):
            # For the case when one value is an integer and the other is a float,
            # we will convert the integer to float and then subtract
            if v1.type == VarType.INT:
                LLVMGenerator.int_to_float(v1.name)  # convert int to float
                v1.name = f"%tmp.{LLVMGenerator.reg - 1}"
                v1.type = VarType.FLOAT
            else:
                LLVMGenerator.int_to_float(v2.name)  # convert int to float
                v2.name = f"%tmp.{LLVMGenerator.reg - 1}"
                v2.type = VarType.FLOAT
            LLVMGenerator.sub_double(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        else:
            error(ctx.getRuleIndex(), "invalid operand types for subtraction operation")

    # Exit a parse tree produced by PieroguszParser#multiply.
    def exitMultiply(self, ctx: PieroguszParser.MultiplyContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if v1.type == VarType.INT and v2.type == VarType.INT:
            LLVMGenerator.mul_i32(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.INT, 0))
        elif v1.type == VarType.FLOAT and v2.type == VarType.FLOAT:
            LLVMGenerator.mul_double(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        elif ((v1.type == VarType.INT and v2.type == VarType.FLOAT) or
              (v1.type == VarType.FLOAT and v2.type == VarType.INT)):
            # For the case when one value is an integer and the other is a float,
            # we will convert the integer to float and then multiply
            if v1.type == VarType.INT:
                LLVMGenerator.int_to_float(v1.name)  # convert int to float
                v1.name = f"%tmp.{LLVMGenerator.reg - 1}"
                v1.type = VarType.FLOAT
            else:
                LLVMGenerator.int_to_float(v2.name)  # convert int to float
                v2.name = f"%tmp.{LLVMGenerator.reg - 1}"
                v2.type = VarType.FLOAT
            LLVMGenerator.mul_double(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        else:
            error(ctx.getRuleIndex(), "invalid operand types for multiplication operation")

    # Exit a parse tree produced by PieroguszParser#divide.
    def exitDivide(self, ctx: PieroguszParser.DivideContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if v1.type == VarType.INT and v2.type == VarType.INT:
            LLVMGenerator.div_i32(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.INT, 0))
        elif v1.type == VarType.FLOAT and v2.type == VarType.FLOAT:
            LLVMGenerator.div_double(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        elif ((v1.type == VarType.INT and v2.type == VarType.FLOAT) or
              (v1.type == VarType.FLOAT and v2.type == VarType.INT)):
            # For the case when one value is an integer and the other is a float,
            # we will convert the integer to float and then divide
            if v1.type == VarType.INT:
                LLVMGenerator.int_to_float(v1.name)  # convert int to float
                v1.name = f"%tmp.{LLVMGenerator.reg - 1}"
                v1.type = VarType.FLOAT
            else:
                LLVMGenerator.int_to_float(v2.name)  # convert int to float
                v2.name = f"%tmp.{LLVMGenerator.reg - 1}"
                v2.type = VarType.FLOAT
            LLVMGenerator.div_double(v1.name, v2.name)
            self.stack.append(Value("%tmp." + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        else:
            error(ctx.getRuleIndex(), "invalid operand types for division operation")

    def exitAnd(self, ctx: PieroguszParser.AndContext):
        right = self.stack.pop()
        left = self.stack.pop()
        left_bool = self.convert_to_bool(left)
        right_bool = self.convert_to_bool(right)
        result = LLVMGenerator.logical_and(left_bool, right_bool)
        self.stack.append(Value(result, VarType.BOOLEAN, 0))

    def exitOr(self, ctx: PieroguszParser.OrContext):
        right = self.stack.pop()
        left = self.stack.pop()
        left_bool = self.convert_to_bool(left)
        right_bool = self.convert_to_bool(right)
        result = LLVMGenerator.logical_or(left_bool, right_bool)
        self.stack.append(Value(result, VarType.BOOLEAN, 0))

    def exitXor(self, ctx: PieroguszParser.XorContext):
        right = self.stack.pop()
        left = self.stack.pop()
        left_bool = self.convert_to_bool(left)
        right_bool = self.convert_to_bool(right)
        result = LLVMGenerator.logical_xor(left_bool, right_bool)
        self.stack.append(Value(result, VarType.BOOLEAN, 0))

    def exitNegation(self, ctx: PieroguszParser.NegationContext):
        v = self.stack.pop()
        bool = self.convert_to_bool(v)
        result = LLVMGenerator.logical_neg(bool)
        self.stack.append(Value(result, VarType.BOOLEAN, 0))

    def exitEqual(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()

        left_bool = self.convert_to_bool(left)
        right_bool = self.convert_to_bool(right)

        result = LLVMGenerator.logical_eq(left_bool, right_bool)
        self.stack.append(Value(result, VarType.BOOLEAN, 0))

    def exitToIntExpression(self, ctx: PieroguszParser.ToIntExpressionContext):
        value = self.stack.pop()
        if value.type == VarType.FLOAT:
            LLVMGenerator.float_to_int(value.name)  # Correctly call the conversion method
            converted_value = Value(f"%tmp.{LLVMGenerator.reg - 1}", VarType.INT, 0)
        elif value.type == VarType.INT:
            # If it's already INT, no conversion needed, but you should handle this logic
            converted_value = value
        else:
            error(ctx.getRuleIndex(), "unsupported conversion type to int")
            return

        self.stack.append(converted_value)

    def exitToFloatExpression(self, ctx: PieroguszParser.ToFloatExpressionContext):
        value = self.stack.pop()

        if value.type == VarType.INT:
            LLVMGenerator.int_to_float(value.name)  # Correctly call the conversion method
            converted_value = Value(f"%tmp.{LLVMGenerator.reg - 1}", VarType.FLOAT, 0)
        elif value.type == VarType.FLOAT:
            # If it's already FLOAT, no conversion needed, but you should handle this logic
            converted_value = value
        else:
            error(ctx.getRuleIndex(), "unsupported conversion type to float")
            return
        self.stack.append(converted_value)

    # Exit a parse tree produced by PieroguszParser#toStringExpression.
    def exitToStringExpression(self, ctx: PieroguszParser.ToStringExpressionContext):
        value = self.stack.pop()
        if value.type == VarType.INT:
            error(ctx.getRuleIndex(), "unsupported conversion type to string")
        if value.type == VarType.FLOAT:
            error(ctx.getRuleIndex(), "unsupported conversion type to string")
        if value.type == VarType.STRING:
            # If it's already FLOAT, no conversion needed, but you should handle this logic
            converted_value = value
        else:
            error(ctx.getRuleIndex(), "unsupported conversion type to string")
            return
        self.stack.append(converted_value)

    def convert_to_bool(self, value):
        if value.type == VarType.INT:
            return LLVMGenerator.int_to_bool(value.name)
        elif value.type == VarType.FLOAT:
            return LLVMGenerator.float_to_bool(value.name)
        elif value.type == VarType.STRING:
            return LLVMGenerator.string_to_bool(value.name)
        elif value.type == VarType.BOOLEAN:
            return LLVMGenerator.generate_boolean(value.name)
        else:
            raise ValueError("Unsupported type for logical operations")

    def exitLoopBlock(self, ctx:PieroguszParser.LoopBlockContext):
        if isinstance(ctx.parentCtx, PieroguszParser.LoopTimesContext):
            LLVMGenerator.loopend()

    def exitRepetitions(self, ctx:PieroguszParser.RepetitionsContext):
        int = ctx.INT()
        if int is not None:
            LLVMGenerator.loopstart(int)
        else:
            error(ctx.getRuleIndex, 'wrong number')

    # Enter a parse tree produced by PieroguszParser#ifBlock.
    def enterIfBlock(self, ctx:PieroguszParser.IfBlockContext):
        LLVMGenerator.ifstart()

    # Exit a parse tree produced by PieroguszParser#ifBlock.
    def exitIfBlock(self, ctx:PieroguszParser.IfBlockContext):
        LLVMGenerator.ifend()

    # Enter a parse tree produced by PieroguszParser#ifBlock.
    def enterElseBlock(self, ctx:PieroguszParser.ElseBlockContext):
        LLVMGenerator.elsestart()

    # Exit a parse tree produced by PieroguszParser#elseBlock.
    def exitElseBlock(self, ctx:PieroguszParser.ElseBlockContext):
        LLVMGenerator.elseend()


    def enterFunctionDefinition(self, ctx: PieroguszParser.FunctionDefinitionContext):
        scope_manager.enter_scope()
        self.current_function_name = ctx.functionName().getText()
        self.functions[self.current_function_name] = {'name': self.current_function_name}

    def exitFunctionDefinition(self, ctx: PieroguszParser.FunctionDefinitionContext):
        LLVMGenerator.function_end(self.current_function_name)
        self.current_function_name = None
        scope_manager.exit_scope()

#     Exit a parse tree produced by PieroguszParser#functionParams.
#     def enterFunctionParams(self, ctx:PieroguszParser.FunctionParamsContext):
#         self.skip_variableDeclaration = True

    # Exit a parse tree produced by PieroguszParser#functionParams.
    def exitFunctionParams(self, ctx:PieroguszParser.FunctionParamsContext):
        params = {}
        for i, param in enumerate(ctx.variableDeclaration()):
            id = param.ID().getText()
            var_type = self.get_var_type_from_declaration(param.dataType())
            params[id] = Value(id, var_type, None)
        self.functions[self.current_function_name]['params'] = params
        LLVMGenerator.function_start(self.current_function_name, params)
#         scope_manager.exit_scope()
#         self.skip_variableDeclaration = False


    def get_var_type_from_declaration(self, dataType):
        if dataType.INT_KEY():
            return VarType.INT
        elif dataType.FLOAT_KEY():
            return VarType.FLOAT
        elif dataType.STRING_KEY():
            return VarType.STRING
        elif dataType.BOOL_KEY():
            return VarType.BOOLEAN
        return VarType.UNKNOWN

    def enterFunctionCall(self, ctx: PieroguszParser.FunctionCallContext):
        func_name = ctx.functionName().getText()
        if func_name not in self.functions:
            raise Exception(f"Function {func_name} not defined")
        self.current_function_name = func_name

    def exitFunctionCall(self, ctx: PieroguszParser.FunctionCallContext):
        func_name = ctx.functionName().getText()
        func_info = self.functions.get(func_name)
        if not func_info:
            raise Exception(f"Function {func_name} not defined")

        arguments = []
        if ctx.functionArguments():
            params = self.functions[self.current_function_name]['params']
            if len(ctx.functionArguments().value()) == len(params):
                print("Params length OK!")
            else:
                error(ctx.getRuleIndex(), "Provided params don't match expected ones")

            for arg in reversed(ctx.functionArguments().value()):
                print("arg", arg.getText())
                v = self.stack.pop()
                try:
                    v = scope_manager.lookup_variable(arg.getText())
                    print("try name", v.name)
#                     scoped_id = scope_manager.get_scoped_id(arg.getText())
#                     print(scoped_id)
                    arguments.append({"type": v.type, "val": v.name})
#                     print('arg', scoped_id)
                except Exception as e:
                    arguments.append({"type": v.type, "val": arg.getText()})
        # Generate code to call the function
        print("func_name call: ",func_name)
        arguments.reverse()
        LLVMGenerator.function_call(func_name, arguments)
        self.current_function_name = None

    def is_function_param(self, id):
        try:
            core_id = self.extract_substring(id)
            current_fparams = self.functions[self.current_function_name]["params"]
            if id in current_fparams:
                return True
            if core_id in current_fparams:
                return True
        except:
            return False

    def extract_substring(self, s):
        start_index = 1  # Start from the second character
        end_index = s.find('.')  # Find the index of the first dot
        if end_index == -1:  # Dot not found
            return s[start_index:]  # Return the substring from the second character to the end
        return s[start_index:end_index]  # Return the substring up to the first dot

    #3 compare
#     def exitLesserThan(self, ctx):
#         left_id = ctx.ID(0).getText()
#         right_value = ctx.value().getText()  # Assuming value returns a textual representation
#         result_reg = f"%{self.get_new_reg()}"
#         LLVMGenerator.compare_lt(left_id, right_value, result_reg)
#
#     def exitLesserThanEqual(self, ctx):
#         left_id = ctx.ID(0).getText()
#         right_value = ctx.value().getText()
#         result_reg = f"%{self.get_new_reg()}"
#         LLVMGenerator.compare_lte(left_id, right_value, result_reg)
#
#     def exitGreaterThan(self, ctx):
#         left_id = ctx.ID().getText()
#         right_value = ctx.value().getText()
#         result_reg = f"%{self.get_new_reg()}"
#         LLVMGenerator.compare_gt(left_id, right_value, result_reg)
#
#     def exitGreaterThanEqual(self, ctx):
#         left_id = ctx.ID(0).getText()
#         right_value = ctx.value().getText()
#         result_reg = f"%{self.get_new_reg()}"
#         LLVMGenerator.compare_gte(left_id, right_value, result_reg)
#
#     def exitIsEqual(self, ctx):
#         left_id = ctx.ID(0).getText()
#         right_value = ctx.value().getText()
#         result_reg = f"%{self.get_new_reg()}"
#         LLVMGenerator.compare_eq(left_id, right_value, result_reg)
#
#     def exitNotEqual(self, ctx):
#         left_id = ctx.ID(0).getText()
#         right_value = ctx.value().getText()
#         result_reg = f"%{self.get_new_reg()}"
#         LLVMGenerator.compare_neq(left_id, right_value, result_reg)

def error(line, msg):
    print("Error, line " + str(line) + ", " + msg, file=sys.stderr)
    sys.exit(1)
