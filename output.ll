; ModuleID = "pierogusz"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"matrix" = alloca [2 x [3 x i32]]
  %".2" = icmp uge i32 0, 2
  br i1 %".2", label %"entry.if", label %"entry.endif"
entry.if:
  %".4" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  ret i32 1
entry.endif:
  %".7" = icmp uge i32 0, 3
  br i1 %".7", label %"entry.endif.if", label %"entry.endif.endif"
entry.endif.if:
  %".9" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9")
  ret i32 1
entry.endif.endif:
  %".12" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 0, i32 0
  store i32 1, i32* %".12"
  %".14" = icmp uge i32 0, 2
  br i1 %".14", label %"entry.endif.endif.if", label %"entry.endif.endif.endif"
entry.endif.endif.if:
  %".16" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16")
  ret i32 1
entry.endif.endif.endif:
  %".19" = icmp uge i32 1, 3
  br i1 %".19", label %"entry.endif.endif.endif.if", label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.if:
  %".21" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21")
  ret i32 1
entry.endif.endif.endif.endif:
  %".24" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 0, i32 1
  store i32 2, i32* %".24"
  %".26" = icmp uge i32 0, 2
  br i1 %".26", label %"entry.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.if:
  %".28" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".29" = call i32 (i8*, ...) @"printf"(i8* %".28")
  ret i32 1
entry.endif.endif.endif.endif.endif:
  %".31" = icmp uge i32 2, 3
  br i1 %".31", label %"entry.endif.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.if:
  %".33" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33")
  ret i32 1
entry.endif.endif.endif.endif.endif.endif:
  %".36" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 0, i32 2
  store i32 3, i32* %".36"
  %".38" = icmp uge i32 1, 2
  br i1 %".38", label %"entry.endif.endif.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.endif.if:
  %".40" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40")
  ret i32 1
entry.endif.endif.endif.endif.endif.endif.endif:
  %".43" = icmp uge i32 0, 3
  br i1 %".43", label %"entry.endif.endif.endif.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif.endif.endif.if:
  %".45" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".46" = call i32 (i8*, ...) @"printf"(i8* %".45")
  ret i32 1
entry.endif.endif.endif.endif.endif.endif.endif.endif:
  %".48" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 1, i32 0
  store i32 4, i32* %".48"
  %".50" = icmp uge i32 1, 2
  br i1 %".50", label %"entry.endif.endif.endif.e...if", label %"entry.endif.endif.endif.e...endif"
entry.endif.endif.endif.e...if:
  %".52" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".53" = call i32 (i8*, ...) @"printf"(i8* %".52")
  ret i32 1
entry.endif.endif.endif.e...endif:
  %".55" = icmp uge i32 1, 3
  br i1 %".55", label %"entry.endif.endif.endif.e...endif.if", label %"entry.endif.endif.endif.e...endif.endif"
entry.endif.endif.endif.e...endif.if:
  %".57" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".58" = call i32 (i8*, ...) @"printf"(i8* %".57")
  ret i32 1
entry.endif.endif.endif.e...endif.endif:
  %".60" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 1, i32 1
  store i32 5, i32* %".60"
  %".62" = icmp uge i32 1, 2
  br i1 %".62", label %"entry.endif.endif.endif.e...endif.endif.if", label %"entry.endif.endif.endif.e...endif.endif.endif"
entry.endif.endif.endif.e...endif.endif.if:
  %".64" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".65" = call i32 (i8*, ...) @"printf"(i8* %".64")
  ret i32 1
entry.endif.endif.endif.e...endif.endif.endif:
  %".67" = icmp uge i32 2, 3
  br i1 %".67", label %"entry.endif.endif.endif.e...endif.endif.endif.if", label %"entry.endif.endif.endif.e...endif.endif.endif.endif"
entry.endif.endif.endif.e...endif.endif.endif.if:
  %".69" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".70" = call i32 (i8*, ...) @"printf"(i8* %".69")
  ret i32 1
entry.endif.endif.endif.e...endif.endif.endif.endif:
  %".72" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 1, i32 2
  store i32 6, i32* %".72"
  %".74" = icmp uge i32 0, 2
  br i1 %".74", label %"entry.endif.endif.endif.e...if.1", label %"entry.endif.endif.endif.e...endif.1"
entry.endif.endif.endif.e...if.1:
  %".76" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".77" = call i32 (i8*, ...) @"printf"(i8* %".76")
  ret i32 1
entry.endif.endif.endif.e...endif.1:
  %".79" = icmp uge i32 0, 3
  br i1 %".79", label %"entry.endif.endif.endif.e...endif.1.if", label %"entry.endif.endif.endif.e...endif.1.endif"
entry.endif.endif.endif.e...endif.1.if:
  %".81" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".82" = call i32 (i8*, ...) @"printf"(i8* %".81")
  ret i32 1
entry.endif.endif.endif.e...endif.1.endif:
  %".84" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 0, i32 0
  %"matrix_elem" = load i32, i32* %".84"
  %".85" = bitcast [4 x i8]* @"fstr" to i8*
  %".86" = call i32 (i8*, ...) @"printf"(i8* %".85", i32 %"matrix_elem")
  %".87" = icmp uge i32 0, 2
  br i1 %".87", label %"entry.endif.endif.endif.e...endif.1.endif.if", label %"entry.endif.endif.endif.e...endif.1.endif.endif"
entry.endif.endif.endif.e...endif.1.endif.if:
  %".89" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".90" = call i32 (i8*, ...) @"printf"(i8* %".89")
  ret i32 1
entry.endif.endif.endif.e...endif.1.endif.endif:
  %".92" = icmp uge i32 1, 3
  br i1 %".92", label %"entry.endif.endif.endif.e...endif.1.endif.endif.if", label %"entry.endif.endif.endif.e...endif.1.endif.endif.endif"
entry.endif.endif.endif.e...endif.1.endif.endif.if:
  %".94" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".95" = call i32 (i8*, ...) @"printf"(i8* %".94")
  ret i32 1
entry.endif.endif.endif.e...endif.1.endif.endif.endif:
  %".97" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 0, i32 1
  %"matrix_elem.1" = load i32, i32* %".97"
  %".98" = bitcast [4 x i8]* @"fstr" to i8*
  %".99" = call i32 (i8*, ...) @"printf"(i8* %".98", i32 %"matrix_elem.1")
  %".100" = icmp uge i32 0, 2
  br i1 %".100", label %"entry.endif.endif.endif.e...if.2", label %"entry.endif.endif.endif.e...endif.2"
entry.endif.endif.endif.e...if.2:
  %".102" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".103" = call i32 (i8*, ...) @"printf"(i8* %".102")
  ret i32 1
entry.endif.endif.endif.e...endif.2:
  %".105" = icmp uge i32 2, 3
  br i1 %".105", label %"entry.endif.endif.endif.e...endif.2.if", label %"entry.endif.endif.endif.e...endif.2.endif"
entry.endif.endif.endif.e...endif.2.if:
  %".107" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".108" = call i32 (i8*, ...) @"printf"(i8* %".107")
  ret i32 1
entry.endif.endif.endif.e...endif.2.endif:
  %".110" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 0, i32 2
  %"matrix_elem.2" = load i32, i32* %".110"
  %".111" = bitcast [4 x i8]* @"fstr" to i8*
  %".112" = call i32 (i8*, ...) @"printf"(i8* %".111", i32 %"matrix_elem.2")
  %".113" = icmp uge i32 1, 2
  br i1 %".113", label %"entry.endif.endif.endif.e...endif.2.endif.if", label %"entry.endif.endif.endif.e...endif.2.endif.endif"
entry.endif.endif.endif.e...endif.2.endif.if:
  %".115" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".116" = call i32 (i8*, ...) @"printf"(i8* %".115")
  ret i32 1
entry.endif.endif.endif.e...endif.2.endif.endif:
  %".118" = icmp uge i32 0, 3
  br i1 %".118", label %"entry.endif.endif.endif.e...endif.2.endif.endif.if", label %"entry.endif.endif.endif.e...endif.2.endif.endif.endif"
entry.endif.endif.endif.e...endif.2.endif.endif.if:
  %".120" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".121" = call i32 (i8*, ...) @"printf"(i8* %".120")
  ret i32 1
entry.endif.endif.endif.e...endif.2.endif.endif.endif:
  %".123" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 1, i32 0
  %"matrix_elem.3" = load i32, i32* %".123"
  %".124" = bitcast [4 x i8]* @"fstr" to i8*
  %".125" = call i32 (i8*, ...) @"printf"(i8* %".124", i32 %"matrix_elem.3")
  %".126" = icmp uge i32 1, 2
  br i1 %".126", label %"entry.endif.endif.endif.e...if.3", label %"entry.endif.endif.endif.e...endif.3"
entry.endif.endif.endif.e...if.3:
  %".128" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".129" = call i32 (i8*, ...) @"printf"(i8* %".128")
  ret i32 1
entry.endif.endif.endif.e...endif.3:
  %".131" = icmp uge i32 1, 3
  br i1 %".131", label %"entry.endif.endif.endif.e...endif.3.if", label %"entry.endif.endif.endif.e...endif.3.endif"
entry.endif.endif.endif.e...endif.3.if:
  %".133" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".134" = call i32 (i8*, ...) @"printf"(i8* %".133")
  ret i32 1
entry.endif.endif.endif.e...endif.3.endif:
  %".136" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 1, i32 1
  %"matrix_elem.4" = load i32, i32* %".136"
  %".137" = bitcast [4 x i8]* @"fstr" to i8*
  %".138" = call i32 (i8*, ...) @"printf"(i8* %".137", i32 %"matrix_elem.4")
  %".139" = icmp uge i32 1, 2
  br i1 %".139", label %"entry.endif.endif.endif.e...endif.3.endif.if", label %"entry.endif.endif.endif.e...endif.3.endif.endif"
entry.endif.endif.endif.e...endif.3.endif.if:
  %".141" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".142" = call i32 (i8*, ...) @"printf"(i8* %".141")
  ret i32 1
entry.endif.endif.endif.e...endif.3.endif.endif:
  %".144" = icmp uge i32 2, 3
  br i1 %".144", label %"entry.endif.endif.endif.e...endif.3.endif.endif.if", label %"entry.endif.endif.endif.e...endif.3.endif.endif.endif"
entry.endif.endif.endif.e...endif.3.endif.endif.if:
  %".146" = bitcast [27 x i8]* @"fstr_error" to i8*
  %".147" = call i32 (i8*, ...) @"printf"(i8* %".146")
  ret i32 1
entry.endif.endif.endif.e...endif.3.endif.endif.endif:
  %".149" = getelementptr inbounds [2 x [3 x i32]], [2 x [3 x i32]]* %"matrix", i32 0, i32 1, i32 2
  %"matrix_elem.5" = load i32, i32* %".149"
  %".150" = bitcast [4 x i8]* @"fstr" to i8*
  %".151" = call i32 (i8*, ...) @"printf"(i8* %".150", i32 %"matrix_elem.5")
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