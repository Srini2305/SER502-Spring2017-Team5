# Written by Mingfei Yang
# Version 1.0.0
# Date: April 28, 2017
# Purpose: Track the temporary values in the arithmetic operations.
__var = None

def GetTempVar():
    global __var
    if not __var:
        __var = TempVar('TOP')
    return __var

class TempVar(object):
    def __init__(self, name):
        self.__value = 0
        self.__flag = False
        self.__name = name
    
    def setValue(self, iValue):
        self.__value = iValue
    
    def setFlag(self, bFlag):
        self.__flag = bFlag
    
    def getValue(self):
        return self.__value

    def getFlag(self):
        return self.__flag

    def getName(self):
        return self.__name
