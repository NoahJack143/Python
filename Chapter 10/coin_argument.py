#Program 10-15
#Import coin
import Coin as c

def main():
    #main receives no arguments
    #it creates an object using the Coin class in Coin.py
    #it outputs the currente state of the object using the get_sideup method
    #then passes the object to flip(coin_obj) to flip the coin
    #finally it outputs the new state of the object using the get_sideup method
    
    #Create an object for the coin
    Coin = c.Coin()
    
    #Shows the side of the coin that is facing up
    print(f'Your coin is currently showing: {Coin.get_sideup()}')
    
    #Call for flip(Coin) to flip the coin
    flip(Coin)
    
def flip(Coin):
    #flip receives coin_obj as a reference to a my_coin object
    #it uses the toss() method in the Coin class
    #and prints a string to indicate the coin has bee tossed
    
    #Toss the coin and print a message to show this
    Coin.toss();print('\nTossing your coin...\n')
    
    #Show the side of the coin that is facing up now
    print(f'Your coin is now showing: {Coin.get_sideup()}')
    
    