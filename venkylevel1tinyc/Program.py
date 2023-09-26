from Function import *
class Program:
    def __init__(self):
        self.functions={}
    def getmainfunction(self):
        return self.functions['main']
    def addfunction(self,name,function):
        self.functions[name]=function
    def print(self):
        print('Program:')
        for i in self.functions:
            self.printfunctionheader(i)
            for j in self.functions[i].getstatementsastlist():
                j.print()
    def printfunctionheader(self,name):
        print(f"\t Procedure: {name} Return Type:{self.functions[name].returntype}")
        