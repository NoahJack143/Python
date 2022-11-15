#Program 10-6: coin_demo4.py
#import the coin module
import Coin

def main(): #Program 10-6
    #main accepts no arguments#it creates an object y_coin using the Coin class in Coin.py
    #it usese the get_sideup() method in the Coin class to display the starting stae
    #it loops 1- times, tossing the coin with the toss() method
    # and displaying the side again with the get_sideup() method
    
    #Assign the class to a variable
    my_coin = Coin.Coin()
    
    #Present the current side of the coin
    print('This side is up: ', my_coin.get_sideup())
    
    #Print a message saying that you are flipping the coin ten times
    print('Tossing the coint ten times...\n')
    
    #Loop 10 times, flip the coin, and then present the side up
    for i in range(1,10):
        my_coin.toss()
        print('Toss ',i,': ', my_coin.get_sideup(), sep='')
        
main()