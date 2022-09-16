import random

def die_roll():
    #dice roll accepts no arguments
    #it rolls a die
    #it returns the roll value
    
    die = random.randint(1,6) #generate a random number from 1 - 6
    
    return die #return the random die roll
