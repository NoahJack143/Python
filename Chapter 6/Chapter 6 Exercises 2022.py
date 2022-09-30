#Imports
import random

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
        amount_of_ran = int(input('How many random numbers would you like to generate? '))
        
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
                
        else:
            print('Please enter a number that is greater than 0')
    #If the try block fails, then have excepts here
    except ValueError:
        print('invalid literal for int() with base 10: ', amount_of_ran)
    except:
        print('An error has occured somewhere.')
    else:
        print('You have successfully generated the numbers.')

ran_num_reader(): #Exercise 8
    #ran num reader accepts no arguments