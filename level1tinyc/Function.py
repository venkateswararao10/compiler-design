from dataclasses import dataclass
from SymbolTable import SymbolTable,SymbolTableEntry
from AST import *
@dataclass
class Function:
    returntype:str
    name:str
    statementsastlist=[]
    localsymboltable:SymbolTable
    def setstatementsastlist(self,sastlist):
        self.setstatementsastlist=sastlist
    def getstatementsastlist(self):
        return self.setstatementsastlist
    def setlocalsymboltable(self,localsymboltable):
        self.localsymboltable=localsymboltable
    def getlocalsymboltable(self):
        return self.localsymboltable
    def print(self):
        print(f"function name: {self.name}  return type: {self.returntype} ")