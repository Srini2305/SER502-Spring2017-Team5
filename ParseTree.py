import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from DevilsCodeLexer import DevilsCodeLexer
from DevilsCodeParser import DevilsCodeParser
from DevilsCodeListener import DevilsCodeListener
from DevilsCodeVisitor import DevilsCodeVisitor

class DevilsCodelistener(DevilsCodeListener):
    def __init__(self):
        self.symbol_table = []

    def enterDec_stmt(self, ctx):
        self.symbol_table.extend(str(ctx.getChild(1).getChild(0)))

    def symbolTable_synthesis(self):
        print("Symbol Table:")
        print(self.symbol_table)
	#To check the program against the symbol table in progress

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
    listener = DevilsCodelistener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.symbolTable_synthesis()
    print(lisp_tree_str)
