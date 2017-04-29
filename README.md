# SER502-Spring2017-Team5
Semester project for SER 502


Install steps:

1. Extract devils.tar.gz to home directory

2. Install the compile script with command:
   "sudo install DVLC /usr/local/bin/DVLC"

3. Get the intermediate code with command:
   "DVLC <FILE_NAME>"

Bug information:
1. Go to antlr4 dirctory, usually "~/.local/lib/python3.5/site-packages/antlr4"

2. Access ParserRuleContext.py

3. In line 116, modify the if statment "if len(self.children)>=i" to "if len(self.children)>i" 
