import sys
import re
from antlr4 import *
from antlr4.InputStream import InputStream
from DevilsCodeLexer import DevilsCodeLexer
from DevilsCodeParser import DevilsCodeParser
from DevilsCodeListener import DevilsCodeListener
from DevilsCodeVisitor import DevilsCodeVisitor

class CustomDevilsCodeListener(DevilsCodeListener):
    def __init__(self):
        self.symbol_table = []
        self.tokens = []

    def enterDec_stmt(self, ctx):
        self.symbol_table.append(str(ctx.getChild(1).getChild(0)))

    def enterExpr(self, ctx):
        self.tokens.append(str(ctx.getChild(0)))

    def enterStmt(self, ctx):
        if(str(ctx.getChild(0)) == "print "):
            self.tokens.append(str(ctx.getChild(1)))
        else:
            self.tokens.append(str(ctx.getChild(0)))

    def enterAssign_expr(self, ctx):
        self.tokens.append(str(ctx.getChild(0)))

    def enterMath_factor(self, ctx):
        self.tokens.append(str(ctx.getChild(0)))

    def enterCpr_term(self, ctx):
        self.tokens.append(str(ctx.getChild(0)))

    def symbolTableChecker(self):
        literalNames = [ "main ", "(", ")", "{", "}",
                     ";", "print ", "=", "+", "-", "*", "/",
                     "while ", "if ", "else ", "true", "false", "int ", "bool " ]
        self.tokens = [ x for x in self.tokens if not re.match('[\[\]]', x) and x not in literalNames]
        self.tokens = set(self.tokens)
        for id in self.tokens:
            if id not in self.symbol_table:
                print("ERROR: " + id + " not declared")

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
    listener = CustomDevilsCodeListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.symbolTableChecker()
    print(lisp_tree_str)
