grammar ocs;
prog:	(cmd* NEWLINE)* ;

//zmienic expr, dodac home, jump, getx, gety, claer, reset, naprawic gramtyke, i wczytywanie z pliki, multi komenty w jendej liniiS, angle nie dyskretne
TRUE: 'TRUE'
    | 'true'
    | 'True';
FALSE: 'FALSE'
    | 'false'
    | 'False';
cmd: go
   | jump
   | home
   | clear
   | reset
   | angle
   | setViev
   | for
   | if
   | getX
   | getY
   | declaration
   | getAngle
   | getItem
   | putItem
   | checkField
   | spaceLeft
   | setValue
   ;

setValue: name '=' expr
    | name '=' name;


setViev: 'SETVIEW' KATY;

spaceLeft: 'spaceLeft';

checkField:'checkField';

container: 'CONTAINER';

putItem: 'putItem';

getItem: 'getItem';

getAngle: 'getAngle';

for: 'FOR' number  block'ENDFOR';
block: '{'cmd*'}' ;
if: 'IF' comparison '?' block 'ENDIF'|
    'IF' comparison '?' block 'ELSE' block 'ENDIF';

comparison
   : expr comparisonOperator expr
   | comparison comparisonOperator comparison
   ;
comparisonOperator: '<'
   | '>'
   | '=='
   | '!='
   | '&'
   | '|'
   ;
name
   : STRING
   ;
value
   : INT
   | TRUE
   | FALSE
   | name;

expr:	value ('*'|'/') (value|expr)
    |	value ('+'|'-') (value|expr)
    |   value comparisonOperator value
    ;
declaration: 'INT' name expr |
       'BOOL' name (TRUE|FALSE)
       | 'BOOL' name expr
       | fun;
getX: 'getX';
getY: 'getY';
go: 'GO' expr|
    'GO' name;

jump: 'JUMP' number number;
home: 'HOME';
clear: 'CLEAR' ;
reset: 'RESET';
angle: 'ANGLE' ('90'|'180'|'270'|'360');
fun: 'FUN' name block return name '->'('INT'|'BOOL')
    |'FUN' name block '->' 'VOID';
return: 'RETURN';
number
   : INT
   ;
KATY: 'PRAWO'|'LEWO'|'GORA'|'DOL';
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
STRING : [a-zA-Z][a-zA-Z0-9_]*;
EOL    : '\r'? '\n'    ;
WS    : [ \t\r\n] -> skip;
