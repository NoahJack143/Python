#Imports
import random

#==============================================================================#

#MAIN FUNCTION FOR EVERYTHING
def m(): #MAIN FUNCTION TO CALL ALL OTHER MAIN FUNCTIONS
    #m accepts no arguments
    #it call call all other main functions
    
    #Table with options
    print('FUNCTION_CALLER.io')
    print('--------------------')
    print('3) Line Numbers')
    print('4) Line Counter')
    print('6) Average of Numbers')
    print('7) Random_Number_File_Writer')
    print('8) Random Number File Reader')
    print('10) Golf Scores')
    print('11) Personal Web Page Generator')
    print('12) Average Steps Taken')
    print('13) Average Steps Taken Version 2')
    print('-')
    #User choice
    print('CHOICE', end='')
    uc = int(input('? '))
    #Make a space between the table and the other main functions
    print(' ')
    print(' ')
    print(' ')
    #Check user choice and send them off!
    if uc == 3:
        line_numbers()
    elif uc == 4:
        line_counter()
    elif uc == 6:
        average_of_numbers()
    elif uc == 7:
        ran_num_writer()
    elif uc == 8:
        ran_num_reader()
    elif uc == 10:
        golf_main()
    elif uc == 11:
        pers_web_gen()
    elif uc == 12:
        avg_steps()
    elif uc == 13:
        avg_steps2()
    else:
        print("You didn't choose an option from the table")
        
#===================================================================================#

def line_numbers(): #Exercise 3
    #line numbers accepts no arguments
    #it will display the contents of the file preceded with
    #the line number followed by a colon. It will also include exception
    #handling for any file that isn't found
    
    #creat a try block in order to have exceptoin handling at the end
    try:
        #open the file
        infile = open('steps.txt', 'r')
        
        #Create an accumulator for all the numbers before the colons
        counter = 1
        
        #create a for loop to list all the steps
        for line in infile: #You won't have to read each line because the "line" already reads them
            #create the text
            print(counter, ': ', sep='', end=line)
            counter += 1
            
        #when the loop ends, close the file
        infile.close()
    #after everything is said and done, have an exception handler
    except FileNotFoundError as err: #if the file isn't found
        print(err)
        
def line_counter(): #Exercise 4
    #line counter accepts no argument
    #it will prompt the user fo ra filename, and then displays the number of
    #lines that are stored in the file. It will output he total number of
    #items(names) in the file. THere will also be an exception handler for
    #any file not found.
    
    #create the try block
    try:
        #prompt the user to find a file to read
        file_to_read = input('Enter the file to read: ')
        
        #open the file that the user wanted
        infile = open(file_to_read, 'r')
        
        #Start off by reading the first line since a while loop is being used
        line = infile.readline()
        
        #Accumulator
        total = 0
        
        #create a loop to see how many items are in the file
        while line != '':
            total += 1 #If the loop continues, then the total will increase because there is still an item in the folder
            line = infile.readline() #Find the next line. If no line, then loop ends
            
        #once the loop ends, close the file
        infile.close()
        
        #Output the total of items in the file for the user to see
        print(file_to_read, 'contains', total, 'lines.')
        
    #create an exception handler to check incase there isn't a file
    except FileNotFoundError:
        print('ERROR: No such file or directory: ', file_to_read, "'", sep='')
            
def average_of_numbers(): #Exercise 6
    #average of numbers accepts no arguments
    #it will open the file named 'numbers.txt' to read. It will then
    #read and calculate the average of all the numbers in the file
    #it will also handle any value or file exceptions
    
    #create a try block
    try:
        #open the file
        infile = open('numbers.txt', 'r')
        
        #Accumulators
        total_items = 0
        sum_of_numbers = 0
        
        #Read the first line since a while loop is being used
        line = infile.readline()
        
        #Create a while loop
        while line != '': #CONVERT LINE
            #add to the accumulators respectively
            total_items += 1
            sum_of_numbers += int(line)
            
            #read the next line and continue the loop if there is another number to be added
            line = infile.readline()
            
        #Once the loop ends, close the file
        infile.close()
        
        #Calculate the average
        average = sum_of_numbers / total_items
        
        #Tell the user the average of all the numbers
        print('There were', total_items, 'items with an average value of', average)
        
    #Include an exception handler to check if there was any value or file exceptions
    except FileNotFoundError:
        print('There was no file...')
    except ValueError:
        print('There was a problem with the values...')
        
def ran_num_writer(): #Exercise 7
    #ran num writer accepts no arguments
    #it will write a series of random numbers to a file. Each random number
    #will be between 1 and 100. THe program will let the user choosethe amount of random
    #numbers there would be.
    
    try: #Create a try block
        #Prompt the user
        response = input('How many random numbers would you like to generate? ')
        
        amount_of_ran = int(response)
        
        #Validate the user's input (Make sure it's > 0
        if amount_of_ran > 0:
            
            #Open the file
            infile = open('random_numbers.txt', 'w')
            
            #create a for loop for the amount of random numbers the user requested
            for line in range(1, amount_of_ran + 1):
                #Create a variable for the random number
                number = random.randint(1, 500)
                
                #Write the number into the file
                infile.write(str(number) + '\n')
                
            #Close the file
            infile.close()
            
        else:
            print('Please enter a number that is greater than 0')
            j = j + 34
    #If the try block fails, then have excepts here
    except ValueError:
        print('invalid literal for int() with base 10: ', response)
    except UnboundLocalError:
        print('An error occured becuase you entered a number less than 0')
    except:
        print('An unknown error occured.')
    else:
        print('You have successfully generated the numbers.')

def ran_num_reader(): #Exercise 8
    #ran num reader accepts no arguments
    #this function will display the random numbers, total the numbers
    #and all the number of numbers read.
    
    try: #create a try block
        #open the file
        infile = open('random_numbers.txt', 'r')
        
        #Accumulators
        counter = 0 #This will count the total amount of numbers
        total = 0 #This will get the sum of all the numbers
        
        #Create a for loop for all the numbers
        for line in infile:
            print('', end=line) #Print each number that is found in the file
            counter += 1 #Increase the counter for every loop
            total += int(line) #Add the new number to the total each time to get the sum of all the numbers
            
        #When the loop ends, close the file
        infile.close()
        
        #Tell the user the total numbers and the sum
        print('The total of the', counter, 'random numbers is:', total)
        
    #If the try block fails, then run the exception
    except:
        print('An error occured some where...')
        
#=====================================================================================================#
        
def golf_main(): #Exercise 10
    #golf main accepts no arguments
    #golf main is the main fucntion that will utilize
    #3 other functions. There will also be validation everywhere
    #and try blocks everywhere
    
    #Create a try block
    try:
        #Get the user's choice 
        user_choice = golf_menu()
        
        #Create a space between the user_choie and the other options
        print(' ')
        
        #Check to see which option they chose and then either call a function or end the main function
        if user_choice == 1:
            golf_read()
        elif user_choice == 2:
            golf_write()
        elif user_choice == 3:
            print('Thank you for using the Hole in Twelve golf management system. Have a great day.')
        
    #If the try block fails somehow, then use this exception
    except:
        print('An error occured somewhere...')
    
def golf_menu(): #For Exercise 10
    #golf menu accepts no arguments
    #it will create a menu for the user, and will let them
    #choose an option
    
    #Create a try block
    try:
        #Text before the table
        print('Welcome to Hole in Twelve golf management system.')
        print('Please choose from the following commands...')
        print('-----------------------------------------------------')
        
        #Create a menu for the user
        print('1) Read golf data')
        print('2) Append golf data')
        print('3) Exit')
        print(' ')
        
        #Prompt the user for their option
        user_choice = int(input('Menu choice: '))
        
        #Create an if statement to validate the user's choice
        if user_choice <1 or user_choice >3:
            print('Please choose an option from the table next time.')
    except TypeError or ValueError or NameError:
        user_choice = print("There was an issue with the user's choice")
    except:
        user_choice = print('An error occured somewhere...')
    else:
        #if everything went right, then return the user's choice
        return user_choice
        
def golf_read(): #For Exercise 10
    #golf read accepts no arguments
    #it will read the file, golf.txt, to the user.
    #The contents within the file will the golfer's name and
    #their score
    
    #Create a try block
    try:
        #open the file
        infile = open('golf.txt', 'r')
        
        #Create a checker to see when there is nothing left in the file to be read
        check = infile.readline()
        
        #Create a while loop to read everything for the user
        while check != '':
            print('', end=check) #print the information for the user
            check = infile.readline() #Check for the next line in the file
            
    #If the try block doesn't successfully run, run these excepts
    except:
        print('There was a problem somewhere...')
    else:
        print('All records successfully read!')
    
def golf_write(): #For Exercise 10
    #golf_write accepts no arguments
    #it will APPEND data into the file, golf.txt.
    
    #Creat a try block
    try: 
        #open the file
        infile = open('golf.txt', 'a')
        
        #Set a variable to see if the user wants to keep going
        keep_going = 'y'
        
        #Start a while loop so the user can add multiple golfers
        while keep_going.lower() == 'y':
        
            #prompt the user for the golfer's name and their scoore
            golfer_name = input("Golfer's name: ")
            score = int(input('Score: '))
            print(' ')
            
            #append the data to the file
            infile.write(golfer_name + '\n')
            infile.write(str(score) + '\n')
            infile.write(' ' + '\n')
            
            #Ask the user if they would like to add another golfer
            keep_going = input('Add another golfer (y/n) ')
            print(' ')
            
            if keep_going != 'n' and keep_going != 'y':
                print("Please choose either 'y' or 'n' next time.")
                keep_going = 'n'
                
        #once the while loop ends, close the file
        infile.close()
        
    except TypeError or ValueError or NameError:
        print("There was a problem with the user's input.")
    except:
        print('An error occured somewhere...')
    else:
        print('Golf data written to golf.txt')

#=========================================================================================#
        
def pers_web_gen(): #Exercise 11
    #pers web gen accepts no arguments
    #it will prompt the user to enter their name, and then ask theuser for a sentence that describes him or her.
    #Once the user has entered the information, the program should create a HTML file with th einput and the HTML
    #code necessary to create the webpage. The webpage program should save the file using the entered name and the
    #extension .html
    
    #Create a try block
    try:
        #prompt the user for their name
        user_name = input('Enter your name: ')
        
        #Prompt the user to write a short description of themself
        desc = input('Write a short description of yourself: ')
        
        #Change the user's name to make it fit for an HTML webpage
        user_name_html = user_name + '.html'
        
        #Create/reopen the html file for the user
        infile = open(user_name_html, 'w')
        
        #html code (USE CONCATINATION (+) )
        html_template = """
        <html>
        <head>
        </head>
        <body>
            <center>
                <h1>""" + user_name + """<h1>
            </center>
            <hr />
                """ + desc + """
            <hr />
        </body>
        </html>
        
        """
        
        #Writing the code into th efile
        infile.write(str(html_template))
        
        #Close the file when all is said and done
        infile.close()
    #If there is a problem, then use this except
    except:
        print('An error occured somewhere...')
    #If there aren't any problems, then tell the user this
    else:
        print('Webpage information saved to', user_name_html)
               
#================================================================================#          
          
def avg_steps(): #Exercise 12
    #avg steps accepts no arguments
    #it will read from steps.txt and average the number of steps taken each month
    #, then outputs the months and the average number of steps for each month
    
    #Create a try block
    try:
        #Open the file
        infile = open('steps.txt', 'r')
        
        #Accumulators
        counter = 0
        total_steps = 0
        
        #Variables for list
        MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        #For loop in order to get the name of the months
        for name in MONTH:
            #A bunch of if statements to check for the amount of days in each month
            if name == 'January':
                DPM = 31
            elif name == 'February':
                DPM = 28
            elif name == 'March':
                DPM = 31
            elif name == 'April':
                DPM = 30
            elif name == 'May':
                DPM = 31
            elif name == 'June':
                DPM = 30
            elif name == 'July':
                DPM = 31
            elif name == 'August':
                DPM = 31
            elif name == 'September':
                DPM = 30
            elif name == 'October':
                DPM = 31
            elif name == 'November':
                DPM = 30
            elif name == 'December':
                DPM = 31
            #Create another for loop in order to read the lines in the file and calculate the
            #average amount of steps per month
            for days in range(1, DPM + 1):
                line = infile.readline()
                total_steps += int(line)
                counter += 1
                #A bunch of if and elif statements to check whether the accumulators meet the requirements.
                #If they do, then the average is calculated for the respected month, and then it's ouptuted
                if counter == 31 and name == 'January': #January
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t', format(average, ',.2f'), 'steps')
                elif counter == 28 and name == 'February': #February
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t', format(average, ',.2f'), 'steps')
                elif counter == 31 and name == 'March': #March
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t\t', format(average, ',.2f'), 'steps')
                elif counter == 30 and name == 'April': #April
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t\t', format(average, ',.2f'), 'steps')
                elif counter == 31 and name == 'May': #May
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t\t', format(average, ',.2f'), 'steps')
                elif counter == 30 and name == 'June': #June
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t\t', format(average, ',.2f'), 'steps')
                elif counter == 31 and name == 'July': #July
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t\t', format(average, ',.2f'), 'steps')
                elif counter == 31 and name == 'August': #August
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t\t', format(average, ',.2f'), 'steps')
                elif counter == 30 and name == 'September': #September
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t', format(average, ',.2f'), 'steps')
                elif counter == 31 and name == 'October': #Obtober
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t', format(average, ',.2f'), 'steps')
                elif counter == 30 and name == 'November': #November
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t', format(average, ',.2f'), 'steps')
                elif counter == 31 and name == 'December': #December
                    average = total_steps / counter
                    total_steps = 0
                    counter = 0
                    print(name, '\t', format(average, ',.2f'), 'steps')
        #when everything is done, close the file
        infile.close()
    #If something goes wrong, then run one of these excepts
    except TypeError as err:
        print(err)
    except:
        print('An error occured somewhere...')
        
def avg_steps2(): #Exercise 12
    #avg steps accepts no arguments
    #it will read from steps.txt and average the number of steps taken each month
    #, then outputs the months and the average number of steps for each month
    #this is just an EXTRA FUNCTION
    
    #Create a try block
    try:
        #Open the file
        infile = open('steps.txt', 'r')
        
        #Accumulators
        counter = 0
        total_steps = 0
        
        #Variables for list
        MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        #For loop in order to get the name of the months
        for name in MONTH:
            #A bunch of if statements to check for the amount of days in each month
            if name == 'January':
                DPM = 31
            elif name == 'February':
                DPM = 28
            elif name == 'March':
                DPM = 31
            elif name == 'April':
                DPM = 30
            elif name == 'May':
                DPM = 31
            elif name == 'June':
                DPM = 30
            elif name == 'July':
                DPM = 31
            elif name == 'August':
                DPM = 31
            elif name == 'September':
                DPM = 30
            elif name == 'October':
                DPM = 31
            elif name == 'November':
                DPM = 30
            elif name == 'Decemer':
                DPM = 31
            #Create another for loop in order to read the lines in the file and calculate the
            #average amount of steps per month
            for days in range(1, DPM + 1):
                line = infile.readline()
                total_steps += int(line)
                counter += 1
            #Make calculations and print the appropraite things
            average = total_steps / counter
            if name == 'April' or name == 'March' or name == 'May' or name == 'June' or name == 'July' or name == 'August':
                name = name + '\t'
            elif name != 'December':
                print(name, '\t', format(average, ',.2f'), 'steps')
            elif name == 'December':
                print('December \t', format(average, ',.2f'), 'steps')
            else:
                print('Name was not found.')
            counter = 0
            total_steps = 0
        infile.close()
    except TypeError as err:
        print(err)