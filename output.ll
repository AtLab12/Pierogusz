; ModuleID = "pierogusz"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = bitcast [15 x i8]* @"str_0" to i8*
  %".3" = bitcast [4 x i8]* @"fstr_str" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  %"intArr" = alloca [2 x i32]
  %".5" = icmp uge i32 0, 2
  br i1 %".5", label %"entry.if", label %"entry.endif"
entry.if:
  %".7" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7")
  ret i32 1
entry.endif:
  %".10" = getelementptr inbounds [2 x i32], [2 x i32]* %"intArr", i32 0, i32 0
  store i32 10, i32* %".10"
  %".12" = icmp uge i32 1, 2
  br i1 %".12", label %"entry.endif.if", label %"entry.endif.endif"
entry.endif.if:
  %".14" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14")
  ret i32 1
entry.endif.endif:
  %".17" = getelementptr inbounds [2 x i32], [2 x i32]* %"intArr", i32 0, i32 1
  store i32 20, i32* %".17"
  %".19" = icmp uge i32 0, 2
  br i1 %".19", label %"entry.endif.endif.if", label %"entry.endif.endif.endif"
entry.endif.endif.if:
  %".21" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21")
  ret i32 1
entry.endif.endif.endif:
  %".24" = getelementptr inbounds [2 x i32], [2 x i32]* %"intArr", i32 0, i32 0
  %"intArr_elem" = load i32, i32* %".24"
  %".25" = bitcast [4 x i8]* @"fstr" to i8*
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".25", i32 %"intArr_elem")
  %".27" = icmp uge i32 1, 2
  br i1 %".27", label %"entry.endif.endif.endif.if", label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.if:
  %".29" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29")
  ret i32 1
entry.endif.endif.endif.endif:
  %".32" = getelementptr inbounds [2 x i32], [2 x i32]* %"intArr", i32 0, i32 1
  %"intArr_elem.1" = load i32, i32* %".32"
  %".33" = bitcast [4 x i8]* @"fstr" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", i32 %"intArr_elem.1")
  %"floatArr" = alloca [2 x float]
  %".35" = icmp uge i32 0, 2
  br i1 %".35", label %"entry.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.if:
  %".37" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".38" = call i32 (i8*, ...) @"printf"(i8* %".37")
  ret i32 1
entry.endif.endif.endif.endif.endif:
  %".40" = getelementptr inbounds [2 x float], [2 x float]* %"floatArr", i32 0, i32 0
  store float 0x40091eb860000000, float* %".40"
  %".42" = icmp uge i32 1, 2
  br i1 %".42", label %"entry.endif.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.if:
  %".44" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".44")
  ret i32 1
entry.endif.endif.endif.endif.endif.endif:
  %".47" = getelementptr inbounds [2 x float], [2 x float]* %"floatArr", i32 0, i32 1
  store float 0x4005ae1480000000, float* %".47"
  %".49" = icmp uge i32 0, 2
  br i1 %".49", label %"entry.endif.endif.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.endif.if:
  %".51" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51")
  ret i32 1
entry.endif.endif.endif.endif.endif.endif.endif:
  %".54" = getelementptr inbounds [2 x float], [2 x float]* %"floatArr", i32 0, i32 0
  %"floatArr_elem" = load float, float* %".54"
  %".55" = bitcast [4 x i8]* @"fstr_float" to i8*
  %".56" = call i32 (i8*, ...) @"printf"(i8* %".55", float %"floatArr_elem")
  %".57" = icmp uge i32 1, 2
  br i1 %".57", label %"entry.endif.endif.endif.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.endif.endif.if:
  %".59" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".60" = call i32 (i8*, ...) @"printf"(i8* %".59")
  ret i32 1
entry.endif.endif.endif.endif.endif.endif.endif.endif:
  %".62" = getelementptr inbounds [2 x float], [2 x float]* %"floatArr", i32 0, i32 1
  %"floatArr_elem.1" = load float, float* %".62"
  %".63" = bitcast [4 x i8]* @"fstr_float" to i8*
  %".64" = call i32 (i8*, ...) @"printf"(i8* %".63", float %"floatArr_elem.1")
  %"stringArr" = alloca [2 x i8*]
  %".65" = bitcast [6 x i8]* @"str_1" to i8*
  %".66" = icmp uge i32 0, 2
  br i1 %".66", label %"entry.endif.endif.endif.e...if", label %"entry.endif.endif.endif.e...endif"
entry.endif.endif.endif.e...if:
  %".68" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".69" = call i32 (i8*, ...) @"printf"(i8* %".68")
  ret i32 1
entry.endif.endif.endif.e...endif:
  %".71" = getelementptr inbounds [2 x i8*], [2 x i8*]* %"stringArr", i32 0, i32 0
  store i8* %".65", i8** %".71"
  %".73" = bitcast [6 x i8]* @"str_2" to i8*
  %".74" = icmp uge i32 1, 2
  br i1 %".74", label %"entry.endif.endif.endif.e...endif.if", label %"entry.endif.endif.endif.e...endif.endif"
entry.endif.endif.endif.e...endif.if:
  %".76" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".77" = call i32 (i8*, ...) @"printf"(i8* %".76")
  ret i32 1
entry.endif.endif.endif.e...endif.endif:
  %".79" = getelementptr inbounds [2 x i8*], [2 x i8*]* %"stringArr", i32 0, i32 1
  store i8* %".73", i8** %".79"
  %".81" = icmp uge i32 0, 2
  br i1 %".81", label %"entry.endif.endif.endif.e...endif.endif.if", label %"entry.endif.endif.endif.e...endif.endif.endif"
entry.endif.endif.endif.e...endif.endif.if:
  %".83" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".84" = call i32 (i8*, ...) @"printf"(i8* %".83")
  ret i32 1
entry.endif.endif.endif.e...endif.endif.endif:
  %".86" = getelementptr inbounds [2 x i8*], [2 x i8*]* %"stringArr", i32 0, i32 0
  %"stringArr_elem" = load i8*, i8** %".86"
  %".87" = bitcast [4 x i8]* @"fstr_str" to i8*
  %".88" = call i32 (i8*, ...) @"printf"(i8* %".87", i8* %"stringArr_elem")
  %".89" = icmp uge i32 1, 2
  br i1 %".89", label %"entry.endif.endif.endif.e...endif.endif.endif.if", label %"entry.endif.endif.endif.e...endif.endif.endif.endif"
entry.endif.endif.endif.e...endif.endif.endif.if:
  %".91" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".92" = call i32 (i8*, ...) @"printf"(i8* %".91")
  ret i32 1
entry.endif.endif.endif.e...endif.endif.endif.endif:
  %".94" = getelementptr inbounds [2 x i8*], [2 x i8*]* %"stringArr", i32 0, i32 1
  %"stringArr_elem.1" = load i8*, i8** %".94"
  %".95" = bitcast [4 x i8]* @"fstr_str" to i8*
  %".96" = call i32 (i8*, ...) @"printf"(i8* %".95", i8* %"stringArr_elem.1")
  %".97" = icmp uge i32 2, 2
  br i1 %".97", label %"entry.endif.endif.endif.e...if.1", label %"entry.endif.endif.endif.e...endif.1"
entry.endif.endif.endif.e...if.1:
  %".99" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".100" = call i32 (i8*, ...) @"printf"(i8* %".99")
  ret i32 1
entry.endif.endif.endif.e...endif.1:
  %".102" = getelementptr inbounds [2 x i32], [2 x i32]* %"intArr", i32 0, i32 2
  %"intArr_elem.2" = load i32, i32* %".102"
  %".103" = bitcast [4 x i8]* @"fstr" to i8*
  %".104" = call i32 (i8*, ...) @"printf"(i8* %".103", i32 %"intArr_elem.2")
  %".105" = icmp uge i32 2, 2
  br i1 %".105", label %"entry.endif.endif.endif.e...endif.1.if", label %"entry.endif.endif.endif.e...endif.1.endif"
entry.endif.endif.endif.e...endif.1.if:
  %".107" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".108" = call i32 (i8*, ...) @"printf"(i8* %".107")
  ret i32 1
entry.endif.endif.endif.e...endif.1.endif:
  %".110" = getelementptr inbounds [2 x float], [2 x float]* %"floatArr", i32 0, i32 2
  %"floatArr_elem.2" = load float, float* %".110"
  %".111" = bitcast [4 x i8]* @"fstr_float" to i8*
  %".112" = call i32 (i8*, ...) @"printf"(i8* %".111", float %"floatArr_elem.2")
  %".113" = icmp uge i32 2, 2
  br i1 %".113", label %"entry.endif.endif.endif.e...endif.1.endif.if", label %"entry.endif.endif.endif.e...endif.1.endif.endif"
entry.endif.endif.endif.e...endif.1.endif.if:
  %".115" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".116" = call i32 (i8*, ...) @"printf"(i8* %".115")
  ret i32 1
entry.endif.endif.endif.e...endif.1.endif.endif:
  %".118" = getelementptr inbounds [2 x i8*], [2 x i8*]* %"stringArr", i32 0, i32 2
  %"stringArr_elem.2" = load i8*, i8** %".118"
  %".119" = bitcast [4 x i8]* @"fstr_str" to i8*
  %".120" = call i32 (i8*, ...) @"printf"(i8* %".119", i8* %"stringArr_elem.2")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

declare void @"read_int"(i32* %".1")

declare void @"read_float"(float* %".1")

@"fstr" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_float" = internal constant [4 x i8] c"%f\0a\00"
@"fstr_str" = internal constant [4 x i8] c"%s\0a\00"
@"fstr_error" = internal constant [27 x i8] c"Array index out of bounds\0a\00"
@"str_0" = internal constant [15 x i8] c"Testing arrays\00"
@"str_1" = internal constant [6 x i8] c"hello\00"
@"str_2" = internal constant [6 x i8] c"world\00"