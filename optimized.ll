; ModuleID = 'output.ll'
source_filename = "output.ll"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-darwin23.4.0"

@fstr = internal constant [4 x i8] c"%d\0A\00"
@fstr_float = internal constant [4 x i8] c"%f\0A\00"
@str_0 = internal constant [14 x i8] c"Testing x sum\00"
@str_1 = internal constant [20 x i8] c"Testing x substract\00"
@str_2 = internal constant [19 x i8] c"Testing x multiply\00"
@str_3 = internal constant [19 x i8] c"Testing x division\00"
@str_4 = internal constant [19 x i8] c"Testing IO reading\00"
@str_5 = internal constant [12 x i8] c"Hello world\00"

define noundef i32 @main() local_unnamed_addr {
entry:
  %.4 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 5)
  %.7 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_float, float 0x400921FB00000000)
  %.10 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_float, float 0x3FF1F84FE0000000)
  %.13 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 8)
  %puts = tail call i32 @puts(ptr nonnull dereferenceable(1) @str_0)
  %.19 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 13)
  %puts8 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str_1)
  %.25 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 3)
  %puts9 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str_2)
  %.31 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 44)
  %puts10 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str_3)
  %.37 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 2)
  %puts11 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str_4)
  %readTest = alloca float, align 4
  call void @read_float(ptr nonnull %readTest)
  %readTest.1 = load float, ptr %readTest, align 4
  %.43 = call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_float, float %readTest.1)
  %puts12 = call i32 @puts(ptr nonnull dereferenceable(1) @str_5)
  ret i32 0
}

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

declare void @read_float(ptr) local_unnamed_addr

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr nocapture noundef readonly) local_unnamed_addr #0

attributes #0 = { nofree nounwind }
