__loopStack = None
__tempStack = None

def GetLoopStack():
    global __loopStack
    if not __loopStack:
        __loopStack = StackEx()
    return __loopStack

def GetTempStack():
    global __tempStack
    if not __tempStack:
        __tempStack = StackEx()
    return __tempStack


class StackEx(object):
    def __init__(self):
        self.__stackList = []
        
        
    def push(self, input):
        self.__stackList.append(input)
    
    
    def pop(self):
        if self.__stackList:
            return self.__stackList.pop()
        return None
