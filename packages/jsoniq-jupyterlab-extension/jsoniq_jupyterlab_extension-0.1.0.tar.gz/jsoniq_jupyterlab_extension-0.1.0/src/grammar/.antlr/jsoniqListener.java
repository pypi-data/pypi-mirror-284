// Generated from /Users/dbuzatu/ETH/ResearchProject/jsoniq-jupyter-plugin/src/grammar/jsoniq.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link jsoniqParser}.
 */
public interface jsoniqListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#moduleAndThisIsIt}.
	 * @param ctx the parse tree
	 */
	void enterModuleAndThisIsIt(jsoniqParser.ModuleAndThisIsItContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#moduleAndThisIsIt}.
	 * @param ctx the parse tree
	 */
	void exitModuleAndThisIsIt(jsoniqParser.ModuleAndThisIsItContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#module}.
	 * @param ctx the parse tree
	 */
	void enterModule(jsoniqParser.ModuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#module}.
	 * @param ctx the parse tree
	 */
	void exitModule(jsoniqParser.ModuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#mainModule}.
	 * @param ctx the parse tree
	 */
	void enterMainModule(jsoniqParser.MainModuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#mainModule}.
	 * @param ctx the parse tree
	 */
	void exitMainModule(jsoniqParser.MainModuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#libraryModule}.
	 * @param ctx the parse tree
	 */
	void enterLibraryModule(jsoniqParser.LibraryModuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#libraryModule}.
	 * @param ctx the parse tree
	 */
	void exitLibraryModule(jsoniqParser.LibraryModuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#prolog}.
	 * @param ctx the parse tree
	 */
	void enterProlog(jsoniqParser.PrologContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#prolog}.
	 * @param ctx the parse tree
	 */
	void exitProlog(jsoniqParser.PrologContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(jsoniqParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(jsoniqParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#statements}.
	 * @param ctx the parse tree
	 */
	void enterStatements(jsoniqParser.StatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#statements}.
	 * @param ctx the parse tree
	 */
	void exitStatements(jsoniqParser.StatementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#statementsAndExpr}.
	 * @param ctx the parse tree
	 */
	void enterStatementsAndExpr(jsoniqParser.StatementsAndExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#statementsAndExpr}.
	 * @param ctx the parse tree
	 */
	void exitStatementsAndExpr(jsoniqParser.StatementsAndExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#statementsAndOptionalExpr}.
	 * @param ctx the parse tree
	 */
	void enterStatementsAndOptionalExpr(jsoniqParser.StatementsAndOptionalExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#statementsAndOptionalExpr}.
	 * @param ctx the parse tree
	 */
	void exitStatementsAndOptionalExpr(jsoniqParser.StatementsAndOptionalExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(jsoniqParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(jsoniqParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#applyStatement}.
	 * @param ctx the parse tree
	 */
	void enterApplyStatement(jsoniqParser.ApplyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#applyStatement}.
	 * @param ctx the parse tree
	 */
	void exitApplyStatement(jsoniqParser.ApplyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#assignStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignStatement(jsoniqParser.AssignStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#assignStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignStatement(jsoniqParser.AssignStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#blockStatement}.
	 * @param ctx the parse tree
	 */
	void enterBlockStatement(jsoniqParser.BlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#blockStatement}.
	 * @param ctx the parse tree
	 */
	void exitBlockStatement(jsoniqParser.BlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void enterBreakStatement(jsoniqParser.BreakStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void exitBreakStatement(jsoniqParser.BreakStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(jsoniqParser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(jsoniqParser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#exitStatement}.
	 * @param ctx the parse tree
	 */
	void enterExitStatement(jsoniqParser.ExitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#exitStatement}.
	 * @param ctx the parse tree
	 */
	void exitExitStatement(jsoniqParser.ExitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#flowrStatement}.
	 * @param ctx the parse tree
	 */
	void enterFlowrStatement(jsoniqParser.FlowrStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#flowrStatement}.
	 * @param ctx the parse tree
	 */
	void exitFlowrStatement(jsoniqParser.FlowrStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(jsoniqParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(jsoniqParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#switchStatement}.
	 * @param ctx the parse tree
	 */
	void enterSwitchStatement(jsoniqParser.SwitchStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#switchStatement}.
	 * @param ctx the parse tree
	 */
	void exitSwitchStatement(jsoniqParser.SwitchStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#switchCaseStatement}.
	 * @param ctx the parse tree
	 */
	void enterSwitchCaseStatement(jsoniqParser.SwitchCaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#switchCaseStatement}.
	 * @param ctx the parse tree
	 */
	void exitSwitchCaseStatement(jsoniqParser.SwitchCaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#tryCatchStatement}.
	 * @param ctx the parse tree
	 */
	void enterTryCatchStatement(jsoniqParser.TryCatchStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#tryCatchStatement}.
	 * @param ctx the parse tree
	 */
	void exitTryCatchStatement(jsoniqParser.TryCatchStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#catchCaseStatement}.
	 * @param ctx the parse tree
	 */
	void enterCatchCaseStatement(jsoniqParser.CatchCaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#catchCaseStatement}.
	 * @param ctx the parse tree
	 */
	void exitCatchCaseStatement(jsoniqParser.CatchCaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#typeSwitchStatement}.
	 * @param ctx the parse tree
	 */
	void enterTypeSwitchStatement(jsoniqParser.TypeSwitchStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#typeSwitchStatement}.
	 * @param ctx the parse tree
	 */
	void exitTypeSwitchStatement(jsoniqParser.TypeSwitchStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#caseStatement}.
	 * @param ctx the parse tree
	 */
	void enterCaseStatement(jsoniqParser.CaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#caseStatement}.
	 * @param ctx the parse tree
	 */
	void exitCaseStatement(jsoniqParser.CaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#annotation}.
	 * @param ctx the parse tree
	 */
	void enterAnnotation(jsoniqParser.AnnotationContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#annotation}.
	 * @param ctx the parse tree
	 */
	void exitAnnotation(jsoniqParser.AnnotationContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#annotations}.
	 * @param ctx the parse tree
	 */
	void enterAnnotations(jsoniqParser.AnnotationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#annotations}.
	 * @param ctx the parse tree
	 */
	void exitAnnotations(jsoniqParser.AnnotationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#varDeclStatement}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclStatement(jsoniqParser.VarDeclStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#varDeclStatement}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclStatement(jsoniqParser.VarDeclStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#varDeclForStatement}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclForStatement(jsoniqParser.VarDeclForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#varDeclForStatement}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclForStatement(jsoniqParser.VarDeclForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(jsoniqParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(jsoniqParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#setter}.
	 * @param ctx the parse tree
	 */
	void enterSetter(jsoniqParser.SetterContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#setter}.
	 * @param ctx the parse tree
	 */
	void exitSetter(jsoniqParser.SetterContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#namespaceDecl}.
	 * @param ctx the parse tree
	 */
	void enterNamespaceDecl(jsoniqParser.NamespaceDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#namespaceDecl}.
	 * @param ctx the parse tree
	 */
	void exitNamespaceDecl(jsoniqParser.NamespaceDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#annotatedDecl}.
	 * @param ctx the parse tree
	 */
	void enterAnnotatedDecl(jsoniqParser.AnnotatedDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#annotatedDecl}.
	 * @param ctx the parse tree
	 */
	void exitAnnotatedDecl(jsoniqParser.AnnotatedDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#defaultCollationDecl}.
	 * @param ctx the parse tree
	 */
	void enterDefaultCollationDecl(jsoniqParser.DefaultCollationDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#defaultCollationDecl}.
	 * @param ctx the parse tree
	 */
	void exitDefaultCollationDecl(jsoniqParser.DefaultCollationDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#orderingModeDecl}.
	 * @param ctx the parse tree
	 */
	void enterOrderingModeDecl(jsoniqParser.OrderingModeDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#orderingModeDecl}.
	 * @param ctx the parse tree
	 */
	void exitOrderingModeDecl(jsoniqParser.OrderingModeDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#emptyOrderDecl}.
	 * @param ctx the parse tree
	 */
	void enterEmptyOrderDecl(jsoniqParser.EmptyOrderDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#emptyOrderDecl}.
	 * @param ctx the parse tree
	 */
	void exitEmptyOrderDecl(jsoniqParser.EmptyOrderDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#decimalFormatDecl}.
	 * @param ctx the parse tree
	 */
	void enterDecimalFormatDecl(jsoniqParser.DecimalFormatDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#decimalFormatDecl}.
	 * @param ctx the parse tree
	 */
	void exitDecimalFormatDecl(jsoniqParser.DecimalFormatDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#qname}.
	 * @param ctx the parse tree
	 */
	void enterQname(jsoniqParser.QnameContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#qname}.
	 * @param ctx the parse tree
	 */
	void exitQname(jsoniqParser.QnameContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#dfPropertyName}.
	 * @param ctx the parse tree
	 */
	void enterDfPropertyName(jsoniqParser.DfPropertyNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#dfPropertyName}.
	 * @param ctx the parse tree
	 */
	void exitDfPropertyName(jsoniqParser.DfPropertyNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#moduleImport}.
	 * @param ctx the parse tree
	 */
	void enterModuleImport(jsoniqParser.ModuleImportContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#moduleImport}.
	 * @param ctx the parse tree
	 */
	void exitModuleImport(jsoniqParser.ModuleImportContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(jsoniqParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(jsoniqParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#contextItemDecl}.
	 * @param ctx the parse tree
	 */
	void enterContextItemDecl(jsoniqParser.ContextItemDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#contextItemDecl}.
	 * @param ctx the parse tree
	 */
	void exitContextItemDecl(jsoniqParser.ContextItemDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDecl(jsoniqParser.FunctionDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDecl(jsoniqParser.FunctionDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#typeDecl}.
	 * @param ctx the parse tree
	 */
	void enterTypeDecl(jsoniqParser.TypeDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#typeDecl}.
	 * @param ctx the parse tree
	 */
	void exitTypeDecl(jsoniqParser.TypeDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#schemaLanguage}.
	 * @param ctx the parse tree
	 */
	void enterSchemaLanguage(jsoniqParser.SchemaLanguageContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#schemaLanguage}.
	 * @param ctx the parse tree
	 */
	void exitSchemaLanguage(jsoniqParser.SchemaLanguageContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(jsoniqParser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(jsoniqParser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(jsoniqParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(jsoniqParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(jsoniqParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(jsoniqParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#exprSingle}.
	 * @param ctx the parse tree
	 */
	void enterExprSingle(jsoniqParser.ExprSingleContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#exprSingle}.
	 * @param ctx the parse tree
	 */
	void exitExprSingle(jsoniqParser.ExprSingleContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#exprSimple}.
	 * @param ctx the parse tree
	 */
	void enterExprSimple(jsoniqParser.ExprSimpleContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#exprSimple}.
	 * @param ctx the parse tree
	 */
	void exitExprSimple(jsoniqParser.ExprSimpleContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#flowrExpr}.
	 * @param ctx the parse tree
	 */
	void enterFlowrExpr(jsoniqParser.FlowrExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#flowrExpr}.
	 * @param ctx the parse tree
	 */
	void exitFlowrExpr(jsoniqParser.FlowrExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#forClause}.
	 * @param ctx the parse tree
	 */
	void enterForClause(jsoniqParser.ForClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#forClause}.
	 * @param ctx the parse tree
	 */
	void exitForClause(jsoniqParser.ForClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#forVar}.
	 * @param ctx the parse tree
	 */
	void enterForVar(jsoniqParser.ForVarContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#forVar}.
	 * @param ctx the parse tree
	 */
	void exitForVar(jsoniqParser.ForVarContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#letClause}.
	 * @param ctx the parse tree
	 */
	void enterLetClause(jsoniqParser.LetClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#letClause}.
	 * @param ctx the parse tree
	 */
	void exitLetClause(jsoniqParser.LetClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#letVar}.
	 * @param ctx the parse tree
	 */
	void enterLetVar(jsoniqParser.LetVarContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#letVar}.
	 * @param ctx the parse tree
	 */
	void exitLetVar(jsoniqParser.LetVarContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#whereClause}.
	 * @param ctx the parse tree
	 */
	void enterWhereClause(jsoniqParser.WhereClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#whereClause}.
	 * @param ctx the parse tree
	 */
	void exitWhereClause(jsoniqParser.WhereClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#groupByClause}.
	 * @param ctx the parse tree
	 */
	void enterGroupByClause(jsoniqParser.GroupByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#groupByClause}.
	 * @param ctx the parse tree
	 */
	void exitGroupByClause(jsoniqParser.GroupByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#groupByVar}.
	 * @param ctx the parse tree
	 */
	void enterGroupByVar(jsoniqParser.GroupByVarContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#groupByVar}.
	 * @param ctx the parse tree
	 */
	void exitGroupByVar(jsoniqParser.GroupByVarContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#orderByClause}.
	 * @param ctx the parse tree
	 */
	void enterOrderByClause(jsoniqParser.OrderByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#orderByClause}.
	 * @param ctx the parse tree
	 */
	void exitOrderByClause(jsoniqParser.OrderByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#orderByExpr}.
	 * @param ctx the parse tree
	 */
	void enterOrderByExpr(jsoniqParser.OrderByExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#orderByExpr}.
	 * @param ctx the parse tree
	 */
	void exitOrderByExpr(jsoniqParser.OrderByExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#countClause}.
	 * @param ctx the parse tree
	 */
	void enterCountClause(jsoniqParser.CountClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#countClause}.
	 * @param ctx the parse tree
	 */
	void exitCountClause(jsoniqParser.CountClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#quantifiedExpr}.
	 * @param ctx the parse tree
	 */
	void enterQuantifiedExpr(jsoniqParser.QuantifiedExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#quantifiedExpr}.
	 * @param ctx the parse tree
	 */
	void exitQuantifiedExpr(jsoniqParser.QuantifiedExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#quantifiedExprVar}.
	 * @param ctx the parse tree
	 */
	void enterQuantifiedExprVar(jsoniqParser.QuantifiedExprVarContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#quantifiedExprVar}.
	 * @param ctx the parse tree
	 */
	void exitQuantifiedExprVar(jsoniqParser.QuantifiedExprVarContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#switchExpr}.
	 * @param ctx the parse tree
	 */
	void enterSwitchExpr(jsoniqParser.SwitchExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#switchExpr}.
	 * @param ctx the parse tree
	 */
	void exitSwitchExpr(jsoniqParser.SwitchExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#switchCaseClause}.
	 * @param ctx the parse tree
	 */
	void enterSwitchCaseClause(jsoniqParser.SwitchCaseClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#switchCaseClause}.
	 * @param ctx the parse tree
	 */
	void exitSwitchCaseClause(jsoniqParser.SwitchCaseClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#typeSwitchExpr}.
	 * @param ctx the parse tree
	 */
	void enterTypeSwitchExpr(jsoniqParser.TypeSwitchExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#typeSwitchExpr}.
	 * @param ctx the parse tree
	 */
	void exitTypeSwitchExpr(jsoniqParser.TypeSwitchExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#caseClause}.
	 * @param ctx the parse tree
	 */
	void enterCaseClause(jsoniqParser.CaseClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#caseClause}.
	 * @param ctx the parse tree
	 */
	void exitCaseClause(jsoniqParser.CaseClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#ifExpr}.
	 * @param ctx the parse tree
	 */
	void enterIfExpr(jsoniqParser.IfExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#ifExpr}.
	 * @param ctx the parse tree
	 */
	void exitIfExpr(jsoniqParser.IfExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#tryCatchExpr}.
	 * @param ctx the parse tree
	 */
	void enterTryCatchExpr(jsoniqParser.TryCatchExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#tryCatchExpr}.
	 * @param ctx the parse tree
	 */
	void exitTryCatchExpr(jsoniqParser.TryCatchExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#catchClause}.
	 * @param ctx the parse tree
	 */
	void enterCatchClause(jsoniqParser.CatchClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#catchClause}.
	 * @param ctx the parse tree
	 */
	void exitCatchClause(jsoniqParser.CatchClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#orExpr}.
	 * @param ctx the parse tree
	 */
	void enterOrExpr(jsoniqParser.OrExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#orExpr}.
	 * @param ctx the parse tree
	 */
	void exitOrExpr(jsoniqParser.OrExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#andExpr}.
	 * @param ctx the parse tree
	 */
	void enterAndExpr(jsoniqParser.AndExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#andExpr}.
	 * @param ctx the parse tree
	 */
	void exitAndExpr(jsoniqParser.AndExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#notExpr}.
	 * @param ctx the parse tree
	 */
	void enterNotExpr(jsoniqParser.NotExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#notExpr}.
	 * @param ctx the parse tree
	 */
	void exitNotExpr(jsoniqParser.NotExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#comparisonExpr}.
	 * @param ctx the parse tree
	 */
	void enterComparisonExpr(jsoniqParser.ComparisonExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#comparisonExpr}.
	 * @param ctx the parse tree
	 */
	void exitComparisonExpr(jsoniqParser.ComparisonExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#stringConcatExpr}.
	 * @param ctx the parse tree
	 */
	void enterStringConcatExpr(jsoniqParser.StringConcatExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#stringConcatExpr}.
	 * @param ctx the parse tree
	 */
	void exitStringConcatExpr(jsoniqParser.StringConcatExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#rangeExpr}.
	 * @param ctx the parse tree
	 */
	void enterRangeExpr(jsoniqParser.RangeExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#rangeExpr}.
	 * @param ctx the parse tree
	 */
	void exitRangeExpr(jsoniqParser.RangeExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#additiveExpr}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpr(jsoniqParser.AdditiveExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#additiveExpr}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpr(jsoniqParser.AdditiveExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#multiplicativeExpr}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpr(jsoniqParser.MultiplicativeExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#multiplicativeExpr}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpr(jsoniqParser.MultiplicativeExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#instanceOfExpr}.
	 * @param ctx the parse tree
	 */
	void enterInstanceOfExpr(jsoniqParser.InstanceOfExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#instanceOfExpr}.
	 * @param ctx the parse tree
	 */
	void exitInstanceOfExpr(jsoniqParser.InstanceOfExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#isStaticallyExpr}.
	 * @param ctx the parse tree
	 */
	void enterIsStaticallyExpr(jsoniqParser.IsStaticallyExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#isStaticallyExpr}.
	 * @param ctx the parse tree
	 */
	void exitIsStaticallyExpr(jsoniqParser.IsStaticallyExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#treatExpr}.
	 * @param ctx the parse tree
	 */
	void enterTreatExpr(jsoniqParser.TreatExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#treatExpr}.
	 * @param ctx the parse tree
	 */
	void exitTreatExpr(jsoniqParser.TreatExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#castableExpr}.
	 * @param ctx the parse tree
	 */
	void enterCastableExpr(jsoniqParser.CastableExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#castableExpr}.
	 * @param ctx the parse tree
	 */
	void exitCastableExpr(jsoniqParser.CastableExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#castExpr}.
	 * @param ctx the parse tree
	 */
	void enterCastExpr(jsoniqParser.CastExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#castExpr}.
	 * @param ctx the parse tree
	 */
	void exitCastExpr(jsoniqParser.CastExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#arrowExpr}.
	 * @param ctx the parse tree
	 */
	void enterArrowExpr(jsoniqParser.ArrowExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#arrowExpr}.
	 * @param ctx the parse tree
	 */
	void exitArrowExpr(jsoniqParser.ArrowExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#arrowFunctionSpecifier}.
	 * @param ctx the parse tree
	 */
	void enterArrowFunctionSpecifier(jsoniqParser.ArrowFunctionSpecifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#arrowFunctionSpecifier}.
	 * @param ctx the parse tree
	 */
	void exitArrowFunctionSpecifier(jsoniqParser.ArrowFunctionSpecifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpr(jsoniqParser.UnaryExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpr(jsoniqParser.UnaryExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#valueExpr}.
	 * @param ctx the parse tree
	 */
	void enterValueExpr(jsoniqParser.ValueExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#valueExpr}.
	 * @param ctx the parse tree
	 */
	void exitValueExpr(jsoniqParser.ValueExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#validateExpr}.
	 * @param ctx the parse tree
	 */
	void enterValidateExpr(jsoniqParser.ValidateExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#validateExpr}.
	 * @param ctx the parse tree
	 */
	void exitValidateExpr(jsoniqParser.ValidateExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#annotateExpr}.
	 * @param ctx the parse tree
	 */
	void enterAnnotateExpr(jsoniqParser.AnnotateExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#annotateExpr}.
	 * @param ctx the parse tree
	 */
	void exitAnnotateExpr(jsoniqParser.AnnotateExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#simpleMapExpr}.
	 * @param ctx the parse tree
	 */
	void enterSimpleMapExpr(jsoniqParser.SimpleMapExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#simpleMapExpr}.
	 * @param ctx the parse tree
	 */
	void exitSimpleMapExpr(jsoniqParser.SimpleMapExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#postFixExpr}.
	 * @param ctx the parse tree
	 */
	void enterPostFixExpr(jsoniqParser.PostFixExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#postFixExpr}.
	 * @param ctx the parse tree
	 */
	void exitPostFixExpr(jsoniqParser.PostFixExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#arrayLookup}.
	 * @param ctx the parse tree
	 */
	void enterArrayLookup(jsoniqParser.ArrayLookupContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#arrayLookup}.
	 * @param ctx the parse tree
	 */
	void exitArrayLookup(jsoniqParser.ArrayLookupContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#arrayUnboxing}.
	 * @param ctx the parse tree
	 */
	void enterArrayUnboxing(jsoniqParser.ArrayUnboxingContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#arrayUnboxing}.
	 * @param ctx the parse tree
	 */
	void exitArrayUnboxing(jsoniqParser.ArrayUnboxingContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterPredicate(jsoniqParser.PredicateContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitPredicate(jsoniqParser.PredicateContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#objectLookup}.
	 * @param ctx the parse tree
	 */
	void enterObjectLookup(jsoniqParser.ObjectLookupContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#objectLookup}.
	 * @param ctx the parse tree
	 */
	void exitObjectLookup(jsoniqParser.ObjectLookupContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#primaryExpr}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpr(jsoniqParser.PrimaryExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#primaryExpr}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpr(jsoniqParser.PrimaryExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#blockExpr}.
	 * @param ctx the parse tree
	 */
	void enterBlockExpr(jsoniqParser.BlockExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#blockExpr}.
	 * @param ctx the parse tree
	 */
	void exitBlockExpr(jsoniqParser.BlockExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#varRef}.
	 * @param ctx the parse tree
	 */
	void enterVarRef(jsoniqParser.VarRefContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#varRef}.
	 * @param ctx the parse tree
	 */
	void exitVarRef(jsoniqParser.VarRefContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#parenthesizedExpr}.
	 * @param ctx the parse tree
	 */
	void enterParenthesizedExpr(jsoniqParser.ParenthesizedExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#parenthesizedExpr}.
	 * @param ctx the parse tree
	 */
	void exitParenthesizedExpr(jsoniqParser.ParenthesizedExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#contextItemExpr}.
	 * @param ctx the parse tree
	 */
	void enterContextItemExpr(jsoniqParser.ContextItemExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#contextItemExpr}.
	 * @param ctx the parse tree
	 */
	void exitContextItemExpr(jsoniqParser.ContextItemExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#orderedExpr}.
	 * @param ctx the parse tree
	 */
	void enterOrderedExpr(jsoniqParser.OrderedExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#orderedExpr}.
	 * @param ctx the parse tree
	 */
	void exitOrderedExpr(jsoniqParser.OrderedExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#unorderedExpr}.
	 * @param ctx the parse tree
	 */
	void enterUnorderedExpr(jsoniqParser.UnorderedExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#unorderedExpr}.
	 * @param ctx the parse tree
	 */
	void exitUnorderedExpr(jsoniqParser.UnorderedExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(jsoniqParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(jsoniqParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(jsoniqParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(jsoniqParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(jsoniqParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(jsoniqParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#functionItemExpr}.
	 * @param ctx the parse tree
	 */
	void enterFunctionItemExpr(jsoniqParser.FunctionItemExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#functionItemExpr}.
	 * @param ctx the parse tree
	 */
	void exitFunctionItemExpr(jsoniqParser.FunctionItemExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#namedFunctionRef}.
	 * @param ctx the parse tree
	 */
	void enterNamedFunctionRef(jsoniqParser.NamedFunctionRefContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#namedFunctionRef}.
	 * @param ctx the parse tree
	 */
	void exitNamedFunctionRef(jsoniqParser.NamedFunctionRefContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#inlineFunctionExpr}.
	 * @param ctx the parse tree
	 */
	void enterInlineFunctionExpr(jsoniqParser.InlineFunctionExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#inlineFunctionExpr}.
	 * @param ctx the parse tree
	 */
	void exitInlineFunctionExpr(jsoniqParser.InlineFunctionExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#insertExpr}.
	 * @param ctx the parse tree
	 */
	void enterInsertExpr(jsoniqParser.InsertExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#insertExpr}.
	 * @param ctx the parse tree
	 */
	void exitInsertExpr(jsoniqParser.InsertExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#deleteExpr}.
	 * @param ctx the parse tree
	 */
	void enterDeleteExpr(jsoniqParser.DeleteExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#deleteExpr}.
	 * @param ctx the parse tree
	 */
	void exitDeleteExpr(jsoniqParser.DeleteExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#renameExpr}.
	 * @param ctx the parse tree
	 */
	void enterRenameExpr(jsoniqParser.RenameExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#renameExpr}.
	 * @param ctx the parse tree
	 */
	void exitRenameExpr(jsoniqParser.RenameExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#replaceExpr}.
	 * @param ctx the parse tree
	 */
	void enterReplaceExpr(jsoniqParser.ReplaceExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#replaceExpr}.
	 * @param ctx the parse tree
	 */
	void exitReplaceExpr(jsoniqParser.ReplaceExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#transformExpr}.
	 * @param ctx the parse tree
	 */
	void enterTransformExpr(jsoniqParser.TransformExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#transformExpr}.
	 * @param ctx the parse tree
	 */
	void exitTransformExpr(jsoniqParser.TransformExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#appendExpr}.
	 * @param ctx the parse tree
	 */
	void enterAppendExpr(jsoniqParser.AppendExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#appendExpr}.
	 * @param ctx the parse tree
	 */
	void exitAppendExpr(jsoniqParser.AppendExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#updateLocator}.
	 * @param ctx the parse tree
	 */
	void enterUpdateLocator(jsoniqParser.UpdateLocatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#updateLocator}.
	 * @param ctx the parse tree
	 */
	void exitUpdateLocator(jsoniqParser.UpdateLocatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#copyDecl}.
	 * @param ctx the parse tree
	 */
	void enterCopyDecl(jsoniqParser.CopyDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#copyDecl}.
	 * @param ctx the parse tree
	 */
	void exitCopyDecl(jsoniqParser.CopyDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#sequenceType}.
	 * @param ctx the parse tree
	 */
	void enterSequenceType(jsoniqParser.SequenceTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#sequenceType}.
	 * @param ctx the parse tree
	 */
	void exitSequenceType(jsoniqParser.SequenceTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#objectConstructor}.
	 * @param ctx the parse tree
	 */
	void enterObjectConstructor(jsoniqParser.ObjectConstructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#objectConstructor}.
	 * @param ctx the parse tree
	 */
	void exitObjectConstructor(jsoniqParser.ObjectConstructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#itemType}.
	 * @param ctx the parse tree
	 */
	void enterItemType(jsoniqParser.ItemTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#itemType}.
	 * @param ctx the parse tree
	 */
	void exitItemType(jsoniqParser.ItemTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#functionTest}.
	 * @param ctx the parse tree
	 */
	void enterFunctionTest(jsoniqParser.FunctionTestContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#functionTest}.
	 * @param ctx the parse tree
	 */
	void exitFunctionTest(jsoniqParser.FunctionTestContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#anyFunctionTest}.
	 * @param ctx the parse tree
	 */
	void enterAnyFunctionTest(jsoniqParser.AnyFunctionTestContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#anyFunctionTest}.
	 * @param ctx the parse tree
	 */
	void exitAnyFunctionTest(jsoniqParser.AnyFunctionTestContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#typedFunctionTest}.
	 * @param ctx the parse tree
	 */
	void enterTypedFunctionTest(jsoniqParser.TypedFunctionTestContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#typedFunctionTest}.
	 * @param ctx the parse tree
	 */
	void exitTypedFunctionTest(jsoniqParser.TypedFunctionTestContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#singleType}.
	 * @param ctx the parse tree
	 */
	void enterSingleType(jsoniqParser.SingleTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#singleType}.
	 * @param ctx the parse tree
	 */
	void exitSingleType(jsoniqParser.SingleTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#pairConstructor}.
	 * @param ctx the parse tree
	 */
	void enterPairConstructor(jsoniqParser.PairConstructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#pairConstructor}.
	 * @param ctx the parse tree
	 */
	void exitPairConstructor(jsoniqParser.PairConstructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#arrayConstructor}.
	 * @param ctx the parse tree
	 */
	void enterArrayConstructor(jsoniqParser.ArrayConstructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#arrayConstructor}.
	 * @param ctx the parse tree
	 */
	void exitArrayConstructor(jsoniqParser.ArrayConstructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#uriLiteral}.
	 * @param ctx the parse tree
	 */
	void enterUriLiteral(jsoniqParser.UriLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#uriLiteral}.
	 * @param ctx the parse tree
	 */
	void exitUriLiteral(jsoniqParser.UriLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#stringLiteral}.
	 * @param ctx the parse tree
	 */
	void enterStringLiteral(jsoniqParser.StringLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#stringLiteral}.
	 * @param ctx the parse tree
	 */
	void exitStringLiteral(jsoniqParser.StringLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsoniqParser#keyWords}.
	 * @param ctx the parse tree
	 */
	void enterKeyWords(jsoniqParser.KeyWordsContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsoniqParser#keyWords}.
	 * @param ctx the parse tree
	 */
	void exitKeyWords(jsoniqParser.KeyWordsContext ctx);
}