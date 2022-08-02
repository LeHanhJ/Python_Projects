class Protected: #creates class Protected
    def __init__(self): #defines function within itself
        self._protectedVar = 0 #assigns 0 to the protectedVar in function Protected()

obj = Protected() #Sets var obj as Protected()
obj._protectedVar = 28 #assigns obj the number 28 as the variable
print(obj._protectedVar) #prints assigned number from previous line




class Private: #create class Private
    def __init__(self): #defines function within itself
        self.__privateVar = 2 #sets __privateVar to be 2 initially

    def getPrivate(self): #defines getPrivate function
        print(self.__privateVar) #prints __privateVar, which was previously defined as 2

    def setPrivate(self,private): #defines setPrivate function, adds "private" to make sure we call upon it when we change the variable
        self.__privateVar = private #uses "private" as assigned in input setPrivate() function

obj = Private() #calls Private() function, which is initially 2
obj.getPrivate() #prints out __privateVar variable, which as said before is 2
obj.setPrivate(99) #sets setPrivate() to 99 by giving "private" argument
obj.getPrivate() #updates getPrivate function with update
