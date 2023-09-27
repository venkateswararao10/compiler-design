from SymbolTable import *
from abc import ABC,abstractmethod
datatype={'int':int,'string':str,'float':float}
class AST(ABC):
        def getdatatype(self):
                pass
        @abstractmethod
        def print(self,f=None):
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
        def print(self,f=None):
                if f is None:
                        print(f"Name : {self.symbol.name}",end=')\n')
                else:
                        f.write(f"Name : {self.symbol.name})\n")
class NumberAST(AST):
        def __init__(self,number):
                self.number=number
        def print(self,f=None):
                if f is None:
                        print(f"Number : {self.number}",end=')\n')
                else:
                        f.write(f"Number : {self.number})\n")
        def getdatatype(self):
                return type(self.number)
class AssignAST(AST):
        def __init__(self,left,right):
                self.left=left
                self.right=right
        def checkdatatypes(self):
                return True if self.left.getdatatype()==self.right.getdatatype() else False
        def print(self,f=None):
                if f is None:
                        print('\t\tAssign:')
                        print('\t\t\tLHS:(',end='')
                        self.left.print()
                        print('\t\t\tRHS:(',end='')
                        self.right.print()
                else:
                        f.write('\t\tAssign:\n')
                        f.write('\t\t\tLHS:(')
                        self.left.print(f)
                        f.write('\t\t\tRHS:(')
                        self.right.print(f)
class PrintAST(AST):
        def __init__(self,nameast):
                self.name=nameast
        def print(self,f=None):
                if f is None:
                        print('\t\tPrint:')
                        print('\t\t\t(',end="")
                        self.name.print()
                else:
                        f.write('\t\tPrint:\n')
                        f.write('\t\t\t(')
                        self.name.print(f)

