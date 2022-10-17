#Imports
import random

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
        print('\n\n\n\n\n\n\n')
        
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
        print(acc_nums)
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

def tic_tac_toe1(): #Exercise 11
    #tic tac toe1 accepts no arguments
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
  
#========================================================================================#
        
def white_elephant(): #Exercise 12
    #white elephant accepts no arguments
    #it will use three lists that will take a name from each list
    #and each of them will give a gift to a person
    #from another apartment. People from the same list can't give
    #gifts to each other
    
    #Create a try block
    try:
        
        #Create a list of every person inside of each department
        DD = ['Julia','Oliver','Abigail']
        HRD = ['Camden','Kayleigh','Cooper','Kerrigan']
        SF = ['Avery','Charlotte','Elle']
        
        for num in range(1, 10):
            
            #Boolean variable
            cont = False
            
            #Make two more lists that will contain those who have given and those who have recieved
            given = []
            received = []
            
            #Choose a random list
            index = random.randint(0,2)
            if index == 0:
                giving_comp = DD
            elif index == 1:
                giving_comp = HRD
            else:
                giving_comp = SF
            
            while not cont:
                #Choose a random person from that list and then add them to the given list
                index = random.randint(0,len(giving_comp)-1)
                gifter = giving_comp[index]
                if gifter in given:
                    cont = False
                else:
                    cont = True
                    given.append(gifter)
            cont = False
            
            #Find a receiving company
            while not cont:
                index = random.randint(0,2)
                if index == 0:
                    receiving_comp = DD
                elif index == 1:
                    receiving_comp = HRD
                else:
                    receiving_comp = SF
                if receiving_comp == giving_comp:
                    cont = False
                else:
                    cont = True
            cont = False
            
            #Find a person from the receiving company
            while not cont:
                    index = random.randint(0,len(receiving_comp)-1)
                    receiver = receiving_comp[index]
                    if receiver in received:
                        cont = False
                    else:
                        cont = True
                        received.append(receiver)
                        
            #print the results
            print(gifter, 'gifts to', received)
        print(given)
        print(received)
    except NameError:
        print('oo')
