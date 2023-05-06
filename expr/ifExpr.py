import expr.compareValue as compareValue
import expr.calcValue as calcValue
import expr.logicalCompare as logicalCompare
import commands.visitFun as visitFun
def todo(block):
    block.append("")
    todo = []
    s = ""
    for i in block:
        if i == "":
            todo.append(s[:-1])
            s = ""
        else:
            s += i + " "

    todo = list(filter(None, todo))
    for i in todo:
        c = 0
        if '{' in i:
            c = 1
            index = todo.index(i)
            for j in range(len(todo)-1, index, -1):
                if '}' in todo[j]:
                    todo[index] = '  '.join(todo[index:j+1])
                    s = todo[index]
                    s.join(' }')
                    for k in range(j, index, -1):
                        todo.pop(k)
                    break


    return todo
def ifcommand(condition,block, variables_dict,visitor, elseblock = None):
    if 'and' in condition or 'or' in condition:
        condition = logicalCompare.compare(condition, variables_dict)
    else:
        condition = compareValue.compare(condition[0], variables_dict)
    if condition:
        comm = todo(block)
        for i in comm:
            visitFun.visitFun(i, visitor)

    elif elseblock != None:
        comm = todo(elseblock)
        for i in comm:
            visitFun.visitFun(i, visitor)