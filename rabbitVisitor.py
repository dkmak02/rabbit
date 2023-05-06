# Generated from rabbit.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .rabbitParser import rabbitParser
else:
    from rabbitParser import rabbitParser

# This class defines a complete generic visitor for a parse tree produced by rabbitParser.

class rabbitVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by rabbitParser#prog.
    def visitProg(self, ctx:rabbitParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#Command.
    def visitCommand(self, ctx:rabbitParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#ForBlock.
    def visitForBlock(self, ctx:rabbitParser.ForBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#IfBlock.
    def visitIfBlock(self, ctx:rabbitParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#Reassignment.
    def visitReassignment(self, ctx:rabbitParser.ReassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#DeclarationExpr.
    def visitDeclarationExpr(self, ctx:rabbitParser.DeclarationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#ReverseBoolVar.
    def visitReverseBoolVar(self, ctx:rabbitParser.ReverseBoolVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#reverseBool.
    def visitReverseBool(self, ctx:rabbitParser.ReverseBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#restart.
    def visitRestart(self, ctx:rabbitParser.RestartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#print.
    def visitPrint(self, ctx:rabbitParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#declaration.
    def visitDeclaration(self, ctx:rabbitParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#if.
    def visitIf(self, ctx:rabbitParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#block.
    def visitBlock(self, ctx:rabbitParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#for.
    def visitFor(self, ctx:rabbitParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#comparison.
    def visitComparison(self, ctx:rabbitParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#getX.
    def visitGetX(self, ctx:rabbitParser.GetXContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#getY.
    def visitGetY(self, ctx:rabbitParser.GetYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#setValue.
    def visitSetValue(self, ctx:rabbitParser.SetValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#angle.
    def visitAngle(self, ctx:rabbitParser.AngleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#setView.
    def visitSetView(self, ctx:rabbitParser.SetViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#spaceLeft.
    def visitSpaceLeft(self, ctx:rabbitParser.SpaceLeftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#checkField.
    def visitCheckField(self, ctx:rabbitParser.CheckFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#putItem.
    def visitPutItem(self, ctx:rabbitParser.PutItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#getItem.
    def visitGetItem(self, ctx:rabbitParser.GetItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#getAngle.
    def visitGetAngle(self, ctx:rabbitParser.GetAngleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#jump.
    def visitJump(self, ctx:rabbitParser.JumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#sleep.
    def visitSleep(self, ctx:rabbitParser.SleepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#go.
    def visitGo(self, ctx:rabbitParser.GoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#home.
    def visitHome(self, ctx:rabbitParser.HomeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:rabbitParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#name.
    def visitName(self, ctx:rabbitParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#value.
    def visitValue(self, ctx:rabbitParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#InfiExpr.
    def visitInfiExpr(self, ctx:rabbitParser.InfiExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rabbitParser#NumberExpr.
    def visitNumberExpr(self, ctx:rabbitParser.NumberExprContext):
        return self.visitChildren(ctx)



del rabbitParser