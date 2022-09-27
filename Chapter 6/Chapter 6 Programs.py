#Imports
import os #Operating System. Used for giving Python more access to files

def file_write():
    #accepts no arguments
    #it opens the file lotr.txt
    #and writes the names of three lotr characters
    
    #open foile
    outfile = open('lotr.txt', 'w') #If the file didn't exist before, then Python will create a file
    
    #write three lotr names
    outfile.write('Frodo Baggins\n')
    outfile.write('Grandalf\n')
    outfile.write('Aragorn\n')
    
    #close the file
    outfile.close()
    
def file_read():
    #accepts no arguments
    #it opens the file lotr.txt
    #and reads the entire conents of the file
    #it then outputs the contents of the file
    
    #open the file
    infile = open('lotr.txt', 'r')
    
    #read the contents
    file_contents = infile.read()
    
    #Close the file
    infile.close()
    
    #print the contents
    print(file_contents)
    
def line_read():
    #accepts no arguments
    #it opens the file lotr.txt
    #and reads the conents of the file one line at a time
    #it then outputs the conents of the file
    
    #open the file
    infile = open('lotr.txt', 'r')
    
    #read the three lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    #close the file
    infile.close()
    
    #print the lines
    print(line1)
    print(line2)
    print(line3)

def write_names(): #Program 6-4
    #write names accepts no arguments
    #it prompts the user for the names of three friends
    #and assigns each name to a unique variable
    #it opens friends.txt and writes each name to the file
    #on it's own line and the file
    
    #Text for the prompts
    print('Please enter the names of three friends.')
    
    #Prompt the user to enter the name of their friends
    friend1 = input('Friend 1:')
    friend2 = input('Friend 2:')
    friend3 = input('Friend 3:')
    
    #open the file
    open_file = open('friends.txt', 'a') #'a' stands for appending, which means adding onto.
    #'w' stands for write, which will rewrite the file, and 'r' stands for reading
    
    #write in the file
    open_file.write(friend1 + '\n')
    open_file.write(friend2 + '\n')
    open_file.write(friend3 + '\n')
    
    #close file
    open_file.close()
    
    #print their names
    print(friend1)
    print(friend2)
    print(friend3)
    
def strip_newline(): #Program 6-5
    #strip newline accepts noa rguments
    #it opens the file lotr.txt and reads each line
    #it strips the newline '\n' charactesr from each line
    #and prints the lines
    
    #open the file
    infile = open('lotr.txt', 'r')
    
    #read the lines and strip them
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    #Strip them
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    #Close the file
    infile.close()
    
    #print the lines
    print(line1)
    print(line2)
    print(line3)
    
def write_numbers(): #Program 6-6
    #write numbers accepts no arguments
    #it takes input from the user in the form of three inteers
    #it opens the file numbers.txt
    #and writes the three numbers to the file as strings
    
    #Gain input from the user
    number1 = int(input('Please enter a number: '))
    number2 = int(input('Please enter a number: '))
    number3 = int(input('Please enter a number: '))
    
    #Print another thing
    print('Your numbers have been written to numbers.txt.')
    
    #open/create the file
    open_file = open('numbers.txt', 'w')
    
    #write the numbers into the file as strings
    open_file.write(str(number1) + '\n')
    open_file.write(str(number2) + '\n')
    open_file.write(str(number3) + '\n')
    
    #Close the file
    open_file.close()
    
def read_numbers(): #Program 6-7
    #read numbers accepts no arguments
    #it opens the file numbers.txt and reads in each line
    #converting each from a string to an integer
    #it totals and outputs the three numbers and their ttoal
    
    #open the file and get the numbers
    open_file = open('numbers.txt', 'r')
    
    #gets the lines from the file
    num1 = int(open_file.readline())
    num2 = int(open_file.readline())
    num3 = int(open_file.readline())
    
    #close the file
    open_file.close
    
    #Get the sum of thsoe numbers
    total = num1 + num2 + num3
    
    print('Here is your problem:', num1, '+', num2, '+', num3, '=', total)
    
def write_sales(): #Program 6-8
    #write sales accepts noa rguments
    #it prompts the user for the number of days to input slaes
    #for each iteration it writes the sale to the file sales.txt
    #after all days have been processed
    #it closes the file and outputs a message
    
    #Prompt the user for the amount of sales
    sales = int(input('How many days do you want to enter sales for? '))
    
    #Open/create the file
    infile = open('sales.txt', 'w')
    
    #Begin the loop for the sales to be put into
    for RANDOM_INTEGER in range(1, sales + 1):
        print('Enter the sales for day #', RANDOM_INTEGER, end='')
        sale4day = int(input(': '))
        infile.write(str(sale4day) + '\n')
        
    #Close the file
    infile.close()
    
    #When the file closes, print this
    print('All data has been saved to sales.txt')
    
def read_sales(): #Program 6-9
    #read sales accepts no arguments
    #it opens and reads from sales.txt
    #it loops until it reaches the end of the file
    #each iteration of the loop will output the amount
    #and read the next line
    
    #open the file
    infile = open('sales.txt', 'r')
    
    #begin a loop to output each line that is in the file
    for line in infile:
        amount = float(line)
        print(amount)
        
    #When the loop ends, close the file
    infile.close()
    
def read_sales_while():
    
    #Open the file
    sales_file = open('sales.txt', 'r')
    
    #Prime the file
    line = sales_file.readline()
    
    #Begin the loop and get each line
    while line != '':
        amount = float(line)
        
        print(format(amount, ',.2f'))
        
    #Close the file
    sales_file.close()
        
def write_video_times(): #Program 6-11
    #write video times accpets no arguments
    #open the videotimes.txt
    #it creates a loop for the total videos
    #writes the video length to a file
    #and then closes the file
    
    #Get initial input for the video user first
    videos = int(input('How many videos are in the project? '))
    
    #open/create the file
    openfile = open('video_times.txt', 'w')
    
    #Create the loop in order to get the length of each video
    for loop in range(1, videos + 1):
        print("What is the length for the ", loop, "st vide", sep='', end='')
        length = input("o? ")
        openfile.write(str(length) + '\n') #'\n' creates a new line
    #The reason "'\n'" is outside the "str(length)", is because the length will be converted
    #to a string, AND THEN it will have that new line added. You can't convert a new line.
    
    #When the loop ends, close the file
    openfile.close()
    
    #Tell the user that the times have been written into the file
    print('All times have been written to video_times.txt.')
        
def read_video_times(): #Program 6-12
    #read video times accepts no arguments
    #it will read the times that are within the file that was created
    #in the last program
    
    #Open the file
    openfile = open('video_times.txt', 'r')
    
    #Set the variable before the assignment
    video = 1
    time = 0
    running_total_time = 0
    
    #Create a loop to read each line individually on their own line
    for time in openfile:
        #Strip it
        time = time.rstrip('\n')
        
        #Then print the video # and the length of the video in seconds
        print('For video #' + str(video) + ', the length was ',time, ' seconds long', sep='')
        
        #Get the running total of the time and increase the counter
        video += 1
        running_total_time += float(time)
    
    #When the loop ends, close the file
    openfile.close()
    
    #Then output the total time for all the videos
    print('The running total of time is', running_total_time, 'seconds')
    
def save_emp_records(): #Program 6-13
    #save emp records accepts no arguments
    #it prompts the user for the the number of employee records
    #it opens a file employees.txt and saves
    #the records Name, ID #, and Department to the file
    #it outputs a finished message with the filename
    
    #Ask the user for the amount of employee records they're going to put in
    employees = int(input('How many employee records do you want to enter? '))
    
    if employees > 0:
        
        #Open the file
        openfile = open('employees.txt', 'w')
        
        #Create the loop and begin saving and asking the user for data
        for line in range(1, employees + 1):
            #The employee number
            print('Enter data for employee #', line, sep='')
            
            #prompt the user for more data
            name = input('Name: ')
            ID = input('ID Number: ')
            department = input('Department: ')
            print(' ')
            
            #Write all the data for that employee
            openfile.write(name + '\n')
            openfile.write(ID + '\n')
            openfile.write(department + '\n')
        
        #When the loop ends, close the file
        openfile.close()
        
        #Tell the user that you've saved the data
        print('All records were saved to employees.txt.')
        
    else:
        print('You need employees')
    
def read_emp_records(): #Program 6-14
    #read emp records accepts no arguments
    #it opens the file employees.txt
    #and loops for each line in the file
    #outputting the record for Employee Name, ID #, and Department
    
    #open the file
    openfile = open('employees.txt', 'r')
    
    #Create the variables
    counter = 1
    name = openfile.readline() #Prime the variable
    
    #Begin the while loop to reach each of the names as long as there is text to be read
    while name != '': #This is saying, 'run while name does not equal nothing'
        #Fetch the data and assign varaibles to them
        line1 = name #The name
        line2 = openfile.readline() #ID number
        line3 = openfile.readline() #Department
        
        #Strip the text from the file
        line1 = line1.rstrip('\n')
        line2 = line2.rstrip('\n')
        line3 = line3.rstrip('\n')
        
        #Print the data
        print('Name: ', line1)
        print('ID #: ', line2)
        print('Department: ', line3)
        
        #Get the new varaible for name to make sure that there is still text to check
        name = openfile.readline()#This is to make the WHILE LOOP end eventually
        print(' ') #Make a space between everything to make it all look good
    
    #When name equals nothing, the loop will end and close the file
    openfile.close()
    
    #Tell the user one last thing
    print('That is all the data')
    
def write_coffee(): #Program 6-15
    #write coffee accepts no arguments
    #it opens the file coffee.txt to append
    #it loops while the user wants to continue entering records
    #it prompts the user for the coffee description and number of pounds
    #the user should be prompted if they want to continue
    
    #prime the loop, open the file to append, display the header
    another = 'y'
    coffee_file= open('coffee.txt', 'a')
    
    #loop to get the records
    while another.lower() == 'y':
        print('Enter the following coffee data:\n')
        desc = input('Description: ')
        pounds = input('Quantity (in pounds): ')
        
        #append the data to the file
        coffee_file.write(desc + '\n')
        coffee_file.write(pounds + '\n')
        
        #prompt for another entry
        another = input('\nDo you wish to enter another coffee? (y to continue): ')
    
    #Close the file and output saved message
    coffee_file.close()
    print('\nAll data appended to coffee.txt.')
    
def read_coffee(): #Program 6-16
    #read coffee accepts no arguments
    #it loops to read the records in coffee.txt
    #and outputs the description and pounds of coffee
    
    #open coffee.txt and read the first description
    coffee_file = open('coffee.txt', 'r')
    desc = coffee_file.readline()
    
    #loop to read, strip, and output each record
    while desc != '':
        pounds = coffee_file.readline()
        
        #strip the newline
        desc = desc.rstrip('\n')
        pounds = pounds.rstrip('\n')
        
        print('\nDescription:', desc)
        print('Quantity (in pounds):', pounds)
        
        #Get the new description
        desc = coffee_file.readline() #Without this, the WHILE LOOP will run endlessly
        
    #Close the file and output to the user
    coffee_file.close()
    print('\nAll records retrived.')
    
def search_coffee(): #Program 6-17
    #search coffee accepts no arguments
    #it searched coffee.txt for a string the user enters
    #if no record matches, it outputs a message to the user
    
    #a boolean flag to determine search status
    found = False
    
    #get input from the user
    search = input('Enter a coffee description to search for: ')
    
    #open the file coffee.txt
    coffee_file = open('coffee.txt', 'r')
    
    #get the frist description from the file
    desc = coffee_file.readline()
    
    #loop to read each line of the file
    while desc != '':
        pounds = coffee_file.readline()
        
        #Strip the newline from the descriptoin
        desc = desc.rstrip('\n')
        
        if desc.lower() == search.lower(): #Determines if the record is foundn and displays the record if so
            print('\nRecordfound:\n')
            print('Description:', desc)
            print('Quantity (in pounds):', pounds)
            found = True #toggle the flag varaible to true
        #get the next descriptoin
        desc = coffee_file.readline()
        
    #Close the file when all the descriptions were reached
    coffee_file.close()
    
    if not found: #Found = False #not stands for 'if found = false
        print('\nThe record was not found.')
        
def modify_coffee(): #Program 6-18
    #modify coffee accepts no arguments
    #it imports the os module - this is needed to perform OS related file commands
    #it searches through the records and allows the user to modify the quantity
    
    #boolean flag variable
    found = False
    
    #Get the serach description and new quantity
    search = input('Enter the coffee description to modify: ')
    new_qty = input('Enter the new quantity: ')
    
    #open the coffee.txt file to read and a new temporary file to write
    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    #read the first description
    desc = coffee_file.readline()
    
    #loop to read the process each line
    while desc != '':
        qty = coffee_file.readline()
        
        #strip newline
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower() == desc.lower(): #Coffee found
            #write the description and new quantity to the temporary file
            temp_file.write(desc + '\n')
            temp_file.write(new_qtu + '\n')
            found = True
        else: #these are not the droids you're loking for
            #Write the original record to the temp file
            temp_file.write(desc + '\n')
            temp_file.write(qty + '\n')
            
        #read the next description
        desc = coffe_file.readline()
        
    #all records have been processed, remove and rename files
    coffee_file.close()
    temp_file.close()
    
    #delete the original
    os.remove('coffee.txt')
    
    #rename the temp file to coffee.txt
    os.rename('temp.txt', 'coffee.txt')
    
    #description not found
    if found == False:
        print('\nRecord not found.')
    else:
        print('THe quantity for', search, 'has been updated to', new_qty, 'pounds.')
