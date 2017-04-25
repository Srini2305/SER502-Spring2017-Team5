# Generated from DevilsCode.g4 by ANTLR 4.7
from antlr4 import *

# This class defines a complete listener for a parse tree produced by DevilsCodeParser.
class DevilsCodeListener(ParseTreeListener):
    
    # Enter a parse tree produced by DevilsCodeParser#program.
    def enterProgram(self, ctx):
        # Declare the global row number counter
        global rowNum

        # Set row number to 0
        rowNum = 0
        # Create or Override Intermediate Code File
        iCodeFile = open('DevilsCodeIntermediate', 'w')
        writeStr = str(rowNum) + ' ' + 'BEGIN' + '\n'
        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#program.
    def exitProgram(self, ctx):
        # Declare the global row number counter
        global rowNum

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'END' + '\n'
        iCodeFile.write(writeStr)
        iCodeFile.close()

        pass


    # Enter a parse tree produced by DevilsCodeParser#stmtlists.
    def enterStmtlists(self, ctx):
        pass

    # Exit a parse tree produced by DevilsCodeParser#stmtlists.
    def exitStmtlists(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#stmt.
    def enterStmt(self, ctx):
        # Declare the global row number counter
        global rowNum

        lChild = ctx.getChild(0).getText()

        if lChild == 'print ':
            iCodeFile = open('DevilsCodeIntermediate', 'a')
            rChild = ctx.getChild(1).getText()
            writeStr = str(rowNum) + ' ' + 'PRINT' + ' ' + rChild + '\n'
            iCodeFile.write(writeStr)
            iCodeFile.close()

        pass

    # Exit a parse tree produced by DevilsCodeParser#stmt.
    def exitStmt(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#expr.
    def enterExpr(self, ctx):
        pass

    # Exit a parse tree produced by DevilsCodeParser#expr.
    def exitExpr(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#dec_stmt.
    def enterDec_stmt(self, ctx):
        # Declare the global row number counter
        global rowNum

        dataType = ctx.getChild(0).getText()  # Data Type
        rChild = ctx.getChild(1)  # Identifier or expression

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'DEC' + ' '
        # For DATA_TYPE IDENT
        if (rChild.getChild(0) is None):
            writeStr += ( rChild.getText() + ' ' + dataType + '\n' )
        # For DATA_TYPE assign_expr
        else:
            ident = rChild.getChild(0).getText()
        #    value = rChild.getChild(2).getText()
            writeStr += ( ident + ' ' + dataType + '\n' )
        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#dec_stmt.
    def exitDec_stmt(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#assign_expr.
    def enterAssign_expr(self, ctx):
        # Declare the global row number counter
        global rowNum

        ident = ctx.getChild(0).getText()
        expr = ctx.getChild(2).getText()

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'ASSN' + ' ' + ident + ' '
        # Right child is an Expression, use Temp to represent the value of Expression
        if ('+' in expr or '-' in expr or '*' in expr or '/' in expr):
            writeStr += ('E' + str(rowNum) + '\n')
        # Right child is an IDENT or a value
        else:
            writeStr += (expr + '\n')
        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#assign_expr.
    def exitAssign_expr(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#math_expr.
    def enterMath_expr(self, ctx):
        # Declare the global row number counter
        global rowNum

        # Declare two global flag for nested expression
        global nestedLT
        global nestedRT

        lOperand = ctx.getChild(0).getText()
        rOperand = ' '
        # Get the operator and right operand if them exist
        if ( ctx.getChild(1) ):
            op = ctx.getChild(1).getText()
        else:
            return
        if ( ctx.getChild(2) ):
            rOperand = ctx.getChild(2).getText()

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' '
        # If operator exists
        if (op == '+'):
            writeStr += ('ADD' + ' ' + 'E' + str(rowNum - 1) + ' ')
        elif (op == '-'):
            writeStr += ('SUB' + ' ' + 'E' + str(rowNum - 1) + ' ')
        else:
            return

        # If Expr is nested with Term
        if ('+' in lOperand or '-' in lOperand or '*' in lOperand or '/' in lOperand):
            #nestedLT = True
            writeStr += ('LT' + str(rowNum) + ' ')
        else:
            writeStr += (lOperand + ' ')

        if ('+' in rOperand or '-' in rOperand or '*' in rOperand or '/' in rOperand):
            #nestedRT = True
            writeStr += ('RT' + str(rowNum) + '\n')
        else:
            writeStr += (rOperand + '\n')

        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#math_expr.
    def exitMath_expr(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#math_term.
    def enterMath_term(self, ctx):
        # Declare global row number counter
        global rowNum
        # Declare two global flag for nested expression
        global nestedRT

        #print(rowNum, nestedTerm)
        lOperand = ctx.getChild(0).getText()
        rOperand = ' '
        # Get the operator and right operand if them exist
        if ( ctx.getChild(1) ):
            op = ctx.getChild(1).getText()
        else:
            return
        if ( ctx.getChild(2) ):
            rOperand = ctx.getChild(2).getText()

        iCodeFile = open('DevilsCodeIntermediate', 'a+')
        writeStr = str(rowNum) + ' '
        term = 'RT'
        # If operator exists
        if (op == '*'):
            writeStr += ('MUL' + ' ' + term + str(rowNum - 1) + ' ')
        elif (op == '/'):
            writeStr += ('DIV' + ' ' + term + str(rowNum - 1) + ' ')
        else:
            return

        # If Expr is nested
        #if ('+' in lOperand or '-' in lOperand or '*' in lOperand or '/' in lOperand):
            #nestedLT = True
            #writeStr += ('LT' + str(rowNum) + ' ')
        #else:
        writeStr += (lOperand + ' ')

        #if ('+' in rOperand or '-' in rOperand or '*' in rOperand or '/' in rOperand):
            #nestedRT = True
            #writeStr += ('RT' + str(rowNum) + '\n')
        #else:
        writeStr += (rOperand + '\n')

        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#math_term.
    def exitMath_term(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#math_factor.
    def enterMath_factor(self, ctx):
        pass

    # Exit a parse tree produced by DevilsCodeParser#math_factor.
    def exitMath_factor(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#number.
    def enterNumber(self, ctx):
        pass

    # Exit a parse tree produced by DevilsCodeParser#number.
    def exitNumber(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#while_stmt.
    def enterWhile_stmt(self, ctx):
        # Declare the global row number counter
        global rowNum
        # Declare the global loop row counter
        global loopRow

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'LOOP' + '\n'
        #loopRow.append(rowNum)
        loopRow = rowNum
        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#while_stmt.
    def exitWhile_stmt(self, ctx):
        # Declare the global row number counter
        global rowNum
        # Declare the global loop row counter
        global loopRow

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'GOTO' + ' ' + str(loopRow) + '\n'       
        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass


    # Enter a parse tree produced by DevilsCodeParser#if_stmt.
    def enterIf_stmt(self, ctx):
        # Declare the global row number counter
        global rowNum

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'COND' + '\n'       
        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#if_stmt.
    def exitIf_stmt(self, ctx):
        # Declare the global row number counter
        global rowNum

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'COND_END' + '\n'       
        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass


    # Enter a parse tree produced by DevilsCodeParser#cpr_expr.
    def enterCpr_expr(self, ctx):
        # Declare the global row number counter
        global rowNum

        cmpSymbol = ctx.getChild(1).getText()
        cmpLeft = ctx.getChild(0).getText()
        cmpRight = ctx.getChild(2).getText()

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        if (cmpSymbol == '<'):
            writeStr = str(rowNum) + ' ' + 'CMPL' + ' '
        elif (cmpSymbol == '<='):
            writeStr = str(rowNum) + ' ' + 'CMPLE' + ' '
        elif (cmpSymbol == '>'):
            writeStr = str(rowNum) + ' ' + 'CMPG' + ' '
        elif (cmpSymbol == '>='):
            writeStr = str(rowNum) + ' ' + 'CMPGE' + ' '
        else:
            writeStr = str(rowNum) + ' ' + 'CMPE' + ' '
        writeStr += cmpLeft + ' ' + cmpRight + '\n'
        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#cpr_expr.
    def exitCpr_expr(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#cpr_term.
    def enterCpr_term(self, ctx):
        pass

    # Exit a parse tree produced by DevilsCodeParser#cpr_term.
    def exitCpr_term(self, ctx):
        pass


