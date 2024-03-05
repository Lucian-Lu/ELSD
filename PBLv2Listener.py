# Generated from PBLv2.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PBLv2Parser import PBLv2Parser
else:
    from PBLv2Parser import PBLv2Parser

# This class defines a complete listener for a parse tree produced by PBLv2Parser.
class PBLv2Listener(ParseTreeListener):

    # Enter a parse tree produced by PBLv2Parser#prog.
    def enterProg(self, ctx:PBLv2Parser.ProgContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#prog.
    def exitProg(self, ctx:PBLv2Parser.ProgContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#block.
    def enterBlock(self, ctx:PBLv2Parser.BlockContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#block.
    def exitBlock(self, ctx:PBLv2Parser.BlockContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#statement.
    def enterStatement(self, ctx:PBLv2Parser.StatementContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#statement.
    def exitStatement(self, ctx:PBLv2Parser.StatementContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#inStatement.
    def enterInStatement(self, ctx:PBLv2Parser.InStatementContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#inStatement.
    def exitInStatement(self, ctx:PBLv2Parser.InStatementContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#comment.
    def enterComment(self, ctx:PBLv2Parser.CommentContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#comment.
    def exitComment(self, ctx:PBLv2Parser.CommentContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#varAssignment.
    def enterVarAssignment(self, ctx:PBLv2Parser.VarAssignmentContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#varAssignment.
    def exitVarAssignment(self, ctx:PBLv2Parser.VarAssignmentContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#value.
    def enterValue(self, ctx:PBLv2Parser.ValueContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#value.
    def exitValue(self, ctx:PBLv2Parser.ValueContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#ifBlock.
    def enterIfBlock(self, ctx:PBLv2Parser.IfBlockContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#ifBlock.
    def exitIfBlock(self, ctx:PBLv2Parser.IfBlockContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#pipeStream.
    def enterPipeStream(self, ctx:PBLv2Parser.PipeStreamContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#pipeStream.
    def exitPipeStream(self, ctx:PBLv2Parser.PipeStreamContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#function.
    def enterFunction(self, ctx:PBLv2Parser.FunctionContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#function.
    def exitFunction(self, ctx:PBLv2Parser.FunctionContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#inputData.
    def enterInputData(self, ctx:PBLv2Parser.InputDataContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#inputData.
    def exitInputData(self, ctx:PBLv2Parser.InputDataContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#functionName.
    def enterFunctionName(self, ctx:PBLv2Parser.FunctionNameContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#functionName.
    def exitFunctionName(self, ctx:PBLv2Parser.FunctionNameContext):
        pass


    # Enter a parse tree produced by PBLv2Parser#varName.
    def enterVarName(self, ctx:PBLv2Parser.VarNameContext):
        pass

    # Exit a parse tree produced by PBLv2Parser#varName.
    def exitVarName(self, ctx:PBLv2Parser.VarNameContext):
        pass



del PBLv2Parser