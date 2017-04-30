# Written by Mingfei Yang
# Version 1.0.0
# Date: April 28, 2017
# Purpose: Stack Structure for Intermediate Code Generation

__loopStack = None
__rnStack = None
__condStack = None

def GetLoopStack():
    global __loopStack
    if not __loopStack:
        __loopStack = StackEx()
    return __loopStack

def GetRNStack():
    global __rnStack
    if not __rnStack:
        __rnStack = StackEx()
    return __rnStack

def GetCondStack():
    global __condStack
    if not __condStack:
        __condStack = StackEx()
    return __condStack


class StackEx(object):
    def __init__(self):
        self.__stackList = []

    def isEmpty(self):
        if self.__stackList == []:
            return True
        else:
            return False

    def stackSize(self):
        return len(self.__stackList)
        
    def push(self, input):
        self.__stackList.append(input)
    
    
    def pop(self):
        if self.__stackList:
            return self.__stackList.pop()
        return None
