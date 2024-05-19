// Generated from Pierogusz.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PieroguszParser}.
 */
public interface PieroguszListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PieroguszParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(PieroguszParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link PieroguszParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(PieroguszParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link PieroguszParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(PieroguszParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PieroguszParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(PieroguszParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PieroguszParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(PieroguszParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link PieroguszParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(PieroguszParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link PieroguszParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void enterPrintStmt(PieroguszParser.PrintStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link PieroguszParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void exitPrintStmt(PieroguszParser.PrintStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link PieroguszParser#readStmt}.
	 * @param ctx the parse tree
	 */
	void enterReadStmt(PieroguszParser.ReadStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link PieroguszParser#readStmt}.
	 * @param ctx the parse tree
	 */
	void exitReadStmt(PieroguszParser.ReadStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link PieroguszParser#assignStmt}.
	 * @param ctx the parse tree
	 */
	void enterAssignStmt(PieroguszParser.AssignStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link PieroguszParser#assignStmt}.
	 * @param ctx the parse tree
	 */
	void exitAssignStmt(PieroguszParser.AssignStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link PieroguszParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(PieroguszParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PieroguszParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(PieroguszParser.ExprContext ctx);
}