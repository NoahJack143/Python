#This module will test out many ways to make the game tic tac toe
#There will programs that will have a computer against a computer
#a computer against a player, and a player against another player


#=============================================================================================================#

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
        x = 'x'
        o = 'o'
        
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
            print(board[0], '\n', board[1], '\n', board[2], '\n/n', sep = '')
            if keep_going2 and c > 4:
                
                #Call for the function game_over() to check if there was been a winner
                done = game_over(board)
                
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
        victor = winner(board)
        
        #Check to see the results and then print the appropriate messaage
        if victor == x or victor == o:
            print(board[0], '\n', board[1], '\n', board[2], '\nThe winner was player ', victor, end='.', sep = '')
        else:
            print(board[0], '\n', board[1], '\n', board[2], '\nThe game ended in a tie', end='.', sep = '')
        
    #Have an excpet statement to catch any problems
    except ValueError:
        print('There was an issue when computing the game')
    else:
        #If everything worked, print a blank line for the next program
        print()
                
def game_over(board):
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
                    
                #Check the rows
                if board[rows][0] != '-' and board[rows][0] == board[rows][1] == board[rows][2]:
                    winner = True
                #Increase rows every time
                rows += 1
                #If there is a winner, then break out of the column
                if winner:
                    break
        
        #Run each loop if there isn't a winner
        if not winner:
            
            #Create a variable for the columns
            column = 0
            
            #Create a loop for the columns on the board      #THERE IS SOMETHING WRONG WITH THE COLUMNS
            for row in board:
                    
                #Check each column
                if board[0][column] != '-' and board[0][column] == board[1][column] == board[2][column]:
                    winner = True
                #Increase the variable column to move to the next column for every loop
                column += 1
                #Break out of the loop if there is a winner
                if winner:
                    break
                
            #Reset the variable to 0 every time
            column = 0
                
        #Run each loop if there isn't a winner
        if not winner:
                
            #Check the top left to bottom right diagonal
            if board[0][0] != '-' and board[0][0] == board[1][1] == board[2][2]:
                winner = True
            
            #Check the top right to bottom left diagonal
            elif board[0][2] != '-' and board[0][2] == board[1][1] == board[2][0]:
                winner = True
                
        #If none of the other if statements have found a winner, then return false
        if not winner:
            return False
        #If one of them has found a winner, return true
        elif winner:
            return True
        
    #Have an exception
    except NameError:
        print('There was problem within the checker(board) function')
        
def winner(board):
    #winner1 accepts one argument
    #it will find out which player won the game
    
    #Use a try block just in case
    try:
        #Use variables for simplicity
        x = 'x'
        o = 'o'
        
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
    except:
        print('There was a problem within the winner1(board) function.')
        
#=============================================================================================================#        
      
#This program is taken from the tic_tac_toe() made in Chapter 7 Exercises 2022.
#The function within Chapter 7 Exercises 2022 may change later
def tic_tac_toe2(): #Exercise 11
    #tic tac toe accepts no arguments
    #it will have two computers play against each other
    #in a game of tic tac toe
    
    #Create a try block
    try:
        
        #Create the board by using a two dimensional list
        board = [['-','-','-'],
                 ['-','-','-'],
                 ['-','-','-']
            ]
        
        #Create a counter to keep track of the rounds and to see who's turn it is
        counter = 0
        
        #Create a boolean variable for the while loop
        keep_going = True
        
        #Ues a variable to determine who goes first
        symbol = 'x'
        
        #Create a while loop in order to loop enough times for all the spots on the board to be filled
        while keep_going:
            
            #Find the random numbers for the row and for the column
            row = random.randint(0,2)
            column = random.randint(0,2)
            
            #Find out if the element is taken up by an X or an O
            if board[row][column] == '-':
                board[row][column] = symbol #Replace the empty spot
                
                #Change the second boolean
                keep_going2 = True
                
                #Swtich turns
                if (counter % 2) == 0:
                    symbol = 'o'
                elif (counter % 2) == 1:
                    symbol = 'x'
                
            
            #If the spot on the board is taken up, then loop again
            else:
                #Change the second boolean and loop again
                keep_going2 = False
                
                #Decrease the counter so that the game will act as if nothing ever happened when it loops again
                counter -= 1
                
            #Create an if statement that will go run if the element isn't taken up by X or O
            if keep_going2 and counter > 3:
                
                #Call for the function game_over(board) to check and see if there is a winner or not
                keep_going, victor = game_over2(board)
                
            #Increase the counter every time
            counter += 1
            
            #Check to see if there is any room left on the board
            if counter > 8:
                keep_going = False
                
        #When the while loop ends, call for the function winner to find out who won the game, or if the game ended in a tie
        results = winner2(victor)
        
        #Print the game board and the appropriate message for the user
        print(board[0], '\n', board[1], '\n', board[2], '\n', results, sep='')
        
    except TypeError as err:
        print(err)
                
def game_over2(board): #For Exercise 11
    #game over2 accepts one argument
    #it will find out if there is a winner
    
    #Use variables for simplicity
    x = 'x'
    o = 'o'
    
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
        return False, x
    
    #Check to see if there is a column full of x's
    elif top_left_x and mid_left_x and bot_left_x or top_mid_x and middle_x and bot_mid_x or top_right_x and mid_right_x and bot_right_x:
        return False, x
    
    #Check to see if there are diagonal x's
    elif top_left_x and middle_x and bot_right_x or top_right_x and middle_x and bot_left_x:
        return False, x
    
#o        #Check to see if there is a row of o's
    elif top_left_o and top_mid_o and top_right_o or mid_left_o and middle_o and mid_right_o or bot_left_o and bot_mid_o and bot_right_o:
        return False, o
    
    #Check to see if there is a column full of o's
    elif top_left_o and mid_left_o and bot_left_o or top_mid_o and middle_o and bot_mid_o or top_right_o and mid_right_o and bot_right_o:
        return False, o
    
    #Check to see if there are diagonal o's
    elif top_left_o and middle_o and bot_right_o or top_right_o and middle_o and bot_left_o:
        return False, o
    
    #If there is no winner, then return True to keep looping
    else:
        return True, 'tie'
    
def winner2(victor): #For Exercise 11
    #winner2 accepts one argument
    #it will find out the results of the game and will
    #return the results to the main function
    
    #Check to see who the victor was if any
    if victor == 'x':
        result = '\nThe winner is player x.\nGG'
    elif victor == 'o':
        result = '\nThe winner is player o.\nGG'
    elif victor == 'tie':
        result = '\nThe game resulted in a tie.\nGG'
    
    #Return the results
    return result

#=============================================================================================================#


#list[ran_num]
#remove ran_num from list and then choose another random number from the list