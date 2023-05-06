from commands import visitFun


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
def forcommand(iterator, block, variables_dict, visitor):
    comm = todo(block)
    for i in range(iterator):
        for j in comm:
            if '}' in j:
                if '{' in j:
                    pass
                else:
                    #replace { with i
                    j = j.replace('}', '')
            visitFun.visitFun(j, visitor)
