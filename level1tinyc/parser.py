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
        @_('return_type ID "(" ")" "{" statements "}"')
        def program(self,value):
                self.localsymbol=SymbolTable()
                self.mainfunc=Function(value.return_type,value.ID,self.localsymbol)
                self.mainfunc.setstatementsastlist(value.statements)
                self.prog.addfunctiondetails(value.ID,self.mainfunc)
                if self.prog.getmainfunction() == None:
                        print('sorry,there is no main function')
                else:
                        return self.prog
        @_('INT')
        def return_type(self,value):
                return value[0]
        @_('statement ";" statements')
        def statements(self,value):
                return [value[0]] + value[2]
        @_('statement ";"')
        def statements(self,value):
                return [value[0]]
        @_('declaration_stmt','assisgnment_stmt','print_stmt')
        def statement(self,value):
                return value[0]
        @_('type list_of_variables')
        def declaration_stmt(self,value):
                x=self.prog.getmainfunction().getlocalsymboltable()
                for var in value[1]:
                        if x.nameinsymboltable(var)==False:
                                entry=SymbolTableEntry(var,value[0])
                                self.prog.getmainfunction().getlocalsymboltable().addsymboltable(entry)
                                self.prog.getmainfunction().getlocalsymboltable().print()
                        else:
                                print(f"Error: redeclaration of '{val}'")
        @_('ID "," list_of_variables')
        def list_of_variables(self,value):
                x=self.prog.getmainfunction().getlocalsymboltable().getsymbolentry(value.ID)
                return [nameAST(x)]+value[2]
        @_('ID')
        def list_of_variables(self,value):
                x=self.prog.getmainfunction().getlocalsymboltable().getsymbolentry(value.ID)
                return [nameAST(x)]
        @_('ID "=" ID')
        def assisgnment_stmt(self,value):
                x=self.prog.getmainfunction().getlocalsymboltable().getsymbolentry(value.ID0)
                y=self.prog.getmainfunction().getlocalsymboltable().getsymbolentry(value.ID1)
                left=nameASTT(x)
                right=nameAST(y)
                return assignAST(left,right)
        @_('ID "=" CONST')
        def assisgnment_stmt(self,value):
                x=self.prog.getmainfunction().getlocalsymboltable().getsymbolentry(value.ID0)
                y=numberAST(value.CONST)
                return assignAST(nameAST(x),y)
        @_('PRINT ID')
        def print_stmt(self,value):
                x=self.prog.getmainfunction().getlocalsymboltable().getsymbolentry(value.ID0)
                return printAST(nameAST(x))
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
