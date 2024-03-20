SOLeAI - DSL for Speech to Text, Optical Character Recognition and Large Language Model
---
---
<b>General info</b>
* Grammar written in ANTLR.
* Lexer and Parser generated using ANTLR.
---
<b>Installation guide:</b>
1. Download ANTLR from the official website - https://www.antlr.org/download.html
2. Copy the files from the remote repository to your local machine using git clone
3. Run the program using cat .\input.txt|antlr4-parse SOLeAI.g4 prog -gui or cat 
.\input.txt|antlr4-parse SOLeAI.g4 prog -tree
---
<b>Grammar example:</b><br>
<p>Two dummy files can be found in the current directory - "input.txt", which features an example of
how our DSL's grammar, and "parse_tree_example.png", which is the parse tree for the dummy file.<br>
For a more detailed explanation of the grammar, refer to "SOLeAI.g4", where you can find the whole
grammar definition.</p>