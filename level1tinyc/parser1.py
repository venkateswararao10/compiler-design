from sly import Parser
from LexicalAnalyzerForTinyC import lexer
from Ast import *
from SymbolTable import *
from Program import *
from Function import Function
import argparse
a=argparse.ArgumentParser()
a.add_argument('InputFile')
args=a.parse_args()
class parser(Parser):
        def __init__(self):
                #self.tinycprogram=Program()
                #self.fun=Function('main',int)
                self.localSymbolTable={}
                self.sastlist=[]
        tokens=lexer.tokens
        literals=lexer.literals
        @_('return_type ID "(" ")" "{" statements "}"')
        def program(self,t):
                tinycprogram=Program()
                fun=Function('main',int)
                #self.fun.setStatementsAstList(t.statements)
                #self.tinycprogram.addFunctionDetails(t.ID,self.fun)
                fun.setStatementsAstList(t.statements)
                fun.localSymbolTable=self.localSymbolTable
                tinycprogram.addFunctionDetails(t.ID,fun)
                tinycprogram.print()
        @_('statement ";" statements')
        def statements(self,t):
                return t.statements
        @_('statement ";"')
        def statements(self,t):
                return t.statement
        @_('assignment_stmt','print_stmt')
        def statement(self,t):
                self.sastlist.append(t[0])
                return self.sastlist
        @_('declaration_stmt')
        def statement(self,t):
                pass
        @_('INT')
        def return_type(self,t):
                pass
        @_('INT list_of_variables')
        def declaration_stmt(self,t):
                pass
        @_('ID "," list_of_variables')
        def list_of_variables(self,t):
                if t.ID in self.localSymbolTable.keys():
                        print("cannot declare two variables with same names")
                else:
                        s=SymbolTableEntry(t.ID,int)
                        #self.fun.localSymboltable.addSymbol(s)
                        self.localSymbolTable[t.ID]=s
        @_(' ID ')
        def list_of_variables(self,t):
                #if self.fun.localSymboltable.isVarInSymbolTable(t.ID):
                if t.ID in self.localSymbolTable.keys():
                        print("cannot declare two variables with same names")
                else:
                        s=SymbolTableEntry(t.ID,int)
                        self.localSymbolTable[t.ID]=s
        @_('ID "=" expr')
        def assignment_stmt(self,t):
                #if self.fun.localSymboltable.isVarInSymbolTable(t.ID0) and self.fun.localSymboltable.isVarInSymbolTable(t.ID1):
                if t.ID0 in self.localSymbolTable.keys() and t.ID1 in self.localSymbolTable.keys():
                        left=NameAst(self.localSymbolTable[t.ID0])
                        right=NameAst(self.localSymbolTable[t.ID1])
                        node=AssignAst(left,right)
                        if node.checkDataTypes():
                                return node
                        else:
                                print("error occurred at assignment statement")
        @_('expr "+" expr')
        def expr(self,t):
                return t.expr0+t.expr1
        @_('expr "-" expr')
        def expr(self,t):
                return t.expr0-t.expr1
        @_('expr "*" expr')
        def expr(self,t):
                return t.expr0*t.expr1
        @_('expr "/" expr')
        def expr(self,t):
                return t.expr0/expr1
        @_('ID')
        def expr(self,t):
                return t.ID
        @_('NUMBER')
        def expr(self,t):
                return t.NUMBER
        @_('ID "=" NUMBER')
        #def assignment_stmt(self,t):

                #if self.fun.localSymboltable.isVarInSymbolTable(t.ID):

                #if t.ID in self.localSymbolTable.keys():
                        #left=NameAst(self.localSymbolTable[t.ID])
                        #right=NumberAst(t.NUMBER)
                        #node=AssignAst(left,right)
                        #if node.checkDataTypes():
                        #       return node
                        #else:
                        #       print("error occurred at assignment statement")
        @_('PRINT ID')
        def print_stmt(self,t):
                #if self.fun.localSymboltable.isVarInSymbolTable(t.ID):
                if t.ID in self.localSymbolTable.keys():
                        symbol=NameAst(self.localSymbolTable[t.ID])
                        node=PrintAst(symbol)
                        return node
                else:
                        print("given symbol is not declared")
tinycFile=open(args.InputFile,'r')
l=lexer()
p=parser()
p.parse(l.tokenize(tinycFile.read()))












class SymbolTable:
    def __init__(self):
        self.symboltable={}
    def addSymbol(self,symbol):
        self.symboltable[symbol.name]=symbol
    def isVarInSymbolTable(self,name):
        if name in self.symboltable.keys():
            return True
        else:
            return False
    def printSymbolTable(self):
        for i in self.symboltable:
            print(i)









from lexer import lexer
from sly import Parser
from AST import *
from Function import *
from Program import *
from SymbolTable import *
from dataclasses import dataclass
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
                        return prog
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
                        x[value.ID]=s


        @_('ID "=" ID')
        def assisgnment_stmt(self,value):
                x=self.localsymboltable.symboltable
                if value.ID0 in x.keys() and value.ID1 in x.keys():
                left=nameASTT(x[value.ID0])
                right=nameAST(x[value.ID1])
                return assignAST(left,right)
        @_('ID "=" CONST')
        def assisgnment_stmt(self,value):
                x=self.localsymboltable.symboltable
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
print(par.parse(lex.tokenize(expression)))



from sly import Parser
from LexicalAnalyzerForTinyC import lexer
from Ast import *
from SymbolTable import *
from Program import *
from Function import Function
import argparse
a=argparse.ArgumentParser()
a.add_argument('InputFile')
args=a.parse_args()
class parser(Parser):
        def __init__(self):
                #self.tinycprogram=Program()
                #self.fun=Function('main',int)
                self.localSymbolTable={}
                self.sastlist=[]
        tokens=lexer.tokens
        literals=lexer.literals
        precedence=(('left','+','-'),('left','*','/'))
        @_('return_type ID "(" ")" "{" statements "}"')
        def program(self,t):
                tinycprogram=Program()
                fun=Function('main',int)
                #self.fun.setStatementsAstList(t.statements)
                #self.tinycprogram.addFunctionDetails(t.ID,self.fun)
                fun.setStatementsAstList(t.statements)
                fun.localSymbolTable=self.localSymbolTable
                tinycprogram.addFunctionDetails(t.ID,fun)
                tinycprogram.print()
        @_('statement ";" statements')
        def statements(self,t):
                return t.statements
        @_('statement ";"')
        def statements(self,t):
                return t.statement
        @_('assignment_stmt','print_stmt')
        def statement(self,t):
                self.sastlist.append(t[0])
                return self.sastlist
        @_('declaration_stmt')
        def statement(self,t):
                pass
        @_('INT')
        def return_type(self,t):
                pass
        @_('INT list_of_variables')
        def declaration_stmt(self,t):
                pass
        @_('ID "," list_of_variables')
        def list_of_variables(self,t):
                if t.ID in self.localSymbolTable.keys():
                        print("cannot declare two variables with same names")
                else:
                        s=SymbolTableEntry(t.ID,int)
                        #self.fun.localSymboltable.addSymbol(s)
                        self.localSymbolTable[t.ID]=s
        @_(' ID ')
        def list_of_variables(self,t):
                #if self.fun.localSymboltable.isVarInSymbolTable(t.ID):
                if t.ID in self.localSymbolTable.keys():
                        print("cannot declare two variables with same names")
                else:
                        s=SymbolTableEntry(t.ID,int)
                        self.localSymbolTable[t.ID]=s
        @_('ID "=" expr')
        def assignment_stmt(self,t):
                #if self.fun.localSymboltable.isVarInSymbolTable(t.ID0) and self.fun.localSymboltable.isVarInSymbolTable(t.ID1):
                if t.ID in self.localSymbolTable.keys():
                        left=NameAst(self.localSymbolTable[t.ID])
                        right=t.expr
                        node=AssignAst(left,right)
                        if node.checkDataTypes():
                                return node
                        else:
                                print("error occurred at assignment statement")
        @_('expr "+" expr')
        def expr(self,t):
                node=AddAst(t.expr0,t.expr1)
                if node.checkDataTypes():
                        return node
                else:
                        print("error occurred in arithmetic expression")
        @_('expr "-" expr')
        def expr(self,t):
                node=SubAst(t.expr0,t.expr1)
                if node.checkDataTypes():
                        return node
                else:
                        print("error occurred in arithmetic expression")
        @_('expr "*" expr')
        def expr(self,t):
                node=MulAst(t.expr0,t.expr1)
                if node.checkDataTypes():
                        return node
                else:
                        print("error occurred in arithmetic expression")
        @_('expr "/" expr')
        def expr(self,t):
                node=DivAst(t.expr0,t.expr1)
                if node.checkDataTypes():
                        return node
                else:
                        print("error occurred in arithmetic expression")
        @_('ID')
        def expr(self,t):
                if t.ID in self.localSymbolTable.keys():
                        node=NameAst(self.localSymbolTable[t.ID])
                        return node
                else:
                        print(f"{t.ID} not declared")
        @_('NUMBER')
        def expr(self,t):
                node=NumberAst(t.NUMBER)
                return node
        #@_('ID "=" NUMBER')
        #def assignment_stmt(self,t):

                #if self.fun.localSymboltable.isVarInSymbolTable(t.ID):
        @_('NUMBER')
        def expr(self,t):
                node=NumberAst(t.NUMBER)
                return node
        #@_('ID "=" NUMBER')
        #def assignment_stmt(self,t):

                #if self.fun.localSymboltable.isVarInSymbolTable(t.ID):

                #if t.ID in self.localSymbolTable.keys():
                        #left=NameAst(self.localSymbolTable[t.ID])
                        #right=NumberAst(t.NUMBER)
                        #node=AssignAst(left,right)
                        #if node.checkDataTypes():
                        #       return node
                        #else:
                        #       print("error occurred at assignment statement")
        @_('PRINT ID')
        def print_stmt(self,t):
                #if self.fun.localSymboltable.isVarInSymbolTable(t.ID):
                if t.ID in self.localSymbolTable.keys():
                        symbol=NameAst(self.localSymbolTable[t.ID])
                        node=PrintAst(symbol)
                        return node
                else:
                        print("given symbol is not declared")
tinycFile=open(args.InputFile,'r')
l=lexer()
p=parser()
p.parse(l.tokenize(tinycFile.read()))


