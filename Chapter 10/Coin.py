import random

#class Coin simulates a coin being tossed
#note that the name of the class has a capital letter for the first
#letter, this is a standard programming convention and should be followed

class Coin:
    #a class should begin with the __init__() method
    #this method executes first, as an initialization of the class
    #the (self) parameter is a generally accepted naming convention
    #for the parameter within a class, and is required
    
    #-------------------------Data Attributes-------------------#
    #initialize the data attribute with 'heads' to indicate
    #the coin beings in a head's up position
    
    def __init__(self):
        self.__sideup='Heads'
        
    #---------------------------Instance Methods---------------#
    #the toss method generates a random number in a range of 0 through 1
    #if the number is 0, sideup is assigned 'Heads'
    #otherwise sideup is assigned 'Tails'
    def toss(self):
        if random.randint(0,1)==0:
            self.__sideup='Heads'
        else:
            self.__sideup='Tails'
    
    #get sideup method returns the current state of the oint
    #or the side that is facing up
    
    def get_sideup(self):
        return self.__sideup