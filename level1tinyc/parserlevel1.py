from lexer import lexer
from sly import Parser
from AST import *
from Function import *
from Program import *
from SymbolTable import *
from dataclasses import dataclass
#@dataclass
class parser(Parser):
        def __init__(self):
                self.localsymboltable=SymbolTable()
                self.sastlist=[]
        tokens=lexer.tokens
        literals=lexer.literals
        @_('return_type ID "(" ")" "{" statements "}"')
        def program(self,value):
                prog=Program()
                func=Function(value.return_type,value.ID,self.localsymboltable)
                func.setstatementsastlist(value.statements)
                prog.addfunctiondetails(value.ID,func)
                if prog.getmainfunction() == None:
                        print('sorry,there is no main function')
                else:
                        return prog.print()
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
                x=self.localsymboltable.symboltable
                if value.ID in x.keys():
                        print("cannot declare two variables with same names")
                else:
                        s=SymbolTableEntry(value.ID,'int')
                        x[value.ID]=s
        @_('ID')
        def list_of_variables(self,value):
                x=self.localsymboltable.symboltable
                if value.ID in x.keys():
                        print("cannot declare two variables with same names")
                else:
                        s=SymbolTableEntry(value.ID,'int')
        @_('ID "=" ID')
        def assisgnment_stmt(self,value):
                x=self.localsymboltable.symboltable
                if value.ID0 in x.keys() and value.ID1 in x.keys():
                        left=nameAST(x[value.ID0])
                        right=nameAST(x[value.ID1])
                        return assignAST(left,right)
        @_('ID "=" CONST')
        def assisgnment_stmt(self,value):
                x=self.localsymboltable.symboltable
                if value.ID in x.keys():
                        left=nameAST(x[value.ID])
                        right=numberAST(value.CONST)
                        return assignAST(left,right)
        @_('PRINT ID')
        def print_stmt(self,value):
                x=self.localsymboltable.symboltable
                if value.ID in x.keys():
                         y=nameAST(x[value.ID])
                         return printAST(y)
        @_('INT')
        def type(self,value):
                return value[0]
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
