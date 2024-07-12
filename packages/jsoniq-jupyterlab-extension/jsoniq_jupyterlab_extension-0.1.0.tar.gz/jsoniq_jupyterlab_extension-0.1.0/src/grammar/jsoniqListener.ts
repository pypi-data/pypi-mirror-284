// Generated from ./src/grammar/jsoniq.g4 by ANTLR 4.13.1

import {
  ErrorNode,
  ParseTreeListener,
  ParserRuleContext,
  TerminalNode
} from 'antlr4ng';

import { ModuleAndThisIsItContext } from './jsoniqParser.js';
import { ModuleContext } from './jsoniqParser.js';
import { MainModuleContext } from './jsoniqParser.js';
import { LibraryModuleContext } from './jsoniqParser.js';
import { PrologContext } from './jsoniqParser.js';
import { ProgramContext } from './jsoniqParser.js';
import { StatementsContext } from './jsoniqParser.js';
import { StatementsAndExprContext } from './jsoniqParser.js';
import { StatementsAndOptionalExprContext } from './jsoniqParser.js';
import { StatementContext } from './jsoniqParser.js';
import { ApplyStatementContext } from './jsoniqParser.js';
import { AssignStatementContext } from './jsoniqParser.js';
import { BlockStatementContext } from './jsoniqParser.js';
import { BreakStatementContext } from './jsoniqParser.js';
import { ContinueStatementContext } from './jsoniqParser.js';
import { ExitStatementContext } from './jsoniqParser.js';
import { FlowrStatementContext } from './jsoniqParser.js';
import { IfStatementContext } from './jsoniqParser.js';
import { SwitchStatementContext } from './jsoniqParser.js';
import { SwitchCaseStatementContext } from './jsoniqParser.js';
import { TryCatchStatementContext } from './jsoniqParser.js';
import { CatchCaseStatementContext } from './jsoniqParser.js';
import { TypeSwitchStatementContext } from './jsoniqParser.js';
import { CaseStatementContext } from './jsoniqParser.js';
import { AnnotationContext } from './jsoniqParser.js';
import { AnnotationsContext } from './jsoniqParser.js';
import { VarDeclStatementContext } from './jsoniqParser.js';
import { VarDeclForStatementContext } from './jsoniqParser.js';
import { WhileStatementContext } from './jsoniqParser.js';
import { SetterContext } from './jsoniqParser.js';
import { NamespaceDeclContext } from './jsoniqParser.js';
import { AnnotatedDeclContext } from './jsoniqParser.js';
import { DefaultCollationDeclContext } from './jsoniqParser.js';
import { OrderingModeDeclContext } from './jsoniqParser.js';
import { EmptyOrderDeclContext } from './jsoniqParser.js';
import { DecimalFormatDeclContext } from './jsoniqParser.js';
import { QnameContext } from './jsoniqParser.js';
import { DfPropertyNameContext } from './jsoniqParser.js';
import { ModuleImportContext } from './jsoniqParser.js';
import { VarDeclContext } from './jsoniqParser.js';
import { ContextItemDeclContext } from './jsoniqParser.js';
import { FunctionDeclContext } from './jsoniqParser.js';
import { TypeDeclContext } from './jsoniqParser.js';
import { SchemaLanguageContext } from './jsoniqParser.js';
import { ParamListContext } from './jsoniqParser.js';
import { ParamContext } from './jsoniqParser.js';
import { ExprContext } from './jsoniqParser.js';
import { ExprSingleContext } from './jsoniqParser.js';
import { ExprSimpleContext } from './jsoniqParser.js';
import { FlowrExprContext } from './jsoniqParser.js';
import { ForClauseContext } from './jsoniqParser.js';
import { ForVarContext } from './jsoniqParser.js';
import { LetClauseContext } from './jsoniqParser.js';
import { LetVarContext } from './jsoniqParser.js';
import { WhereClauseContext } from './jsoniqParser.js';
import { GroupByClauseContext } from './jsoniqParser.js';
import { GroupByVarContext } from './jsoniqParser.js';
import { OrderByClauseContext } from './jsoniqParser.js';
import { OrderByExprContext } from './jsoniqParser.js';
import { CountClauseContext } from './jsoniqParser.js';
import { QuantifiedExprContext } from './jsoniqParser.js';
import { QuantifiedExprVarContext } from './jsoniqParser.js';
import { SwitchExprContext } from './jsoniqParser.js';
import { SwitchCaseClauseContext } from './jsoniqParser.js';
import { TypeSwitchExprContext } from './jsoniqParser.js';
import { CaseClauseContext } from './jsoniqParser.js';
import { IfExprContext } from './jsoniqParser.js';
import { TryCatchExprContext } from './jsoniqParser.js';
import { CatchClauseContext } from './jsoniqParser.js';
import { OrExprContext } from './jsoniqParser.js';
import { AndExprContext } from './jsoniqParser.js';
import { NotExprContext } from './jsoniqParser.js';
import { ComparisonExprContext } from './jsoniqParser.js';
import { StringConcatExprContext } from './jsoniqParser.js';
import { RangeExprContext } from './jsoniqParser.js';
import { AdditiveExprContext } from './jsoniqParser.js';
import { MultiplicativeExprContext } from './jsoniqParser.js';
import { InstanceOfExprContext } from './jsoniqParser.js';
import { IsStaticallyExprContext } from './jsoniqParser.js';
import { TreatExprContext } from './jsoniqParser.js';
import { CastableExprContext } from './jsoniqParser.js';
import { CastExprContext } from './jsoniqParser.js';
import { ArrowExprContext } from './jsoniqParser.js';
import { ArrowFunctionSpecifierContext } from './jsoniqParser.js';
import { UnaryExprContext } from './jsoniqParser.js';
import { ValueExprContext } from './jsoniqParser.js';
import { ValidateExprContext } from './jsoniqParser.js';
import { AnnotateExprContext } from './jsoniqParser.js';
import { SimpleMapExprContext } from './jsoniqParser.js';
import { PostFixExprContext } from './jsoniqParser.js';
import { ArrayLookupContext } from './jsoniqParser.js';
import { ArrayUnboxingContext } from './jsoniqParser.js';
import { PredicateContext } from './jsoniqParser.js';
import { ObjectLookupContext } from './jsoniqParser.js';
import { PrimaryExprContext } from './jsoniqParser.js';
import { BlockExprContext } from './jsoniqParser.js';
import { VarRefContext } from './jsoniqParser.js';
import { ParenthesizedExprContext } from './jsoniqParser.js';
import { ContextItemExprContext } from './jsoniqParser.js';
import { OrderedExprContext } from './jsoniqParser.js';
import { UnorderedExprContext } from './jsoniqParser.js';
import { FunctionCallContext } from './jsoniqParser.js';
import { ArgumentListContext } from './jsoniqParser.js';
import { ArgumentContext } from './jsoniqParser.js';
import { FunctionItemExprContext } from './jsoniqParser.js';
import { NamedFunctionRefContext } from './jsoniqParser.js';
import { InlineFunctionExprContext } from './jsoniqParser.js';
import { InsertExprContext } from './jsoniqParser.js';
import { DeleteExprContext } from './jsoniqParser.js';
import { RenameExprContext } from './jsoniqParser.js';
import { ReplaceExprContext } from './jsoniqParser.js';
import { TransformExprContext } from './jsoniqParser.js';
import { AppendExprContext } from './jsoniqParser.js';
import { UpdateLocatorContext } from './jsoniqParser.js';
import { CopyDeclContext } from './jsoniqParser.js';
import { SequenceTypeContext } from './jsoniqParser.js';
import { ObjectConstructorContext } from './jsoniqParser.js';
import { ItemTypeContext } from './jsoniqParser.js';
import { FunctionTestContext } from './jsoniqParser.js';
import { AnyFunctionTestContext } from './jsoniqParser.js';
import { TypedFunctionTestContext } from './jsoniqParser.js';
import { SingleTypeContext } from './jsoniqParser.js';
import { PairConstructorContext } from './jsoniqParser.js';
import { ArrayConstructorContext } from './jsoniqParser.js';
import { UriLiteralContext } from './jsoniqParser.js';
import { StringLiteralContext } from './jsoniqParser.js';
import { KeyWordsContext } from './jsoniqParser.js';

/**
 * This interface defines a complete listener for a parse tree produced by
 * `jsoniqParser`.
 */
export class jsoniqListener implements ParseTreeListener {
  /**
   * Enter a parse tree produced by `jsoniqParser.moduleAndThisIsIt`.
   * @param ctx the parse tree
   */
  enterModuleAndThisIsIt?: (ctx: ModuleAndThisIsItContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.moduleAndThisIsIt`.
   * @param ctx the parse tree
   */
  exitModuleAndThisIsIt?: (ctx: ModuleAndThisIsItContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.module`.
   * @param ctx the parse tree
   */
  enterModule?: (ctx: ModuleContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.module`.
   * @param ctx the parse tree
   */
  exitModule?: (ctx: ModuleContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.mainModule`.
   * @param ctx the parse tree
   */
  enterMainModule?: (ctx: MainModuleContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.mainModule`.
   * @param ctx the parse tree
   */
  exitMainModule?: (ctx: MainModuleContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.libraryModule`.
   * @param ctx the parse tree
   */
  enterLibraryModule?: (ctx: LibraryModuleContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.libraryModule`.
   * @param ctx the parse tree
   */
  exitLibraryModule?: (ctx: LibraryModuleContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.prolog`.
   * @param ctx the parse tree
   */
  enterProlog?: (ctx: PrologContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.prolog`.
   * @param ctx the parse tree
   */
  exitProlog?: (ctx: PrologContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.program`.
   * @param ctx the parse tree
   */
  enterProgram?: (ctx: ProgramContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.program`.
   * @param ctx the parse tree
   */
  exitProgram?: (ctx: ProgramContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.statements`.
   * @param ctx the parse tree
   */
  enterStatements?: (ctx: StatementsContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.statements`.
   * @param ctx the parse tree
   */
  exitStatements?: (ctx: StatementsContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.statementsAndExpr`.
   * @param ctx the parse tree
   */
  enterStatementsAndExpr?: (ctx: StatementsAndExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.statementsAndExpr`.
   * @param ctx the parse tree
   */
  exitStatementsAndExpr?: (ctx: StatementsAndExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.statementsAndOptionalExpr`.
   * @param ctx the parse tree
   */
  enterStatementsAndOptionalExpr?: (
    ctx: StatementsAndOptionalExprContext
  ) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.statementsAndOptionalExpr`.
   * @param ctx the parse tree
   */
  exitStatementsAndOptionalExpr?: (
    ctx: StatementsAndOptionalExprContext
  ) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.statement`.
   * @param ctx the parse tree
   */
  enterStatement?: (ctx: StatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.statement`.
   * @param ctx the parse tree
   */
  exitStatement?: (ctx: StatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.applyStatement`.
   * @param ctx the parse tree
   */
  enterApplyStatement?: (ctx: ApplyStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.applyStatement`.
   * @param ctx the parse tree
   */
  exitApplyStatement?: (ctx: ApplyStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.assignStatement`.
   * @param ctx the parse tree
   */
  enterAssignStatement?: (ctx: AssignStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.assignStatement`.
   * @param ctx the parse tree
   */
  exitAssignStatement?: (ctx: AssignStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.blockStatement`.
   * @param ctx the parse tree
   */
  enterBlockStatement?: (ctx: BlockStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.blockStatement`.
   * @param ctx the parse tree
   */
  exitBlockStatement?: (ctx: BlockStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.breakStatement`.
   * @param ctx the parse tree
   */
  enterBreakStatement?: (ctx: BreakStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.breakStatement`.
   * @param ctx the parse tree
   */
  exitBreakStatement?: (ctx: BreakStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.continueStatement`.
   * @param ctx the parse tree
   */
  enterContinueStatement?: (ctx: ContinueStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.continueStatement`.
   * @param ctx the parse tree
   */
  exitContinueStatement?: (ctx: ContinueStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.exitStatement`.
   * @param ctx the parse tree
   */
  enterExitStatement?: (ctx: ExitStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.exitStatement`.
   * @param ctx the parse tree
   */
  exitExitStatement?: (ctx: ExitStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.flowrStatement`.
   * @param ctx the parse tree
   */
  enterFlowrStatement?: (ctx: FlowrStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.flowrStatement`.
   * @param ctx the parse tree
   */
  exitFlowrStatement?: (ctx: FlowrStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.ifStatement`.
   * @param ctx the parse tree
   */
  enterIfStatement?: (ctx: IfStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.ifStatement`.
   * @param ctx the parse tree
   */
  exitIfStatement?: (ctx: IfStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.switchStatement`.
   * @param ctx the parse tree
   */
  enterSwitchStatement?: (ctx: SwitchStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.switchStatement`.
   * @param ctx the parse tree
   */
  exitSwitchStatement?: (ctx: SwitchStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.switchCaseStatement`.
   * @param ctx the parse tree
   */
  enterSwitchCaseStatement?: (ctx: SwitchCaseStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.switchCaseStatement`.
   * @param ctx the parse tree
   */
  exitSwitchCaseStatement?: (ctx: SwitchCaseStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.tryCatchStatement`.
   * @param ctx the parse tree
   */
  enterTryCatchStatement?: (ctx: TryCatchStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.tryCatchStatement`.
   * @param ctx the parse tree
   */
  exitTryCatchStatement?: (ctx: TryCatchStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.catchCaseStatement`.
   * @param ctx the parse tree
   */
  enterCatchCaseStatement?: (ctx: CatchCaseStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.catchCaseStatement`.
   * @param ctx the parse tree
   */
  exitCatchCaseStatement?: (ctx: CatchCaseStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.typeSwitchStatement`.
   * @param ctx the parse tree
   */
  enterTypeSwitchStatement?: (ctx: TypeSwitchStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.typeSwitchStatement`.
   * @param ctx the parse tree
   */
  exitTypeSwitchStatement?: (ctx: TypeSwitchStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.caseStatement`.
   * @param ctx the parse tree
   */
  enterCaseStatement?: (ctx: CaseStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.caseStatement`.
   * @param ctx the parse tree
   */
  exitCaseStatement?: (ctx: CaseStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.annotation`.
   * @param ctx the parse tree
   */
  enterAnnotation?: (ctx: AnnotationContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.annotation`.
   * @param ctx the parse tree
   */
  exitAnnotation?: (ctx: AnnotationContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.annotations`.
   * @param ctx the parse tree
   */
  enterAnnotations?: (ctx: AnnotationsContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.annotations`.
   * @param ctx the parse tree
   */
  exitAnnotations?: (ctx: AnnotationsContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.varDeclStatement`.
   * @param ctx the parse tree
   */
  enterVarDeclStatement?: (ctx: VarDeclStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.varDeclStatement`.
   * @param ctx the parse tree
   */
  exitVarDeclStatement?: (ctx: VarDeclStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.varDeclForStatement`.
   * @param ctx the parse tree
   */
  enterVarDeclForStatement?: (ctx: VarDeclForStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.varDeclForStatement`.
   * @param ctx the parse tree
   */
  exitVarDeclForStatement?: (ctx: VarDeclForStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.whileStatement`.
   * @param ctx the parse tree
   */
  enterWhileStatement?: (ctx: WhileStatementContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.whileStatement`.
   * @param ctx the parse tree
   */
  exitWhileStatement?: (ctx: WhileStatementContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.setter`.
   * @param ctx the parse tree
   */
  enterSetter?: (ctx: SetterContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.setter`.
   * @param ctx the parse tree
   */
  exitSetter?: (ctx: SetterContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.namespaceDecl`.
   * @param ctx the parse tree
   */
  enterNamespaceDecl?: (ctx: NamespaceDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.namespaceDecl`.
   * @param ctx the parse tree
   */
  exitNamespaceDecl?: (ctx: NamespaceDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.annotatedDecl`.
   * @param ctx the parse tree
   */
  enterAnnotatedDecl?: (ctx: AnnotatedDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.annotatedDecl`.
   * @param ctx the parse tree
   */
  exitAnnotatedDecl?: (ctx: AnnotatedDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.defaultCollationDecl`.
   * @param ctx the parse tree
   */
  enterDefaultCollationDecl?: (ctx: DefaultCollationDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.defaultCollationDecl`.
   * @param ctx the parse tree
   */
  exitDefaultCollationDecl?: (ctx: DefaultCollationDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.orderingModeDecl`.
   * @param ctx the parse tree
   */
  enterOrderingModeDecl?: (ctx: OrderingModeDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.orderingModeDecl`.
   * @param ctx the parse tree
   */
  exitOrderingModeDecl?: (ctx: OrderingModeDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.emptyOrderDecl`.
   * @param ctx the parse tree
   */
  enterEmptyOrderDecl?: (ctx: EmptyOrderDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.emptyOrderDecl`.
   * @param ctx the parse tree
   */
  exitEmptyOrderDecl?: (ctx: EmptyOrderDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.decimalFormatDecl`.
   * @param ctx the parse tree
   */
  enterDecimalFormatDecl?: (ctx: DecimalFormatDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.decimalFormatDecl`.
   * @param ctx the parse tree
   */
  exitDecimalFormatDecl?: (ctx: DecimalFormatDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.qname`.
   * @param ctx the parse tree
   */
  enterQname?: (ctx: QnameContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.qname`.
   * @param ctx the parse tree
   */
  exitQname?: (ctx: QnameContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.dfPropertyName`.
   * @param ctx the parse tree
   */
  enterDfPropertyName?: (ctx: DfPropertyNameContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.dfPropertyName`.
   * @param ctx the parse tree
   */
  exitDfPropertyName?: (ctx: DfPropertyNameContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.moduleImport`.
   * @param ctx the parse tree
   */
  enterModuleImport?: (ctx: ModuleImportContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.moduleImport`.
   * @param ctx the parse tree
   */
  exitModuleImport?: (ctx: ModuleImportContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.varDecl`.
   * @param ctx the parse tree
   */
  enterVarDecl?: (ctx: VarDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.varDecl`.
   * @param ctx the parse tree
   */
  exitVarDecl?: (ctx: VarDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.contextItemDecl`.
   * @param ctx the parse tree
   */
  enterContextItemDecl?: (ctx: ContextItemDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.contextItemDecl`.
   * @param ctx the parse tree
   */
  exitContextItemDecl?: (ctx: ContextItemDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.functionDecl`.
   * @param ctx the parse tree
   */
  enterFunctionDecl?: (ctx: FunctionDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.functionDecl`.
   * @param ctx the parse tree
   */
  exitFunctionDecl?: (ctx: FunctionDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.typeDecl`.
   * @param ctx the parse tree
   */
  enterTypeDecl?: (ctx: TypeDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.typeDecl`.
   * @param ctx the parse tree
   */
  exitTypeDecl?: (ctx: TypeDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.schemaLanguage`.
   * @param ctx the parse tree
   */
  enterSchemaLanguage?: (ctx: SchemaLanguageContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.schemaLanguage`.
   * @param ctx the parse tree
   */
  exitSchemaLanguage?: (ctx: SchemaLanguageContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.paramList`.
   * @param ctx the parse tree
   */
  enterParamList?: (ctx: ParamListContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.paramList`.
   * @param ctx the parse tree
   */
  exitParamList?: (ctx: ParamListContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.param`.
   * @param ctx the parse tree
   */
  enterParam?: (ctx: ParamContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.param`.
   * @param ctx the parse tree
   */
  exitParam?: (ctx: ParamContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.expr`.
   * @param ctx the parse tree
   */
  enterExpr?: (ctx: ExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.expr`.
   * @param ctx the parse tree
   */
  exitExpr?: (ctx: ExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.exprSingle`.
   * @param ctx the parse tree
   */
  enterExprSingle?: (ctx: ExprSingleContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.exprSingle`.
   * @param ctx the parse tree
   */
  exitExprSingle?: (ctx: ExprSingleContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.exprSimple`.
   * @param ctx the parse tree
   */
  enterExprSimple?: (ctx: ExprSimpleContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.exprSimple`.
   * @param ctx the parse tree
   */
  exitExprSimple?: (ctx: ExprSimpleContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.flowrExpr`.
   * @param ctx the parse tree
   */
  enterFlowrExpr?: (ctx: FlowrExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.flowrExpr`.
   * @param ctx the parse tree
   */
  exitFlowrExpr?: (ctx: FlowrExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.forClause`.
   * @param ctx the parse tree
   */
  enterForClause?: (ctx: ForClauseContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.forClause`.
   * @param ctx the parse tree
   */
  exitForClause?: (ctx: ForClauseContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.forVar`.
   * @param ctx the parse tree
   */
  enterForVar?: (ctx: ForVarContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.forVar`.
   * @param ctx the parse tree
   */
  exitForVar?: (ctx: ForVarContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.letClause`.
   * @param ctx the parse tree
   */
  enterLetClause?: (ctx: LetClauseContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.letClause`.
   * @param ctx the parse tree
   */
  exitLetClause?: (ctx: LetClauseContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.letVar`.
   * @param ctx the parse tree
   */
  enterLetVar?: (ctx: LetVarContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.letVar`.
   * @param ctx the parse tree
   */
  exitLetVar?: (ctx: LetVarContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.whereClause`.
   * @param ctx the parse tree
   */
  enterWhereClause?: (ctx: WhereClauseContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.whereClause`.
   * @param ctx the parse tree
   */
  exitWhereClause?: (ctx: WhereClauseContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.groupByClause`.
   * @param ctx the parse tree
   */
  enterGroupByClause?: (ctx: GroupByClauseContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.groupByClause`.
   * @param ctx the parse tree
   */
  exitGroupByClause?: (ctx: GroupByClauseContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.groupByVar`.
   * @param ctx the parse tree
   */
  enterGroupByVar?: (ctx: GroupByVarContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.groupByVar`.
   * @param ctx the parse tree
   */
  exitGroupByVar?: (ctx: GroupByVarContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.orderByClause`.
   * @param ctx the parse tree
   */
  enterOrderByClause?: (ctx: OrderByClauseContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.orderByClause`.
   * @param ctx the parse tree
   */
  exitOrderByClause?: (ctx: OrderByClauseContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.orderByExpr`.
   * @param ctx the parse tree
   */
  enterOrderByExpr?: (ctx: OrderByExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.orderByExpr`.
   * @param ctx the parse tree
   */
  exitOrderByExpr?: (ctx: OrderByExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.countClause`.
   * @param ctx the parse tree
   */
  enterCountClause?: (ctx: CountClauseContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.countClause`.
   * @param ctx the parse tree
   */
  exitCountClause?: (ctx: CountClauseContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.quantifiedExpr`.
   * @param ctx the parse tree
   */
  enterQuantifiedExpr?: (ctx: QuantifiedExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.quantifiedExpr`.
   * @param ctx the parse tree
   */
  exitQuantifiedExpr?: (ctx: QuantifiedExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.quantifiedExprVar`.
   * @param ctx the parse tree
   */
  enterQuantifiedExprVar?: (ctx: QuantifiedExprVarContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.quantifiedExprVar`.
   * @param ctx the parse tree
   */
  exitQuantifiedExprVar?: (ctx: QuantifiedExprVarContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.switchExpr`.
   * @param ctx the parse tree
   */
  enterSwitchExpr?: (ctx: SwitchExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.switchExpr`.
   * @param ctx the parse tree
   */
  exitSwitchExpr?: (ctx: SwitchExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.switchCaseClause`.
   * @param ctx the parse tree
   */
  enterSwitchCaseClause?: (ctx: SwitchCaseClauseContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.switchCaseClause`.
   * @param ctx the parse tree
   */
  exitSwitchCaseClause?: (ctx: SwitchCaseClauseContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.typeSwitchExpr`.
   * @param ctx the parse tree
   */
  enterTypeSwitchExpr?: (ctx: TypeSwitchExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.typeSwitchExpr`.
   * @param ctx the parse tree
   */
  exitTypeSwitchExpr?: (ctx: TypeSwitchExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.caseClause`.
   * @param ctx the parse tree
   */
  enterCaseClause?: (ctx: CaseClauseContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.caseClause`.
   * @param ctx the parse tree
   */
  exitCaseClause?: (ctx: CaseClauseContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.ifExpr`.
   * @param ctx the parse tree
   */
  enterIfExpr?: (ctx: IfExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.ifExpr`.
   * @param ctx the parse tree
   */
  exitIfExpr?: (ctx: IfExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.tryCatchExpr`.
   * @param ctx the parse tree
   */
  enterTryCatchExpr?: (ctx: TryCatchExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.tryCatchExpr`.
   * @param ctx the parse tree
   */
  exitTryCatchExpr?: (ctx: TryCatchExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.catchClause`.
   * @param ctx the parse tree
   */
  enterCatchClause?: (ctx: CatchClauseContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.catchClause`.
   * @param ctx the parse tree
   */
  exitCatchClause?: (ctx: CatchClauseContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.orExpr`.
   * @param ctx the parse tree
   */
  enterOrExpr?: (ctx: OrExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.orExpr`.
   * @param ctx the parse tree
   */
  exitOrExpr?: (ctx: OrExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.andExpr`.
   * @param ctx the parse tree
   */
  enterAndExpr?: (ctx: AndExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.andExpr`.
   * @param ctx the parse tree
   */
  exitAndExpr?: (ctx: AndExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.notExpr`.
   * @param ctx the parse tree
   */
  enterNotExpr?: (ctx: NotExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.notExpr`.
   * @param ctx the parse tree
   */
  exitNotExpr?: (ctx: NotExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.comparisonExpr`.
   * @param ctx the parse tree
   */
  enterComparisonExpr?: (ctx: ComparisonExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.comparisonExpr`.
   * @param ctx the parse tree
   */
  exitComparisonExpr?: (ctx: ComparisonExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.stringConcatExpr`.
   * @param ctx the parse tree
   */
  enterStringConcatExpr?: (ctx: StringConcatExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.stringConcatExpr`.
   * @param ctx the parse tree
   */
  exitStringConcatExpr?: (ctx: StringConcatExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.rangeExpr`.
   * @param ctx the parse tree
   */
  enterRangeExpr?: (ctx: RangeExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.rangeExpr`.
   * @param ctx the parse tree
   */
  exitRangeExpr?: (ctx: RangeExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.additiveExpr`.
   * @param ctx the parse tree
   */
  enterAdditiveExpr?: (ctx: AdditiveExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.additiveExpr`.
   * @param ctx the parse tree
   */
  exitAdditiveExpr?: (ctx: AdditiveExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.multiplicativeExpr`.
   * @param ctx the parse tree
   */
  enterMultiplicativeExpr?: (ctx: MultiplicativeExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.multiplicativeExpr`.
   * @param ctx the parse tree
   */
  exitMultiplicativeExpr?: (ctx: MultiplicativeExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.instanceOfExpr`.
   * @param ctx the parse tree
   */
  enterInstanceOfExpr?: (ctx: InstanceOfExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.instanceOfExpr`.
   * @param ctx the parse tree
   */
  exitInstanceOfExpr?: (ctx: InstanceOfExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.isStaticallyExpr`.
   * @param ctx the parse tree
   */
  enterIsStaticallyExpr?: (ctx: IsStaticallyExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.isStaticallyExpr`.
   * @param ctx the parse tree
   */
  exitIsStaticallyExpr?: (ctx: IsStaticallyExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.treatExpr`.
   * @param ctx the parse tree
   */
  enterTreatExpr?: (ctx: TreatExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.treatExpr`.
   * @param ctx the parse tree
   */
  exitTreatExpr?: (ctx: TreatExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.castableExpr`.
   * @param ctx the parse tree
   */
  enterCastableExpr?: (ctx: CastableExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.castableExpr`.
   * @param ctx the parse tree
   */
  exitCastableExpr?: (ctx: CastableExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.castExpr`.
   * @param ctx the parse tree
   */
  enterCastExpr?: (ctx: CastExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.castExpr`.
   * @param ctx the parse tree
   */
  exitCastExpr?: (ctx: CastExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.arrowExpr`.
   * @param ctx the parse tree
   */
  enterArrowExpr?: (ctx: ArrowExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.arrowExpr`.
   * @param ctx the parse tree
   */
  exitArrowExpr?: (ctx: ArrowExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.arrowFunctionSpecifier`.
   * @param ctx the parse tree
   */
  enterArrowFunctionSpecifier?: (ctx: ArrowFunctionSpecifierContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.arrowFunctionSpecifier`.
   * @param ctx the parse tree
   */
  exitArrowFunctionSpecifier?: (ctx: ArrowFunctionSpecifierContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.unaryExpr`.
   * @param ctx the parse tree
   */
  enterUnaryExpr?: (ctx: UnaryExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.unaryExpr`.
   * @param ctx the parse tree
   */
  exitUnaryExpr?: (ctx: UnaryExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.valueExpr`.
   * @param ctx the parse tree
   */
  enterValueExpr?: (ctx: ValueExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.valueExpr`.
   * @param ctx the parse tree
   */
  exitValueExpr?: (ctx: ValueExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.validateExpr`.
   * @param ctx the parse tree
   */
  enterValidateExpr?: (ctx: ValidateExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.validateExpr`.
   * @param ctx the parse tree
   */
  exitValidateExpr?: (ctx: ValidateExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.annotateExpr`.
   * @param ctx the parse tree
   */
  enterAnnotateExpr?: (ctx: AnnotateExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.annotateExpr`.
   * @param ctx the parse tree
   */
  exitAnnotateExpr?: (ctx: AnnotateExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.simpleMapExpr`.
   * @param ctx the parse tree
   */
  enterSimpleMapExpr?: (ctx: SimpleMapExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.simpleMapExpr`.
   * @param ctx the parse tree
   */
  exitSimpleMapExpr?: (ctx: SimpleMapExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.postFixExpr`.
   * @param ctx the parse tree
   */
  enterPostFixExpr?: (ctx: PostFixExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.postFixExpr`.
   * @param ctx the parse tree
   */
  exitPostFixExpr?: (ctx: PostFixExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.arrayLookup`.
   * @param ctx the parse tree
   */
  enterArrayLookup?: (ctx: ArrayLookupContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.arrayLookup`.
   * @param ctx the parse tree
   */
  exitArrayLookup?: (ctx: ArrayLookupContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.arrayUnboxing`.
   * @param ctx the parse tree
   */
  enterArrayUnboxing?: (ctx: ArrayUnboxingContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.arrayUnboxing`.
   * @param ctx the parse tree
   */
  exitArrayUnboxing?: (ctx: ArrayUnboxingContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.predicate`.
   * @param ctx the parse tree
   */
  enterPredicate?: (ctx: PredicateContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.predicate`.
   * @param ctx the parse tree
   */
  exitPredicate?: (ctx: PredicateContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.objectLookup`.
   * @param ctx the parse tree
   */
  enterObjectLookup?: (ctx: ObjectLookupContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.objectLookup`.
   * @param ctx the parse tree
   */
  exitObjectLookup?: (ctx: ObjectLookupContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.primaryExpr`.
   * @param ctx the parse tree
   */
  enterPrimaryExpr?: (ctx: PrimaryExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.primaryExpr`.
   * @param ctx the parse tree
   */
  exitPrimaryExpr?: (ctx: PrimaryExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.blockExpr`.
   * @param ctx the parse tree
   */
  enterBlockExpr?: (ctx: BlockExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.blockExpr`.
   * @param ctx the parse tree
   */
  exitBlockExpr?: (ctx: BlockExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.varRef`.
   * @param ctx the parse tree
   */
  enterVarRef?: (ctx: VarRefContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.varRef`.
   * @param ctx the parse tree
   */
  exitVarRef?: (ctx: VarRefContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.parenthesizedExpr`.
   * @param ctx the parse tree
   */
  enterParenthesizedExpr?: (ctx: ParenthesizedExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.parenthesizedExpr`.
   * @param ctx the parse tree
   */
  exitParenthesizedExpr?: (ctx: ParenthesizedExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.contextItemExpr`.
   * @param ctx the parse tree
   */
  enterContextItemExpr?: (ctx: ContextItemExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.contextItemExpr`.
   * @param ctx the parse tree
   */
  exitContextItemExpr?: (ctx: ContextItemExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.orderedExpr`.
   * @param ctx the parse tree
   */
  enterOrderedExpr?: (ctx: OrderedExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.orderedExpr`.
   * @param ctx the parse tree
   */
  exitOrderedExpr?: (ctx: OrderedExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.unorderedExpr`.
   * @param ctx the parse tree
   */
  enterUnorderedExpr?: (ctx: UnorderedExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.unorderedExpr`.
   * @param ctx the parse tree
   */
  exitUnorderedExpr?: (ctx: UnorderedExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.functionCall`.
   * @param ctx the parse tree
   */
  enterFunctionCall?: (ctx: FunctionCallContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.functionCall`.
   * @param ctx the parse tree
   */
  exitFunctionCall?: (ctx: FunctionCallContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.argumentList`.
   * @param ctx the parse tree
   */
  enterArgumentList?: (ctx: ArgumentListContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.argumentList`.
   * @param ctx the parse tree
   */
  exitArgumentList?: (ctx: ArgumentListContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.argument`.
   * @param ctx the parse tree
   */
  enterArgument?: (ctx: ArgumentContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.argument`.
   * @param ctx the parse tree
   */
  exitArgument?: (ctx: ArgumentContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.functionItemExpr`.
   * @param ctx the parse tree
   */
  enterFunctionItemExpr?: (ctx: FunctionItemExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.functionItemExpr`.
   * @param ctx the parse tree
   */
  exitFunctionItemExpr?: (ctx: FunctionItemExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.namedFunctionRef`.
   * @param ctx the parse tree
   */
  enterNamedFunctionRef?: (ctx: NamedFunctionRefContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.namedFunctionRef`.
   * @param ctx the parse tree
   */
  exitNamedFunctionRef?: (ctx: NamedFunctionRefContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.inlineFunctionExpr`.
   * @param ctx the parse tree
   */
  enterInlineFunctionExpr?: (ctx: InlineFunctionExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.inlineFunctionExpr`.
   * @param ctx the parse tree
   */
  exitInlineFunctionExpr?: (ctx: InlineFunctionExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.insertExpr`.
   * @param ctx the parse tree
   */
  enterInsertExpr?: (ctx: InsertExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.insertExpr`.
   * @param ctx the parse tree
   */
  exitInsertExpr?: (ctx: InsertExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.deleteExpr`.
   * @param ctx the parse tree
   */
  enterDeleteExpr?: (ctx: DeleteExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.deleteExpr`.
   * @param ctx the parse tree
   */
  exitDeleteExpr?: (ctx: DeleteExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.renameExpr`.
   * @param ctx the parse tree
   */
  enterRenameExpr?: (ctx: RenameExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.renameExpr`.
   * @param ctx the parse tree
   */
  exitRenameExpr?: (ctx: RenameExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.replaceExpr`.
   * @param ctx the parse tree
   */
  enterReplaceExpr?: (ctx: ReplaceExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.replaceExpr`.
   * @param ctx the parse tree
   */
  exitReplaceExpr?: (ctx: ReplaceExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.transformExpr`.
   * @param ctx the parse tree
   */
  enterTransformExpr?: (ctx: TransformExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.transformExpr`.
   * @param ctx the parse tree
   */
  exitTransformExpr?: (ctx: TransformExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.appendExpr`.
   * @param ctx the parse tree
   */
  enterAppendExpr?: (ctx: AppendExprContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.appendExpr`.
   * @param ctx the parse tree
   */
  exitAppendExpr?: (ctx: AppendExprContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.updateLocator`.
   * @param ctx the parse tree
   */
  enterUpdateLocator?: (ctx: UpdateLocatorContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.updateLocator`.
   * @param ctx the parse tree
   */
  exitUpdateLocator?: (ctx: UpdateLocatorContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.copyDecl`.
   * @param ctx the parse tree
   */
  enterCopyDecl?: (ctx: CopyDeclContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.copyDecl`.
   * @param ctx the parse tree
   */
  exitCopyDecl?: (ctx: CopyDeclContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.sequenceType`.
   * @param ctx the parse tree
   */
  enterSequenceType?: (ctx: SequenceTypeContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.sequenceType`.
   * @param ctx the parse tree
   */
  exitSequenceType?: (ctx: SequenceTypeContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.objectConstructor`.
   * @param ctx the parse tree
   */
  enterObjectConstructor?: (ctx: ObjectConstructorContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.objectConstructor`.
   * @param ctx the parse tree
   */
  exitObjectConstructor?: (ctx: ObjectConstructorContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.itemType`.
   * @param ctx the parse tree
   */
  enterItemType?: (ctx: ItemTypeContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.itemType`.
   * @param ctx the parse tree
   */
  exitItemType?: (ctx: ItemTypeContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.functionTest`.
   * @param ctx the parse tree
   */
  enterFunctionTest?: (ctx: FunctionTestContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.functionTest`.
   * @param ctx the parse tree
   */
  exitFunctionTest?: (ctx: FunctionTestContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.anyFunctionTest`.
   * @param ctx the parse tree
   */
  enterAnyFunctionTest?: (ctx: AnyFunctionTestContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.anyFunctionTest`.
   * @param ctx the parse tree
   */
  exitAnyFunctionTest?: (ctx: AnyFunctionTestContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.typedFunctionTest`.
   * @param ctx the parse tree
   */
  enterTypedFunctionTest?: (ctx: TypedFunctionTestContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.typedFunctionTest`.
   * @param ctx the parse tree
   */
  exitTypedFunctionTest?: (ctx: TypedFunctionTestContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.singleType`.
   * @param ctx the parse tree
   */
  enterSingleType?: (ctx: SingleTypeContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.singleType`.
   * @param ctx the parse tree
   */
  exitSingleType?: (ctx: SingleTypeContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.pairConstructor`.
   * @param ctx the parse tree
   */
  enterPairConstructor?: (ctx: PairConstructorContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.pairConstructor`.
   * @param ctx the parse tree
   */
  exitPairConstructor?: (ctx: PairConstructorContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.arrayConstructor`.
   * @param ctx the parse tree
   */
  enterArrayConstructor?: (ctx: ArrayConstructorContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.arrayConstructor`.
   * @param ctx the parse tree
   */
  exitArrayConstructor?: (ctx: ArrayConstructorContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.uriLiteral`.
   * @param ctx the parse tree
   */
  enterUriLiteral?: (ctx: UriLiteralContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.uriLiteral`.
   * @param ctx the parse tree
   */
  exitUriLiteral?: (ctx: UriLiteralContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.stringLiteral`.
   * @param ctx the parse tree
   */
  enterStringLiteral?: (ctx: StringLiteralContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.stringLiteral`.
   * @param ctx the parse tree
   */
  exitStringLiteral?: (ctx: StringLiteralContext) => void;
  /**
   * Enter a parse tree produced by `jsoniqParser.keyWords`.
   * @param ctx the parse tree
   */
  enterKeyWords?: (ctx: KeyWordsContext) => void;
  /**
   * Exit a parse tree produced by `jsoniqParser.keyWords`.
   * @param ctx the parse tree
   */
  exitKeyWords?: (ctx: KeyWordsContext) => void;

  visitTerminal(node: TerminalNode): void {}
  visitErrorNode(node: ErrorNode): void {}
  enterEveryRule(node: ParserRuleContext): void {}
  exitEveryRule(node: ParserRuleContext): void {}
}
