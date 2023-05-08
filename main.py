import commands.visitFun as visitFun
import commands.declarationCheck as declarationCheck
from MyVisitor import MyVisitor


if __name__ == "__main__":
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

