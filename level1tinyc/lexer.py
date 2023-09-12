from sly import Lexer
from dataclasses import dataclass
@dataclass
class lexer(Lexer):
    literals={";","=","(",")","{","}"}
    tokens={ID,CONST,INT,PRINT}
    ignore=' \t'
    ignore_comment=r"\#.*"
    ignore_newline=r'\n+'
    ID=r'[a-zA-z][a-zA-Z0-9]*'
    CONST=r'[0-9]+'
    ID['int']=INT
    ID['print']=PRINT
    def CONST(self,t):
        t.value=int(t.value)
        return t
if __name__=='__main__':
    tinyc=lexer()
    expression='''int main(){
        int a=30;
        print a;
        }'''
    for token in tinyc.tokenize(expression):
        print(f"type->{token.type} value->{token.value}")

