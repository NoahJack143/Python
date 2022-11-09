#MAIN MENU FUNCTION
def m(): #MAIN MENU
    #m accepts no arguments
    #it will call other functions
    
    print('\n' * 100)
    print('MAIN MENU\n---------------\n'+
          '3) File Encryption\n3.1) '+
          'File Creating (For Exercise 9-3)\n' +
          '3.2) File Decryption (For Exercise 9-3)\n4) '+
          'Unique Words\n7) '+
          'World Series Winners\n9) '+
          'Blackjack Simulation\n '+
          '10) File Encryption V.1.1\n'+
          '11) File Decryption V.1.1\n'+
          '---------------')
    
    #Prompt the user for an main function to call with validation
    while True:
        try:
            ui = float(input('Which main function would you like to call? '))
        except:
            print('\nEnter a number...\n')
        else:
            try:
    
                #Check to see if the user input is any of the option
                if ui == 3:
                    function = encrypting_code
                elif ui == 3.1:
                    function = test_file
                elif ui == 3.2:
                    function = decrypting_code
                elif ui == 4:
                    function = unique_words
                elif ui == 7:
                    function = world_series_winners
                elif ui == 9:
                    function = blackjack
                elif ui == 10:
                    function = encrypting_code2
                elif ui == 11:
                    function = decrypting_code2
                else:
                    f
            except:
                print('\nPlease choose an option from the table.\n')
            else:
                print('\n'*100)
                function()
                break
    

#====Imports=====#

import random

#==========#

def encrypting_code(): #Exercise 3
    #encrypting_code accepts no arguments
    #it will take contents from a file, convert them to
    #the symbol representing each character from the contents
    #and then move those contents into another file
    
    #Create a dictionary for uppercase letter, numbers, and symbols
    code_upper = {'A':'B','B':'C','C':'D','D':'E','E':'F','F':'G','G':'H','H':'I','I':'J','J':'K','K':'L','L':'M',
            'M':'N','N':'O','O':'P','P':'Q','Q':'R','R':'S','S':'T','T':'U','U':'V','V':'W','W':'X','X':'Y','Y':'Z','Z':'A',
                  '1':'2','2':'3','3':'4','4':'5','5':'6','6':'7','7':'8','8':'9','9':'0','0':'1',
                  '!':'@','@':'#','#':'$','$':'%','%':'^','^':'&','&':'*','*':'(','(':')',')':'!',
                  '`':'~','~':"`",',':'<','<':',','.':">",">":',','/':'?','?':'/',';':":",":":';',"'":'"','"':"'",
                  '[':"{","{":'[',']':"}","}":']','-':"_","_":'-','=':"+","+":'='
            }
    code={} #Create a dictionary to add in lowercase letters
    for key in code_upper: #Have a for loop to add everything to a single dictionary
        value = code_upper[key]
        code[key] = value
        if key.isalnum():
            code[key.lower()] = value.lower()
    
    #Prompt the user for a file to be opened. Validation will be included for this
    while True:
        file = input('Which file would you like to open? ')
        try:
            infile = open(file,'r')
        except:
            print('\nPlease open a file that exists.\n')
        else:
            break
    
    #Create a string for the contens from within the file
    contents = ''
    
    #Take everything from within the file and concatenate it to contents, then close the file and open the encryption file
    for line in infile:
        contents+=line
    infile.close()
    infile = open('Encrypted_Version.txt','w')

    #Create a new string for the encrypted contents
    encrypted_contents = ''
    next_char = 0

    #Have a for loop and move the newly encrypted contentes to the string, encrypted_contents
    for char in range(len(contents)):
        if next_char != 1:
            old_value = contents[char]
            new_value = code.get(old_value,'00')
            if new_value == '00':
                if old_value == ' ': #This will run if the old_value is a ' '
                    encrypted_contents+=old_value
                else:
                    try:
                        if contents[char+1] == 'n': #This will run if the '\' is with an 'n'
                            encrypted_contents+='\n'
                            next_char = 1 #Skip the letter 'n' in order to not have extra code
                        else:
                            encrypted_contents+=old_value #This will run if the '\' is without an 'n'
                    except:
                        encrypted_contents+=old_value #This part will run if the '\' is at the end of contents
            else:
                encrypted_contents+=new_value #This will add the new value to encrypted_contents if the old_value isn't '\' or ' '
        else:
            next_char = 0
        
    #Move the encrypted content into the file, Encrypted_Version, and close the file
    infile.write(encrypted_contents)
    infile.close()
    
    #Tell the user that the contents have been put into the file
    print(f'\nThe contents from the file, {file}, have been encrypted and put into the file, Encrypted_Version')
    
def test_file(): #Creates a file for encrypting_code() #For Exercise 3
    #test file accepts no arguments
    #it will let the user create a file
    
    #Prompt the user for the name of the file
    file = input('What would you like to call the file? ')
    
    #Rewrite or create a file
    infile = open(file,'w')
    
    #Prompt the user what they would like to be inside the file
    contents = input('What message would you like to put in the file? ')
    
    #Write the contents and then close the file
    infile.write(contents)
    infile.close()
    
def decrypting_code(): #For Exercise 3
    #decrypting code accepts no arguments
    #it will read the specific file created by
    #encrypting_code(), and decrypt the contents
    #from within the file
    
    #Create the same dictionary from the main function
    code_upper = {'A':'B','B':'C','C':'D','D':'E','E':'F','F':'G','G':'H','H':'I','I':'J','J':'K','K':'L','L':'M',
            'M':'N','N':'O','O':'P','P':'Q','Q':'R','R':'S','S':'T','T':'U','U':'V','V':'W','W':'X','X':'Y','Y':'Z','Z':'A',
                  '1':'2','2':'3','3':'4','4':'5','5':'6','6':'7','7':'8','8':'9','9':'0','0':'1',
                  '!':'@','@':'#','#':'$','$':'%','%':'^','^':'&','&':'*','*':'(','(':')',')':'!',
                  '`':'~','~':"`",',':'<','<':',','.':">",">":',','/':'?','?':'/',';':":",":":';',"'":'"','"':"'",
                  '[':"{","{":'[',']':"}","}":']','-':"_","_":'-','=':"+","+":'='
            }
    code={} #Create a dictionary to add in lowercase letters
    for key in code_upper: #Have a for loop to add everything to a single dictionary
        value = code_upper[key]
        code[value] = key
        if key.isalnum() and not key.isdigit():
            code[value.lower()] = key.lower()
    
    #Open the file from the ecrypting_code() function
    infile = open('Encrypted_Version.txt','r')
    
    #Create a string for the contens from within the file
    contents = ''
    
    #Take everything from within the file and concatenate it to contents, then close the file
    for line in infile:
        contents+=line
    infile.close()
    
    #Create a new string for the decrypted contents
    decrypted_contents = ''
    next_char = 0

    #Have a for loop and move the decrypted contentes to the string, decrypted_contents
    for char in range(len(contents)):
        if next_char != 1:
            old_value = contents[char]
            new_value = code.get(old_value,'00')
            if new_value == '00':
                if old_value == ' ': #This will run if the old_value is a ' '
                    decrypted_contents+=old_value
                else:
                    try:
                        if contents[char+1] == 'n': #This will run if the '\' is with an 'n'
                            decrypted_contents+='\n'
                            next_char = 1 #Skip the letter 'n' in order to not have extra code
                        else:
                            decrypted_contents+=old_value #This will run if the '\' is without an 'n'
                    except:
                        decrypted_contents+=old_value #This part will run if the '\' is at the end of contents
            else:
                decrypted_contents+=new_value #This will add the new value to decrypted_contents if the old_value isn't '\' or ' '
        else:
            next_char = 0
    
    #Print the decrypted_contents for the user
    print('Here is the decrypted message.\n')
    print(decrypted_contents)

#================================================================================#

def unique_words(): #Exercise 4
    #unique words accepts no arguments
    #it will read contents from a file, put them
    #into a set, and then find only the unique
    #words, and then tell the user
    
    #Prompt the user for a file to be opened. Validation will be included for this
    while True:
        file = input('Which file would you like to open? (Included the file extension if needed) ')
        try:
            infile = open(file,'r')
        except:
            print('\nPlease open a file that exists.\n')
        else:
            break
    
    #Create a variable standing for a string, create a for loop,
    #and put everything from within the file into the string, and close the file
    contents = ''
    for line in infile:
        contents+=line
    infile.close()
    
    #split the contents in contents
    contents = contents.split()
    
    new_contents = []
    for word in contents:
        if word[(len(word)-1):] == ',' or word[(len(word)-1):] == '.' or word[(len(word)-1):] == ':':
            new_contents.append(word[:(len(word)-1)].upper())
        else:
            new_contents.append(word.upper())
    
    #put the contents into a set
    set_contents = set(new_contents)
    
    #put the contents back into a list
    contents = list(set_contents)
    
    #Print the contents for the user
    print(f'\nHere are all the unique words from the file, {file}.\n')
    print(contents)
    
#================================================================================#
    
def world_series_winners(): #Exercise 7
    #world series winners accepts no arguments
    #it will read contents from the file, WorldSeries.txt
    #put the contents into two dictionaries, and prompt the user
    #for a year, and then say which team won the world seires
    #that year AND how many times that team has won the world series.
    
    #open the file
    infile = open('WorldSeries.txt', 'r')
    
    #Create two dictionaries with names tied to their purpose, and create a list
    times_won = {}
    winner_per_year = {}
    teams = []
    
    #Create an accumulator, and move the contents into team names into
    #the dictionary as values with the key being the year. Also move the names
    #of the teams into the list, teams
    year = 1903
    c=1
    for line in infile:
        if line[:3] == 'Wor':
            u = 'skip'
        else:
            winner_per_year[str(year)] = line.rstrip('\n')
        year+=1
        teams.append(line.rstrip('\n'))
    
    #Create a new set using the list
    teams_set = set(teams)
    
    #Create a for loop in order to see how many times each team
    #has won the world series, and move the team name and their win_count
    #into the dictionary, times_won
    for name in teams_set:
        win_count = teams.count(name)
        times_won[name] = win_count
    
    #Prompt the uesr for a year between 1903 2008, include validation
    while True:
        year = input('Choose a year betwen 1903 and 2008: ')
        try:
            if int(year) >= 1903 and int(year) <= 2008:
                break
            else:
                print('\nPlease choose year between 1903 and 2008.\n')
        except:
            print('\nPlease enter numbers only.\n')
    
    #Find which team won in the chosen year, and if a team actually won that year
    #output the team AND tell how many times that team has won, if not, then
    #tell the user that no one won that year
    team = teams[(int(year)-1903)]
    win_count = times_won[team]
    if int(year) == 1904 or int(year) == 1994:
        print(f'\nThe World Series was not played in {year}.')
    else:
        print(f'\nThe team that won in {year} was {team}.')
        print(f'The {team} won {win_count} time(s).')

#================================================================================#
        
def blackjack():
    #blackjack accepts no arguments
    #it will simlulate a simplified version of the game Blackjack
    
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
    
    #Create a list for the order of dealings and two dictionaries for the two players
    #also create two variables that will represent the player's points, and an accumulator
    dealt_cards = []
    player1_deck = {}
    player2_deck = {}
    player1_pts = 0
    player2_pts = 0
    counter = 1
    dealings = 0
    
    #Create a for loop for every card
    for i in range(1,52):
        
        #If the it's player 1's turn
        if (i%2) == 1:
            
            #Find a card and it's number from the deck
            card = random.choice(list(deck))
            value = deck.pop(card)
            
            #Move the card and it's value into the respective deck
            player1_deck[card] = value
            
        #If the it's player 1's turn
        elif (i%2) == 0:
            
            #Find a card and it's number from the deck
            card = random.choice(list(deck))
            value = deck.pop(card)
            
            #Move the card and it's value into the respective deck
            player2_deck[card] = value
        
        #Appent he card to the list
        dealt_cards.append(card)
            
    #Loop for every card in the list, dealt_cards
    for card in dealt_cards:
        
        #Find out where the card is from and find it's value. Change a boolean variable
        #to see who's turn it is too
        try:
            pts = player1_deck[card]    #ADD SOMETHING HERE THAT WILL ADD THE CARD TO THE PLAYERS INDIVIDUAL DECKS
            turn = True
        except:
            pts = player2_deck[card]
            turn = False
        
        #Check to see who's turn it was, and move accordingly
        if turn:
            #Check card AND how many points the player has and move accordingly
            if card[:3] == 'Ace' and player1_pts > 10:
                player1_pts += 1
            else:
                player1_pts += pts
        else:
            #Check card AND how many points the player has and move accordingly
            if card[:3] == 'Ace' and player2_pts > 10:
                player2_pts += 1
            else:
                player2_pts += pts

        #After every two turns, check the players' points and see if there is
        #a winner or a tie. If either case occured, reset the points
        if (counter%2) == 0:
            if player1_pts > 21 and player2_pts > 21:
                print('The results is a draw.')
                print(f'Player 1 had {player1_pts}.')
                print(f'Player 2 had {player2_pts}.')
                for card in dealt_cards:
                    if (counter%2) == 0:
                        dealt_card = player1_deck[card]
                        print(f'{dealt_card}')
                    else:
                        dealt_card = player2_deck[card]
                        print(f'{
                player1_pts = 0
            elif player1_pts > 21 and player2_pts < 22:
                print('Player 2 has won.')
                print(f'Player 1 had {player1_pts}.')
                print(f'Player 2 had {player2_pts}.')
                player1_pts = 0
            elif player1_pts < 22 and player2_pts > 21:
                print('Player 1 has won.')
                print(f'Player 1 had {player1_pts}.')
                print(f'Player 2 had {player2_pts}.')
                player1_pts = 0
            if player1_pts == 0:
                player2_pts = 0
                dealings = 0
                counter = 0
                print()

        #Increase the counter
        counter += 1
        dealings += 1
def encrypting_code2(): #Exercise 3
    #encrypting_code accepts no arguments
    #it will take contents from a file, convert them to
    #the symbol representing each character from the contents
    #and then move those contents into another file
    
    #Create a dictionary for uppercase letter, numbers, and symbols
    code = {}
    num = 160
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    other = '''`1234567890-=~!@#$%^&*()_+,./<>?;':"[]{}|'''
    for i in range(0,3):
        if i == 1:
            alphabet = alphabet.upper()
        for letter in alphabet:
            code[letter] = chr(num)
            num += 1
        if i == 2:
            for letter in other:
                code[letter] = letter
                num += 1
    
    #Prompt the user for a file to be opened. Validation will be included for this
    while True:
        file = input('Which file would you like to open? ')
        try:
            infile = open(file,'r')
        except:
            print('\nPlease open a file that exists.\n')
        else:
            break
    
    #Create a string for the contents from within the file
    contents = ''
    
    #Take everything from within the file and concatenate it to contents, then close the file and open the encryption file
    for line in infile:
        contents+=line
    infile.close()
    infile = open('Encrypted_Version.txt','w')

    #Create a new string for the encrypted contents
    encrypted_contents = ''
    next_char = 0

    #Have a for loop and move the newly encrypted contentes to the string, encrypted_contents
    for char in range(len(contents)):
        if next_char != 1:
            old_value = contents[char]
            new_value = code.get(old_value,'00')
            if new_value == '00':
                if old_value == ' ': #This will run if the old_value is a ' '
                    encrypted_contents+=old_value
                else:
                    try:
                        if contents[char+1] == 'n': #This will run if the '\' is with an 'n'
                            encrypted_contents+='\n'
                            next_char = 1 #Skip the letter 'n' in order to not have extra code
                        else:
                            encrypted_contents+=old_value #This will run if the '\' is without an 'n'
                    except:
                        encrypted_contents+=old_value #This part will run if the '\' is at the end of contents
            else:
                encrypted_contents+=new_value #This will add the new value to encrypted_contents if the old_value isn't '\' or ' '
        else:
            next_char = 0
        
    #Move the encrypted content into the file, Encrypted_Version, and close the file
    infile.write(str(encrypted_contents))
    infile.close()
    
    #Tell the user that the contents have been put into the file
    print(f'\nThe contents from the file, {file}, have been encrypted and put into the file, Encrypted_Version')



def decrypting_code2(): #For Exercise 3
    #decrypting code accepts no arguments
    #it will read the specific file created by
    #encrypting_code(), and decrypt the contents
    #from within the file
    
    #Create the same dictionary from the main function
    code = {}
    num = 160
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    other = '''`1234567890-=~!@#$%^&*()_+,./<>?;':"[]{}|'''
    for i in range(0,3):
        if i == 1:
            alphabet = alphabet.upper()
        for letter in alphabet:
            code[letter] = chr(num)
            num += 1
        if i == 2:
            for letter in other:
                code[letter] = letter
                num += 1
    new_code = {}
    for character in code:
        value = code[character]
        new_code[value] = character
    
    
    #Open the file from the ecrypting_code() function
    infile = open('Encrypted_Version.txt','r')
    
    #Create a string for the contens from within the file
    contents = ''
    
    #Take everything from within the file and concatenate it to contents, then close the file
    for line in infile:
        contents+=line
    infile.close()
    
    #Create a new string for the decrypted contents
    decrypted_contents = ''
    next_char = 0

    #Have a for loop and move the decrypted contentes to the string, decrypted_contents
    for char in range(len(contents)):
        if next_char != 1:
            old_value = contents[char]
            new_value = new_code.get(old_value,'00')
            if new_value == '00':
                if old_value == ' ': #This will run if the old_value is a ' '
                    decrypted_contents+=old_value
                else:
                    try:
                        if contents[char+1] == 'n': #This will run if the '\' is with an 'n'
                            decrypted_contents+='\n'
                            next_char = 1 #Skip the letter 'n' in order to not have extra code
                        else:
                            decrypted_contents+=old_value #This will run if the '\' is without an 'n'
                    except:
                        decrypted_contents+=old_value #This part will run if the '\' is at the end of contents
            else:
                decrypted_contents+=new_value #This will add the new value to decrypted_contents if the old_value isn't '\' or ' '
        else:
            next_char = 0
    
    #Print the decrypted_contents for the user
    print('Here is the decrypted message.\n')
    print(decrypted_contents)
        
m()