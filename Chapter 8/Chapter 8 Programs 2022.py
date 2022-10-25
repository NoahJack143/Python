#Imports
import login

def count_t(): #Program 8-1
    #count t accepts no arguents
    #it prompts the user for a word
    #and iterates through each letter
    #counting the number of upper and lower case t's
    #it outputs the total number of times it appeard in the word
    
    #Prompt the user for a word
    user_input = input('Please enter a word: ')
    
    #Create an accumualtor
    c = 0
    
    #Check to see how many times the letter 'T' or 't' appears in the word
    for letter in user_input:
        if letter.lower() == 't':
            c += 1
            
    #Print the output
    print('The letter T or t appears', c, 'times in the word:', user_input)
 
#==========#
 
#COUNT T IN KYLE'S WAY
def count_t_no():
    print('The letter T or t appears ' + str(input('Please enter a word: ').count('t' and 'T')) + ' times.')
    
#==========#
    
#f' formats everything as a string
#string are immutable (unreversible)
    
    
def concatenate(): #Program 8-2
    #concatenate accepts no arguments
    #it concatenates and prints the two strings
    #Carmen and Sandiego
    
    #print
    print('Where in the world in Carmen')
    
    #Concatenate
    print('Where in the world is Carmen' + ' Sandiego') #could also be name = Carmen. name += ' Sandiego'.
    
#==========#
    
def generate_login(): #Prgoram 8-4
    #get login accepts no arguments
    #it prompts the user for a first name, last name, and id number
    #it passes the values to login.get_long_name()
    #and receives the new user login
    
    #Prompt the user for the first name, last name, and id number
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idn = input('Enter your id number: ')
    
    #Call for the other function to create a new login
    new_login = login.get_login_name(first, last, idn)
    
    #Print the new login for the user
    print('Your system login name is:\n', new_login)
    
#==========#
    
def string_test(): #Program 8-5
    #string test accepts no arugments
    #it takes input from the user in the form of a string
    #and performs a veriety of testse on the string
    
    #get input from the user
    us = input('Enter a string to evaluate: ')
    
    #perform string tests
    if us.isalnum():
        print('The string only contains alphanumeric characters.')
    if us.isdigit():
        print('The string only contains digits.')
    if us.isalpha():
        print('The string aonly contains alpha characters.')
    if us.isspace():
        print('The stringonly contains whitespaces.')
    if us.islower():
        print('The string is all lowercase.')
    if us.isupper():
        print('The string is all uppercase.')
    
    print()
    print('Your string converted to all uppsercase is: ', us.upper())
    print('Your string converted to all lowercase is: ', us.lower())
    
#==========#
    
def validate_password(): #Program  8-7
    #validate password accepts noa rugments
    #it prompts the user for a password
    #and passes the password to login.valid_password
    #to loop while the password is invalid
    
    #Boolean variable with while loop
    cont = False
    while not cont:
        
        #prompt the user to enter a password
        password = input('Please enter your password: ')
        
        #Call for a function to check to requirements
        checker = login.valid_password(password)
        
        #Check to see if all requirements are met
        if not checker:
            print('The pasword you entered is not valid. Please try again.')
        else:
            cont = True
            
    #If requirements are met, print that the password is accepted
    print('Password accepted.')
    
#==========#
    
def repetition(): #Program 8-8
    #repetition accepts no aguments
    #it multiples 'z' by ranges(1,10)
    #then multiples 'z' by range(8,0,-1)
    
    #print z range(1,10-times increasing in length
    for count in range(1,10):
        print('Z' * count)
        
    for count in range(8, 0, -1):
        print('Z' * count)
        
#=========#
        
def string_split(): #Program 8-9
    #string split accepts no arguments
    #it splits the string one two three four
    #adding it to a list
    
    #Create the string to be split later
    string = 'one/two/thre/four'
    
    #spit the text
    string_splitted = string.split('/')
    
    #print
    print(string_splitted)
    
#==========#
    
def split_date(): #Program 8-10
    #split date accepts no arguments
    #it creates a date string of 11/26/2018
    #and pslits the date into mm dd yyyy
    
    #Create the string to be split later
    date = '11/26/2018'
    
    #split the date
    splitted_date = date.split('/')
    
    #assign the month, days, and years to theri own variables
    month = splitted_date[0]
    days = splitted_date[1]
    year = splitted_date[2]
    
    #Print the output
    print('Month:', month, '\nDay:', days, '\nYear:', year)