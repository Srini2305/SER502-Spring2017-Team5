/** Grammar For DevilsCode */

grammar DevilsCode;

/** Parser  Rules */
/** Start Rule */
program
    : 'main ' '(' ')' 
      '{' 
      stmtlists
      '}' 
    ;

/** Statement Lists 
* <stmts> ::= <stmts> <stmt> | ε
*/
stmtlists
    : stmtlists stmt
    | /* epsilon */
    ;

/** Statement 
* <stmt> ::= <expr> ';'
*          | <dec_stmt> ';'
*          | <while_stmt>
*          | <if_stmt>
*          | '{' <stmts> '}'
*/
stmt 
    : expr ';'
    | dec_stmt ';'
    | while_stmt
    | if_stmt
    | '{' stmtlists '}'
    | 'print ' IDENT ';'
    | 'print ' number ';'
    ;

/** Expression
* <expr> ::= <id>
*          | <assign_expr>
*          | <math_expr>
*          | <cpr_expr>
*/
expr
    : IDENT
    | assign_expr
    | math_expr
    | cpr_expr
    ;

/** Declaration
* <dec_stmt> ::= <data_type> <id> 
*              | <data_type> <assign_expr>
*/
dec_stmt
    : DATA_TYPE IDENT
    | DATA_TYPE assign_expr
    ;

/** Assignment
* <assign_expr> ::= <id> ‘=’ <expr>
*/
assign_expr
    : IDENT '=' expr
    ;

/** Arithmetic expression
* <math_expr> ::= <math_expr> '+' <math_term>
*               | <math_expr> '-' <math_term> 
*               | <math_term>
*
* <math_term> ::= <math_term> '*' <math_factor> 
*               | <math_term> '/' <math_factor> 
*               | <math_factor>
*
* <math_factor> ::= <number> | '(' <math_expr> ')'
*
* <number> ::= <number> <digit> | <digit>
*/
math_expr
    : math_expr '+' math_term
    | math_expr '-' math_term
    | math_term
    ;

math_term
    : math_term '*' math_factor
    | math_term '/' math_factor
    | math_factor
    ;

math_factor
    : number
    | '(' math_expr ')'
    | IDENT
    ;

number
    : number DIGIT
    | DIGIT
    ;

/** Iteration - While Loop 
* <while_stmt> ::= while '(' <expr> ')' <stmt>
*/
while_stmt
    : 'while ' '(' expr ')' stmt ;

/** Condition - If Statement
* <if_stmt> ::= if '(' <expr> ')' <stmt>
*             | if '(' <expr> ')' <stmt> else <stmt>
*/
if_stmt
    : 'if ' '(' expr ')' stmt (else_stmt)?
    ;

else_stmt
    : 'else' stmt
    ;

/** Comparison
* <cpr_expr> ::= <cpr_term> <cpr_symbol> <cpr_term>
* <cpr_term> ::= <id> | <number> | '(' <math_expr> ')'
*/
cpr_expr 
    : cpr_term CPR_SYMBOL cpr_term
    ;

cpr_term
    : IDENT
    | number
    | '(' math_expr ')'
    ;

/** ******************************************************* */
/** Lexer Rules */
/**  Data Type */
DATA_TYPE : 'int ' | 'bool ' ;

/** Identifier - Start with lower case letter */
IDENT : [a-z] ([a-zA-Z] | '0'..'9')* ;

/** Digit */
DIGIT : [0-9] ;

/** Comparison Operators
* <cpr_symbol> ::= '<' | '<=' | '>' | '>=' | '=='
*/
CPR_SYMBOL : '<' | '<=' | '>' | '>=' | '==' ;

/** White Space (Ignored) */
WS : [ \r\t\n]+ -> skip ;
