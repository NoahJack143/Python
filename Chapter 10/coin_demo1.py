#Program 10-2 - coin_demo1.py
import Coin

def main():
    #coin main accepts no arguments
    #it uses the Coin class to create an object
    
    #create an object from the Coin class
    my_coin = Coin.Coin()
    
    #display the side f the coin that is facin up
    print('\nThis side is up: ', my_coin.get_sideup())
    
    #toss the coin
    print('\nTossing the coin...\n')
    my_coin.toss()
    
    #display the side of the coin that is facing up
    print('This side is up: ', my_coin.get_sideup())

#Call the main function to flip the coin
main()