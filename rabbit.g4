grammar rabbit;
KATY: ('prawo'|'lewo'|'gora'|'dol');
prog:	cmd;
cmd: go #Command
   | jump #Command
   | home #Command
   | angle #Command
   | setView #Command
   | for #Command
   | if #IfBlock
   | getX #Command
   | getY #Command
   | getAngle #Command
   | getItem #Command
   | putItem #Command
   | checkField #Command
   | spaceLeft #Command
   | setValue #Reassignment
   | sleep #Command
   | declaration #DeclarationExpr
   | sleep #Command
   | print #Command
   | restart #Command
   ;

restart: 'reset';

print: 'print 'expr;
declaration: 'int ' name ' 'expr
        | 'bool ' name ' '(TRUE|FALSE)
        | 'bool ' name' ' comparison;
block: '{'cmd*'}' ;
if: 'if ' comparison '?' block 'endif'|
    'if ' comparison '?' block 'else' block 'endif';
for: 'for' expr  block 'endfor';
comparison
   : (expr) comparisonOperator (expr|comparison)|expr
   ;
getX: 'getX';
getY: 'getY';
setValue: 'name ' expr|
    'name ' (TRUE|FALSE);

angle: 'angle ' ('90'|'180'|'270'|'360');

setView: 'setview ' KATY;

spaceLeft: 'spaceLeft';

checkField:'checkField';


putItem: 'putItem';

getItem: 'getItem';

getAngle: 'getAngle';

jump: 'jump 'expr ' ' expr;

sleep: 'sleep ' expr;
go:
    'go ' expr;
home:
    'home';
comparisonOperator: '<'
   | '>'
   | '=='
   | '!='
   | '<='
   | '>='
   | ' and '
   | ' or '
   ;
name
   : STRING
   ;
value
   : INT
   | TRUE
   | FALSE
   | name
   | ('90'|'180'|'270'|'360');

expr:
        value ('*'|'/') (value|expr)        #InfiExpr
    |	value ('+'|'-') (value|expr)        #InfiExpr
    |   value                               #NumberExpr
    ;
INT  : [-]*[0-9]+;
TRUE: 'TRUE'
    | 'true'
    | 'True';
FALSE: 'FALSE'
    | 'false'
    | 'False';
STRING : [a-zA-Z][a-zA-Z0-9_]*;
WS   : [ \t]+ -> skip ;
