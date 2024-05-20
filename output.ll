; ModuleID = "pierogusz"
target triple = "arm64-apple-darwin23.4.0"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 5, i32* %"x"
  %"x.1" = load i32, i32* %"x"
  %".3" = bitcast [4 x i8]* @"fstr" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %"x.1")
  %"y" = alloca float
  store float 0x400921fb00000000, float* %"y"
  %"y.1" = load float, float* %"y"
  %".6" = bitcast [4 x i8]* @"fstr_float" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", float %"y.1")
  %"p" = alloca float
  store float 0x3ff1f84fe0000000, float* %"p"
  %"p.1" = load float, float* %"p"
  %".9" = bitcast [4 x i8]* @"fstr_float" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", float %"p.1")
  %"x1" = alloca i32
  store i32 8, i32* %"x1"
  %"x1.1" = load i32, i32* %"x1"
  %".12" = bitcast [4 x i8]* @"fstr" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %"x1.1")
  %"xSum" = alloca i32
  %"x.2" = load i32, i32* %"x"
  %"x1.2" = load i32, i32* %"x1"
  %"addtmp" = add i32 %"x.2", %"x1.2"
  store i32 %"addtmp", i32* %"xSum"
  %"xSum.1" = load i32, i32* %"xSum"
  %".15" = bitcast [4 x i8]* @"fstr" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %"xSum.1")
  %"xSub" = alloca i32
  %"x1.3" = load i32, i32* %"x1"
  %"x.3" = load i32, i32* %"x"
  %"subtmp" = sub i32 %"x1.3", %"x.3"
  store i32 %"subtmp", i32* %"xSub"
  %"xSub.1" = load i32, i32* %"xSub"
  %".18" = bitcast [4 x i8]* @"fstr" to i8*
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", i32 %"xSub.1")
  %"xMul" = alloca i32
  %"x.4" = load i32, i32* %"x"
  %"x1.4" = load i32, i32* %"x1"
  %"multmp" = mul i32 %"x.4", %"x1.4"
  store i32 %"multmp", i32* %"xMul"
  %"xMul.1" = load i32, i32* %"xMul"
  %".21" = bitcast [4 x i8]* @"fstr" to i8*
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21", i32 %"xMul.1")
  %"xDiv" = alloca i32
  %"x1.5" = load i32, i32* %"x1"
  %"divtmp" = sdiv i32 %"x1.5", 4
  store i32 %"divtmp", i32* %"xDiv"
  %"xDiv.1" = load i32, i32* %"xDiv"
  %".24" = bitcast [4 x i8]* @"fstr" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %"xDiv.1")
  %"readTest" = alloca float
  call void @"read_float"(float* %"readTest")
  %"readTest.1" = load float, float* %"readTest"
  %".27" = bitcast [4 x i8]* @"fstr_float" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", float %"readTest.1")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

declare void @"read_int"(i32* %".1")

declare void @"read_float"(float* %".1")

@"fstr" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_float" = internal constant [4 x i8] c"%f\0a\00"