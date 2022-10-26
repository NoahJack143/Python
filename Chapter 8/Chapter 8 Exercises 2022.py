

#==========#

def sum_of_digits(): #Exercsise 2
    #sum of digits accepts no arguments
    #it will ask the user to enter a series of single digit numbers
    #it will then output the sum of the single digit numbers
    #validating will be used for the user input
    
    #Prompt the user for a series of single digit numbers without spaces
    ui = input('Enter a series of single digit numbers without spaces: ')
    
    #Create a boolean if needed variable and a checker
    if not ui.isdigit() or ui.isspace():
        cont = False
    else:
        cont = True
            
    #Check if needed
    while not cont:
        ui = input('Enter a series of single digit numbers WITHOUT spaces or letters.')
        
        #Check again
        if not ui.isdigit() or ui.isspace():
            cont = False
        else:
            cont = True
        
    #Get the sum of the numbers
    c = 0
    for number in ui:
        c += int(number)
    
    #Print the output
    print('The sum of your string is:', c)
    
#================================================================================#
    
def date_converter(): #Exercise 3
    #date converter accepts no arguments
    #it will read a string in the format of 01/02/2007 and
    #will output the date if the string is formatted correctly
    
    #List of dates and days
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                   'September', 'October', 'November', 'December']
    months = ['01','02','03','04','05','06','07','08','09','10','11','12'] #You could combine months and days into one list to make this shorter
    days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16',
            '17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    
    #Create a boolean variable and a while loop
    cont = False
    while not cont:
        
        #Try block
        try:
            
            #Ask the user for the date
            date = input('\nEnter a date in the format mm/dd/yyyy: ')
            
            #Check to see if the format is formatted correctly and split the date if so
            if date[:1].isdigit() and date[3:4].isdigit() and date[6:].isdigit() and date[2] == '/' and date[5] == '/' and date.isalnum():
                date_splitted = date.split('/')
            else:
                t = b
            
            #Check to see if the month, day, and year are all valid
            if date_splitted[0] in months and date_splitted[1] in days and len(date_splitted[2]) == 4:
                m = date_splitted[0]
                d = date_splitted[1]
                y = date_splitted[2]
            else:
                0/0
            
            #Check to see if the month and day and valid with each other
            if m == '02' and int(d) > 28:
                m += 1
            elif m =='04' or m == '06' or m == '09' or m == '11':
                if int(d) > 30:
                    m += 1
            
            #Check for the name of the month apply a name to m
            index = 0
            for month in months:
                if m == month:
                    m = month_names[index]
                else:
                    index += 1
            
        #If soemthing goes wrong, ask again and continue looping
        except NameError:
            print('\nCheck your formatting and make sure there are no letters.')
        except ZeroDivisionError:
            print('\nMake sure you month number and day number are actual month and day numbers.' +
                  '\nAlso make sure that your year has 4 digits.')
        except TypeError:
            print('\nMake sure that your day is appropriate according to your month.')
        #If something goes right, then print the outcome and stop looping
        else:
            print(f'\nThe date is: {m} {d}, {y}')
            cont = True
            
#================================================================================#
            
def morse_code(): #Exercise 4
    #morse code accepts no arguments
    #morse code will take input from the user and change
    #their message into morse code
    
    #Create lists for the morse code and create variables for the alphabet and numbers
    alphabet_list = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••', '--',
              '-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••']
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers_list = ['•----', '••---', '•••---', '••••-', '•••••', '-••••', '--•••', '---••', '----•', '-----']
    numbers = '1234567890'
    
    #Ask the user to input a message to be encoded
    message = input('Enter a mesage to encode to morse code: ')

    #Boolean variable and while loop to keep asking for a valid code
    cont = False
    while not cont:
        
        
        #try block
        try:
            
            #copy the message and then strip the old message
            message2 = message
            message = message.strip()
            
            #Check to see if the message is valid
            if message.isalnum():
                t = 1
            else:
                t = b
            
            #Check to see if the character is a number or letter and print the right morse code
            for letter in message2:
                if letter.isalpha():
                    index = alphabet.find(letter.lower())
                    morse_code = alphabet_list[index]
                    message2 = message2.replace(letter, morse_code + ' ')
                elif letter.isdigit():
                    index = numbers.find(letter)
                    morse_code = numbers_list[index]
                    message2 = message2.replace(letter, morse_code + ' ')
                else:
                    t = b
               
        #If something went wrong
        except NameError:
            message = input('Enter only numbers and letters: ')
        #If everything worked
        else:
            print(message2)
            cont = True
            
#================================================================================#
            
def phone_converter(): #Exercise 5
    #phone converter accepts no arguments
    #it will ask the user for a phone number
    #and then it will convert it into numbers
    
    #Create a two dimensional list with all of the letters and the alphabet
    numpad = [['abc'],['def'],['ghi'],['jkl'],['mno'],['pqrs'],['tuv'],['wxyz']]
    alphabet = 'abcdefghijklmnopqrstubwxyz'
    
    #Boolean variable with while loop
    cont = False
    while not cont:
        
        #try block
        try:
            
            #Ask the user for a number
            tpn = input('Enter a telephone number in the form of XXX-XXX-XXXX: ')
            
            #Check to see if the phone number is valid
            if tpn[:2].isalnum() and tpn[3] == '-' and tpn[4:6].isalnum() and tpn[7] == '-' and tpn[8:].isalnum():
                t = 1
            else:
                t = b
            
            #Check for every character in the tpn and move on accordingly
            for character in tpn:
                if character.isalpha():
                    index = alphabet.find(character)
                    
                else:
                    t = 1