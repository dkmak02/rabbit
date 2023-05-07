import pygame
from rabbit import Rabbit
from antlr4 import FileStream, CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener
from rabbitLexer import rabbitLexer
from rabbitParser import rabbitParser
from rabbitVisitor import rabbitVisitor
from rabbitListener import rabbitListener
import commands.Commands as Commands
import expr.calcValue as calcValue
import expr.compareValue as compareValue
import expr.logicalCompare as logicalCompare
import expr.ifExpr as ifExpr
import commands.visitFun as visitFun
import commands.declarationCheck as declarationCheck
import expr.forExpr as forExpr
from MyVisitor import MyVisitor
from commands.Commands import Commands

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
    rabbit = Rabbit(WINDOWX, WINDOWY)
    rabbitImg = pygame.image.load('rabbit.png')
    rabbit.setImage(rabbitImg)
    screen.fill(white)
    rabbit.draw(screen)
    pygame.display.flip()
    pygame.display.set_icon(rabbitImg)
    pygame.display.set_caption("Rabbit")
    cmd = Commands(rabbit, screen)

    with open("tests/test.rabbit", "r") as f:
        for line in f:
            if line != "\n":
                declarationCheck.declarationCheck(line)

        f.seek(0)
        print('\n\n\n')
        s = ''

        for line in f:
            if line != "\n":
                visitor = MyVisitor(cmd)
                visitFun.visitFun(line, visitor)

