## Introduction
Semester project for SER 502

## Development Environment
Systems: Ubuntu 16.04 LTS

Tools to build compiler: Python 3.5.2 and ANTLR 4.7

Tools to build runtime: Jave SE 1.6

## Installation Instruction
Steps:

1. Install Python 3.5.2 and Jave SE Runtime 1.6 or above

𝐏𝐲𝐭𝐡𝐨𝐧 𝟑.𝟓.𝟐 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐚𝐭𝐢𝐨𝐧 𝐒𝐭𝐞𝐩𝐬:

$ sudo apt-get install build-essential checkinstall

$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

$ cd /usr/src

$ wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz

$ sudo tar xzf Python-3.5.2.tgz

$ cd Python-3.5.2

$ sudo ./configure

$ sudo make altinstall

These tools would be mandatorily needed for the environment to function.

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
