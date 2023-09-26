from SymbolTable import *
class Function:
    def __init__(self,name,returntype):
        self.name=name
        self.returntype=returntype
        self.localsymboltable=SymbolTable()
        self.statementsastlist=[]
    def setlocalsymboltable(self,symboltable):
        self.localsymboltable=symboltable
    def getlocalsymboltable(self):
        return self.localsymboltable
    def setstatementsastlist(self,sastlist):
        self.statementsastlist=sastlist
    def getstatementsastlist(self):
        return self.statementsastlist