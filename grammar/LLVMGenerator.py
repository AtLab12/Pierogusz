from Models import VarType
llvm_type = {
    VarType.INT: "i32",
    VarType.FLOAT: "double",
    VarType.STRING: "i8",
    VarType.BOOLEAN: "i1"
}

class LLVMGenerator:
    header_text = ""
    main_text = ""
    main_tmp = 1
    reg = 1
    str = 1
    br = 0
    buffer = ""
    brstack = []
    elsestan= 0
    functions = {}


    ##################### DECLARE ################################
    @staticmethod
    def declare_i32(id, global_=False):
        if global_:
            LLVMGenerator.header_text += f"{id} = global i32 0\n"
        else:
            LLVMGenerator.buffer += f"{id} = alloca i32\n"

    @staticmethod
    def declare_double(id, global_=False):
        if global_:
            LLVMGenerator.header_text += f"{id} = global double 0.0\n"
        else:
            LLVMGenerator.buffer += f"{id} = alloca double\n"

    @staticmethod
    def declare_string(id, global_=False):
        if global_:
            LLVMGenerator.header_text += f"{id} = private unnamed_addr global [1 x i8] zeroinitializer\n"
        else:
            LLVMGenerator.buffer += f"{id} = alloca i8*\n"

    @staticmethod
    def declare_bool(id, global_=False):
        if global_:
            LLVMGenerator.header_text += f"{id} = global i1 false\n"
        else:
            LLVMGenerator.buffer += f"{id} = alloca i1\n"

    ##################### ASSIGN ################################
    @staticmethod
    def assign_i32(scoped_id, value):
        LLVMGenerator.buffer += f"store i32 {value}, i32* {scoped_id}\n"

    @staticmethod
    def assign_double(scoped_id, value):
        LLVMGenerator.buffer += f"store double {value}, double* {scoped_id}\n"

    @staticmethod
    def assign_bool(scoped_id, value):
        val = 'true' if value else 'false'
        LLVMGenerator.buffer += f"store i1 {val}, i1* {scoped_id}\n"

    @staticmethod
    def assign_string(scoped_id):
        LLVMGenerator.buffer += f"store i8* %tmp.{LLVMGenerator.reg - 1}, i8** {scoped_id}\n"


    ##################### LOAD ################################
    @staticmethod
    def load_i32(scoped_id):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = load i32, i32* {scoped_id}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def load_double(scoped_id):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = load double, double* {scoped_id}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def load_bool(scoped_id):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = load i1, i1* {scoped_id}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def load_string(scoped_id):
        LLVMGenerator.string_pointer()
#         LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = load i8*, i8** {scoped_id}\n"
#         LLVMGenerator.reg += 1

    @staticmethod
    def load_variable(scoped_id, type):
        if type == VarType.INT:
            LLVMGenerator.load_i32(scoped_id)
        elif type == VarType.FLOAT:
            LLVMGenerator.load_double(scoped_id)
        elif type == VarType.STRING:
#             LLVMGenerator.load_string(scoped_id)
            return
        elif type == VarType.BOOLEAN:
            LLVMGenerator.load_bool(scoped_id)


    ##################### PRINT ################################

    @staticmethod
    def printf_i32(id):
#         LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = load i32, i32* {id}\n"
#         LLVMGenerator.reg += 1
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 {id})\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def printf_double(id):
#         LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = load double, double* {id}\n"
#         LLVMGenerator.reg += 1
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %tmp.{LLVMGenerator.reg - 1})\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def printf_boolean(scoped_id):
        # Assuming scoped_id is an i1 (boolean in LLVM)
        # First, extend it to an integer for printing
#         LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = load i1, i1* {scoped_id}\n"
        bool_reg = LLVMGenerator.reg
#         LLVMGenerator.reg += 1

        # Select the appropriate string based on the boolean value
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = select i1 %tmp.{bool_reg-1}, i8* getelementptr inbounds ([6 x i8], [6 x i8]* @strTrue, i32 0, i32 0), i8* getelementptr inbounds ([7 x i8], [7 x i8]* @strFalse, i32 0, i32 0)\n"
        str_reg = LLVMGenerator.reg
        LLVMGenerator.reg += 1

        # Print the selected string
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = call i32 (i8*, ...) @printf(i8* %tmp.{str_reg})\n"
        LLVMGenerator.reg += 1

        # Return the register that potentially holds the result from printf (not generally used)
        return f"%tmp.{LLVMGenerator.reg}"

    @staticmethod
    def printf_string(id):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = load i8*, i8** {id}\n"
        LLVMGenerator.reg += 1
        # Correct the format string to use `%s` for printing strings
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %tmp.{LLVMGenerator.reg - 1})\n"
        LLVMGenerator.reg += 1


    ##################### SCAN ################################

    @staticmethod
    def scanf_i32(scoped_id):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strsi, i32 0, i32 0), i32* {scoped_id})\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def scanf_double(scoped_id):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strsd, i32 0, i32 0), double* {scoped_id})\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def scanf_string(id, l):
        LLVMGenerator.buffer += f"{id} = alloca [{l+1} x i8]\n"
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = getelementptr [{l+1} x i8], [{l+1} x i8]* {id}, i32 0, i32 0\n"
        ptr_reg = LLVMGenerator.reg
        LLVMGenerator.reg += 1
        LLVMGenerator.buffer += f"call i32 (i8*, ...) @scanf(i8* getelementptr ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i8* %tmp.{ptr_reg})\n"

#         string_id = f"str{LLVMGenerator.str}"
#         LLVMGenerator.allocate_string(string_id, l)
#         # Get the pointer to the start of the array to pass to scanf
#         LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = getelementptr inbounds [{l + 1} x i8], [{l + 1} x i8]* {string_id}, i64 0, i64 0\n"
#         ptr_reg = LLVMGenerator.reg
#         LLVMGenerator.reg += 1
#         # Store the pointer in the provided identifier (assuming id is an i8**)
#         LLVMGenerator.buffer += f"store i8* %{ptr_reg}, i8** %{id}\n"
#         LLVMGenerator.str += 1
#         # Call scanf with the format string for reading a line
#         format_string = "@strs"  # Ensure this global variable has %[^\n]s as its content
#         LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* {format_string}, i32 0, i32 0), i8* %{ptr_reg})\n"
#         LLVMGenerator.reg += 1

    @staticmethod
    def scanf_boolean(value_reg):
        # Allocate space for the integer input
        temp_int_reg = f"%tmp.{LLVMGenerator.reg}"
        LLVMGenerator.buffer += f"{temp_int_reg} = alloca i32\n"
        LLVMGenerator.reg += 1

        # Read integer using scanf into the allocated space
        LLVMGenerator.buffer += f"call i32 (i8*, ...) @scanf(i8* getelementptr ([3 x i8], [3 x i8]* @.strsbool, i32 0, i32 0), i32* {temp_int_reg})\n"

        # Load the integer from the allocated space into a new register
        loaded_int_reg = LLVMGenerator.reg
        LLVMGenerator.buffer += f"%{loaded_int_reg} = load i32, i32* %{temp_int_reg}\n"
        LLVMGenerator.reg += 1

        # Convert the loaded integer to a boolean (i1)
        bool_reg = LLVMGenerator.reg
        LLVMGenerator.buffer += f"%{bool_reg} = icmp ne i32 0, %{loaded_int_reg}\n"  # true if not zero
        LLVMGenerator.reg += 1

        # Store the boolean result at the original value_reg (assumed to be a pointer to i1)
        LLVMGenerator.buffer += f"store i1 %{bool_reg}, i1* %{value_reg}\n"

        return f"%{bool_reg}"


    ######################## STRING #######################

    @staticmethod
    def constant_string(content):
        l = len(content) + 1
        global_id = f"@str.{LLVMGenerator.str}"
        LLVMGenerator.header_text += f"{global_id} = private unnamed_addr constant [{l} x i8] c\"{content}\\00\"\n"
        LLVMGenerator.str += 1
        return global_id  # Returns the name of the global string

#     @staticmethod
#     def load_string(id):
#         # This assumes id is a pointer to a pointer (i8**)
#         LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = load i8*, i8** {id}\n"
#         LLVMGenerator.reg += 1
#         return f"%tmp.{LLVMGenerator.reg - 1}"

#     @staticmethod
#     def constant_string(content):
#         l = len(content) + 1
#         LLVMGenerator.header_text += f"@str{LLVMGenerator.str} = constant [{l} x i8] c\"{content}\\00\"\n"
#         n = f"str{LLVMGenerator.str}"
#         LLVMGenerator.allocate_string(n, (l - 1))
#         LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = bitcast [{l} x i8]* %{n} to i8*\n"
#         LLVMGenerator.buffer += f"call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %tmp.{LLVMGenerator.reg}, i8* align 1 getelementptr inbounds ([{l} x i8], [{l} x i8]* @{n}, i32 0, i32 0), i64 {l}, i1 false)\n"
#         LLVMGenerator.reg += 1
#         LLVMGenerator.buffer += f"%ptr{n} = alloca i8*\n"
#         LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = getelementptr inbounds [{l} x i8], [{l} x i8]* %{n}, i64 0, i64 0\n"
#         LLVMGenerator.reg += 1
#         LLVMGenerator.buffer += f"store i8* %tmp.{LLVMGenerator.reg - 1}, i8** %ptr{n}\n"
#         LLVMGenerator.str += 1

    @staticmethod
    def string_pointer(id, l):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = getelementptr inbounds [{l + 1} x i8], [{l + 1} x i8]* %{id}, i64 0, i64 0\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def allocate_string(id, length):
        LLVMGenerator.buffer += "%" + id + " = alloca [" + str(length + 1) + " x i8]\n"

#     @staticmethod
#     def create_global_string(content):
#         # Assume unique identifier generation
#         unique_id = f"@.str{len(content)}"
#         print(f"{unique_id} = private unnamed_addr constant [{len(content)+1} x i8] c\"{content}\\00\"")
#         return unique_id

    ######################## MATH #######################

    @staticmethod
    def get_var_for_math(val, type: VarType):
        tmp = val
        if val[0] == '@':
            LLVMGenerator.load_variable(val, type)
            tmp = f"%tmp.{LLVMGenerator.reg-1}"
        return tmp

    @staticmethod
    def get_vars_for_math(val1, val2, type: VarType):
        tmp_val1 = LLVMGenerator.get_var_for_math(val1, type)
        tmp_val2 = LLVMGenerator.get_var_for_math(val2, type)
        return tmp_val1, tmp_val2

    @staticmethod
    def add_i32(val1, val2):
        tmp_val1, tmp_val2 = LLVMGenerator.get_vars_for_math(val1, val2, VarType.INT)

        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = add i32 {tmp_val1}, {tmp_val2}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def add_double(val1, val2):
        tmp_val1, tmp_val2 = LLVMGenerator.get_vars_for_math(val1, val2, VarType.FLOAT)
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = fadd double {tmp_val1}, {tmp_val2}\n"
        LLVMGenerator.reg += 1

#     @staticmethod
#     def add_string(id1, l1, id2, l2):
#         # NIE DZIAŁA
#         total_length = l1 + l2 + 1  # +1 for the null terminator
#         LLVMGenerator.allocate_string(f"concat_str", total_length)
#         concat_ptr = f"%concat_str"
#         LLVMGenerator.buffer += f"%tmp1 = call i8* @strcpy(i8* {concat_ptr}, i8* {id1})\n"
#         LLVMGenerator.reg += 1
#         LLVMGenerator.buffer += f"%tmp2 = call i8* @strcat(i8* {concat_ptr}, i8* {id2})\n"
#         LLVMGenerator.reg += 1
#
    def add_string(id1, id2, result_id, l1, l2):
        total_length = int(l1) + int(l2)
        LLVMGenerator.buffer += f"{result_id} = alloca [{total_length + 1} x i8]\n"
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = call i8* @strcat(i8* getelementptr ([{l1 + 1} x i8], [{l1 + 1} x i8]* {id1}, i32 0, i32 0), getelementptr ([{l2 + 1} x i8], [{l2 + 1} x i8]* {id2}, i32 0, i32 0))\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def sub_i32(val1, val2):
        tmp_val1, tmp_val2 = LLVMGenerator.get_vars_for_math(val1, val2, VarType.INT)
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = sub i32 {tmp_val2}, {tmp_val1}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def sub_double(val1, val2):
        tmp_val1, tmp_val2 = LLVMGenerator.get_vars_for_math(val1, val2, VarType.FLOAT)
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = fsub double {tmp_val2}, {tmp_val1}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def div_i32(val1, val2):
        tmp_val1, tmp_val2 = LLVMGenerator.get_vars_for_math(val1, val2, VarType.INT)
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = sdiv i32 {tmp_val2}, {tmp_val1}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def div_double(val1, val2):
        tmp_val1, tmp_val2 = LLVMGenerator.get_vars_for_math(val1, val2, VarType.FLOAT)
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = fdiv double {tmp_val2}, {tmp_val1}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def mul_i32(val1, val2):
        tmp_val1, tmp_val2 = LLVMGenerator.get_vars_for_math(val1, val2, VarType.INT)
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = mul i32 {tmp_val1}, {tmp_val2}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def mul_double(val1, val2):
        tmp_val1, tmp_val2 = LLVMGenerator.get_vars_for_math(val1, val2, VarType.FLOAT)
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = fmul double {tmp_val1}, {tmp_val2}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def int_to_float(id):
        tmp_val = LLVMGenerator.get_var_for_math(id, VarType.INT)

        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = sitofp i32 {tmp_val} to double\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def float_to_int(id):
        tmp_val = LLVMGenerator.get_var_for_math(id, VarType.FLOAT)
        # LLVMGenerator.load_variable(id, VarType.FLOAT)
        # tmp_val1 = f"%tmp.{LLVMGenerator.reg-1}"

        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = fptosi double {tmp_val} to i32\n"
        LLVMGenerator.reg += 1

    ###################### LOGIC #######################
    @staticmethod
    def generate_boolean(value):
        val = 'true' if value else 'false'
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = add i1 {val}, false\n"  # Simple way to assign a boolean value to a register
        LLVMGenerator.reg += 1
        return f"%tmp.{LLVMGenerator.reg - 1}"

    @staticmethod
    def int_to_bool(value):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = icmp ne i32 {value}, 0\n"
        LLVMGenerator.reg += 1
        return f"%tmp.{LLVMGenerator.reg - 1}"

    @staticmethod
    def float_to_bool(value):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = fcmp one double {value}, 0.0\n"
        LLVMGenerator.reg += 1
        return f"%tmp.{LLVMGenerator.reg - 1}"

    @staticmethod
    def string_to_bool(value):
        first_char = f"%tmp.{LLVMGenerator.reg} = load i8, i8* {value}\n"
        LLVMGenerator.reg += 1
        result = f"%tmp.{LLVMGenerator.reg} = icmp ne i8 {first_char}, 0\n"
        LLVMGenerator.buffer += result
        LLVMGenerator.reg += 1
        return f"%tmp.{LLVMGenerator.reg - 1}"

    @staticmethod
    def icmp(id, value):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = load i32, i32* %{id}\n"
        LLVMGenerator.reg += 1
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = icmp eq i32 %tmp.{LLVMGenerator.reg - 1},{value}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def logical_eq(left, right, type='i1'):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = icmp eq {type} {left}, {right}\n"
        LLVMGenerator.reg += 1
        return f"%tmp.{LLVMGenerator.reg - 1}"

    @staticmethod
    def logical_and(op1, op2):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = and i1 {op1}, {op2}\n"
        LLVMGenerator.reg += 1
        return f"%tmp.{LLVMGenerator.reg - 1}"

    @staticmethod
    def logical_or(op1, op2):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = or i1 {op1}, {op2}\n"
        LLVMGenerator.reg += 1
        return f"%tmp.{LLVMGenerator.reg - 1}"

    @staticmethod
    def logical_xor(op1, op2):
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = xor i1 {op1}, {op2}\n"
        LLVMGenerator.reg += 1
        return f"%tmp.{LLVMGenerator.reg - 1}"

    @staticmethod
    def logical_neg(op):
        # XOR with 1 performs negation on a boolean
        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = xor i1 {op}, 1\n"
        LLVMGenerator.reg += 1
        return f"%tmp.{LLVMGenerator.reg - 1}"


    ################################ LOOP #########################################################
    @staticmethod
    def loopstart(repetitions):
        counter_id = f"%loop.{LLVMGenerator.reg}"
        LLVMGenerator.declare_i32(counter_id, False)
        LLVMGenerator.assign_i32(counter_id, 0)
        LLVMGenerator.br += 1
        LLVMGenerator.buffer += f"br label %cond{LLVMGenerator.br}\n"
        LLVMGenerator.buffer += f"cond{LLVMGenerator.br}:\n"

        LLVMGenerator.load_i32(counter_id)
        LLVMGenerator.add_i32(f"%tmp.{LLVMGenerator.reg-1}", "1")
        LLVMGenerator.assign_i32(counter_id, f"%tmp.{LLVMGenerator.reg-1}")

        LLVMGenerator.buffer += f"%tmp.{LLVMGenerator.reg} = icmp slt i32 %tmp.{LLVMGenerator.reg-2}, {repetitions}\n"
        LLVMGenerator.reg += 1

        LLVMGenerator.buffer += f"br i1 %tmp.{LLVMGenerator.reg-1}, label %true{LLVMGenerator.br}, label %false{LLVMGenerator.br}\n"
        LLVMGenerator.buffer += f"true{LLVMGenerator.br}:\n"
        LLVMGenerator.brstack.append(LLVMGenerator.br)

    @staticmethod
    def loopend():
        b =  LLVMGenerator.brstack.pop()
        LLVMGenerator.buffer += f"br label %cond{b}\n"
        LLVMGenerator.buffer += f"false{b}:\n"


    ################################ IF #########################################################
    @staticmethod
    def ifstart():
        LLVMGenerator.br += 1
        LLVMGenerator.elsestan = LLVMGenerator.reg-1
        LLVMGenerator.buffer += f"br i1 %tmp.{LLVMGenerator.reg-1}, label %true{LLVMGenerator.br}, label %false{LLVMGenerator.br}\n"
        LLVMGenerator.buffer += f"true{LLVMGenerator.br}:\n"
        LLVMGenerator.brstack.append(LLVMGenerator.br)

    @staticmethod
    def ifend():
        b =  LLVMGenerator.brstack.pop()
        LLVMGenerator.buffer += f"br label %false{b}\n"
        LLVMGenerator.buffer += f"false{b}:\n"


    @staticmethod
    def elsestart():
        LLVMGenerator.br += 1
        # Branch to the 'else' block if the condition is false
        LLVMGenerator.buffer += f"br i1 %tmp.{LLVMGenerator.elsestan}, label %true{LLVMGenerator.br}, label %false{LLVMGenerator.br}\n"
        LLVMGenerator.buffer += f"false{LLVMGenerator.br}:\n"
        LLVMGenerator.brstack.append(LLVMGenerator.br)

    @staticmethod
    def elseend():
        b =  LLVMGenerator.brstack.pop()
        LLVMGenerator.buffer += f"br label %true{b}\n"
        LLVMGenerator.buffer += f"true{b}:\n"

    ################################ FUNCTIONS #########################################################

    @staticmethod
    def function_start(name, params):
        LLVMGenerator.main_text += LLVMGenerator.buffer
        LLVMGenerator.buffer = ""
        LLVMGenerator.main_tmp = LLVMGenerator.reg
        param_code = ', '.join([f"{llvm_type[p.type]} %{p.name}" for p in params.values()])
        LLVMGenerator.buffer += f"define void @{name}({param_code}){{\n"
        LLVMGenerator.reg = 1

    @staticmethod
    def function_end(name):
        LLVMGenerator.buffer += "  ret void\n"
        LLVMGenerator.buffer += "}\n"
        LLVMGenerator.header_text += LLVMGenerator.buffer
        LLVMGenerator.buffer = ""
        LLVMGenerator.reg = LLVMGenerator.main_tmp

    @staticmethod
    def function_call(name, arguments):
        # Prepare argument list for passing to the function
        arg_list = ', '.join([f"{llvm_type[arg['type']]} {arg['val']}" for arg in arguments])
#         LLVMGenerator.buffer += f"  %call{LLVMGenerator.reg} = call void @{name}({arg_list})\n"
        LLVMGenerator.buffer += f" call void @{name}({arg_list})\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def close_main():
        LLVMGenerator.main_text += LLVMGenerator.buffer

    @staticmethod
    def generate():
        text = ""
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @scanf(i8*, ...)\n"
        text += "declare i8* @strcpy(i8*, i8*)\n"
        text += "declare i8* @strcat(i8*, i8*)\n"
        text += "declare i32 @atoi(i8*)\n"
        text += "declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg)\n"
        text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
        text += "@strps = constant [4 x i8] c\"%s\\0A\\00\"\n"
        text += "@strsi = constant [3 x i8] c\"%d\\00\"\n"
        text += "@strsd = constant [4 x i8] c\"%lf\\00\"\n"
        # text += "@strs = constant [3 x i8] c\"%s10\00\"\n"
        text += "@strs = constant [6 x i8] c\"%[^\n]\00\"\n"
        text += "@strspi = constant [3 x i8] c\"%d\00\"\n"
        text += "@.strpbool = constant [3 x i8] c\"%d\\00\"\n"

        # Prepare the true and false strings as global constants
        text += "@strTrue = private unnamed_addr constant [6 x i8] c\"true\\0A\\00\"\n"
        text += "@strFalse = private unnamed_addr constant [7 x i8] c\"false\\0A\\00\"\n"

        text += "\n"
        text += LLVMGenerator.header_text
        text += "define i32 @main() nounwind {\n"
        text += LLVMGenerator.main_text
        text += "  ret i32 0\n"
        text += "}\n"
        return text


generator = LLVMGenerator()
