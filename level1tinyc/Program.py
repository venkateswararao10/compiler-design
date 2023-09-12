from dataclasses import dataclass
@dataclass
class Program:
    functions={}
    def addfunctiondetails(self,name,function):
        self.functions[name]=function
    def print(self):
        print('Program:')
        for funname,function in self.functions.items():
            function.print()
    def getmainfunction(self):
        for funname,function in self.functions.items():
            if funname=='main':
                return function

