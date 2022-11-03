import random

def card_dealer_main(): #Program 9-1
    #card dealer main accpets no arguments
    #it calls create_deck to generate a deck of cards
    #and takes input from the user for the number of cards to deal
    #it then calls deal_cards to deal the number of cards to the user
    
    #Create the deck by calling create_deck
    deck = create_deck()
    
    #Ask the user how many cards they would like to be dealt
    deal = int(input('How many cards do you wish to be dealt? '))
    
    #Call for deal_cards(deck, number)
    hand = deal_cards(deck, deal)
    
    #For every single key in the user's hand, print out the card and it's value
    print('\nHere is your hand:\n')
    for card in hand:
        print(card)
    
    #For every single key in the dictionary, add it to the new total
    total = 0
    for card in hand:
        total += hand[card]
        
    print(f'\nYour hand has the value {total}')
def create_deck():
    #create deck accepts no arguments
    #it generates a dictionary with the name of the card as the key
    #and the point vaue of the card as the value
    #and returns the dictionary of cards
    
    deck = {'Ace of Spades' : 1, '2 of Spades' : 2, '3 of Spades' : 3,
        '4 of Spades' : 4, '5 of Spades' : 5, '6 of Spades' : 6,
        '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9,
        '10 of Spades' : 10, 'Jack of Spades' : 10, 'Queen of Spades' : 10,
        'King of Spades' : 10,
        
        'Ace of Hearts' : 1, '2 of Hearts' : 2, '3 of Hearts' : 3,
        '4 of Hearts' : 4, '5 of Hearts' : 5, '6 of Hearts' : 6,
        '7 of Hearts' : 7, '8 of Hearts' : 8, '9 of Hearts' : 9,
        '10 of Hearts' : 10, 'Jack of Hearts' : 10, 'Queen of Hearts' : 10,
        'King of Hearts' : 10,
        
        'Ace of Clubs' : 1, '2 of Clubs' : 2, '3 of Clubs' : 3,
        '4 of Clubs' : 4, '5 of Clubs' : 5, '6 of Clubs' : 6,
        '7 of Clubs' : 7, '8 of Clubs' : 8, '9 of Clubs' : 9,
        '10 of Clubs' : 10, 'Jack of Clubs' : 10, 'Queen of Clubs' : 10,
        'King of Clubs' : 10,
        
        'Ace of Diamonds' : 1, '2 of Diamonds' : 2, '3 of Diamonds' : 3,
        '4 of Diamonds' : 4, '5 of Diamonds' : 5, '6 of Diamonds' : 6,
        '7 of Diamonds' : 7, '8 of Diamonds' : 8, '9 of Diamonds' : 9,
        '10 of Diamonds' : 10, 'Jack of Diamonds' : 10, 'Queen of Diamonds' : 10,
        'King of Diamonds' : 10}
    
    return deck
    
def deal_cards(deck, number):
    #deal cards accepts deck as a dictionary and number as an integer
    #it verifies number isn't greater than the eck size
    #if it is, it sets the number to the legth of the dec size to not
    #exceed the maximum index
    #it randomly selects and removes akey/value from the deck
    #it prints the card and calculates the value of the hand
    #after all cards have been dealt, it outputs the total value of the hand
    
    #Create a new dictionary for the user's hand
    user_hand = {}
    
    #Check to see if the number is greater than the deck size
    if number > len(deck):
        number = len(deck)
        
    #Loop for the total amount of the times the user wants to
    for i in range(number):

        #Find a card and it's number from the deck
        card = random.choice(list(deck))
        value = deck.pop(card)
        
        #Move the card and it's number to the user's hand
        user_hand[card] = value
    
    #Return the user's hand
    return user_hand