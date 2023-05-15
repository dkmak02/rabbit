grammar rabbit;
KATY: ('prawo'|'lewo'|'gora'|'dol');
prog:	cmd;
cmd: go #Command
   | jump #Command
   | home #Command
   | angle #Command
   | setView #Command
   | for #ForBlock
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
   | reverseBool #ReverseBoolVar
   | fun #Function
   | call #CallFunction
   ;

call: name '('(name', '|expr', ')*(name|expr)*')';

fun:('bool '|'int '|'void ')  name '('(name', '|INT', ')*(name|INT)?') ' block (' ' ( 'return ' expr))?;

reverseBool: name ' !'name;


restart: 'reset';

print: 'print 'expr;
declaration: 'int ' name ' '(expr|call)
        | 'bool ' name ' '(TRUE|FALSE)
        | 'bool ' name' ' (comparison|call);

if: 'if ' comparison ' ? ' block (' else ' block)?;
block: '{ ' (cmd ' '+)+ '}';
for: 'for ' expr ' '  block;
comparison: expr comparisonOperator (expr | comparison) | '(' comparison ')' | value;
getX: 'getX';
getY: 'getY';
setValue: name ' ' expr|
    name ' '  (TRUE|FALSE) |
    name' ' comparison;

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
    'go ' (expr);
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
   | call
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
WS: [\r]+ -> skip;
TAB: [\t]+;
NEWLINE : [\r\n]+;
