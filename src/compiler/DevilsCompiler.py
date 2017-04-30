# Author: Hari Iyer
# Version: 3.0.0
# Date: April 28, 2017
# Purpose: An integrated sequence of steps for Lexical analysis and Parse Tree generation.

import sys
import re
from antlr4 import *
from antlr4.InputStream import InputStream
from DevilsCodeLexer import DevilsCodeLexer
from DevilsCodeParser import DevilsCodeParser
from DevilsCodeListener import DevilsCodeListener

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    file_name = sys.argv[1].rsplit('.', 1)[0]
    lexer = DevilsCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DevilsCodeParser(token_stream, file_name)
    tree = parser.program()

    lisp_tree_str = tree.toStringTree(recog=parser)
    listener = DevilsCodeListener(file_name)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.symbolTableChecker()
