

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
            if date[:1].isdigit() and date[3:4].isdigit() and date[6:].isdigit() and date[2] == '/' and date[5] == '/':
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
    #get input from thw user, convert the phone number, and output the convertted number
    #Create a two dimensional list with all of the letters and the alphabet
    numpad = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    #Boolean variable with while loop
    cont = False
    while not cont:
        #try block
        try:
            #Ask the user for a number and copy their message
            tpn = input('Enter a telephone number in the form of XXX-XXX-XXXX: ')
            #Check to see if the phone number is valid
            if tpn[:2+1].isalnum() and tpn[3] == '-' and tpn[4:6+1].isalnum() and tpn[7] == '-' and tpn[8:].isalnum() and len(tpn) == 12:
                t = 1
            else:
                t = b
            #Check for every character in the tpn and move on accordingly + Accumulator
            for character in tpn:
                index = 0
                for group in numpad:
                    if not character.isalpha():
                        break
                    elif character.lower() in group:
                        tpn = tpn.replace(character, str(index))
                        break
                    else:
                        index += 1      
        #Run the excepts after the loop is over
        except NameError:
            print('There is an issue with your input.')
        else: #If everything works, output the new phone number
            print('Here is your convereted telephone number:', tpn)
            cont = True
            
#================================================================================#
            
def avg_num_words(): #Exercise 6
    #avg num words accepts no arguments
    #it will read froma file and will calculate the total
    #number of words, total number of sentences, and average
    #number of words per sentence in the document
    #A WORD IS CONSIDERED ANYTHING SEPARATED BY A SPACE
    
    #create a try block
    try:
        
        #open the file
        file = 'text.txt'
        infile = open(file, 'r')
        
        #Put every thing from the file and put it into a list
        contents = ''
        for line in infile:
            contents += line
        
        #Split the text base on the new lines to find the amount of sentences
        sentences = contents.split('\n')
        
        #Find out how many sentences there are in total
        index_s = 0
        for sentence in sentences:
            index_s += 1
        
        #Split the text base on spaces to find out how many words there are
        contents = contents.replace('\n', ' ') #Take out the new lines
        words = contents.split(' ') #Split every single word by splitting the spaces
        
        #Find out how many words there are in total
        index_w = 0
        for word in words:
            index_w += 1
        
        #Calculate the average words per sentence
        average = index_w / index_s
    
    #If there is a problem, run the exception
    except:
        print('There was a problem with the file or the calculations')
    else:
        print('The file',file,'has',index_w,'words.\n' +
              'There are',index_s,'total sentences.\n' +
              'The average number of words per sentence is:',format(average, '.2f'))

#================================================================================#
        
def igpay_atinlay(): #Exercise 12
    #igpya_atinlay accepts no arguments
    #it will convert english words into "Pig Latin"
    #it will output the user's message in "Pig Latin"
    
    #Get a message from the user
    message = input('Enter a message to convert to pig latin: ')
    
    #Separate every word in the user's message
    message = message.split()
    
    #Create an empty list for the converted words
    new_message = []
    
    #Make a loop that will look at every word
    index = 1
    for word in message:
        word = word[1:].upper() + word[0].upper() + 'AY '
        new_message.append(word)
        
    #Print the new message
    for word in new_message:
        print(word, end='')
        
#================================================================================#
        
def pb_main(): #Exercise 13
    #pb main accepts no arguments
    #it will call for anther function
    #and it will find out the most and least
    #frequently occuring lotto numbers
    print('hi')
    #Call for the function, pb_frequency, to find out the frequency of all lotto numbers
    
def pb_frequency(): #For Exercise 13
    #pb frequency accepts no arguments
    #pb frequency will find out how often each number appears
    #it will open the file pbnumbers.txt and will read all
    #of the numbers within the file
    
    #open the file
    infile = open('pbnumbers.txt', 'r')
    
    #move everything from within the file into a single string and then split them by spaces
    contents = ''
    for line in infile:
        contents += line.replace('\n', ' ')
    contents = contents.split()
    
    
    #Create a list that will have all of the numbers the could be chosen
    lotto_numbers = ['01','02','03','04','05','06','07','08','09']
    for num in range(1,69):
        lotto_numbers.append(str(num))
        
    #Create an empty list, a boolean variable, and then an accumulator, then make a nested loop, and then a try block
    frequency = []
    c = 0
    for num in lotto_numbers:
        c = contents.count(str(num))
        frequency.append(c)
    print(frequency)
    
pb_frequency()
