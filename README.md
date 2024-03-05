Quick setup guide:
1. pip install antlr4-python3-runtime
2. If the commands don't work, then install ANTLR v4 as a plugin 
(File->Settings->Plugins). The .g4 file should change its icon
3. Alternatively to step 2, you could try downloading the .jar file - https://www.antlr.org/download.html; I didn't
install it this way so I don't know if it would behave the same.

Antlr commands:
1. antlr4-parse PBLv2.g4 prog -tree <-- Parsing, requires input in the form of the defined grammar
2. antlr4 -Dlanguage=Python3 PBLv2.g4  <-- Generates the tokens and builds the Lexer, Parser, etc. from the Grammar

Possible reasons as to why our Grammar doesn't behave the way it should:
1. Position matters when defining the grammar - https://stackoverflow.com/questions/27541957/antlr4-lexer-rules-dont-work-as-expected