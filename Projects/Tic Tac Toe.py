#Imports
import random

#=============================================================================================================#

def tic_tac_toe1(): #Computer V.s Computer
    #tic tac toe1 accepts no arguments
    #it is going to put two computers against each other in
    #a game of tic tac toe
    
    #Create a try block to catch any exceptions
    try:
        
        #Create the board
        board = [['-','-','-'],
                 ['-','-','-'],
                 ['-','-','-']
                 ]
        
        #Create a boolean variable for the while loop
        keep_going = True
        
        #Create a counter to know when to check for a winner
        #and for when 9 turns have been made
        c = 1
        
        #Create two variables that will stand for 'X' and 'O' for simplicity
        x = 'X'
        o = 'O'
        
        #Create a symbol that will represent either 'X' or 'O'
        #Player X will always move first
        symbol = x
        
        #Create a while loop to loop for each turn
        while keep_going:
            
            #Create two random numbers for either of the computers' move
            row = random.randint(0,2)
            col = random.randint(0,2)
            
            #Check to see if that spot on the board is taken up or not
            if board[row][col] == '-': #If the spot is open
                board[row][col] = symbol
                keep_going2 = True
            else: #If the spot is occupied by an 'X' or an 'O'
                keep_going2 = False
                c -= 1 #Decrease the counter when a computer tries playing in a played spot
                
            #Create an if statement that will run if keep_going2 is True
            #and if there has been at least 4 turns.
            if keep_going2 and c > 4:
                
                #Call for the function game_over to check if there was been a winner
                done = checker(board)
                
                #Check and see what game_over returned
                if done:
                    keep_going = False
                elif not done:
                    keep_going = True
                
            #Increase the accumulator
            c += 1
            
            #If there has been 9 turns, then the game is over
            if c > 9:
                keep_going = False
                
            #Switch turns
            if (c % 2) == 0:
                symbol = o
            elif (c % 2) == 1:
                symbol = x
        
        #Call for another function to find out who won, if either of the computers did
        winner = winner1(board)
        
        #Check to see the results and then print the appropriate messaage
        if winner == x or winner == o:
            print(board[0], '\n', board[1], '\n', board[2], '\nThe winner was player ', winner, end='.', sep = '')
        else:
            print(board[0], '\n', board[1], '\n', board[2], '\nThe game ended in a tie', end='.', sep = '')
        
    #Have an excpet statement to catch any problems
    except ValueError:
        print('oo')
                
def checker(board):
    #This function will check to see if there has been a winner on the board
    
    #Create another try block just in case
    try:
        
        #Create a boolean variable to check if there has been a winner
        winner = False
        
        #Run each loop if there isn't a winner
        if not winner:
            
            #Create a variable for the rows
            rows = 0
            
            #Create a for loop for the rows on the board
            for row in board:
                for col in row:
                    
                    #Check the rows
                    if board[rows][0] != '-' and board[rows][0] == board[rows][1] == board[rows][2]:
                        winner = True
                        return winner
                #Increase rows every time
                rows += 1
                #If there is a winner, then break out of the column
                if winner:
                    break
        
        #Run each loop if there isn't a winner
        elif not winner:
            
            #Create a variable for the columns
            column = 0
            #Reset rows
            rows = 0
            
            #Create a loop for the columns on the board      #THERE IS SOMETHING WRONG WITH THE COLUMNS
            for row in board:
                for col in row:
                    
                    #Check each column
                    if board[column][rows] != '-' and board[column][rows] == board[column][rows] == board[column][rows]:
                        winner = True
                        return winner
                    #Increase the variable column to move to the next column for every loop
                    column += 1
                #Break out of the loop if there is a winner
                if winner:
                    break
                
                #Reset the variable to 0 every time
                column = 0
                #Increase rows every time
                
        #Run each loop if there isn't a winner
        elif not winner:
            
            #Create a loop for both of the diagonals
            for row in range(1, 3):
                
                #Check the top left to bottom right diagonal
                if board[0][0] != '-' and board[0][0] == board[1][1] == [2][2]:
                    winner = True
                    return winner
                
                #If there is a winner, break out of the loop
                if winner:
                    break
                
                #Check the top right to bottom left diagonal
                if board[0][2] != '-' and board[0][2] == [1][1] == board[2][0]:
                    winner = True
                    return winner
                
                #If there is a winner, break out of the loop
                if winner:
                    break
                
        else:
            return False
        
    #Have an exception
    except NameError:
        print('There was problem within the game_over() function')
        
def winner1(board):
    #winner1 accepts one argument
    #it will find out if there is a winner
    
    #Use variables for simplicity
    x = 'X'
    o = 'O'
    
    #Create an accumulator and many booleans
    element = 1
    x_row = 0
    x_col = 0
    x_diag = 0
    o_row = 0
    o_col = 0
    o_diag = 0
    
    #Set all the boolean variables to avoid an UnboundLocalError
    top_left_x = False
    top_mid_x = False
    top_right_x = False
    mid_left_x = False
    middle_x = False
    mid_right_x = False
    bot_left_x = False
    bot_mid_x = False
    bot_right_x = False
    top_left_o = False
    top_mid_o = False
    top_right_o = False
    mid_left_o = False
    middle_o = False
    mid_right_o = False
    bot_left_o = False
    bot_mid_o = False
    bot_right_o = False
    
    #Nested for loop and a bunch of if elif statements
    for row in board:
        for col in row:
    #x        #Check for the x's
            if col == x and element == 1:
                top_left_x = True
            elif col == x and element == 2:
                top_mid_x = True
            elif col == x and element == 3:
                top_right_x = True
            elif col == x and element == 4:
                mid_left_x = True
            elif col == x and element == 5:
                middle_x = True
            elif col == x and element == 6:
                mid_right_x = True
            elif col == x and element == 7:
                bot_left_x = True
            elif col == x and element == 8:
                bot_mid_x = True
            elif col == x and element == 9:
                bot_right_x = True
            
    #o        #Check for the o's
            elif col == o and element == 1:
                top_left_o = True
            elif col == o and element == 2:
                top_mid_o = True
            elif col == o and element == 3:
                top_right_o = True
            elif col == o and element == 4:
                mid_left_o = True
            elif col == o and element == 5:
                middle_o = True
            elif col == o and element == 6:
                mid_right_o = True
            elif col == o and element == 7:
                bot_left_o = True
            elif col == o and element == 8:
                bot_mid_o = True
            elif col == o and element == 9:
                bot_right_o = True
                
            #Increase the accumulator for every loop
            element += 1
                
#x        #Check to see if there is a row of x's 
    if top_left_x and top_mid_x and top_right_x or mid_left_x and middle_x and mid_right_x or bot_left_x and bot_mid_x and bot_right_x:
        return x
    
    #Check to see if there is a column full of x's
    elif top_left_x and mid_left_x and bot_left_x or top_mid_x and middle_x and bot_mid_x or top_right_x and mid_right_x and bot_right_x:
        return x
    
    #Check to see if there are diagonal x's
    elif top_left_x and middle_x and bot_right_x or top_right_x and middle_x and bot_left_x:
        return x
    
#o        #Check to see if there is a row of o's
    elif top_left_o and top_mid_o and top_right_o or mid_left_o and middle_o and mid_right_o or bot_left_o and bot_mid_o and bot_right_o:
        return o
    
    #Check to see if there is a column full of o's
    elif top_left_o and mid_left_o and bot_left_o or top_mid_o and middle_o and bot_mid_o or top_right_o and mid_right_o and bot_right_o:
        return o
    
    #Check to see if there are diagonal o's
    elif top_left_o and middle_o and bot_right_o or top_right_o and middle_o and bot_left_o:
        return o
    
    #If there is no winner, then return True to keep looping
    else:
        return 'tie'