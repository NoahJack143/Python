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
                if not IsValid(inches) or float(inches) < 0: #If the user's input isn't valid, destroy the list and ruin the function
                    cont = False
                elif validation: #Append the input into the list if the input is valid
                    rainfall.append(inches)
        
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
            maximum = rainfall2[0] #Find the minimum
            
            for num in rainfall: #Loop through all the elemnts in list Y
                
                if maximum == num: #If minimum matches, then index will = the location of that element in list Y
                    index = c

                c += 1 #Increase the counter every time

            max_month = months[index] #Find the month with the least rainfall
            
            #Once the maximum and minimum have been found, find the total rainfall
            #for the year and the average rain per month
            
            #TOTAL RAINFALL
            
            #Variable
            total_rain = 0
            
            #Loop for each year
            for rain in rainfall:
                total_rain += rain
                
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
    except:
        print('There was an error somewhere.')

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
            acc_nums.append(line)
            
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
    except:
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
        while keep_going.lower():
                
            #Open the file diver_test_key and read it
            infile = open('driver_test_key.txt', 'r')
                
            #Ask the user which file of student answers they would like to open and check
            wanted_file = input("Which student's answers would you like to check? ")
            
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
    except:
        print('Something went wrong...')
        
#==========================================================#
        
def tic_tac_toe(): #Exercise 11
    #tic tac toe accepts no arguments
    #it will play the game, tic tac toe
    #user other functions for this game
    #two computers will clash it out!!!!!
    
    #Create a try block
    try:
        
        #Set variables for two players (computers)
        x = 'x'
        o = 'o'
        
        #Create a variable to see who's turn it is. player x will always go first
        turn = x
        
        #Create a counter for the amount of turns in the game
        plays = 1
        
        #Create the empty two-dimensional list
        game_board = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']]
        #Create a boolean that will stay true until the game is over
        cont = True #Continue = True
        #Create a while loop to check if the game_board
        while cont:
        
def game_over(board): #For Exercise 11
    #game over accepts one argument
    #it will return True/False depending if all the plays
    #have been made without a winner
    
    #Variables from the main function
    x = 'x'
    o = 'x'
    
    board = [[x,x,x],[o,o,o],[o,o,o]]
    
    #Create multiple boards with possible outcomes
    if board.index[1][1] == x and board.index[1][2] == x and board.index[1][3] == x:
        print('hi')
    
def winner(board): #For Exercise 11
    #it will return True/False and the winner
    
    