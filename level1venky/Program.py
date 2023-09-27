from Function import *
class Program:
        def __init__(self):
                self.functions={}
        def getmainfunction(self):
                return self.functions['main']
        def addfunction(self,name,function):
                self.functions[name]=function
        def print(self,f):
                if f is None:
                        print('Program:')
                        for i in self.functions:
                                self.printfunctionheader(i)
                                for j in self.functions[i].getstatementsastlist():
                                        j.print()
                else:
                        f.write('Program:\n')
                        for i in self.functions:
                                self.printfunctionheader(i,f)
                                for j in self.functions[i].getstatementsastlist():
                                        j.print(f)
        def printfunctionheader(self,name,f=None):
                if f is None:
                        print(f"\t Procedure: {name} Return Type:{self.functions[name].returntype}")
                else:
                        f.write(f"\t Procedure: {name} Return Type:{self.functions[name].returntype}\n")

