; ModuleID = 'output.ll'
source_filename = "output.ll"
target triple = "x86_64-unknown-linux-gnu"

@fstr = internal constant [4 x i8] c"%d\0A\00"
@fstr_float = internal constant [4 x i8] c"%f\0A\00"
@str_0 = internal constant [15 x i8] c"Testing arrays\00"
@str_1 = internal constant [6 x i8] c"hello\00"
@str_2 = internal constant [6 x i8] c"world\00"
@str = private unnamed_addr constant [26 x i8] c"Array index out of bounds\00", align 1

; Function Attrs: nofree nounwind
define i32 @main() local_unnamed_addr #0 {
entry:
  %puts = tail call i32 @puts(i8* nonnull dereferenceable(1) getelementptr inbounds ([15 x i8], [15 x i8]* @str_0, i64 0, i64 0))
  %.26 = tail call i32 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fstr, i64 0, i64 0), i32 10)
  %.34 = tail call i32 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fstr, i64 0, i64 0), i32 20)
  %.56 = tail call i32 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fstr_float, i64 0, i64 0), float 0x40091EB860000000)
  %.64 = tail call i32 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fstr_float, i64 0, i64 0), float 0x4005AE1480000000)
  %puts1 = tail call i32 @puts(i8* nonnull dereferenceable(1) getelementptr inbounds ([6 x i8], [6 x i8]* @str_1, i64 0, i64 0))
  %puts2 = tail call i32 @puts(i8* nonnull dereferenceable(1) getelementptr inbounds ([6 x i8], [6 x i8]* @str_2, i64 0, i64 0))
  %puts3 = tail call i32 @puts(i8* nonnull dereferenceable(1) getelementptr inbounds ([26 x i8], [26 x i8]* @str, i64 0, i64 0))
  ret i32 1
}

; Function Attrs: nofree nounwind
declare noundef i32 @printf(i8* nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
declare noundef i32 @puts(i8* nocapture noundef readonly) local_unnamed_addr #0

attributes #0 = { nofree nounwind }
