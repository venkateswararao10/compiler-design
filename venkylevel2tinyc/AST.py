from SymbolTable import *
from abc import ABC,abstractmethod
datatype={'int':int,'string':str,'double':float}
arthmeticoperator={'Addition':'+','Subtraction':'-','Multiplication':'*','Division':'/','Remainder':'%'}
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
class ArithmeticAST(AST):
    def __init__(self,left,right,operator):
        self.left=left
        self.right=right
        self.operator=operator
    def checkdatatypes(self):
        if self.left.getdatatype()==self.right.getdatatype():
            return True
        else:
            return False
    def print(self):
        if self.operator in arthmeticoperator.keys():
            print(f"\t\tarthmeticoperator[self.operator]")
            print('\t\t\tLHS:(',end='')
            self.left.print()
            print(')')
            print('\t\t\tOPERATOR:(',end='')
            print(arthmeticoperator[self.operator])
            print(')')
            print('\t\t\tRHS:(',end='')
            self.right.print()
            print(')')
    def getdatatype(self):
        if self.checkdatatypes():
            return self.left.getdatatype()