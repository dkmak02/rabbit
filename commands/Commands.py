import time

class Commands:
    def __init__(self, rabbit, screen):
        self.rabbit = rabbit
        self.screen = screen
    def goCommand(self, val):
        self.rabbit.mvForward(val, self.screen)
        print(val)
    def homeCommand(self):
        self.rabbit.home()
        print("You are home.")
    def angleCommand(self):
        print("not implemented yet")
    def jumpCommand(self):
        print("not implemented yet")
    def resetCommand(self):
        print("not implemented yet")
    def getXCommand(self):
        print("not implemented yet")
    def getYCommand(self):
        print("not implemented yet")
    def setViewCommand(self):
        print("not implemented yet")
    def sleepCommand(self, val):
        time.sleep(val)
    def printCommand(self, variables_dict, var):
        print(variables_dict[var[0]]["type"],'{',var[0],': ', variables_dict[var[0]]["value"],'}')