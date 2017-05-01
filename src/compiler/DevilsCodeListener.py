# Generated from DevilsCode.g4 by ANTLR 4.7
# Modified by Hari Iyer and Mingfei Yang
# Date: April 21, 2017
# Version: 2
# Purpose: Parse Tree traversal

from antlr4 import *
import re
import os
import GlobalStack as gStack
import TempVar as tVar

# This class defines a complete listener for a parse tree produced by DevilsCodeParser.
class DevilsCodeListener(ParseTreeListener):
    def __init__(self, file_name):
        self.symbol_table = []
        self.tokens = []
        self.file_name = file_name

       # Open intermediate code file to apppend str
    def appendICode(self, writeStr):
        # Append writeStr into File
        iCodeFile = open(self.file_name + '.ic', 'a')
        iCodeFile.write(writeStr)
        iCodeFile.close()

        pass

    # Insert GOTO into intermediate code file
    def insertGOTO(self, targetRow):
        # Global rN for writing GOTO
        global rN

        rN = gStack.GetRNStack()
        # Write GOTO
        lines = []
        iCodeFile = open(self.file_name + '.ic', 'r')
        for line in iCodeFile:
            lines.append(line)
        iCodeFile.close()
        lNum = rN.pop()
        lOffset = rN.stackSize()
        lines.insert(lNum - lOffset, str(lNum) + ' GOTO ' + str(targetRow) + '\n')
        writeStr = ''.join(lines)
        iCodeFile = open(self.file_name + '.ic', 'w+')
        iCodeFile.write(writeStr)
        iCodeFile.close()

        pass


    # Enter a parse tree produced by DevilsCodeParser#program.
    def enterProgram(self, ctx):
        # Declare the global row number counter
        global rowNum
        global condFlag
        condFlag = False
        # Set row number to 0
        rowNum = 0
        # Create or Override Intermediate Code File
        iCodeFile = open(self.file_name + '.ic', 'w')
        writeStr = str(rowNum) + ' ' + 'START' + '\n'
        iCodeFile.write(writeStr)
        iCodeFile.close()
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#program.
    def exitProgram(self, ctx):
        # Declare the global row number counter
        global rowNum

        # End symbol for intermediate code
        writeStr = str(rowNum) + ' ' + 'STOP' + '\n'
        self.appendICode(writeStr)
        rowNum += 1
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

        # For print stmt
        if lChild == 'print ':
            rChild = ctx.getChild(1).getText()
            writeStr = str(rowNum) + ' ' + 'PRINT' + ' ' + rChild + '\n'
            self.appendICode(writeStr)
            rowNum += 1
        # { Stmt }
        if lChild == '{':
            # Generate BEGIN for open brackets
            writeStr = str(rowNum) + ' ' + 'BEGIN' + '\n'
            self.appendICode(writeStr)
            rowNum += 1
        pass

    
    # Exit a parse tree produced by DevilsCodeParser#stmt.
    def exitStmt(self, ctx):
        # Declare the global row number counter
        global rowNum
        # Global rN stack
        global rN
        # Global CondFlag and ElseFlag
        global condFlag
        global ifFlag
        global elseFlag

        lChild = ctx.getChild(0).getText()
        if lChild == '{' and condFlag:
            # If it's printing END for ELSE block, insert GOTO first
            if not ifFlag and not elseFlag:
                self.insertGOTO(rowNum)

            writeStr = str(rowNum) + ' ' + 'END' + '\n'       
            self.appendICode(writeStr)
            rowNum += 1
            ifFlag = False

            # If condFlag and elseFlag are True, generate ELSE
            if condFlag and elseFlag:
                # Write GOTO
                self.insertGOTO(rowNum - 1)
                # Write ELSE
                writeStr = str(rowNum) + ' ' + 'ELSE' + '\n'
                self.appendICode(writeStr)
                rowNum += 1
                # Push the rowNum of ELSE for GOTO
                rN = gStack.GetRNStack()
                rN.push(rowNum)
                rowNum += 1
                elseFlag = False
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
        if '=' in ctx.getChild(1).getText():
            self.symbol_table.append(str(ctx.getChild(1).getChild(0)))
        else:
            self.symbol_table.append(str(ctx.getChild(1)))
        global rowNum

        dataType = ctx.getChild(0).getText()  # Data Type
        rChild = ctx.getChild(1)  # Identifier or expression

        writeStr = str(rowNum) + ' ' + 'DEC' + ' '

        # For DATA_TYPE IDENT format
        if (rChild.getChild(0) is None):
            writeStr += ( rChild.getText() + ' ' + dataType.upper() + '\n' )
        # For DATA_TYPE assign_expr format
        else:
            ident = rChild.getChild(0).getText()
            #value = rChild.getChild(2).getText()
            writeStr += ( ident + ' ' + dataType.upper() + '\n' )
        self.appendICode(writeStr)
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
        global Temp

        Temp = tVar.GetTempVar()

        ident = ctx.getChild(0).getText()
        expr = ctx.getChild(2).getText()

        writeStr = str(rowNum) + ' ' + 'ASSN' + ' ' + ident + ' '
        # If Right child is an Expression
        # then Temp Variable will represent the value of Expression
        if ( '+' in expr or '-' in expr or '*' in expr or '/' in expr ):
            writeStr += (Temp.getName() + '\n')
        # Right child is an IDENT or a value
        else:
            writeStr += (expr + '\n')

        self.appendICode(writeStr)
        rowNum += 1

        # Set Temp variables' flag to False after each Assignment
        # Release temp variables
        Temp.setFlag(False)
        pass


    # Enter a parse tree produced by DevilsCodeParser#math_expr.
    def enterMath_expr(self, ctx):
        self.tokens.append(str(ctx.getChild(0)))
        pass

    def symbolTableChecker(self):
        literalNames = [ "main ", "(", ")", "{", "}",
                     ";", "print ", "=", "+", "-", "*", "/",
                     "while ", "if ", "else", "true", "false", "int ", "bool " ]
        self.tokens = [ x for x in self.tokens if not re.match('[\[\]]', x) and x not in literalNames]
        for id in self.tokens:
            if id not in self.symbol_table:
                print("ERROR: " + id + " not declared")
                os.remove(self.file_name + '.ic')
                quit()

    # Exit a parse tree produced by DevilsCodeParser#math_expr.
    def exitMath_expr(self, ctx):
        # Declare the global row number counter
        global rowNum

        # Declare two global temp variables
        global Temp

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
            Temp.setFlag(True)
            writeStr += (Temp.getName() + ' ')
        # Else lOperand is IDENT or Number
        else:
            writeStr += (lOperand + ' ')

        # If rOperand is Term with op
        if ('+' in rOperand or '-' in rOperand or '*' in rOperand or '/' in rOperand ):
            # If TOP is occupied, it must be represented by TOP
            Temp.setFlag(True)
            writeStr += (Temp.getName() + '\n')
        # Else lOperand is IDENT or Number
        else:
            writeStr += (rOperand + '\n')

        self.appendICode(writeStr)
        rowNum += 1
        if op:
            Temp.setFlag(True)
        pass


    # Enter a parse tree produced by DevilsCodeParser#math_term.
    def enterMath_term(self, ctx):
        pass

    # Exit a parse tree produced by DevilsCodeParser#math_term.
    def exitMath_term(self, ctx):
        # Declare global row number counter
        global rowNum
        # Declare two global Temp Var
        global Temp

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
            Temp.setFlag(True)
            writeStr += (Temp.getName() + ' ')
        # If left operand is IDENT or Number
        else:
            writeStr += (lOperand + ' ')
            
        # If right operand is Term or Factor->(expr)
        if ('*' in rOperand or '/' in rOperand or '(' in rOperand ):
            Temp.setFlag(True)
            writeStr += (Temp.getName() + '\n')
        else:
            writeStr += (rOperand + '\n')
        self.appendICode(writeStr)
        rowNum += 1

        # Set Flag of Temp Variable TOP
        # It must be used
        if op:
            Temp.setFlag(True)

        pass


    # Enter a parse tree produced by DevilsCodeParser#math_factor.
    def enterMath_factor(self, ctx):
        pass

    # Exit a parse tree produced by DevilsCodeParser#math_factor.
    def exitMath_factor(self, ctx):
        # Global Row Number
        global rowNum
        # Global Temp Variables
        global Temp
        
        # Set or Get Temp Var
        Temp = tVar.GetTempVar()

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

        writeStr = str(rowNum) + ' ' + 'LOOP' + '\n'
        loopRowStack.push(rowNum)
        self.appendICode(writeStr)
        rowNum += 1

        pass

    # Exit a parse tree produced by DevilsCodeParser#while_stmt.
    def exitWhile_stmt(self, ctx):
        # Declare the global row number counter
        global rowNum
        # Declare the global loop row stack
        global loopRowStack
        global rN
        rN = gStack.GetRNStack()
        writeStr = str(rowNum) + ' ' + 'GOTO' + ' ' + str(loopRowStack.pop()) + '\n'       
        self.appendICode(writeStr)
        rowNum += 1
        # END for Loop
        writeStr = str(rowNum) + ' ' + 'END' + '\n'       
        self.appendICode(writeStr)

        # Insert in Line rN
        self.insertGOTO(rowNum)

        rowNum += 1
        pass

    # Enter a parse tree produced by DevilsCodeParser#if_stmt.
    def enterIf_stmt(self, ctx):
        # Declare the global row number counter
        global rowNum
        # Global CondFlag, IfFlag and ElseFlag
        global condFlag
        global ifFlag
        global elseFlag

        condFlag = True
        ifFlag = True

        # If 'else' exists, it should be the 6th child
        elseKey = ctx.getChild(5)
        if elseKey:
            elseFlag = True
        else:
            elseFlag = False

        writeStr = str(rowNum) + ' ' + 'IF' + '\n'       
        self.appendICode(writeStr)

        rowNum += 1
        pass

    # Exit a parse tree produced by DevilsCodeParser#if_stmt.
    def exitIf_stmt(self, ctx):
        # Declare the global row number counter
        global rowNum
        # Global CondFlag, IfFlag and ElseFlag
        global condFlag
        global ifFlag
        global elseFlag

        rN = gStack.GetRNStack()

        elseKey = ctx.getChild(5)
        # If no ELSE stmt, Complete GOTO Line labeled by rN
        if not elseKey:
            self.insertGOTO(rowNum - 1)

        condFlag = False
        ifFlag = False
        elseFlag = False
        pass

    # Enter a parse tree produced by DevilsCodeParser#else_stmt.
    def enterElse_stmt(self, ctx):
        pass

    # Exit a parse tree produced by DevilsCodeParser#else_stmt.
    def exitElse_stmt(self, ctx):
        pass

     # Enter a parse tree produced by DevilsCodeParser#cpr_expr.
    def enterCpr_expr(self, ctx):
        # Declare the global row number counter
        global rowNum

        cmpSymbol = ctx.getChild(1).getText()
        cmpLeft = ctx.getChild(0).getText()
        cmpRight = ctx.getChild(2).getText()

        if (cmpSymbol == '<'):
            writeStr = str(rowNum) + ' ' + 'SML' + ' '
        elif (cmpSymbol == '<='):
            writeStr = str(rowNum) + ' ' + 'SMLEQL' + ' '
        elif (cmpSymbol == '>'):
            writeStr = str(rowNum) + ' ' + 'GTR' + ' '
        elif (cmpSymbol == '>='):
            writeStr = str(rowNum) + ' ' + 'GTREQL' + ' '
        else:
            writeStr = str(rowNum) + ' ' + 'EQL' + ' '
        writeStr += cmpLeft + ' ' + cmpRight + '\n'
        self.appendICode(writeStr)
        rowNum += 1
        pass

    # Exit a parse tree produced by DevilsCodeParser#cpr_expr.
    def exitCpr_expr(self, ctx):
        # Global Row Num
        global rowNum
        # Global rN for writing END rowNum back
        global rN
        
        rN = gStack.GetRNStack()
        rN.push(rowNum)

        rowNum += 1
        pass


    # Enter a parse tree produced by DevilsCodeParser#cpr_term.
    def enterCpr_term(self, ctx):
        self.tokens.append(str(ctx.getChild(0)))
        pass

    # Exit a parse tree produced by DevilsCodeParser#cpr_term.
    def exitCpr_term(self, ctx):
        pass
