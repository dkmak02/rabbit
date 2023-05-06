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
        type = variables_dict[name]["type"]
        if type == 'int':
            value = self.visitInfiExpr(value)
        elif type == 'bool':
            value = self.visitBoolExpr(value)
        variables_dict[name] = {"type": variables_dict[name]["type"], "value": value}

    def visitCommand(self, ctx):
        val = ctx.getText().split(" ")
        command = val[0]
        val = val[1:]
        match command:
            case "go":
                val = self.visitInfiExpr(val)
                Commands.goCommand(int(val))
            case "home":
                Commands.homeCommand()
            case "angle":
                Commands.angleCommand()
            case "jump":
                Commands.jumpCommand()
            case "reset":
                Commands.resetCommand()
            case "getX":
                Commands.getXCommand()
            case "getY":
                Commands.getYCommand()
            case "setView":
                Commands.setViewCommand()
            case "sleep":
                Commands.sleepCommand(int(val[0]))
            case "if":
                print("not implemented yet")
            case "for":
                print("not implemented yet")
            case "print":
                Commands.printCommand(variables_dict, val)
        return (command, val)

    def visitInfiExpr(self, split_string):
        return calcValue.calcValue(split_string, variables_dict)


if __name__ == "__main__":
    with open("tests/fortest.rabbit", "r") as f:
        for line in f:
            if line != "\n":
                declarationCheck.declarationCheck(line)
                # line = line.strip()
                # data = InputStream(line)
                # # lexer
                # lexer = rabbitLexer(data)
                # stream = CommonTokenStream(lexer)
                # # parser
                # parser = rabbitParser(stream)
                # listener = rabbitListener()
                # parser.addParseListener(listener)
                # try:
                #     _ = parser.prog()
                # except Exception as err:
                #     print(err)
                #     exit()


        f.seek(0)
        print('\n\n\n')
        s = ''
        for line in f:
            if line != "\n":
                visitor = MyVisitor()
                visitFun.visitFun(line, visitor)
                # line = line.strip()
                # data = InputStream(line)
                # # lexer
                # lexer = rabbitLexer(data)
                # stream = CommonTokenStream(lexer)
                # # parser
                # parser = rabbitParser(stream)
                # tree = parser.prog()
                # # evaluator
                #
                # output = visitor.visit(tree)

