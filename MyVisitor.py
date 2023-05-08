from commands import splitBlock, visitFun
from expr import logicalCompare, compareValue, ifExpr, calcValue, forExpr
from rabbitVisitor import rabbitVisitor
import commands.Commands as Commands
variables_dict = {}
functions_dict = {}
def fun_c(comm,wating,to_remove,visitor):
    for i in comm:
        visitFun.visitFun(i, visitor)
    for w in wating:
        variables_dict[w] = wating[w]
    for t in to_remove:
        variables_dict.pop(t)
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
        val = ctx.getText().split(" ")
        condition = val[1:val.index('?')]
        start = 1
        end = 0
        to = 0
        for i in range(val.index('{')+1, len(val)):
            if val[i] == '{':
                start += 1
            if val[i] == '}':
                end += 1
            if start == end:
                to = i
                break
        block = val[val.index('{')+1:to]
        for v in condition:
            val.pop(val.index(v))
        for v in block:
            val.pop(val.index(v))
        val.pop(val.index('{'))
        val.pop(val.index('}'))
        if 'else' in val:
            start = 1
            end = 0
            to = 0
            for i in range(val.index('{') + 1, len(val)):
                if val[i] == '{':
                    start += 1
                if val[i] == '}':
                    end += 1
                if start == end:
                    to = i
                    break
            elseblock = val[val.index('{')+1:to]
            ifExpr.ifcommand(condition, block, variables_dict, visitor, elseblock)
        else:
            ifExpr.ifcommand(condition, block, variables_dict, visitor)
    def visitForBlock(self, ctx):
        val = ctx.getText().split(" ")
        iterator = calcValue.calcValue(val[1], variables_dict)
        start = 1
        end = 0
        to = 0
        for i in range(val.index('{') + 1, len(val)):
            if val[i] == '{':
                start += 1
            if val[i] == '}':
                end += 1
            if start == end:
                to = i
                break
        block = val[val.index('{') + 1:to]
        forExpr.forcommand(int(iterator), block, variables_dict, visitor)
    def visitDeclarationExpr(self, ctx):
        val = ctx.getText().split(" ")
        type = val[0]
        name = val[1]
        value = val[2:]
        if type == 'int':
            if '(' in value[0]:
                value = self.visitCall(value)
            value = self.visitInfiExpr(value)
        elif type == 'bool':
            if '(' in value[0]:
                value = self.visitCall(value)
            value = self.visitBoolExpr(value)
        variables_dict[name] = {"type": type, "value": value}
    def visitFunction(self, ctx):
        val = ctx.getText().split(" ")
        type = val[0] + '-' + 'fun'
        name_args = val[1:val.index('{')]
        name = ' '.join(name_args).split('(')[0]
        args = ' '.join(name_args).split('(')[1].split(')')[0].split(',')
        value = val[val.index('{'):]
        if type == 'void-fun' and 'return' in value:
            raise ValueError(
                "Void type function cannot return a value")
        functions_dict[name] = {"type": type,"args": args, "value": value}

    def visitCall(self, ctx):
        val = ctx
        if isinstance(ctx, list):
            pass
        else:
            val = ctx.getText().split(" ")
        name = ' '.join(val).split('(')[0]
        args = ' '.join(val).split('(')[1].split(')')[0].split(',')
        args_len = len(args)
        fun_args = functions_dict[name]["args"]
        if name not in functions_dict:
            raise ValueError(
                "Function " + name + " is not defined")
        if args_len != len(functions_dict[name]["args"]):
            raise ValueError(
                "Function " + name + " takes " + str(functions_dict[name]["args"]) + " arguments, " + str(args_len) + " given")
        type = functions_dict[name]["type"].split('-')[0]
        value = functions_dict[name]["value"]
        to_return = None
        if 'return' in value:
            to_return = value[value.index('return')+1:]
        comm = value[value.index('{') + 1:value.index('}')]
        comm = splitBlock.todo(comm)
        wating = {}
        to_remove = []
        for a,b in zip(fun_args, args):
            a = a.replace(' ', '')
            b = b.replace(' ', '')
            if a in variables_dict:
                if b in variables_dict:
                    wating[a] = variables_dict[a]
                    variables_dict[a] = variables_dict[b]
                else:
                    wating[a] = variables_dict[a].copy()
                    variables_dict[a]['value'] = b
            else:
                to_remove.append(a)
                if b in variables_dict:
                    variables_dict[a] = variables_dict[b]
                else:
                    variables_dict[a] = {'type': 'int', 'value': b}

        if type == 'int':
            to_return = self.visitInfiExpr(to_return)
            fun_c(comm, wating, to_remove, visitor)
            return to_return
        elif type == 'bool':
            to_return = self.visitInfiExpr(to_return)
            fun_c(comm, wating, to_remove, visitor)
            return to_return
        else:
            fun_c(comm, wating, to_remove, visitor)





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
        bools = ['True', 'False', 'true', 'false']
        if split_string[0] in bools:
            raise ValueError(
                "Cannot perform mathematical operations on boolean values")
        return calcValue.calcValue(split_string, variables_dict)
    def visitReverseBoolVar(self, ctx):
        val = ctx.getText().split(" ")
        name = val[0]
        val = val[1:]
        val = val[0][1:]
        variables_dict[name]["value"] = not variables_dict[val]["value"]


visitor = MyVisitor()
