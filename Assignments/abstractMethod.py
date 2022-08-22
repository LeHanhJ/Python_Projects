from abc import ABC, abstractmethod

class Water(ABC): 
    def ouncesTotal(self, amount):
        print("The total amount of water you have in your bottle is " + amount +" ounces today.")
    @abstractmethod
    def ouncesDrank(self,amount):
        pass

class waterDrank(Water):
    def ouncesDrank(self, amount):
        print("You've consumed {} ounces of water so far.".format(amount))

obj = waterDrank()
obj.ouncesTotal("48")
obj.ouncesDrank("32")
