import commands.visitFun as visitFun
import commands.declarationCheck as declarationCheck
from MyVisitor import MyVisitor, CMD
import pygame
from rabbit import Rabbit
from commands.Commands import Commands

WINDOWX = 500
WINDOWY = 500

TURTLE_WIDTH = 25
TURTLE_HEIGHT = 25
NOSEANGLE = 15

if __name__ == "__main__":
    rabbit = Rabbit()
    rabbit.start()
    rabbit.home()
    CMD().set(Commands(rabbit))

    with open("tests/cmd.rabbit", "r") as f:
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

