from lexer import lexer
from sly import Parser
from AST import *
from Function import *
from Program import *
from SymbolTable import *
from dataclasses import dataclass
@dataclass
class parser(Parser):
        tokens=lexer.tokens
        literals=lexer.literals
        memory={}
        prog=Program()
        #mainfunc=Function()
        #localsymbol=SymbolTable()
        @_('return_type ID "(" ")" "{" statements "}"')
        def program(self,value):
                        self.localsymbol=SymbolTable()
                        self.mainfunc=Function(value.ID,value.return_type,self.localsymbol)
                        self.mainfunc.setstatementsastlist(value.statements)
                        self.prog.addfunctiondetails(value.ID,self.mainfunc)
        @_('INT')
        def return_type(self,value):
                        pass
        @_('statement ";" statements')
        def statements(self,value):
                        pass
        @_('statement ";"')
        def statements(self,value):
                        pass
        @_('declaration_stmt')
        def statement(self,value):
                        pass
        @_('assisgnment_stmt')
        def statement(self,value):
                        pass
        @_('type list_of_variables')
        def declaration_stmt(self,value):
                        pass
        @_('ID "," list_of_variables')
        def list_of_variables(self,value):
                        pass
        @_('ID')
        def list_of_variables(self,value):
                 self.memory[value.ID]=0
        @_('ID "=" ID')
        def assisgnment_stmt(self,value):
                        self.memory[value.ID0]=self.memory[value.ID1]
        @_('ID "=" CONST')
        def assisgnment_stmt(self,value):
                        self.memory[value.ID]=value.CONST
        @_('print_stmt')
        def statement(self,value):
                        pass
        @_('PRINT ID')
        def print_stmt(self,value):
                        print(self.memory[value.ID])
                        print(type(self.memory[value.ID]))
        @_('INT')
        def type(self,value):
                pass
lex=lexer()
par=parser()
expression='''int main(){
int a;
         a=30;
b=a;
print a;
print b; }
'''
par.parse(lex.tokenize(expression))