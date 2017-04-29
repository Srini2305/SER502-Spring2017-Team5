# Generated from DevilsCode.g4 by ANTLR 4.7
from antlr4 import *
import re
import os
import GlobalStack as gStack
import TempVar as tVar

# This class defines a complete listener for a parse tree produced by DevilsCodeParser.
class DevilsCodeListener(ParseTreeListener):
    def __init__(self):
        self.symbol_table = []
        self.tokens = []

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

        # End symbol for intermediate code
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
        if(str(ctx.getChild(0)) == "print "):
            self.tokens.append(str(ctx.getChild(1)))
        else:
            self.tokens.append(str(ctx.getChild(0)))
        # Declare the global row number counter
        global rowNum

        lChild = ctx.getChild(0).getText()

        # Print stmt
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
        self.tokens.append(str(ctx.getChild(0)))
        pass

    # Exit a parse tree produced by DevilsCodeParser#expr.
    def exitExpr(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#dec_stmt.
    def enterDec_stmt(self, ctx):
        # Declare the global row number counter
        self.symbol_table.append(str(ctx.getChild(1).getChild(0)))
        global rowNum

        dataType = ctx.getChild(0).getText()  # Data Type
        rChild = ctx.getChild(1)  # Identifier or expression

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'DEC' + ' '

        # For DATA_TYPE IDENT format
        if (rChild.getChild(0) is None):
            writeStr += ( rChild.getText() + ' ' + dataType.upper() + '\n' )
        # For DATA_TYPE assign_expr format
        else:
            ident = rChild.getChild(0).getText()
            #value = rChild.getChild(2).getText()
            writeStr += ( ident + ' ' + dataType.upper() + '\n' )

        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#dec_stmt.
    def exitDec_stmt(self, ctx):
        pass


    # Enter a parse tree produced by DevilsCodeParser#assign_expr.
    def enterAssign_expr(self, ctx):
        self.tokens.append(str(ctx.getChild(0)))
        pass

    # Exit a parse tree produced by DevilsCodeParser#assign_expr.
    # Print ASSN after arithmetic operations
    def exitAssign_expr(self, ctx):
        # Declare the global row number counter
        global rowNum
        # Declare the global temp variable
        global Temp1, Temp2

        Temp1 = tVar.GetTempVar_1()
        Temp2 = tVar.GetTempVar_2()

        ident = ctx.getChild(0).getText()
        expr = ctx.getChild(2).getText()

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'ASSN' + ' ' + ident + ' '
        # If Right child is an Expression
        # then Temp Variable will represent the value of Expression
        if ( '+' in expr or '-' in expr or '*' in expr or '/' in expr ):
            writeStr += (Temp1.getName() + '\n')
        # Right child is an IDENT or a value
        else:
            writeStr += (expr + '\n')

        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        # Set Temp variables' flag to False after each Assignment
        # Release temp variables
        Temp1.setFlag(False)
        Temp2.setFlag(False)

        pass


    # Enter a parse tree produced by DevilsCodeParser#math_expr.
    def enterMath_expr(self, ctx):
        self.tokens.append(str(ctx.getChild(0)))
        pass

    def symbolTableChecker(self, isLexicalError):
        literalNames = [ "main ", "(", ")", "{", "}",
                     ";", "print ", "=", "+", "-", "*", "/",
                     "while ", "if ", "else ", "true", "false", "int ", "bool " ]
        self.tokens = [ x for x in self.tokens if not re.match('[\[\]]', x) and x not in literalNames]
        if isLexicalError:
            os.remove("DevilsCodeIntermediate")
            quit()
        for id in self.tokens:
            if id not in self.symbol_table:
                print("ERROR: " + id + " not declared")
                os.remove("DevilsCodeIntermediate")

    # Exit a parse tree produced by DevilsCodeParser#math_expr.
    def exitMath_expr(self, ctx):
        # Declare the global row number counter
        global rowNum

        # Declare two global temp variables
        global Temp1, Temp2

        lOperand = ctx.getChild(0).getText()
        rOperand = ' '
        # Get the operator and right operand if them exist
        if ( ctx.getChild(1) ):
            op = ctx.getChild(1).getText()
        # If op does not exist, it would not be an Expr
        else:
            return
        if ( ctx.getChild(2) ):
            rOperand = ctx.getChild(2).getText()

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' '
        # If operator exists
        if (op == '+'):
            writeStr += ('ADD' + ' ')
        elif (op == '-'):
            writeStr += ('SUB' + ' ')
        else:
            return

        # If lOperand is Expr with op
        if ('+' in lOperand or '-' in lOperand or '*' in lOperand or '/' in lOperand ):
            # If TOP and TOP1 are occupied, it must be represented by TOP
            if Temp1.getFlag() and Temp2.getFlag():
                Temp1.setFlag(True)
                writeStr += (Temp1.getName() + ' ')
            else:
                Temp2.setFlag(True)
                writeStr += (Temp2.getName() + ' ')
        # Else lOperand is IDENT or Number
        else:
            writeStr += (lOperand + ' ')

        # If rOperand is Term with op
        if ('+' in rOperand or '-' in rOperand or '*' in rOperand or '/' in rOperand ):
            # If TOP is occupied, it must be represented by TOP
            Temp1.setFlag(True)
            writeStr += (Temp1.getName() + '\n')
        # Else lOperand is IDENT or Number
        else:
            writeStr += (rOperand + '\n')

        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1
        pass


    # Enter a parse tree produced by DevilsCodeParser#math_term.
    def enterMath_term(self, ctx):
        pass

    # Exit a parse tree produced by DevilsCodeParser#math_term.
    def exitMath_term(self, ctx):
        # Declare global row number counter
        global rowNum
        # Declare two global Temp Var
        global Temp1, Temp2

        #print(rowNum, nestedTerm)
        lOperand = ctx.getChild(0).getText()
        rOperand = ' '
        # Get the operator and right operand if them exist
        # Child 1: op
        if ( ctx.getChild(1) ):
            op = ctx.getChild(1).getText()
        else:
            return
        # Child 2: Right operand
        if ( ctx.getChild(2) ):
            rOperand = ctx.getChild(2).getText()

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' '

        # If operator exists
        if (op == '*'):
            writeStr += ('MUL' + ' ')
        elif (op == '/'):
            writeStr += ('DIV' + ' ')
        else:
            return

        # If left operand is Term or Factor->(expr)
        if ('*' in lOperand or '/' in lOperand or '(' in lOperand ):
            # Temp 1 is used, Temp 2 is not used
            if ( Temp1.getFlag() and not Temp2.getFlag() ):
                writeStr += (Temp1.getName() + ' ')
            # Temp 2 is used, Temp 1 is not used
            else:
                writeStr += (Temp2.getName() + ' ')
        # If left operand is IDENT or Number
        else:
            writeStr += (lOperand + ' ')
            
        # If right operand is Term or Factor->(expr)
        if ('*' in rOperand or '/' in rOperand or '(' in rOperand ):
            # Temp 1 is used, Temp 2 is not used
            if ( Temp1.getFlag() and not Temp2.getFlag() ):
                writeStr += (Temp1.getName() + '\n')
            # Temp 2 is used, Temp 1 is not used
            else:
                writeStr += (Temp2.getName() + '\n')
        else:
            writeStr += (rOperand + '\n')

        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        # Set Flag of Temp Variable TOP
        # It must be used
        if not Temp1.getFlag():
            Temp1.setFlag(True)

        pass


    # Enter a parse tree produced by DevilsCodeParser#math_factor.
    def enterMath_factor(self, ctx):
        pass

    # Exit a parse tree produced by DevilsCodeParser#math_factor.
    def exitMath_factor(self, ctx):
        # Global Row Number
        global rowNum
        # Global Temp Variables
        global Temp1, Temp2
        
        # Set or Get Temp Var
        Temp1 = tVar.GetTempVar_1()
        Temp2 = tVar.GetTempVar_2()

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
        # Declare the global loop row stack
        global loopRowStack

        loopRowStack = gStack.GetLoopStack()

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'LOOP' + '\n'
        loopRowStack.push(rowNum)
        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#while_stmt.
    def exitWhile_stmt(self, ctx):
        # Declare the global row number counter
        global rowNum
        # Declare the global loop row stack
        global loopRowStack

        iCodeFile = open('DevilsCodeIntermediate', 'a')
        writeStr = str(rowNum) + ' ' + 'GOTO' + ' ' + str(loopRowStack.pop()) + '\n'       
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
        self.tokens.append(str(ctx.getChild(0)))
        pass

    # Exit a parse tree produced by DevilsCodeParser#cpr_term.
    def exitCpr_term(self, ctx):
        pass

