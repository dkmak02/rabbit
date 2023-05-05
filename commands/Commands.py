import time

def goCommand(val):
    print("not implemented yet")
    print(val)
def homeCommand():
    print("You are home.")
def angleCommand():
    print("not implemented yet")
def jumpCommand():
    print("not implemented yet")
def resetCommand():
    print("not implemented yet")
def getXCommand():
    print("not implemented yet")
def getYCommand():
    print("not implemented yet")
def setViewCommand():
    print("not implemented yet")
def sleepCommand(val):
    time.sleep(val)

def printCommand(variables_dict, var):
    print(variables_dict[var[0]]["type"],'{',var[0],': ', variables_dict[var[0]]["value"],'}')