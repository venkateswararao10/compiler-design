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
            self.localsymboltable.print()
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
          for val in value[1]:
                if val in self.localsymboltable.symboltable.keys():
                    print("cannot declare two variables with same names")
                else:
                    s=SymbolTableEntry(val,value[0])
                    self.localsymboltable.symboltable[val]=s
    @_('ID "," list_of_variables')
    def list_of_variables(self,value):
           return [value.ID]+ value[2]
    @_('ID')
    def list_of_variables(self,value):
        return [value.ID]
    @_('ID "=" expr')
    def assisgnment_stmt(self,value):
            if value.ID in self.localsymboltable.symboltable.keys() and value.expr:
                    left=NameAST(self.localsymboltable.symboltable[value.ID])
                    right=value.expr
                    node=AssignAST(left=left,right=right)
                    return node if node.checkdatatypes() else print('error')
    @_('expr arop expr')
    def expr(self,value):
        if value.ID in self.localsymboltable.symboltable.keys():
                left=value.expr0
                right=value.expr1
                operator=value.arop
                node=ArithmeticAST(left=left,right=right,operator=operator)
                return node if node.checkdatatypes() else print('error')
    @_('ADDITION','SUBTRACTION','MULTIPLICATION','DIVISION','REMAINDER')
    def arop(self,value):
           return value[0]
    '''@_('ADDITION')
    def arop(self,value):
           return value[0]
    @_('SUBTRACTION')
    def arop(self,value):
           return value[0]
    @_('MULTIPLICATION')
    def arop(self,value):
           return value[0]
    @_('DIVISION')
    def arop(self,value):
           return value[0]
    @_('REMAINDER')
    def arop(self,value):
           return value[0]'''
    @_('ID')
    def expr(self,t):
           if t.ID in self.localsymboltable.symboltable.keys():
                  return NameAST(self.localsymboltable.symboltable[t.ID])
    @_('INTCONSTANT')
    def expr(self,t):
           return NumberAST(t.INTCONSTANT)
    @_('DOUBLECONSTANT')
    def expr(self,t):
           return NumberAST(t[0])
    
    @_('PRINT ID')
    def print_stmt(self,value):
        if value.ID in self.localsymboltable.symboltable.keys():
                return PrintAST(NameAST(self.localsymboltable.symboltable[value.ID]))
    @_('INT')
    def type(self,value):
            return value[0]
    @_('DOUBLE')
    def type(self,value):
            return value[0] 
       
lex=lexer()
par=parser()
expression='''int main(){
int a;
int b;
double c;
        a=30;
b=a+90;

print a;
print b; }
'''
par.parse(lex.tokenize(expression))
