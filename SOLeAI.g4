grammar SOLeAI;

prog: (sorb)* EOF;
sorb: NEWLINE* statement NEWLINE+ | NEWLINE* block NEWLINE*;
block: '{' (sorb|NEWLINE)* '}';
statement: varAssignment | ifBlock | pipeStream | comment;
comment: COMMENT_STRING;
varAssignment: varName '=' (value|pipeStream);
value: STRING | varName;
ifBlock: 'if' '(' (value|pipeStream) ')' (statement|block);
pipeStream: (function|inputData) ('->' function)*;
function: functionName value*;
inputData: 'messageText'|'messageImage'|'messageAudio';
functionName: ALPHANUM;
varName: ALPHANUM;

STRING: '"' ~["\r\n]* '"';
COMMENT_STRING: '//' ~[\n\r]*;
ALPHANUM: [a-zA-Z]+[a-zA-Z0-9]*;
NEWLINE : ('\r'?'\n')+;
WHITESPACE : (' ' | '\t')+ -> skip;

