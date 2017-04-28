__var1 = None
__var2 = None

def GetTempVar_1():
    global __var1
    if not __var1:
        __var1 = TempVar('TOP')
    return __var1

def GetTempVar_2():
    global __var2
    if not __var2:
        __var2 = TempVar('TOP1')
    return __var2

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
