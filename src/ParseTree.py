import sys
import re
from antlr4 import *
from antlr4.InputStream import InputStream
from DevilsCodeLexer import DevilsCodeLexer
from DevilsCodeParser import DevilsCodeParser
from DevilsCodeListener import DevilsCodeListener
from DevilsCodeVisitor import DevilsCodeVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = DevilsCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DevilsCodeParser(token_stream)
    tree, isLexicalError = parser.program()

    lisp_tree_str = tree.toStringTree(recog=parser)
    listener = DevilsCodeListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.symbolTableChecker(isLexicalError)
