import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from DevilsCodeLexer import DevilsCodeLexer
from DevilsCodeParser import DevilsCodeParser

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = DevilsCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DevilsCodeParser(token_stream)
    tree = parser.program()

    lisp_tree_str = tree.toStringTree(recog=parser)
    f = open('Intermediate_Code', 'w')
    f.write(''+lisp_tree_str+'\n')
    f.close()
    print('\nParse tree for the program: \n\n' + lisp_tree_str)
