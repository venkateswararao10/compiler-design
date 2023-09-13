from dataclasses import dataclass
@dataclass
class SymbolTableEntry:
    name:str
    datatype:int
    value=0
    def getsymbolname(self):
        return self.name
    def getdatatype(self):
        return self.datatype
    def print(self):
        print(f'Name: {self.name}, DataType: {self.datatype}, Value: {self.value}')
@dataclass
class SymbolTable:
    symboltable={}
    def addSymbol(self,symbol):
        self.symboltable[symbol.name]=symbol
    def nameinsymboltable(self,name):
        if name in self.symboltable.keys():
            return True
        else:
            return False
    def print(self):
        for i in self.symboltable:
            print(i)
