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
    lne33 = infile.readline()
    
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
    line = sales_filereadline()
    
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
    
    #Get input the video user first
    videos = int(input('How many videos are in the project? '))
    length = int(input('What is the length of the videos? '))
    
    #open/create the file
    openfile = open('videotimes.txt', 'r'