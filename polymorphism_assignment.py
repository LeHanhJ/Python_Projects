#Parent class Instrument
class instrument:
    name = " "
    percussion = False
    family = " "

    def instrument_info(self):
        self.name = input("Enter your instrument: ")
        self.percussion = input("Percussion - True or False? ")
        self.family = input("Instrument family: ")
        print(self.name + " is in the " + self.family + " family.")

#child class guitar
class guitar(instrument):
    brand = " "
    acoustic = True

    def instrument_info(self):
        self.name = input("Enter your instrument: ")
        self.family = input("Instrument family: ")
        self.brand = input("Brand of guitar: ")
        self.acoustic = input("Acoustic, True or False: ")
        print(self.name + " is in the " + self.family + " family and is of the " + self.brand + " brand.")
    
#child class brass
class brass(instrument):
    valved = True
    size = " "

    def instrument_info(self):
        self.name = input("Enter your instrument: ")
        self.family = input("Instrument family: ")
        self.valved = input("Valved, True or False:")
        self.size = input("Size, Small, Medium, Large: ")
        print(self.name + " is in the " + self.family + " family.")
    
#child class woodwind
class woodwind(instrument):
    number_of_reeds = 1
    material = " "

    def instrument_info(self):
        self.name = input("Enter your instrument: ")
        self.family = input("Instrument family: ")
        self.number_of_reeds = input("Number of Reeds:")
        self.material = input("Material: ")
        print(self.name + " has " + str(self.number_of_reeds) + " reeds. It is made out of " + self.material)


guitar = guitar()
guitar.instrument_info()


trumpet = brass()
trumpet.instrument_info()

saxophone = woodwind()
saxophone.instrument_info()
