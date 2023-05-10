import time

class Commands:
    def __init__(self, rabbit):
        self.rabbit = rabbit
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
        print("not implemented yet")
    def getYCommand(self):
        print("not implemented yet")
    def setViewCommand(self, val):
        self.rabbit.rotate(val)
    def sleepCommand(self, val):
        time.sleep(val)
    def printCommand(self, variables_dict, var):
        print(variables_dict[var[0]]["type"],'{',var[0],': ', variables_dict[var[0]]["value"],'}')