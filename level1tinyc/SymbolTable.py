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
    table=[]
    def addsymboltable(self,symbol):
        self.table.append(symbol)
    def nameinsymboltable(self,name):
        for symbol in self.table:
            if symbol.getsymbolname()==name:
                return True
        return False
    def getsymbolentry(self,name):
        for symbol in self.table:
            if symbol.getsymbolname()==name:
                return symbol
    def print(self):
        for i in self.table:
            i.print()
