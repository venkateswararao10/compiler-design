from lexer import lexer
from sly import Parser
from AST import *
from Function import Function
from SymbolTable import *
from Program import Program
class parser(Parser):
    literals=lexer.literals
    tokens=lexer.tokens
    def __init__(self):
        self.localsymboltable=SymbolTable()
        self.sastlist=[]
    @_('return_type ID "(" ")" "{" statements "}"')
    def program(self,t):
        program=Program()
        function=Function(t.ID,t.return_type)
        function.setlocalsymboltable(self.localsymboltable)
        print(self.sastlist)
        function.setstatementsastlist(self.sastlist)
        program.addfunction(t.ID,function)
        if program.getmainfunction() == None:
            print('error occured in program')
        else:
            program.print()
    @_('INT')
    def return_type(self,value):
                return value[0]
    @_('statement ";" statements')
    def statements(self,value):
                return value.statements
    @_('statement ";"')
    def statements(self,value):
                return value.statement
    @_('declaration_stmt')
    def statement(self,t):
                pass
    @_('assisgnment_stmt','print_stmt')
    def statement(self,value):
            self.sastlist.append(value[0])
            return self.sastlist
    @_('type list_of_variables')
    def declaration_stmt(self,value):
                pass
    @_('ID "," list_of_variables')
    def list_of_variables(self,value):
            if value.ID in self.localsymboltable.symboltable.keys():
                    print("cannot declare two variables with same names")
            else:
                    s=SymbolTableEntry(value.ID,'int')
                    self.localsymboltable.symboltable[value.ID]=s
    @_('ID')
    def list_of_variables(self,value):
        if value.ID in self.localsymboltable.symboltable.keys():
                    print("cannot declare two variables with same names")
        else:
                    s=SymbolTableEntry(value.ID,'int')
                    self.localsymboltable.symboltable[value.ID]=s
    @_('ID "=" ID')
    def assisgnment_stmt(self,value):
            if value.ID0 in self.localsymboltable.symboltable.keys() and value.ID1 in self.localsymboltable.symboltable.keys():
                    left=NameAST(self.localsymboltable.symboltable[value.ID0])
                    right=NameAST(self.localsymboltable.symboltable[value.ID1])
                    node=AssignAST(left=left,right=right)
                    return node if node.checkdatatypes() else print('error')
    @_('ID "=" NUMBER')
    def assisgnment_stmt(self,value):
        if value.ID in self.localsymboltable.symboltable.keys():
                left=NameAST(self.localsymboltable.symboltable[value.ID])
                right=NumberAST(value.NUMBER)
                node=AssignAST(left=left,right=right)
                return node if node.checkdatatypes() else print('error')
    @_('PRINT ID')
    def print_stmt(self,value):
        if value.ID in self.localsymboltable.symboltable.keys():
                return PrintAST(NameAST(self.localsymboltable.symboltable[value.ID]))
    @_('INT')
    def type(self,value):
            return value[0]
        
lex=lexer()
par=parser()
expression='''int main(){
int a;
int b;
        a=30;
b=a;
print a;
print b; }
'''
par.parse(lex.tokenize(expression))
