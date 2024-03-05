grammar PBLv2;

prog: NEWLINE* (statement|block)* NEWLINE* EOF;
block: '{' (WHITESPACE|NEWLINE)* statement* (WHITESPACE|NEWLINE)* '}' NEWLINE+;
statement: inStatement NEWLINE*; // Changed NEWLINE+ to NEWLINE*
inStatement: varAssignment | ifBlock | pipeStream | comment;
comment: WHITESPACE* '//' UNQUOTED_STRING*;
varAssignment: varName WHITESPACE* '=' WHITESPACE* (value|pipeStream);
value: STRING | varName;
ifBlock: 'if' WHITESPACE* '(' (value|pipeStream) ')' WHITESPACE* (statement|block);
pipeStream: (function|inputData) (WHITESPACE*'->'WHITESPACE* function)*;
function: functionName value*;
inputData: 'messageText'|'messageImage'|'messageAudio';
functionName: ALPHANUM;
varName: ALPHANUM;

STRING: '"' ~["\r\n]* '"';
UNQUOTED_STRING: ~[\r\n]+;
ALPHANUM: [a-zA-Z]+[a-zA-Z0-9]*;
NEWLINE : [\r\n]+;
WHITESPACE : (' ' | '\t');

// Added a '*' to UNQUOTED_STRING in comment
// Non-terminals:
// Terminals:

// add comment capability
// add variables and pipes
// comparison, ifs, blocks
// message type checking

// ] Send gas for june
// [ image
// june = image -> ocr -> llm "find the gas volume indication, respond only with a number" -> findNumber
// ] Send for july
// [ image
// july = --//--
// llm "find the difference between these values" june july

// text = image -> ocrRecognize
// if (text -> llmYesNo "Is there a person's name in the text?") {
//   text -> llmPrompt "Get the customer name from the following text:" -> respond
// } else {}
//
// ocrDetect NEWLINE
//         | ocrRecognize NEWLINE
//         | ocrReadText NEWLINE
//         | ocrReadTextLang NEWLINE
//         | llmTrain NEWLINE
//         | llmLoad NEWLINE
//         | llmGenerateText NEWLINE
//         | llmRetrieveParams NEWLINE
//         | sttRecognize NEWLINE
//         | sttProcess NEWLINE
//         | sttTranscribe NEWLINE
//         | sttConvert NEWLINE;
//
//ocrDetect: 'detect' WHITESPACE 'imagePath=' STRING;
//
//ocrRecognize: 'recognize' WHITESPACE 'imagePath=' STRING;
//
//ocrReadText: 'read_text' WHITESPACE 'imagePath=' STRING;
//
//ocrReadTextLang: 'read_text_lang' WHITESPACE 'imagePath=' STRING;
//
//llmTrain: 'train' WHITESPACE 'trainingData=' STRING;
//
//llmLoad: 'load' WHITESPACE 'modelPath=' STRING;
//
//llmGenerateText: 'generate_text' WHITESPACE 'prompt=' STRING;
//
//llmRetrieveParams: 'retrieve_params' WHITESPACE 'modelName=' STRING;
//
//sttRecognize: 'recognize' WHITESPACE 'audioPath=' STRING;
//
//sttProcess: 'process' WHITESPACE 'audioPath=' STRING;
//
//sttTranscribe: 'transcribe' WHITESPACE 'audioPath=' STRING;
//
//sttConvert: 'convert' WHITESPACE 'audioPath=' STRING;
//
