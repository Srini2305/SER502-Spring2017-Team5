## Instruction
Semester project for SER 502

## Development Environment
Systems: Linux

Tools to build compiler: Python 3.5.2 and ANTLR 4.7

Tools to build runtime: Jave 1.6

## Installation Instruction

Steps:

1. Install Python 3.5.2 and Jave RE

2. Install ANTLR 4.7 with command "pip install antlr4-python3-runtime"

3. Extract devils.tar.gz to home directory

4. Install the compile script with command:
   "sudo install DVLC /usr/local/bin/DVLC"

Bug information:
1. Go to antlr4 dirctory, usually "~/.local/lib/python3.5/site-packages/antlr4"

2. Access ParserRuleContext.py

3. In line 116, modify the if-statment "if len(self.children)>=i" to "if len(self.children)>i" 

## How to Use
1. Get the intermediate code with command: "DVLC <FILE_NAME>"


## YouTube Link
