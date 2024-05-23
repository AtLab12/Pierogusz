grammar Pierogusz;

program: statement+;

statement: varDecl | arrayDecl | printStmt | readStmt | assignStmt | arrayAssignStmt;

varDecl: 'int' ID ';' | 'float32' ID ';' | 'float64' ID ';' | 'string' ID ';';
arrayDecl: ('int' | 'float32' | 'float64' | 'string') ID '[' INT ']' ';';

printStmt: 'print' expr ';';
readStmt: 'read' ID ';';
assignStmt: ID '=' expr ';';
arrayAssignStmt: ID '[' expr ']' '=' expr ';';

expr:
    expr ('+' | '-' | '*' | '/') expr
    | ID
    | ID '[' expr ']'
    | INT
    | FLOAT
    | SCIENTIFIC_FLOAT
    | STRING;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]*;
SCIENTIFIC_FLOAT: [0-9]+ ('.' [0-9]*)? [eE] [+-]? [0-9]+;
STRING: '"' (~["\r\n])* '"';
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
