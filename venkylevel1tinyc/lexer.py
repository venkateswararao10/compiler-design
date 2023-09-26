from sly import Lexer
class lexer(Lexer):
    tokens={INT,PRINT,ID,NUMBER}
    literals={'(',')','{','}',';',',','='}
    ignore=r'\t '
    ignore_newline=r'\n+'
    ignore_comments=r'\#.*'
    ID=r'[a-zA-Z][0-9a-zA-Z]*'
    ID['int']=INT
    ID['print']=PRINT
    NUMBER=r'\d+'
    def NUMBER(self,t):
        t.value=int(t.value)
        return t
if __name__=='__main__':
        expression='''
        int main(){
        int a,b; # comments
        a=40;
        b=a;
        print b;
        print a;
        }
        '''
        l=lexer()
        for token in l.tokenize(expression):
            print(f'type->{token.type} value->{token.value}')

