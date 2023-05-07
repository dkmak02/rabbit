import expr.compareValue as compareValue
import expr.calcValue as calcValue
import expr.logicalCompare as logicalCompare
import commands.visitFun as visitFun
import commands.splitBlock as splitBlock
def ifcommand(condition,block, variables_dict,visitor, elseblock = None):
    if 'and' in condition or 'or' in condition:
        condition = logicalCompare.compare(condition, variables_dict)
    else:
        condition = compareValue.compare(condition[0], variables_dict)
    if condition:
        comm = splitBlock.todo(block)
        for i in comm:
            visitFun.visitFun(i, visitor)

    elif elseblock != None:
        comm = splitBlock.todo(block)
        for i in comm:
            visitFun.visitFun(i, visitor)