class animal: #created a class of animal, with number of legs, location, and environment as attributes
    number_of_legs = 4
    location = 'Unknown' #what country is this mosts commonly seen?
    environment = 'Unknown' #what kind of environment does this animal prefer?
    backbone = "Vertebrate" #is the animal a vertebrate or invertebrate?

class canine(animal): #created a class of canine, which inherits attributes from the animal class.
    breed = ' ' #for many different kind of dog breeds
    domesticated = True #is the canine able to be domesticated?
    
class arthropod(animal): #created a class aarthropod, which inherits attributes from the animal class.
    mode_of_transportation: ' ' #many arthropods can fly or have many legs
    body_segments: 2 #arthropods can have one to many body segments




if __name__ == "__main__":
    
