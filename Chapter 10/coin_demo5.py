#Program coin_demo5.py
#import Coin.py
import Coin

def main():
    #Create three objects from the coinc lass
    c1= Coin.Coin()
    c2= Coin.Coin()
    c3= Coin.Coin()
    
    #Present the coins
    print('Here are the current state of the three coins:')
    print(f'Coin 1 is: {c1.get_sideup()}')
    print(f'Coin 2 is: {c2.get_sideup()}')
    print(f'Coin 3 is: {c3.get_sideup()}')
    
    #Toss all of the coins
    c1.toss()
    c2.toss()
    c3.toss()
    
    #Present the coins again
    print('Here are the new states of the three coins:')
    print(f'Coin 1 is: {c1.get_sideup()}')
    print(f'Coin 2 is: {c2.get_sideup()}')
    print(f'Coin 3 is: {c3.get_sideup()}')