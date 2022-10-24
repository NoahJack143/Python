#Imports
import random
import matplotlib.pyplot as plt

#==============================================#

def m(): #Exercise 0
    #m accepts no arguments
    #it will call for other MAIN FUNCTIONS
    
        #Text before and inside the table
        print('Main Function caller\n---------------------\n' +
        '2) Lotter Number Generator\n3) Rainfall Statistics\n5) Charge Account Validation\n' +
        "7) Driver's License Exam\n11) Tic Tac Toe\n12) White Elephant Exchange\n" +
        "13) Magic 8 Ball\n14) Expense Pie Chart\n15) 1994 Weekly Gas Graph\n" +
        "----------------------")
        
        #Prompt the user for an main function to call
        ui = int(input('Which main function would you like to call? '))
        print('\n' * 100)
        
        #List of options
        options = [2,3,5,7,11,12,13,14,15]
        
        #Check to see if the user input is any of the option
        if ui == 2:
            lottery()
        elif ui == 3:
            rainfall()
        elif ui == 5:
            charge_accts()
        elif ui == 7:
            drivers_exam()
        elif ui == 11:
            tic_tac_toe()
        elif ui == 12:
            white_elephant()
        elif ui == 13:
            magic_8_ball()
        elif ui == 14:
            expense_pie_chart()
        elif ui == 15:
            weekly_gas_graph()
        else:
            print('Please choose an option from the table.')
            
#==========================================================#
 
def IsValid(string): #Program EX1 #MAKE SURE STRING IS A STRING BEFORE SENDING: '123' #NOT: 123
    #IsValid accepts one argument
    #it will rtun True if the value passed to it is a string
    #containing only numbers and False if it has any characters other
    #than numbers
    
    if string.isnumeric():
        #the string only contains numbers
        return True
    else:
        #The string contains charcters other than numbers
        return False

#==========================================================      
def lottery(): #Exercise 2
    #lottery accepts no arguments
    #it will generate a seven-digit- lottery number.
    #it should generate seven random numbers, each in the range of 0 through
    #0, and assign each number to a list element. Then write another loop
    #that displays the contents of the list
    
    #Create a try block incase something fails
    try:
    
        #Create an accumulator
        c = 0 #Counter
        
        #Create an empty list
        lot_nums = []
        
        #Tell the user that you are generating the lottery numbers
        print('Generating lotto numbers...')
        
        #Create a while loop
        while c != 7:
            #Generate a random number
            number = random.randint(0,9)
            
            #Put the number into a list
            lot_nums.append(number)
            
            #Increase the counter
            c += 1
        
        #Tell the user something before showing the lottery numbers they drew
        print('your lotto numbers are:')
        
        #After breaking out of the loop, write another loop to display the numbers
        for num in lot_nums:
            print(num)
    #Use this except incase something goes wrong
    except:
        print('An error has occured with the lottery machine.\n' +
              'Please try again later.')

#=============================================================#
        
def rainfall(): #Exercise 3
    #rainfall accepts no arguments
    #it will let the user enter the total INCHES of rainfall for each of 12 months
    #into a list. Then, it will calculate and display the total rainfall
    #for the year, the average monthly rainfall, the months with the
    #highest and lowest amount
    #USER VALIDATIONS AND HANDLE EXCEPTIONS
    
    #Use try blocks
    try:
        #Create a list of the months
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July'
                  , 'August', 'September', 'October', 'November', 'December']
        
        #Create an empty list for the next bit of questions
        rainfall = []
        
        #Boolean variable
        cont = True
        
        #Ask the user to tell the inches of rainfall for each month   #CREATE USER VALIDATION # USER IsValid
        
        for month in months:
            if cont:
                #Ask the user for input
                print('Enter the rainfall for', month, end='')
                inches = input(': ')
                
                #Validate the user's input every time
                if not IsValid(inches) or int(inches) < 0: #If the user's input isn't valid, destroy the list and ruin the function
                    cont = False
                else: #Append the input into the list if the input is valid
                    rainfall.append(int(inches))
        
        #Only continue with the function if the boolean variable is true
        if cont:
            
            #After for loop is over, copy the list
            #rainfall2 = X , rainfall = Y
            rainfall2 = []
            
            for element in rainfall:
                rainfall2.append(element)
            
            
            #sort the numbers in list X
            rainfall2.sort()
            
            #Accumulator and counter variables
            c = 0
            index = -1
            
            #read the first element in list X and see where it is located in list Y
            minimum = rainfall2[0] #Find the minimum
            
            for num in rainfall: #Loop through all the elemnts in list Y
                
                if minimum == num: #If minimum matches, then index will = the location of that element in list Y
                    index = c
                    
                c += 1 #Increase the counter every time

            min_month = months[index] #Find the month with the least rainfall
            
            #Reverse the order of the numbers in list X
            rainfall2.reverse()
            
            #Accumulator counter variables
            c = 0
            index = -1
            
            #read the first element in list X and see where it is located in list Y
            maximum = rainfall2[0] #Find the maximum
            
            for num in rainfall: #Loop through all the elemnts in list Y
                
                if maximum == num: #If maximum matches, then index will = the location of that element in list Y
                    index = c

                c += 1 #Increase the counter every time

            max_month = months[index] #Find the month with the least rainfall
            
            #Once the maximum and minimum have been found, find the total rainfall
            #for the year and the average rain per month
            
            #TOTAL RAINFALL
            
            #Variable for the total amount of rain
            total_rain = 0
            
            #Loop for each year
            for rain in rainfall:
                total_rain += int(rain)
                
            #AVERAGE RAIN P/ MONTH
                
            average_rain = total_rain / 12
            
            #Once all is said and done, print everything that has been found
            print()
            print(min_month, 'had the least rain with', minimum, 'inches of rain.')
            print(max_month, 'had the most rain with', maximum, 'inches of rain.')
            print('Total rain for the year:', format(total_rain, ',.2f'), 'inches')
            print('Average rain per month:', format(average_rain, ',.2f'), 'inches')
        else: #If cont is False, purposely crash the program
            a = b * 2
    except NameError:
        print("There was a problem with the user's input.")

#==================================================================#
        
def charge_accts(): #Exercise 5
    #charge accts accepts no arguments
    #it will read the contents of a file and put them into a list. It will then ask the
    #user to enter a charge account number. The program will then determine whether the
    #number is valid by passing the information to the function IsValid.
    #Then, based on the return value of IsValid, the program should display a message
    #indicating if the number is valid or invalid, and prompt the user for another
    #number. Valid all inputs to be numeric only.
    
    #Start by creating a try block
    try:
        #open the file and read it
        infile = open('charge_accounts.txt', 'r')
        
        #Create an empty list
        acc_nums = []
        
        #Read the first line in the file
        line = infile.readline()
        
        #Read the line in the file and then put the line into the list
        while line != '':
            #append the line(account number) into the list
            acc_nums.append(line.rstrip('\n'))
            
            #Read the next line in the file
            line = infile.readline()
        
        #Create a while loop to continue until the user no longer wants to
        cont = True
        
        #Another boolean variable
        bad_input = False

        #Once the list has been created, ask the user for an account
        while cont:
            #Ask the user for an account number if they haven't entered a bad input yet or if the loop has just restarted
            if not bad_input:
                wanted_acc = input('\nEnter an account number: ')
                
            #Ask the user with a hint if they entered a bad number last time    
            if bad_input:
                wanted_acc = input('\nEnter an account number (numeric only): ')
                
            #Validate the user's input and check for the number if the input is valid
            if IsValid(wanted_acc):
                
                #If the input is all numbers, then change the boolean
                bad_input = False
                
                #Check for the user's input in the list
                if wanted_acc in acc_nums:
                    
                    #If the item is found, tell the user
                    print('\nThe account number is valid.')
                else:
                    
                    #If the input isn't in the list
                    print('\nThe number is invalid.')
            #If the user's input isn't valid ask them again with a hint on whey their last input was wrong
            else:
                bad_input = True
                print()
                
            #Ask the user if they want to continue ONLY if their input is good
            if not bad_input:
                conti = input('\nCheck another account number? (y/n) ')
            
            #Check their response and give the appropriate feedback and only run if the input is good
            if not bad_input:
                if conti == 'y':
                    cont = True
                elif conti == 'n':
                    cont = False
                elif conti != 'y' and conti != 'n' and not conti.isnumeric():
                    cont = False
                    print('Please enter either "y" or "n" next time.')
                else:
                    cont = False
                    print('Please enter a letter next time.')
                
    #Once everything is said and done, have the exceptions
    except TypeError:
        print('There was a problem somewhere.')
    #If everything went right, close the file
    else:
        infile.close()
        
#====================================================================#
        
def drivers_exam(): #Exercise 7
    #drivers_exam accepts no arguments
    #it will ask the user for the test to grade and read the student's
    #answers for each of the 20 questions from a test file. These answers
    #should be stored in another list. After the student's answers have been read from the file,
    #the program should display a message indicating whether the student passes or faile the exam
    #(at least 15/20 to pass)it should then display the total number of correctly answered questions, the total
    #number of incorrectly, answered questions, and a list showing the question number of the incorreclty
    #answered questions.
    
    #Start off by creating a try block
    try:
        
        #Set the boolean variable to True
        keep_going = 'y'
        
        #Create a while loop here in order to loop again if the user would like to
        while keep_going.lower() == 'y':
                
            #Open the file diver_test_key and read it
            infile = open('driver_test_key.txt', 'r')
                
            #Ask the user which file of student answers they would like to open and check
            wanted_file = input("\nWhich student's answers would you like to check? (Include the file name extention)")
            
            #Open the file that the user requested and read it
            student_answers = open(wanted_file, 'r')
            
            #Read the first line in each file and add a counter
            key_line = infile.readline()
            student_line = student_answers.readline()
            c = 1 #Counter
            
            #Create accumulators for amount of correct answers and for the answers missed
            correct = 0
            incorrect = 0
            
            #Create an empty list in order to know which problems were wrong
            incor_probs = []
            
            #Begin a while loop for every for all the lines in the answer key
            while key_line != '':
                
                #check to see if the student's answer matches the correct answer and add to the appropriate accumulator
                if key_line == student_line:
                    correct += 1
                elif key_line != student_line:
                    incorrect += 1
                    #If the answer is wrong, add the problem # to the list, incor_probs
                    incor_probs.append(c)
                
                #Read the next line in both of the files
                key_line = infile.readline()
                student_line = student_answers.readline()
                
                #At the end of every loop, add to the counter to know which problem is being worked on
                c += 1
            
            #Tell the user how many answers they got correct out of 20
            print('You answered', correct, 'questions correctly out of 20\n')
            
            #Tell the user how many questions they missed and the minimum the needed to pass.
            print('You missed ', incorrect, '. The minimum you could miss to pass is 5.\n', sep='')
            
            #Tell the user if they passed or failed
            if incorrect > 5:
                print('YOU FAILED.\n')
            elif incorrect <= 5:
                print('You passed...\n')
                
            #Tell the user which questions they missed if any
            if incorrect > 0:
                print('Here are the questions you missed.\n', incor_probs)
                print()
            elif incorrect < 1:
                print("You didn't miss anything...\n")
                
            #Ask the user if they would like to check another test
            print('Would you like to check another', end='')
            keep_going = input('? (y/n) ')
            
            #No matter what, close the files to reset the lines
            infile.close()
            student_answers.close()
            
    #If something went wrong, then use the except message.
    except FileNotFoundError:
        print('\nThe file, ', wanted_file, ', does not exist.', sep='' )
    except:
        print('\nAn unknown error occured.')
        
#==========================================================#

def tic_tac_toe(): #Exercise 11
    #tic tac toe accepts no arguments
    #it is going to put two computers against each other in
    #a game of tic tac toe
    #this program is quite long in order to meet the requirements
    #from the document(even though it's missing one requirement)
    
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
  
#===============#
  
def ttt_comp_comp(): #Computer V.s Computer --- EXTRA WAY TO WRITE TIC TAC TOE(inspired version)
    #ttt comp comp accepts no arguments
    #it will have two computers go against each other
    #in a game of Tic Tac Toe
    
    #Create the board
    board = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']
             ]
    
    #Set Variables for simplicity
    x = 'x'
    o = 'o'
    
    #Create a variable that will stand for both of the symbols
    symbol = x
    
    #Create a for loop
    for turn in range(9):
        
        #while loop to get an open spot on the board
        cont = False
        while not cont:
            #Find a random spot on the board
            row = random.randint(0,2)
            col = random.randint(0,2)
            
            #Check to see if that spot on the board is taken and then move accordingly
            if board[row][col] == '-':
                board[row][col] = symbol
                cont = True
            else:
                cont = False
        
        #If the board is filled, end the loop and say there was a tie
        if turn == 9:
            break
        
        #Check for a winner if there could be one
        winner = False
        if turn > 4:
            winner = game_over(board, row, col)
        
        #If there is a winner, then close the loop and check to see who won
        if winner:
            break
        
        #Swtich the symbols at the end of each loop
        if symbol == o:
            symbol = x
        elif symbol == x:
            symbol = o
    
    #Print the board
    for row1 in board:
        print(row1)
    #Check the outcome and print accordingly
    if winner:
        victor = board[row][col]
        print(f'Player {victor} won the game.\nGG')
    elif not winner:
        print('The game ended in a tie!\nGG')  
  
def game_over(board, row, col):
    #check accepts three arguments
    #it will check for a winner with the given information
    
    #Check horizontally for the played spot
    if board[row][0] == board[row][1] == board[row][2] != '-':
        return True
    #Check verticaly for the played spot
    if board[0][col] == board[1][col] == board[2][col] != '-':
        return True
    #Check for both of the diagonal possibilities
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return True
    if board[0][2] == board[1][1] == [2][0] != '-':
        return True
    #If all fails, return False
    return False

#========================================================================================#
    
def white_elephant(): #Exercise 12
    #white elephant accepts no arguments
    #it will output a list for a Secret Santa event between three departments, and people from the same department can't gift to each other
    
    people = [['Julia','Oliver','Abigail'],['Camden','Kayleigh','Cooper','Kerrigan'],['Avery','Charlotte','Elle']] #Two dimensional list with names in respective companies
    random.shuffle(people[0]) #Shuffle the names from the Development Department
    random.shuffle(people[1]) #Shuffle the names from the Human Resources Department
    random.shuffle(people[2]) #Shuffle the names from the Sales Department
    for num in range(0,2+1): #A for loop that will loop three times
        try: #try block
            print(people[0][num],' gifts to ',people[1][num],'\n',people[1][num],' gifts to ',people[2][num],'\n',people[2][num],' gifts to ',people[0][num+1], sep='') #print the gifter and receiver
        except: #exception for when there isn't enough people in the Development Department for the loop to continue with
            print(people[2][2],'gifts to',people[1][3]) #Print the remaining two gifters and receivers in their respective spots
            print(people[1][3],'gifts to',people[0][0])
    
#===============#

def white2(): #EXTRA WAY TO WRITE WHITE_ELEPHANT
    DD = ['Julia','Oliver','Abigail']
    HRD = ['Camden','Kayleigh','Cooper','Kerrigan']
    SD = ['Avery','Charlotte','Elle']
    random.shuffle(DD)
    random.shuffle(HRD)
    random.shuffle(SD)
    match = []   
    max_length = len(DD)
    if max_length < len(HRD):
          max_length = len(HRD)
    if max_length < len(SD):
          max_length = len(SD)   
    index = 0    
    while index < max_length:   
        if index < len(DD):
            match.append(DD[index])
        if index < len(HRD):
            match.append(HRD[index])
        if index < len(SD):
            match.append(SD[index])
        index += 1
    index = 0
    for num in range(1,10+1):
        try:
            print(match[index],'gifts to', match[index+1])   
            index += 1
        except:
            print(match[9],'gifts to', match[0])
            break
      
#=======================================================#
        
def magic_8_ball(): #For Exercise 13
    #magic 8 ball accepts no arguments
    #it will give the user random responsese
    #to yes or no questions
    
    #Create a try block
    try:
        
        #Open the file
        infile = open('8_ball_responses.txt', 'r')
        
        #Create an empty list
        responses = []
        
        #Read the first line in the file
        line = infile.readline()
        
        #Make a while loop and move every line into a list
        while line != '':
            
            #appen the line into the list
            responses.append(line.rstrip('\n'))
            
            #Read the next line
            line = infile.readline()
            
        #Create a boolean variable
        done = False
        
        #Create a while loop
        while not done:
            
            #Ask the user for a question
            question = input('What is your question? ')
            
            #Get a random index number
            index = random.randint(0,11)
            
            #Get a response from the list
            response = responses[index]
            
            #print the response for the user
            print('\n', response, '\n')
            
            #Ask the user if they want to ask another question
            keep_going = input('Do you want to ask another question? (y/n): ')
            print()
            
            #Check their response
            if keep_going == 'y':
                done = False
            elif keep_going == 'n':
                done = True
            elif keep_going != 'y' and keep_going != 'n':
                done = True
            
    #Have an exception handling message
    except:
        print('There was an issue with the great 8 ball.')
    #If everything went right, close the file and output a message
    else:
        infile.close()
        print('Beware the prophecy... Take care.')
        
#=======================================================#
        
def expense_pie_chart(): #Exercise 14
    #expense pie chart accepts no arguments
    #it will be a main function and will prompt the user for
    #their monthly expenses. Then it will call the function show_chart(categories) and
    #it output the chart
    
    #Create a try block
    try:
        
        #Open a file and write in it
        infile = open('monthly_expenses.txt', 'w')
        
        #Create a list of expenses you'd ask the user about
        categories = ['rent','gas','food','clothing','car payment','misc']
        
        #Create an index variable / accumulator
        index = 0
        
        #Create a boolean variable
        keep_going = False

        #Create a while loop
        while not keep_going:
            #Try block
            try:
                #ask the user about their expenses for every category
                print('How much do you spend in the category of', categories[index], end='')
                expense = int(input('? '))
                #Validate the input and move on accordingly
                if expense >= 0 and IsValid(str(expense)):
                    keep_going = False
                    infile.write(str(expense) + '\n')
                    index += 1
                else:
                    print('\nPlease enter a proper number\n')
            except:
                keep_going = True
        
        #Close the file
        infile.close()
                
        #call for the function show_chart(categories)
        show_chart(categories)
    except FileNotFoundError:
        print('Oops, the file may not exist')
        
def show_chart(categories): #For Exercise 14
    #show_chart accepts one argument
    #it will display the chart based on the data gathered by
    #expense pie chart
    
    #first, create a try block
    try:
        
        #open the file and read it
        infile2 = open('monthly_expenses.txt', 'r')
        
        #Assign categories to another variable
        cat_labels = categories
        
        #Create an empty list for the sizes of each section in the circle/pie
        cat_size = []
        
        #Read the first line in the file
        line = infile2.readline()
        
        #Use a while loop in order to get each data for their respective category
        while line != '':
            cat_size.append(line.rstrip('\n'))
            line = infile2.readline()
            
        #draw the pie chart
        plt.pie(cat_size, labels=cat_labels)
        
        #Add a title for the pie chart
        plt.title('Monthly Expenses')
            
    except FileNotFoundError:
        print('hi')
    else:
        plt.show()

#==============================================================#
        
def weekly_gas_graph(): #Exercise 15
    #gas averages accepts no arguments
    #it will show the weekly gas averages for each week in the year
    #1994(52 lines). matplotlib will write a function that will
    #read the contents in the file and then it wil lplot the data
    #as a line graph or a bar graph. A title, tick marks,
    #and labels along the X and Y axes will be displayed too
    
    #try block
    try:
        #Open the file
        infile = open('1994_Weekly_Gas_Averages.txt', 'r')
        
        #Set limits for the x and y axis
        plt.xlim(xmin = 0, xmax = 52)
        plt.ylim(ymin = 0, ymax = 52)
        
        #Create an empty two dimensional list
        y_ticks = [[],[]]
        
        #Create an accumulator
        index = 0
        
        #Create loop to get y_ticks
        for line in infile:
            y_ticks[0].append(index)
            index += 1
            y_ticks[1].append(line.rstrip('\n'))
            
        #Use the list y_ticks for the y ticks on the chart
        plt.yticks(y_ticks[0],y_ticks[1])
        
        #Create the x ticks for the chart
        plt.xticks([10,20,30,40,50],['10','20','30','40','50'])
        
        #Create a title for the chart
        plt.title('1994 Weekly Gas Averages')
        
        #Label the x and y axis
        plt.xlabel('Weeks')
        plt.ylabel('Gas Price / Gallon')
        
        #Get the x and y coordinates for the line on the graph
        x_coords = [0,9,10,11,12,13,34,35,36,40,41,42,52]
        y_coords = [0,8,5,4,5,9,34,33,35,40,30,41,52]
        
        #Build the graph
        plt.plot(x_coords,y_coords)
        
        #Draw the graph
        
        #Showg grid lines
        plt.grid(True)
        
        #Display the graph
        plt.show()
        
    #Execptions
    except ModuleNotFoundError:
        print("You don't have the module, matplotlib.")
    except FileNotFoundError:
        print('There was an issue with finding the file.')
    except:
        print('There was an issue with the data that goes into the chart.')

#================================================#
        
m() #Call the m function that will call other main functions