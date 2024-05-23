; ModuleID = "pierogusz"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"x" = alloca float
  %"y" = alloca double
  store float 0x47efffffe0000000, float* %"x"
  store double 0x7ff0000000000000, double* %"y"
  %"x.1" = load float, float* %"x"
  %".4" = bitcast [4 x i8]* @"fstr_float32" to i8*
  %".5" = fpext float %"x.1" to double
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".4", double %".5")
  %"y.1" = load double, double* %"y"
  %".7" = bitcast [5 x i8]* @"fstr_float64" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"y.1")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

declare void @"read_int"(i32* %".1")

declare void @"read_float32"(float* %".1")

declare void @"read_float64"(double* %".1")

@"fstr" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_float32" = internal constant [4 x i8] c"%f\0a\00"
@"fstr_float64" = internal constant [5 x i8] c"%lf\0a\00"
@"fstr_str" = internal constant [4 x i8] c"%s\0a\00"
@"fstr_error" = internal constant [27 x i8] c"Array index out of bounds\0a\00"