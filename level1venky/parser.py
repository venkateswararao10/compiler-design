from lexer import lexer
from sly import Parser
from AST import *
from Function import Function
from SymbolTable import *
from Program import Program
class parser(Parser):
        literals=lexer.literals
        tokens=lexer.tokens
        def __init__(self,flag=1):
                self.flag=flag
                self.localsymboltable=SymbolTable()
                self.sastlist=[]
        @_('return_type ID "(" ")" "{" statements "}"')
        def program(self,t):
                if flag:
                        program=Program()
                        function=Function(t.ID,t.return_type)
                        function.setlocalsymboltable(self.localsymboltable)
                        #print(self.sastlist)
                        function.setstatementsastlist(self.sastlist)
                        program.addfunction(t.ID,function)
                        if program.getmainfunction() == None:
                                print('error occured in program')
                        else:
                                return program
