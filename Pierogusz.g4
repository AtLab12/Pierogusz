grammar Pierogusz;

program: statement+;

statement: varDecl | printStmt | readStmt | assignStmt;

varDecl: 'int' ID ';' | 'float' ID ';';
printStmt: 'print' expr ';';
readStmt: 'read' ID ';';
assignStmt: ID '=' expr ';';

expr: expr ('+' | '-' | '*' | '/') expr | ID | INT | FLOAT;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]*;
WS: [ \t\r\n]+ -> skip;