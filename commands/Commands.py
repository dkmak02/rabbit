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
def sleepCommand():
    print("not implemented yet")
def printCommand(variables_dict, var):
    print(variables_dict[var[0]]["type"],'{',var[0],': ', variables_dict[var[0]]["value"],'}')