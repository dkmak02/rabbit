import time
class Commands:
    def __init__(self, rabbit):
        self.rabbit = rabbit
        self.spaceLeft = 5
        self.maxSpace = 5
        self.items = {(262, 261): 2, (362, 162): 2, (23, 421): 2, (123, 312): 1, (231, 312): 1, (245, 312): 1}
    def goCommand(self, val):
        self.rabbit.mvForward(val)
    def homeCommand(self):
        self.rabbit.home()
    def angleCommand(self, val):
        self.rabbit.rotate(val)
    def jumpCommand(self, x, y):
        self.rabbit.jump(x, y)
    def resetCommand(self):
        self.rabbit.home()
    def getXCommand(self):
        return self.rabbit.getX()
    def getYCommand(self):
        return self.rabbit.getY()
    def setViewCommand(self, val):
        self.rabbit.rotate(val)
    def sleepCommand(self, val):
        time.sleep(val)
    def printCommand(self, variables_dict, var):
        print(variables_dict[var[0]]["type"],'{',var[0],': ', variables_dict[var[0]]["value"],'}')
    def checkFieldCommand(self):
        x, y = int(self.rabbit.getX()), int(self.rabbit.getY())
        print(x, y)
        item = self.items.get((x, y))
        return item
    def spaceLeftCommand(self):
        if self.spaceLeft == 0:
            print("There is no space left")
        return self.rabbit.spaceLeft()
    def putItemCommand(self):
        self.spaceLeft = self.maxSpace
    def getItemCommand(self, item):
        if item == 1:
            if self.spaceLeft > 0:
                self.spaceLeft -= 1
            else:
                print("There is no space left")
        elif item == 2:
            print(self.spaceLeft)
            self.maxSpace += 5
            self.spaceLeft += 5
        else:
            print("There is no item to get")
        print(self.spaceLeft)