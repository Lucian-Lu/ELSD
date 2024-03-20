# Generated from SOLeAI.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SOLeAIParser import SOLeAIParser
else:
    from SOLeAIParser import SOLeAIParser

# This class defines a complete listener for a parse tree produced by SOLeAIParser.
class SOLeAIListener(ParseTreeListener):

    # Enter a parse tree produced by SOLeAIParser#prog.
    def enterProg(self, ctx:SOLeAIParser.ProgContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#prog.
    def exitProg(self, ctx:SOLeAIParser.ProgContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#sorb.
    def enterSorb(self, ctx:SOLeAIParser.SorbContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#sorb.
    def exitSorb(self, ctx:SOLeAIParser.SorbContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#block.
    def enterBlock(self, ctx:SOLeAIParser.BlockContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#block.
    def exitBlock(self, ctx:SOLeAIParser.BlockContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#statement.
    def enterStatement(self, ctx:SOLeAIParser.StatementContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#statement.
    def exitStatement(self, ctx:SOLeAIParser.StatementContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#comment.
    def enterComment(self, ctx:SOLeAIParser.CommentContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#comment.
    def exitComment(self, ctx:SOLeAIParser.CommentContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#varAssignment.
    def enterVarAssignment(self, ctx:SOLeAIParser.VarAssignmentContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#varAssignment.
    def exitVarAssignment(self, ctx:SOLeAIParser.VarAssignmentContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#value.
    def enterValue(self, ctx:SOLeAIParser.ValueContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#value.
    def exitValue(self, ctx:SOLeAIParser.ValueContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#ifBlock.
    def enterIfBlock(self, ctx:SOLeAIParser.IfBlockContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#ifBlock.
    def exitIfBlock(self, ctx:SOLeAIParser.IfBlockContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#pipeStream.
    def enterPipeStream(self, ctx:SOLeAIParser.PipeStreamContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#pipeStream.
    def exitPipeStream(self, ctx:SOLeAIParser.PipeStreamContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#function.
    def enterFunction(self, ctx:SOLeAIParser.FunctionContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#function.
    def exitFunction(self, ctx:SOLeAIParser.FunctionContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#inputData.
    def enterInputData(self, ctx:SOLeAIParser.InputDataContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#inputData.
    def exitInputData(self, ctx:SOLeAIParser.InputDataContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#functionName.
    def enterFunctionName(self, ctx:SOLeAIParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#functionName.
    def exitFunctionName(self, ctx:SOLeAIParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by SOLeAIParser#varName.
    def enterVarName(self, ctx:SOLeAIParser.VarNameContext):
        pass

    # Exit a parse tree produced by SOLeAIParser#varName.
    def exitVarName(self, ctx:SOLeAIParser.VarNameContext):
        pass



del SOLeAIParser