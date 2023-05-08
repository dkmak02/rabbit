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
    pygame.init()
    white = 255, 255, 255
    screen = pygame.display.set_mode((WINDOWX, WINDOWY))
    rabbit = Rabbit(WINDOWX, WINDOWY, WINDOWX, WINDOWY)
    rabbitImg = pygame.image.load('rabbit.png')
    rabbit.setImage(rabbitImg)
    screen.fill(white)
    rabbit.draw(screen)
    pygame.display.flip()
    pygame.display.set_icon(rabbitImg)
    pygame.display.set_caption("Rabbit")
    CMD().set(Commands(rabbit, screen))

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

