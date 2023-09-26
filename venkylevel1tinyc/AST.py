from SymbolTable import *
from abc import ABC,abstractmethod
datatype={'int':int,'string':str,'float':float}
class AST(ABC):
    def getdatatype(self):
        pass
    @abstractmethod
    def print(self):
        pass
    def checkdatatypes(self):
        pass
class NameAST(AST):
    def __init__(self,symboltableentry):
        self.symbol=symboltableentry
    def getdatatype(self):
        for i,j in datatype.items():
            if i == self.symbol.getdatatype():
                return j
    def print(self):
        print(f"Name : {self.symbol.name}",end='')
class NumberAST(AST):
    def __init__(self,number):
        self.number=number
    def print(self):
        print(f"Name : {self.number}",end='')
    def getdatatype(self):
        return type(self.number)
class AssignAST(AST):
    def __init__(self,left,right):
        self.left=left
        self.right=right
    def checkdatatypes(self):
        return True if self.left.getdatatype()==self.right.getdatatype() else False
    def print(self):
        print('\t\tAssign:')
        print('\t\t\tLHS:(',end='')
        self.left.print()
        print(')')
        print('\t\t\tRHS:(',end='')
        self.right.print()
        print(')')
class PrintAST(AST):
    def __init__(self,nameast):
        self.name=nameast
    def print(self):
        print('\t\tPrint:')
        print('\t\t\t(',end="")
        self.name.print()
        print(')')

