import sys

import pygame

from rabbit import Rabbit
from antlr4 import FileStream, CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener
from rabbitLexer import rabbitLexer
from rabbitParser import rabbitParser
from rabbitVisitor import rabbitVisitor
import re
import commands.Commands as Commands
import expr.calcValue as calcValue
import expr.compareValue as compareValue
import expr.logicalCompare as logicalCompare
variables_dict = {}

class MyVisitor(rabbitVisitor):
    def visitNumberExpr(self, ctx):
        print(ctx.getText())
        value = ctx.getText()
        return int(value)

    def visitParenExpr(self, ctx):
        print(ctx.getText())
        return self.visit(ctx.expr())
    def visitBoolExpr(self, ctx):
        if 'and' in ctx or 'or' in ctx:
            return logicalCompare.compare(ctx, variables_dict)
        return compareValue.compare(ctx[0], variables_dict)
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
                Commands.sleepCommand()
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
    while 1:
        data = InputStream(input(">>> "))
        # lexer
        lexer = rabbitLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = rabbitParser(stream)
        tree = parser.prog()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)