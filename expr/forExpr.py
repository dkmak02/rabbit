from commands import visitFun
import commands.splitBlock as splitBlock

def forcommand(iterator, block, variables_dict, visitor):
    comm = splitBlock.todo(block)
    for i in range(iterator):
        for j in comm:
            if '}' in j:
                if '{' in j:
                    pass
                else:
                    #replace { with i
                    j = j.replace('}', '')
            visitFun.visitFun(j, visitor)
