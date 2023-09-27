import argparse
from parser import parser
from lexer import lexer
parsers = argparse.ArgumentParser()

parsers.usage = "tinyCC [options] file"

parsers.add_argument('-tokens',action='store_true',help="Show tokens in file.toks (or out.toks)")
parsers.add_argument('-parse',action='store_true',help="Stop processing with parsing")
parsers.add_argument('-ast', action='store_true',help="Show abstract syntax trees in file.ast (or out.ast)")
parsers.add_argument('-symtab',action='store_true',help="Show symbol table in file.sym (or out.sym)")
parsers.add_argument('-compile',action='store_true',help="Compile the program and generate spim code in file.spim (or out.spim)")
parsers.add_argument('file',help="TinyC Program")
args = parsers.parse_args()

args.compile = True  #default value
if args.tokens:
        try:
                inputfile=open(args.file,'r')
                lex=lexer()
                tokens_file_name = args.file +".toks"
                tokens_file = open(tokens_file_name,"w")
                for token in lex.tokenize(inputfile.read()):
                        tokens_file.write(f'type->{token.type} value->{token.value}\n')
        except Exception as e:
                print(e)
        else:
                print(f'{args.file}.toks successfully created')
        finally:
                tokens_file.close()
                inputfile.close()
    # call tokenize and print tokens into tokens_file
if args.parse:
        # call parser, which should not create Program data structure
        args.ast = False
        args.compile = False
        try:
                inputfile=open(args.file,'r')
                lex=lexer()
                p=parser()
                p.parse(lex.tokenize(inputfile.read()))
                inputfile.close()
        except Exception as e:
                print(e)
        else:
                print('parser successfully executed')
if args.ast:
        try:
                inputfile=open(args.file,'r')
                lex=lexer()
                p=parser()
                obj=p.parse(lex.tokenize(inputfile.read()))
                ast_file_name = args.file +".ast"
                ast_file = open(ast_file_name,"w")
                output=obj.print(ast_file)
                inputfile.close()
                ast_file.close()
        except Exception as e:
                print(e)
        else:
                print(f'{args.file}.ast successfully created')
        # call parser, creates Program object
        # call program.print(), which should print ast
if args.compile:
        target_code_file_name = args.file +".spim"
        target_code_file = open(target_code_file_name,"w")
    # call parser, creates Program object
    # call program.compile(), which should

