class SymbolTableEntry:
    def __init__(self,name,datatype):
        self.name=name
        self.datatype=datatype
    def getsymbolname(self):
        return self.name
    def getdatatype(self):
        return self.datatype
    def print(self):
        print(f"{self.name} - {self.datatype}",end='')
class SymbolTable:
    def __init__(self):
        self.symboltable={}
    def addsymbol(self,symboltableentry):
        self.symboltable[symboltableentry.name]=symboltableentry
    def isnameinSymboltable(self,name):
        if self.symboltable.keys() == name:
            return True
        else:
            return False
    def print(self):
        for name,symboltableentry in self.symboltable.items():
            symboltableentry.print()