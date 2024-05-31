import sys
from antlr4 import *
from PieroguszLexer import PieroguszLexer
from PieroguszParser import PieroguszParser
from PieroguszListener import PieroguszListener
from SyntaxErrorListener import SyntaxErrorListener
from llvmlite import ir, binding


class MyPieroguszListener(PieroguszListener):
    def __init__(self):
        self.module = ir.Module(name="pierogusz")
        self.module.triple = binding.get_default_triple()
        self.builder = None
        self.func = None
        self.symbol_table = {}
        self.array_sizes = {}
        self.matrix_sizes = {}
        self.string_counter = 0  # Unique counter for string variables
        self.printf = None
        self.read_int = None
        self.read_float32 = None
        self.read_float64 = None
        self.global_fmt = None
        self.global_fmt_float32 = None
        self.global_fmt_float64 = None
        self.global_fmt_str = None
        self.global_fmt_error = None
        self.error_string_used = False  # Track if the error string is used

    def enterProgram(self, ctx: PieroguszParser.ProgramContext):
        print("Entering program")
        func_type = ir.FunctionType(ir.IntType(32), [])
        self.func = ir.Function(self.module, func_type, name="main")
        block = self.func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        # Declare the printf function
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

        # Declare the read functions
        read_int_ty = ir.FunctionType(ir.VoidType(), [ir.IntType(32).as_pointer()])
        self.read_int = ir.Function(self.module, read_int_ty, name="read_int")

        read_float32_ty = ir.FunctionType(ir.VoidType(), [ir.FloatType().as_pointer()])
        self.read_float32 = ir.Function(self.module, read_float32_ty, name="read_float32")

        read_float64_ty = ir.FunctionType(ir.VoidType(), [ir.DoubleType().as_pointer()])
        self.read_float64 = ir.Function(self.module, read_float64_ty, name="read_float64")

        # Create the global format string for integers
        fmt = "%d\n\0"
        c_fmt = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8"))
        )
        self.global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        self.global_fmt.initializer = c_fmt
        self.global_fmt.global_constant = True
        self.global_fmt.linkage = "internal"

        # Create the global format string for float32
        fmt_float32 = "%f\n\0"
        c_fmt_float32 = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(fmt_float32)),
            bytearray(fmt_float32.encode("utf8")),
        )
        self.global_fmt_float32 = ir.GlobalVariable(
            self.module, c_fmt_float32.type, name="fstr_float32"
        )
        self.global_fmt_float32.initializer = c_fmt_float32
        self.global_fmt_float32.global_constant = True
        self.global_fmt_float32.linkage = "internal"

        # Create the global format string for float64
        fmt_float64 = "%lf\n\0"
        c_fmt_float64 = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(fmt_float64)),
            bytearray(fmt_float64.encode("utf8")),
        )
        self.global_fmt_float64 = ir.GlobalVariable(
            self.module, c_fmt_float64.type, name="fstr_float64"
        )
        self.global_fmt_float64.initializer = c_fmt_float64
        self.global_fmt_float64.global_constant = True
        self.global_fmt_float64.linkage = "internal"

        # Create the global format string for strings
        fmt_str = "%s\n\0"
        c_fmt_str = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(fmt_str)), bytearray(fmt_str.encode("utf8"))
        )
        self.global_fmt_str = ir.GlobalVariable(
            self.module, c_fmt_str.type, name="fstr_str"
        )
        self.global_fmt_str.initializer = c_fmt_str
        self.global_fmt_str.global_constant = True
        self.global_fmt_str.linkage = "internal"

        # Create the global format string for error messages
        fmt_error = "Array index out of bounds\n\0"
        c_fmt_error = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(fmt_error)),
            bytearray(fmt_error.encode("utf8")),
        )
        self.global_fmt_error = ir.GlobalVariable(
            self.module, c_fmt_error.type, name="fstr_error"
        )
        self.global_fmt_error.initializer = c_fmt_error
        self.global_fmt_error.global_constant = True
        self.global_fmt_error.linkage = "internal"

    def exitProgram(self, ctx: PieroguszParser.ProgramContext):
        print("Exiting program")
        self.builder.ret(ir.Constant(ir.IntType(32), 0))
        print(self.module)
        with open("output.ll", "w") as f:
            f.write(str(self.module))

    def enterVarDecl(self, ctx: PieroguszParser.VarDeclContext):
        var_type = ctx.getChild(0).getText()
        var_name = ctx.getChild(1).getText()
        if var_type == "int":
            var = self.builder.alloca(ir.IntType(32), name=var_name)
        elif var_type == "float32":
            var = self.builder.alloca(ir.FloatType(), name=var_name)
        elif var_type == "float64":
            var = self.builder.alloca(ir.DoubleType(), name=var_name)
        elif var_type == "string":
            var = self.builder.alloca(ir.IntType(8).as_pointer(), name=var_name)
        elif var_type == "bool":
            var = self.builder.alloca(ir.IntType(1), name=var_name)
        self.symbol_table[var_name] = var
        print(f"Declared variable {var_name} of type {var_type}")

    def enterArrayDecl(self, ctx: PieroguszParser.ArrayDeclContext):
        var_type = ctx.getChild(0).getText()
        var_name = ctx.getChild(1).getText()
        size = int(ctx.getChild(3).getText())
        if var_type == "int":
            var = self.builder.alloca(ir.ArrayType(ir.IntType(32), size), name=var_name)
        elif var_type == "float32":
            var = self.builder.alloca(ir.ArrayType(ir.FloatType(), size), name=var_name)
        elif var_type == "float64":
            var = self.builder.alloca(ir.ArrayType(ir.DoubleType(), size), name=var_name)
        elif var_type == "string":
            var = self.builder.alloca(ir.ArrayType(ir.IntType(8).as_pointer(), size), name=var_name)
        elif var_type == "bool":
            var = self.builder.alloca(ir.ArrayType(ir.IntType(1), size), name=var_name)
        self.symbol_table[var_name] = var
        self.array_sizes[var_name] = size
        print(f"Declared array {var_name} of type {var_type} with size {size}")

    def enterMatrixDecl(self, ctx: PieroguszParser.MatrixDeclContext):
        var_type = ctx.getChild(0).getText()
        var_name = ctx.getChild(1).getText()
        size1 = int(ctx.getChild(3).getText())
        size2 = int(ctx.getChild(6).getText())
        if var_type == "int":
            var = self.builder.alloca(ir.ArrayType(ir.ArrayType(ir.IntType(32), size2), size1), name=var_name)
        elif var_type == "float32":
            var = self.builder.alloca(ir.ArrayType(ir.ArrayType(ir.FloatType(), size2), size1), name=var_name)
        elif var_type == "float64":
            var = self.builder.alloca(ir.ArrayType(ir.ArrayType(ir.DoubleType(), size2), size1), name=var_name)
        elif var_type == "string":
            var = self.builder.alloca(ir.ArrayType(ir.ArrayType(ir.IntType(8).as_pointer(), size2), size1), name=var_name)
        elif var_type == "bool":
            var = self.builder.alloca(ir.ArrayType(ir.ArrayType(ir.IntType(1), size2), size1), name=var_name)
        self.symbol_table[var_name] = var
        self.matrix_sizes[var_name] = (size1, size2)
        print(f"Declared matrix {var_name} of type {var_type} with sizes {size1}x{size2}")

    def enterAssignStmt(self, ctx: PieroguszParser.AssignStmtContext):
        var_name = ctx.getChild(0).getText()
        value_expr = ctx.getChild(2)
        value = self.evaluateExpression(value_expr)
        var_ptr = self.symbol_table[var_name]
        self.builder.store(value, var_ptr)
        print(f"Assigned value to variable {var_name}")

    def enterArrayAssignStmt(self, ctx: PieroguszParser.ArrayAssignStmtContext):
        var_name = ctx.getChild(0).getText()
        index_expr = ctx.getChild(2)
        value_expr = ctx.getChild(5)
        index = self.evaluateExpression(index_expr)
        value = self.evaluateExpression(value_expr)

        # Bounds checking
        with self.builder.if_then(self.builder.icmp_unsigned('>=', index, ir.Constant(ir.IntType(32), self.array_sizes[var_name]))):
            fmt_ptr = self.builder.bitcast(self.global_fmt_error, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr])
            self.builder.ret(ir.Constant(ir.IntType(32), 1))
            self.error_string_used = True

        var_ptr = self.symbol_table[var_name]
        element_ptr = self.builder.gep(var_ptr, [ir.Constant(ir.IntType(32), 0), index], inbounds=True)
        self.builder.store(value, element_ptr)
        print(f"Assigned value to array {var_name} at index {index}")

    def enterMatrixAssignStmt(self, ctx: PieroguszParser.MatrixAssignStmtContext):
        var_name = ctx.getChild(0).getText()
        index1_expr = ctx.getChild(2)
        index2_expr = ctx.getChild(5)
        value_expr = ctx.getChild(8)
        index1 = self.evaluateExpression(index1_expr)
        index2 = self.evaluateExpression(index2_expr)
        value = self.evaluateExpression(value_expr)

        # Bounds checking for the first index
        with self.builder.if_then(self.builder.icmp_unsigned('>=', index1, ir.Constant(ir.IntType(32), self.matrix_sizes[var_name][0]))):
            fmt_ptr = self.builder.bitcast(self.global_fmt_error, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr])
            self.builder.ret(ir.Constant(ir.IntType(32), 1))
            self.error_string_used = True

        # Bounds checking for the second index
        with self.builder.if_then(self.builder.icmp_unsigned('>=', index2, ir.Constant(ir.IntType(32), self.matrix_sizes[var_name][1]))):
            fmt_ptr = self.builder.bitcast(self.global_fmt_error, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr])
            self.builder.ret(ir.Constant(ir.IntType(32), 1))
            self.error_string_used = True

        var_ptr = self.symbol_table[var_name]
        element_ptr = self.builder.gep(var_ptr, [ir.Constant(ir.IntType(32), 0), index1, index2], inbounds=True)
        self.builder.store(value, element_ptr)
        print(f"Assigned value to matrix {var_name} at indices [{index1}][{index2}]")

    def enterPrintStmt(self, ctx: PieroguszParser.PrintStmtContext):
        expr = ctx.getChild(1)
        value = self.evaluateExpression(expr)

        if value.type == ir.IntType(32):
            fmt_ptr = self.builder.bitcast(self.global_fmt, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr, value])
        elif value.type == ir.FloatType():
            fmt_ptr = self.builder.bitcast(self.global_fmt_float32, ir.IntType(8).as_pointer())
            float_value = self.builder.fpext(value, ir.DoubleType())  # Extend float to double for printf
            self.builder.call(self.printf, [fmt_ptr, float_value])
        elif value.type == ir.DoubleType():
            fmt_ptr = self.builder.bitcast(self.global_fmt_float64, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr, value])
        elif value.type == ir.IntType(8).as_pointer():
            fmt_ptr = self.builder.bitcast(self.global_fmt_str, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr, value])
        elif value.type == ir.IntType(1):
            bool_value = self.builder.zext(value, ir.IntType(32))  # Zero extend to int for printf
            fmt_ptr = self.builder.bitcast(self.global_fmt, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr, bool_value])

    def enterReadStmt(self, ctx: PieroguszParser.ReadStmtContext):
        var_name = ctx.getChild(1).getText()
        var_ptr = self.symbol_table[var_name]
        var_type = var_ptr.type.pointee

        if var_type == ir.IntType(32):
            self.builder.call(self.read_int, [var_ptr])
        elif var_type == ir.FloatType():
            self.builder.call(self.read_float32, [var_ptr])
        elif var_type == ir.DoubleType():
            self.builder.call(self.read_float64, [var_ptr])

        print(f"Reading value into variable {var_name}")

    def evaluateExpression(self, ctx):
        if ctx.getChildCount() == 1:
            print(f"{ctx.getText()} ctx text")
            if ctx.INT():
                print("Entering INT block")
                return ir.Constant(ir.IntType(32), int(ctx.INT().getText()))
            elif ctx.FLOAT() or ctx.SCIENTIFIC_FLOAT():
                print("Entering FLOAT block")
                float_val = ctx.FLOAT().getText() if ctx.FLOAT() else ctx.SCIENTIFIC_FLOAT().getText()
                parent_ctx = ctx.parentCtx
                var_type = self.getExpectedType(parent_ctx)
                if var_type == ir.FloatType():
                    return ir.Constant(ir.FloatType(), float(float_val))
                elif var_type == ir.DoubleType():
                    return ir.Constant(ir.DoubleType(), float(float_val))
            elif ctx.STRING():
                print("Entering STRING block")
                str_val = ctx.STRING().getText()
                str_val = str_val[1:-1]  # Remove the surrounding quotes
                str_const = ir.Constant(
                    ir.ArrayType(ir.IntType(8), len(str_val) + 1),
                    bytearray(str_val.encode("utf8")) + b"\00",
                )
                global_str_name = f"str_{self.string_counter}"
                self.string_counter += 1
                global_str = ir.GlobalVariable(
                    self.module, str_const.type, name=global_str_name
                )
                global_str.initializer = str_const
                global_str.global_constant = True
                global_str.linkage = "internal"
                return self.builder.bitcast(global_str, ir.IntType(8).as_pointer())
            elif ctx.getText() == "true" or ctx.getText() == "false":
                print("Entering BOOL block")
                bool_val = ctx.getText() == "true"
                return ir.Constant(ir.IntType(1), bool_val)
            elif ctx.ID():
                var_name = ctx.ID().getText()
                print(f"Entering ID block: {var_name} -- var_name")
                print(f"{self.symbol_table} -- symbol table")
                if var_name in self.symbol_table:
                    var_ptr = self.symbol_table[var_name]
                    return self.builder.load(var_ptr, name=var_name)
                else:
                    raise RuntimeError(f"Undefined variable: {var_name}")
        elif ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            print("Entering array indexing block")
            var_name = ctx.ID().getText()
            index_expr = ctx.getChild(2)
            index = self.evaluateExpression(index_expr)

            # Bounds checking
            with self.builder.if_then(self.builder.icmp_unsigned('>=', index, ir.Constant(ir.IntType(32), self.array_sizes[var_name]))):
                fmt_ptr = self.builder.bitcast(self.global_fmt_error, ir.IntType(8).as_pointer())
                self.builder.call(self.printf, [fmt_ptr])
                self.builder.ret(ir.Constant(ir.IntType(32), 1))
                self.error_string_used = True

            var_ptr = self.symbol_table[var_name]
            element_ptr = self.builder.gep(var_ptr, [ir.Constant(ir.IntType(32), 0), index], inbounds=True)
            return self.builder.load(element_ptr, name=f"{var_name}_elem")
        elif ctx.getChildCount() == 7 and ctx.getChild(4).getText() == '[':
            print("Entering matrix indexing block")
            var_name = ctx.ID().getText()
            index1_expr = ctx.getChild(2)
            index2_expr = ctx.getChild(5)
            index1 = self.evaluateExpression(index1_expr)
            index2 = self.evaluateExpression(index2_expr)

            # Bounds checking for the first index
            with self.builder.if_then(self.builder.icmp_unsigned('>=', index1, ir.Constant(ir.IntType(32), self.matrix_sizes[var_name][0]))):
                fmt_ptr = self.builder.bitcast(self.global_fmt_error, ir.IntType(8).as_pointer())
                self.builder.call(self.printf, [fmt_ptr])
                self.builder.ret(ir.Constant(ir.IntType(32), 1))
                self.error_string_used = True

            # Bounds checking for the second index
            with self.builder.if_then(self.builder.icmp_unsigned('>=', index2, ir.Constant(ir.IntType(32), self.matrix_sizes[var_name][1]))):
                fmt_ptr = self.builder.bitcast(self.global_fmt_error, ir.IntType(8).as_pointer())
                self.builder.call(self.printf, [fmt_ptr])
                self.builder.ret(ir.Constant(ir.IntType(32), 1))
                self.error_string_used = True

            var_ptr = self.symbol_table[var_name]
            element_ptr = self.builder.gep(var_ptr, [ir.Constant(ir.IntType(32), 0), index1, index2], inbounds=True)
            return self.builder.load(element_ptr, name=f"{var_name}_elem")
        elif ctx.getChildCount() == 3:
            print("Entering binary operation block")
            left = self.evaluateExpression(ctx.getChild(0))
            right = self.evaluateExpression(ctx.getChild(2))
            op = ctx.getChild(1).getText()

            if left.type == ir.IntType(32) and right.type == ir.IntType(32):
                if op == "+":
                    return self.builder.add(left, right, name="addtmp")
                elif op == "-":
                    return self.builder.sub(left, right, name="subtmp")
                elif op == "*":
                    return self.builder.mul(left, right, name="multmp")
                elif op == "/":
                    return self.builder.sdiv(left, right, name="divtmp")
            elif left.type == ir.FloatType() and right.type == ir.FloatType():
                if op == "+":
                    return self.builder.fadd(left, right, name="addtmp")
                elif op == "-":
                    return self.builder.fsub(left, right, name="subtmp")
                elif op == "*":
                    return self.builder.fmul(left, right, name="multmp")
                elif op == "/":
                    return self.builder.fdiv(left, right, name="divtmp")
            elif left.type == ir.DoubleType() and right.type == ir.DoubleType():
                if op == "+":
                    return self.builder.fadd(left, right, name="addtmp")
                elif op == "-":
                    return self.builder.fsub(left, right, name="subtmp")
                elif op == "*":
                    return self.builder.fmul(left, right, name="multmp")
                elif op == "/":
                    return self.builder.fdiv(left, right, name="divtmp")
            elif left.type == ir.IntType(1) and right.type == ir.IntType(1):
                if op == "AND":
                    return self.builder.and_(left, right, name="andtmp")
                elif op == "OR":
                    return self.builder.or_(left, right, name="ortmp")
                elif op == "XOR":
                    return self.builder.xor(left, right, name="xortmp")
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "NEG":
            print("Entering NEG operation block")
            operand = self.evaluateExpression(ctx.getChild(1))
            if operand.type == ir.IntType(1):
                return self.builder.not_(operand, name="negtmp")

        raise RuntimeError("Unsupported expression")

    def getExpectedType(self, parent_ctx):
        # This method attempts to determine the expected type of an expression
        # based on its context (e.g., variable declarations, assignments)
        if isinstance(parent_ctx, PieroguszParser.VarDeclContext):
            var_type = parent_ctx.getChild(0).getText()
            if var_type == "float32":
                return ir.FloatType()
            elif var_type == "float64":
                return ir.DoubleType()
            elif var_type == "bool":
                return ir.IntType(1)
        elif isinstance(parent_ctx, PieroguszParser.AssignStmtContext):
            var_name = parent_ctx.getChild(0).getText()
            var_ptr = self.symbol_table.get(var_name)
            if var_ptr is not None:
                pointee_type = var_ptr.type.pointee
                return pointee_type
        elif isinstance(parent_ctx, PieroguszParser.ArrayAssignStmtContext):
            var_name = parent_ctx.getChild(0).getText()
            var_ptr = self.symbol_table.get(var_name)
            if var_ptr is not None:
                array_type = var_ptr.type.pointee
                return array_type.element
        elif isinstance(parent_ctx, PieroguszParser.MatrixAssignStmtContext):
            var_name = parent_ctx.getChild(0).getText()
            var_ptr = self.symbol_table.get(var_name)
            if var_ptr is not None:
                matrix_type = var_ptr.type.pointee
                return matrix_type.element.element

        return ir.FloatType()  # Default to float32 if unsure


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = PieroguszLexer(input_stream)
    lexer._listeners = [SyntaxErrorListener()]
    stream = CommonTokenStream(lexer)
    parser = PieroguszParser(stream)
    parser._listeners = [SyntaxErrorListener()]
    tree = parser.program()
    lexer_errors = lexer._listeners[0].getErrors()
    parser_errors = parser._listeners[0].getErrors()

    if lexer_errors or parser_errors:
        return 1

    printer = MyPieroguszListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    return 0


if __name__ == "__main__":
    result = main(sys.argv)
    if result == 1:
        print("Errors were found during lexical and syntax analysis.")
        sys.exit(result)
