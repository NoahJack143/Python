#Imports
import random

#Create the function
def tic_tac_toe(): #Exercise 11
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
        counter = 1
        
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
                board[row][column] = symbol
                keep_going2 = True
            
            #If the spot on the board is taken up, then loop again
            else:
                keep_going2 = False
                counter -= 1
                
            #Create an if statement that will go run if the element isn't taken up by X or O
            if keep_going2 and counter > 4:
                
                #Call for the function game_over(board) to check and see if there is a winner or not
                keep_going, victor = game_over(board)
                
            #Increase the counter every time
            counter += 1
            
            #Check to see if there is any room left on the board
            if counter == 9:
                keep_going == False
            
            #Switch turns
            if (counter % 2) == 0:
                symbol = 'o'
            elif (counter % 2) == 1:
                symbol = 'x'
                
        #When the while loop ends, call for the function winner to find out who won the game, or if the game ended in a tie
        results = winner(victor)
        
        #Print the game board and the appropriate message for the user
        print(board[0], '\n', board[1], '\n', board[2], '\n', results, sep='')
        
    except TypeError as err:
        print(err)
                
def game_over(board): #For Exercise 11
    #game over accepts one argument
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
    
def winner(victor): #For Exercise 11
    #winner accepts one argument
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