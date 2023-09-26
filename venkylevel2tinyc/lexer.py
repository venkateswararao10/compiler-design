from sly import Lexer
class lexer(Lexer):
    tokens={INT,PRINT,ID,DOUBLE,DOUBLECONSTANT,INTCONSTANT,ADDITION,SUBTRACTION,MULTIPLICATION,DIVISION,REMAINDER}
    literals={'(',')','{','}',';',',','=','.'}
    ignore=r'\t '
    ignore_newline=r'\n+'
    ignore_comments=r'\#.*'
    ID=r'[a-zA-Z][0-9a-zA-Z]*'
    ADDITION=r'\+'
    SUBTRACTION=r'-'
    MULTIPLICATION=r'\*'
    DIVISION=r'/'
    REMAINDER=r'%'
    ID['int']=INT
    ID['double']=DOUBLE
    ID['print']=PRINT
    DOUBLECONSTANT=r'[0-9]+\.[0-9]+'
    INTCONSTANT=r'\d+'
    def INTCONSTANT(self,t):
        t.value=int(t.value)
        return t
    def DOUBLECONSTANT(self,t):
        t.value=float(t.value)
        return t
if __name__=='__main__':
        expression='''
        int main(){
        int a,b; # comments
        double c,d;
        a=40;
        b=a;
        c=90.8;
        d=9.6 + 5.6;
        print b;
        print a;
        }
        '''
        l=lexer()
        for token in l.tokenize(expression):
            print(f'type->{token.type} value->{token.value}')

