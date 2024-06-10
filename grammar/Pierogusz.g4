grammar Pierogusz;

// Reguły startowe
prog : (statement SEMI)+ EOF;

block: LCURLY (statement SEMI)* RCURLY;

// Instrukcje
statement
    : variableDeclaration
    | assignment
    | printCall
    | readCall
    | ifElseStatement
    | ifStatement
    | functionDefinition
    | functionCall
    | loopTimes
    | structureDefinition
    ;

variableDeclaration
    : dataType ID
    | structureDeclaration
    ;

assignment : (ID | fieldAccess) ASSIGN expression;

printCall : PRINT LPAREN (ID | fieldAccess) RPAREN ;
//printCall : PRINT LPAREN expression RPAREN ;

readCall : READ LPAREN ID RPAREN ;

expression
    : value
    | conversion
    | logicalExpression
    | additiveExpression
    | LPAREN expression RPAREN
    | structureInstantiation
    | fieldAccess
    ;

logicalExpression
    : simpleLogicalExpression OR simpleLogicalExpression  #or
    | simpleLogicalExpression XOR simpleLogicalExpression #xor
    | simpleLogicalExpression AND simpleLogicalExpression #and
    | simpleLogicalExpression EQ simpleLogicalExpression  #equal
    | EXCLAMATION simpleLogicalExpression    #negation
    | simpleLogicalExpression                #simpleBoolValue
    | BOOL                        #bool
    ;

simpleLogicalExpression
    : value
    | additiveExpression
    | comparisonExp
    ;

additiveExpression
    : multiplicativeExpression #singleValue3
    | additiveExpression PLUS multiplicativeExpression  #add
    | additiveExpression MINUS multiplicativeExpression #substract
    ;

multiplicativeExpression
    : unaryExpression #singleValue2
    | multiplicativeExpression ASTERISK unaryExpression #multiply
    | multiplicativeExpression SLASH unaryExpression    #divide
    ;

unaryExpression
    : primaryExpression #singleValue1
    | PLUS unaryExpression  #positive
    | MINUS unaryExpression #negative
    ;

primaryExpression
    : value
    | conversion
    | LPAREN expression RPAREN
    ;

ifElseStatement: IF condition ifBlock ELSE elseBlock;
ifStatement: IF condition ifBlock;
ifBlock : block;
elseBlock : block;

condition :  LPAREN logicalExpression RPAREN;

comparisonExp
    : ID LT value    #lesserThan
    | ID LTE value   #lesserThanEqual
    | ID GT value    #greaterThan
    | ID GTE value   #greaterThanEqual
    | ID EQ value    #isEqual
    | ID NEQ value   #notEqual
    ;


functionDefinition: FUNCTION functionName LPAREN functionParams RPAREN functionBlock;
functionName: ID;
functionParams :(variableDeclaration (COMMA variableDeclaration)*)?;
functionBlock: block;
functionCall: functionName LPAREN functionArguments RPAREN;
functionArguments: (value (COMMA value)*)?;

loopTimes: LOOP LPAREN repetitions RPAREN loopBlock ;
repetitions: INT;
loopBlock: block;

structureDefinition : STRUCT structureType LCURLY structFieldDef+ RCURLY;

structureDeclaration : structureType ID;

structFieldDef : dataType ID SEMI;
//structFieldDef : variableDeclaration SEMI;

structureInstantiation  : LCURLY fieldInitializationList RCURLY;

fieldInitializationList : fieldInitialization (SEMI fieldInitialization)* SEMI?;

fieldInitialization : ID ASSIGN value;

fieldAccess : ID DOT ID;


conversion
    : TO_INT LPAREN expression RPAREN   #toIntExpression
    | TO_FLOAT LPAREN expression RPAREN #toFloatExpression
    | TO_STRING LPAREN expression RPAREN #toStringExpression
    ;

value
    : ID
    | INT
    | FLOAT
    | STRING
    | BOOL
    | structureInstantiation
    ;

dataType : INT_KEY
    | FLOAT_KEY
    | FLOAT_32_KEY
    | FLOAT_64_KEY
    | STRING_KEY
    | BOOL_KEY
    | structureType
    ;

structureType : ID;


IF: 'if';
THEN: 'then';
ELSE: 'else';
ENDIF: 'eif';

LOOP: 'loop';

FUNCTION: 'function';

PRINT:	'print' ;
READ:	'read' ;

TO_INT : 'toInt';
TO_FLOAT : 'toFloat';
TO_STRING : 'toString';

AND : '&&' ;
OR : '||' ;
XOR : '^^' ;
EQ : '==' ;
NEQ : '!=' ;
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';
ASSIGN : '=';
COMMA : ',' ;
SEMI : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;
LBRACK : '[' ;
RBRACK : ']' ;

INT_KEY: 'int' ;
FLOAT_KEY: 'float';
FLOAT_32_KEY: 'float32';
FLOAT_64_KEY: 'float64';
STRING_KEY: 'string' ;
BOOL_KEY: 'bool' ;
STRUCT : 'struct';

FLOAT : INT DOT INT ;
INT : [0-9]+ ;
STRING: DQ ~["\r\n]* DQ;
BOOL: TRUE | FALSE ;
TRUE: 'true';
FALSE:'false';

PLUS: '+' ;
MINUS: '-' ;
ASTERISK: '*' ;
SLASH: '/';
DOT: '.';
EXCLAMATION: '!';
DQ: '"';
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;
