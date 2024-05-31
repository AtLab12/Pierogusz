grammar Pierogusz;

program: statement+;

statement
    : varDecl 
    | arrayDecl 
    | matrixDecl
    | printStmt 
    | readStmt 
    | assignStmt 
    | arrayAssignStmt 
    | matrixAssignStmt
    ;

varDecl
    : 'int' ID ';' 
    | 'float32' ID ';' 
    | 'float64' ID ';' 
    | 'string' ID ';'
    | 'bool' ID ';'
    ;

arrayDecl
    : ('int' | 'float32' | 'float64' | 'string' | 'bool') ID '[' INT ']' ';'
    ;

matrixDecl
    : ('int' | 'float32' | 'float64' | 'string' | 'bool') ID '[' INT ']' '[' INT ']' ';'
    ;

printStmt
    : 'print' expr ';'
    ;

readStmt
    : 'read' ID ';'
    ;

assignStmt
    : ID '=' expr ';'
    ;

arrayAssignStmt
    : ID '[' expr ']' '=' expr ';'
    ;

matrixAssignStmt
    : ID '[' expr ']' '[' expr ']' '=' expr ';'
    ;

expr
    : expr ('+' | '-' | '*' | '/' | 'AND' | 'OR' | 'XOR') expr
    | 'NEG' expr
    | ID
    | ID '[' expr ']'
    | ID '[' expr ']' '[' expr ']'
    | INT
    | FLOAT
    | SCIENTIFIC_FLOAT
    | STRING
    | BOOL
    ;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]*;
SCIENTIFIC_FLOAT: [0-9]+ ('.' [0-9]*)? [eE] [+-]? [0-9]+;
STRING: '"' (~["\r\n])* '"';
BOOL: 'true' | 'false';
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
