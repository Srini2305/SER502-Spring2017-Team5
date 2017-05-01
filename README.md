## Introduction
Semester project for SER 502

## Development Environment
Systems: Ubuntu 16.04 LTS

Tools to build compiler: Python 3.5.2 and ANTLR 4.7

Tools to build runtime: Jave SE 1.6

## Installation Instruction
Steps:

1. Install Python 3.5.2 and Jave SE Runtime 1.6 or above

2. Extract devils.tar.gz to home directory

3. Install the scipts with command: "sh installScript"

## How to Use
1. Get the intermediate code with command: "dvlc <FILE_NAME>"

2. Run the intermediate code with command: "dvlc-run <FILE_NAME>"

## Bug informaiton:
There is a bug in the original ANTLR library, we fixed it and sepearted the custom version into /src/compiler/

In "ParserRuleContext.py" line 116, the if-statment "if len(self.children) >= i" should be "if len(self.children) > i" 

## YouTube Link
https://youtu.be/O1cP3yY0Z6w
