# Generated from rabbit.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .rabbitParser import rabbitParser
else:
    from rabbitParser import rabbitParser

# This class defines a complete listener for a parse tree produced by rabbitParser.
variables_dict = {}
class rabbitListener(ParseTreeListener):

    # Enter a parse tree produced by rabbitParser#prog.
    def enterProg(self, ctx:rabbitParser.ProgContext):
        pass

    # Exit a parse tree produced by rabbitParser#prog.
    def exitProg(self, ctx:rabbitParser.ProgContext):
        pass


    # Enter a parse tree produced by rabbitParser#Command.
    def enterCommand(self, ctx:rabbitParser.CommandContext):
        pass

    # Exit a parse tree produced by rabbitParser#Command.
    def exitCommand(self, ctx:rabbitParser.CommandContext):
        pass


    # Enter a parse tree produced by rabbitParser#ForBlock.
    def enterForBlock(self, ctx:rabbitParser.ForBlockContext):
        pass

    # Exit a parse tree produced by rabbitParser#ForBlock.
    def exitForBlock(self, ctx:rabbitParser.ForBlockContext):
        pass


    # Enter a parse tree produced by rabbitParser#IfBlock.
    def enterIfBlock(self, ctx:rabbitParser.IfBlockContext):
        pass

    # Exit a parse tree produced by rabbitParser#IfBlock.
    def exitIfBlock(self, ctx:rabbitParser.IfBlockContext):
        pass


    # Enter a parse tree produced by rabbitParser#Reassignment.
    def enterReassignment(self, ctx:rabbitParser.ReassignmentContext):
        pass

    # Exit a parse tree produced by rabbitParser#Reassignment.
    def exitReassignment(self, ctx:rabbitParser.ReassignmentContext):
        pass


    # Enter a parse tree produced by rabbitParser#DeclarationExpr.
    def enterDeclarationExpr(self, ctx:rabbitParser.DeclarationExprContext):
        pass

    # Exit a parse tree produced by rabbitParser#DeclarationExpr.
    def exitDeclarationExpr(self, ctx:rabbitParser.DeclarationExprContext):
        pass


    # Enter a parse tree produced by rabbitParser#ReverseBoolVar.
    def enterReverseBoolVar(self, ctx:rabbitParser.ReverseBoolVarContext):
        pass

    # Exit a parse tree produced by rabbitParser#ReverseBoolVar.
    def exitReverseBoolVar(self, ctx:rabbitParser.ReverseBoolVarContext):
        pass


    # Enter a parse tree produced by rabbitParser#reverseBool.
    def enterReverseBool(self, ctx:rabbitParser.ReverseBoolContext):
        pass

    # Exit a parse tree produced by rabbitParser#reverseBool.
    def exitReverseBool(self, ctx:rabbitParser.ReverseBoolContext):
        pass


    # Enter a parse tree produced by rabbitParser#restart.
    def enterRestart(self, ctx:rabbitParser.RestartContext):
        pass

    # Exit a parse tree produced by rabbitParser#restart.
    def exitRestart(self, ctx:rabbitParser.RestartContext):
        pass


    # Enter a parse tree produced by rabbitParser#print.
    def enterPrint(self, ctx:rabbitParser.PrintContext):
        pass

    # Exit a parse tree produced by rabbitParser#print.
    def exitPrint(self, ctx:rabbitParser.PrintContext):
        pass


    # Enter a parse tree produced by rabbitParser#declaration.
    def enterDeclaration(self, ctx:rabbitParser.DeclarationContext):
        pass

    # Exit a parse tree produced by rabbitParser#declaration.
    def exitDeclaration(self, ctx:rabbitParser.DeclarationContext):
        val = ctx.getText().split(" ")
        type = val[0]
        name = val[1]
        value = val[2:]
        if name in variables_dict.keys():
            raise ValueError(
                "Variable named \"" + name + "\" has already been declared as " + variables_dict[name]['type'] + ".")
        else:
            if type == 'int':
                variables_dict[name] = {"type": type, "value": 0}
            elif type == 'bool':
                variables_dict[name] = {"type": type, "value": False}


    # Enter a parse tree produced by rabbitParser#if.
    def enterIf(self, ctx:rabbitParser.IfContext):
        pass

    # Exit a parse tree produced by rabbitParser#if.
    def exitIf(self, ctx:rabbitParser.IfContext):
        pass


    # Enter a parse tree produced by rabbitParser#block.
    def enterBlock(self, ctx:rabbitParser.BlockContext):
        pass

    # Exit a parse tree produced by rabbitParser#block.
    def exitBlock(self, ctx:rabbitParser.BlockContext):
        pass


    # Enter a parse tree produced by rabbitParser#for.
    def enterFor(self, ctx:rabbitParser.ForContext):
        pass

    # Exit a parse tree produced by rabbitParser#for.
    def exitFor(self, ctx:rabbitParser.ForContext):
        pass


    # Enter a parse tree produced by rabbitParser#comparison.
    def enterComparison(self, ctx:rabbitParser.ComparisonContext):
        pass

    # Exit a parse tree produced by rabbitParser#comparison.
    def exitComparison(self, ctx:rabbitParser.ComparisonContext):
        pass


    # Enter a parse tree produced by rabbitParser#getX.
    def enterGetX(self, ctx:rabbitParser.GetXContext):
        pass

    # Exit a parse tree produced by rabbitParser#getX.
    def exitGetX(self, ctx:rabbitParser.GetXContext):
        pass


    # Enter a parse tree produced by rabbitParser#getY.
    def enterGetY(self, ctx:rabbitParser.GetYContext):
        pass

    # Exit a parse tree produced by rabbitParser#getY.
    def exitGetY(self, ctx:rabbitParser.GetYContext):
        pass


    # Enter a parse tree produced by rabbitParser#setValue.
    def enterSetValue(self, ctx:rabbitParser.SetValueContext):
        pass

    # Exit a parse tree produced by rabbitParser#setValue.
    def exitSetValue(self, ctx:rabbitParser.SetValueContext):
        pass


    # Enter a parse tree produced by rabbitParser#angle.
    def enterAngle(self, ctx:rabbitParser.AngleContext):
        pass

    # Exit a parse tree produced by rabbitParser#angle.
    def exitAngle(self, ctx:rabbitParser.AngleContext):
        pass


    # Enter a parse tree produced by rabbitParser#setView.
    def enterSetView(self, ctx:rabbitParser.SetViewContext):
        pass

    # Exit a parse tree produced by rabbitParser#setView.
    def exitSetView(self, ctx:rabbitParser.SetViewContext):
        pass


    # Enter a parse tree produced by rabbitParser#spaceLeft.
    def enterSpaceLeft(self, ctx:rabbitParser.SpaceLeftContext):
        pass

    # Exit a parse tree produced by rabbitParser#spaceLeft.
    def exitSpaceLeft(self, ctx:rabbitParser.SpaceLeftContext):
        pass


    # Enter a parse tree produced by rabbitParser#checkField.
    def enterCheckField(self, ctx:rabbitParser.CheckFieldContext):
        pass

    # Exit a parse tree produced by rabbitParser#checkField.
    def exitCheckField(self, ctx:rabbitParser.CheckFieldContext):
        pass


    # Enter a parse tree produced by rabbitParser#putItem.
    def enterPutItem(self, ctx:rabbitParser.PutItemContext):
        pass

    # Exit a parse tree produced by rabbitParser#putItem.
    def exitPutItem(self, ctx:rabbitParser.PutItemContext):
        pass


    # Enter a parse tree produced by rabbitParser#getItem.
    def enterGetItem(self, ctx:rabbitParser.GetItemContext):
        pass

    # Exit a parse tree produced by rabbitParser#getItem.
    def exitGetItem(self, ctx:rabbitParser.GetItemContext):
        pass


    # Enter a parse tree produced by rabbitParser#getAngle.
    def enterGetAngle(self, ctx:rabbitParser.GetAngleContext):
        pass

    # Exit a parse tree produced by rabbitParser#getAngle.
    def exitGetAngle(self, ctx:rabbitParser.GetAngleContext):
        pass


    # Enter a parse tree produced by rabbitParser#jump.
    def enterJump(self, ctx:rabbitParser.JumpContext):
        pass

    # Exit a parse tree produced by rabbitParser#jump.
    def exitJump(self, ctx:rabbitParser.JumpContext):
        pass


    # Enter a parse tree produced by rabbitParser#sleep.
    def enterSleep(self, ctx:rabbitParser.SleepContext):
        pass

    # Exit a parse tree produced by rabbitParser#sleep.
    def exitSleep(self, ctx:rabbitParser.SleepContext):
        pass


    # Enter a parse tree produced by rabbitParser#go.
    def enterGo(self, ctx:rabbitParser.GoContext):
        pass

    # Exit a parse tree produced by rabbitParser#go.
    def exitGo(self, ctx:rabbitParser.GoContext):
        pass


    # Enter a parse tree produced by rabbitParser#home.
    def enterHome(self, ctx:rabbitParser.HomeContext):
        pass

    # Exit a parse tree produced by rabbitParser#home.
    def exitHome(self, ctx:rabbitParser.HomeContext):
        pass


    # Enter a parse tree produced by rabbitParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:rabbitParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by rabbitParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:rabbitParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by rabbitParser#name.
    def enterName(self, ctx:rabbitParser.NameContext):
        pass

    # Exit a parse tree produced by rabbitParser#name.
    def exitName(self, ctx:rabbitParser.NameContext):
        pass


    # Enter a parse tree produced by rabbitParser#value.
    def enterValue(self, ctx:rabbitParser.ValueContext):
        pass

    # Exit a parse tree produced by rabbitParser#value.
    def exitValue(self, ctx:rabbitParser.ValueContext):
        pass


    # Enter a parse tree produced by rabbitParser#InfiExpr.
    def enterInfiExpr(self, ctx:rabbitParser.InfiExprContext):
        pass

    # Exit a parse tree produced by rabbitParser#InfiExpr.
    def exitInfiExpr(self, ctx:rabbitParser.InfiExprContext):
        pass


    # Enter a parse tree produced by rabbitParser#NumberExpr.
    def enterNumberExpr(self, ctx:rabbitParser.NumberExprContext):
        pass

    # Exit a parse tree produced by rabbitParser#NumberExpr.
    def exitNumberExpr(self, ctx:rabbitParser.NumberExprContext):
        pass



del rabbitParser