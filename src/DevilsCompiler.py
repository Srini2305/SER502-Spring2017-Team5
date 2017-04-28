import sys
from antlr4 import *
from DevilsCodeLexer import DevilsCodeLexer
from DevilsCodeParser import DevilsCodeParser
from DevilsCodeListener import DevilsCodeListener

def main(argv):
    if (len(argv) > 1):
        input = FileStream(argv[1])
    else:
        input = StdinStream()

    lexer = DevilsCodeLexer(input)
    stream = CommonTokenStream(lexer)
    parser = DevilsCodeParser(stream)
    tree = parser.program()
    printer = DevilsCodeListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    # Print the Tree
    #print(tree.toStringTree(recog=parser))
 
if __name__ == '__main__':
    main(sys.argv)
