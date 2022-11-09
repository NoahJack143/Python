#Imports
import random

#Program
def blackjack(): #Exercise 9
    
    #Create the deck of cards
    deck = {'Ace of Spades' : 11, '2 of Spades' : 2, '3 of Spades' : 3,
        '4 of Spades' : 4, '5 of Spades' : 5, '6 of Spades' : 6,
        '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9,
        '10 of Spades' : 10, 'Jack of Spades' : 10, 'Queen of Spades' : 10,
        'King of Spades' : 10,
        
        'Ace of Hearts' : 11, '2 of Hearts' : 2, '3 of Hearts' : 3,
        '4 of Hearts' : 4, '5 of Hearts' : 5, '6 of Hearts' : 6,
        '7 of Hearts' : 7, '8 of Hearts' : 8, '9 of Hearts' : 9,
        '10 of Hearts' : 10, 'Jack of Hearts' : 10, 'Queen of Hearts' : 10,
        'King of Hearts' : 10,
        
        'Ace of Clubs' : 11, '2 of Clubs' : 2, '3 of Clubs' : 3,
        '4 of Clubs' : 4, '5 of Clubs' : 5, '6 of Clubs' : 6,
        '7 of Clubs' : 7, '8 of Clubs' : 8, '9 of Clubs' : 9,
        '10 of Clubs' : 10, 'Jack of Clubs' : 10, 'Queen of Clubs' : 10,
        'King of Clubs' : 10,
        
        'Ace of Diamonds' : 11, '2 of Diamonds' : 2, '3 of Diamonds' : 3,
        '4 of Diamonds' : 4, '5 of Diamonds' : 5, '6 of Diamonds' : 6,
        '7 of Diamonds' : 7, '8 of Diamonds' : 8, '9 of Diamonds' : 9,
        '10 of Diamonds' : 10, 'Jack of Diamonds' : 10, 'Queen of Diamonds' : 10,
        'King of Diamonds' : 10}
    
    player1_pts = 0
    player2_pts = 0
    player1_deck = []
    player2_deck = []
    total_turns = 1
    
    for turn in range(1,52): #CHANGE THE FIRST NUMBER TO 0 AND CHANGE THE RESPECTIVE NUMBERS LATER
        
        card = random.choice(list(deck))
        value = deck.pop(card)
        
        if (turn%2) == 1:
            if card[:3] == 'Ace' and player1_pts > 10:
                player1_deck.append(card)
                player1_pts+=1
            else:
                player1_deck.append(card)
                player1_pts+=value
        else:
            if card[:3] == 'Ace' and player2_pts > 10:
                player2_deck.append(card)
                player2_pts+=1
            else:
                player2_deck.append(card)
                player2_pts+=value
                
                
        if (turn%2) == 0:
            if player1_pts > 21 and player2_pts > 21:
                winner = 0
                victor(player1_pts, player2_pts, player1_deck, player2_deck, winner, total_turns)
                total_turns = 0
            elif player1_pts > 21:
                winner = 1
                victor(player1_pts, player2_pts, player1_deck, player2_deck, winner, total_turns)
                total_turns = 0
            elif player2_pts > 21:
                winner = 2
                victor(player1_pts, player2_pts, player1_deck, player2_deck, winner, total_turns)
                total_turns = 0
            if total_turns == 0:
                player1_deck = []
                player2_deck = []
                player1_pts = 0
                player2_pts = 0
                print('\n#\n')
        total_turns += 1
        
    if player1_pts == player2_pts:
        msg = 'The round was a draw!'
    elif player1_pts > player2_pts:
        msg = 'Player 2 won the round!'
    elif player2_pts > player1_pts:
        msg = 'Player 1 won the round!'
        
    print(f'{msg}'+
          "\nHere are the players' cards"+
          f"\nPlayer 1's points: {player1_pts}"+
          f"\nPlayer 2's points: {player2_pts}"+
          '\n------------------------------')
    for num in range(len(player1_deck)):
        try:
            print(f'{player1_deck[num]}',end='')
            print(f'\t\t{player2_deck[num]}')
        except:
            print()
def victor(player1_pts, player2_pts, player1_deck, player2_deck, winner, total_turns):
    if winner == 0: #Draw
        msg = 'The round was a draw!'
    elif winner == 1: #1 won
        msg = 'Player 2 won the round!'
    else: #2 won
        msg = 'Player 1 won the round!'
    print(f'{msg}'+
          "\nHere are the players' cards"+
          f"\nPlayer 1's points: {player1_pts}"+
          f"\nPlayer 2's points: {player2_pts}"+
          '\n------------------------------')
    for num in range(int(total_turns-(total_turns/2))):
        print(f'{player1_deck[num]}\t\t{player2_deck[num]}')
