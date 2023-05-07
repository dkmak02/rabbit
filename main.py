import sys
import pygame
from rabbit import Rabbit
from antlr4 import FileStream, CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener
from rabbitLexer import rabbitLexer
from rabbitParser import rabbitParser
from rabbitVisitor import rabbitVisitor
from rabbitListener import rabbitListener
import re
import commands.Commands as Commands
import expr.calcValue as calcValue
import expr.compareValue as compareValue
import expr.logicalCompare as logicalCompare
import expr.ifExpr as ifExpr
import commands.visitFun as visitFun
import commands.declarationCheck as declarationCheck
import expr.forExpr as forExpr
from commands.Commands import Commands

variables_dict = {}


class MyVisitor(rabbitVisitor):
    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitBoolExpr(self, ctx):
        if 'and' in ctx or 'or' in ctx:
            return logicalCompare.compare(ctx, variables_dict)
        return compareValue.compare(ctx[0], variables_dict)
    def visitIfBlock(self, ctx):
        print(ctx.getText())
        val = ctx.getText().split(" ")
        condition = val[1:val.index('?')]
        block = val[val.index('{')+1:val.index('}')]

        for v in condition:
            val.pop(val.index(v))
        for v in block:
            val.pop(val.index(v))
        val.pop(val.index('{'))
        val.pop(val.index('}'))
        if 'else' in val:
            elseblock = val[val.index('{')+1:val.index('}')]
            ifExpr.ifcommand(condition, block, variables_dict, visitor, elseblock)
        else:
            ifExpr.ifcommand(condition, block, variables_dict, visitor)
    def visitForBlock(self, ctx):
        val = ctx.getText().split(" ")
        iterator = calcValue.calcValue(val[1], variables_dict)
        block = val[val.index('{')+1:val.index('}')+1]
        forExpr.forcommand(int(iterator), block, variables_dict, visitor)
    def visitDeclarationExpr(self, ctx):
        val = ctx.getText().split(" ")
        type = val[0]
        name = val[1]
        value = val[2:]
        if type == 'int':
            value = self.visitInfiExpr(value)
        elif type == 'bool':
            value = self.visitBoolExpr(value)
        variables_dict[name] = {"type": type, "value": value}

    def visitReassignment(self, ctx):
        val = ctx.getText().split(" ")
        name = val[0]
        value = val[1:]
        try:
            type = variables_dict[name]["type"]
            if type == 'int':
                value = self.visitInfiExpr(value)
            elif type == 'bool':
                value = self.visitBoolExpr(value)
            variables_dict[name] = {"type": variables_dict[name]["type"], "value": value}
        except Exception as err:
            print("Variable named \"" + name + "\" has not been declared.")
            exit()

    def visitCommand(self, ctx):
        val = ctx.getText().split(" ")
        command = val[0]
        val = val[1:]
        match command:
            case "go":
                val = self.visitInfiExpr(val)
                cmd.goCommand(int(val))
            case "home":
                cmd.homeCommand()
            case "angle":
                cmd.angleCommand()
            case "jump":
                cmd.jumpCommand()
            case "reset":
                cmd.resetCommand()
            case "getX":
                cmd.getXCommand()
            case "getY":
                cmd.getYCommand()
            case "setView":
                cmd.setViewCommand()
            case "sleep":
                cmd.sleepCommand(int(val[0]))
            case "if":
                print("not implemented yet")
            case "for":
                print("not implemented yet")
            case "print":
                cmd.printCommand(variables_dict, val)
        return (command, val)

    def visitInfiExpr(self, split_string):
        return calcValue.calcValue(split_string, variables_dict)

    def visitReverseBoolVar(self, ctx):
        val = ctx.getText().split(" ")
        name = val[0]
        val = val[1:]
        val = val[0][1:]
        variables_dict[name]["value"] = not variables_dict[name]["value"]

WINDOWX = 500
WINDOWY = 500

#RABBIT PROPERTIES
TURTLE_WIDTH = 25
TURTLE_HEIGHT = 25
NOSEANGLE  = 15

if __name__ == "__main__":
    pygame.init()
    white = 255, 255, 255
    screen = pygame.display.set_mode((WINDOWX, WINDOWY))
    rabbit = Rabbit(WINDOWX, WINDOWY, WINDOWX, WINDOWY)
    rabbitImg = pygame.image.load('rabbit.png')
    rabbit.setImage(rabbitImg)
    screen.fill(white)
    rabbit.draw(screen)
    pygame.display.flip()
    pygame.display.set_icon(rabbitImg)
    pygame.display.set_caption("Rabbit")
    cmd = Commands(rabbit, screen)

    with open("tests/fortest.rabbit", "r") as f:
        for line in f:
            if line != "\n":
                declarationCheck.declarationCheck(line)

        f.seek(0)
        print('\n\n\n')
        s = ''

        for line in f:
            if line != "\n":
                visitor = MyVisitor()
                visitFun.visitFun(line, visitor)
