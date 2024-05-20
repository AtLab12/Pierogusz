; ModuleID = 'output.ll'
source_filename = "output.ll"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-darwin23.4.0"

@fstr = internal constant [4 x i8] c"%d\0A\00"
@fstr_float = internal constant [4 x i8] c"%f\0A\00"

define noundef i32 @main() local_unnamed_addr {
entry:
  %.4 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 5)
  %.7 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_float, float 0x400921FB00000000)
  %.10 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_float, float 0x3FF1F84FE0000000)
  %.13 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 8)
  %.16 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 13)
  %.19 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 3)
  %.22 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 40)
  %.25 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr, i32 2)
  %readTest = alloca float, align 4
  call void @read_float(ptr nonnull %readTest)
  %readTest.1 = load float, ptr %readTest, align 4
  %.28 = call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_float, float %readTest.1)
  ret i32 0
}

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

declare void @read_float(ptr) local_unnamed_addr

attributes #0 = { nofree nounwind }
