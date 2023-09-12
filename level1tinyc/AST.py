from abc import ABC,abstractmethod
from dataclasses import dataclass
from SymbolTable import *
@dataclass
class AST(ABC):
    @abstractmethod
    def print(self):
        pass
    def typecheckAST(self):
        pass
    def getdatatype(self):
        pass
@dataclass
class numberAST(AST):
        value:int
        def print(self):
             print(f"Num:{self.value}",end="")
        def getDataType(self):
		        return type(self.value)
@dataclass
class nameAST(AST):
        name:SymbolTableEntry
        def print(self):
            print("Name:",self.symbolEntry,end="")
        def getdatatype(self):
              return SymbolTable.getsymbolentry(self.name).getdatatype()
@dataclass
class assignAST(AST):
                left:SymbolTableEntry
                right:SymbolTableEntry
                def typeCheckAST(self):
                        if(self.left.getDataType()== self.right.getDataType()):
                            return True
                        return False
                def print(self):
                        print("\t\tAssign:")
                        print("\t\t\tLHS (",end="")
                        self.left.print()
                        print(")")
                        # print(SymbolTable.getSymbolEntry(self.left.symbolEntry).name,"  )")
                        print("\t\t\tRHS (",end="")
                        self.right.print()
                        print(")")  
@dataclass
class printAst(AST):
        symbolEntry:SymbolTableEntry
        def print(self):
            print("\t\tPrint: ")
            print(f"\t\t\t",end="")
            self.symbolEntry.print()
            print()