class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 28
print(obj._protectedVar)




class Private:
    def __init__(self):
        self.__privateVar = 2

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self,private):
        self.__privateVar = private

obj = Private()
obj.getPrivate()
obj.setPrivate(99)
obj.getPrivate()
