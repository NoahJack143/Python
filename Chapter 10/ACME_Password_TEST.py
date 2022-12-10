#Imports
#-----#
import pickle
import random

#-----#

def bot_checker(): #THIS WILL LIKELY NOT BE USED
    
    #Try to open the files and read them, if an Error occurs, create the files and exit
    try:
        infile = open('words.dat', 'rb')
    except:
        print('The file, words.dat, does not exist...')
    else:
        #Create the list of words
        words = pickle.load(infile)
        
        #Create a list for the colors of the rainbow
        rainbow_colors = ['red','orange','yellow','green','blue','purple']
        
        #Create a code list for teh colors of the rainbow
        code_list = ['der','egnaro','wolley','neerg','eulb','elprup']
        
        #Loop until there are proper values in the color_values list
        while True:
            
            #Create / reset the values for the colors
            color_values = [0,0,0,0,0,0]
            
            #Create / reset the values for the random words
            random_words = []
            
            #Pick three random words and append them to the list
            for i in range(0,3):
                random_words.append(words[random.randint(0,len(words))])
                
            #Put the three random words into a single string
            string = '' #Create an empty string first
            for i in random_words:
                string+=i
                
            #For every letter in the string, find out if they match any of the first letters of the colors in the rainbow
            #If so, add an amount to the colors value
            for letter in string:
                for color in rainbow_colors:
                    if letter[0] == color[0]:
                        index = rainbow_colors.index(color)
                        color_values[index] += 1
            
            #Check to see if there are two maxes in the list, if so, repeat this process.
            color_values_sorted = list(sorted(color_values, reverse=True))
            if color_values_sorted[0] == color_values_sorted[1]:
                continue
            else:
                break
        
        #Find out which coded color to use
        wanted_answer = code_list[color_values.index(color_values_sorted[0])]
        
        #Tell the user the needed information to find the code
        print(f'\nHere is the piece of information you need to find the password: {string}\n')
        
        #Finally, ask the user for a code
        user_answer = input('What is the answer to this code? (hint: colors of the rainbow) ')
        
        #Check the user's input
        if wanted_answer == user_answer:
            print('\nYou have the right answer!')
            return True
        else:
            print('\nSorry, you have the wrong answer.')
            return False
    
    
def bot_checker2():
    
    #Create a 2-dimentional list
    boxes = [['[0]','[0]','[0]'],
             ['[0]','[0]','[0]'],
             ['[0]','[0]','[0]']
             ]
    
    #Pick a random number between 1 and 9
    selected_box = random.randint(1,9)
    
    #Based on the selected_box, find where that box is within the list
    if selected_box > 6:
        selected_box -= 7
        row = 2
    elif selected_box > 3:
        selected_box -= 4
        row = 1
    else:
        selected_box -= 1
        row = 0
        
    #Replace the selected box in the list, boxes, with a new box
    boxes[row][selected_box] = '[1]'
    
    #Show the user the boxes
    for rows in boxes: print(rows)
    
    #VALIDATION
    while True:
        try:
            #Ask the user where the box is at
            where = int(input('\nWhich box has the number 1 in it? '))
            break
        except:
            print('\nEnter a number representing the wanted box.')
    
    #Check the row based on their response
    if where > 6:
        where -= 7
        row = 2
    elif where > 3:
        where -= 4
        row = 1
    else:
        where -= 1
        row = 0
    
    #Check to see if their response is correct and respond accordingly
    if boxes[row][where] == '[1]':
        print('\nYou have selected the right box.')
        return True
    else:
        print('\nYou have chosen the wrong box.')
        return False
    
def admin_information(wanted_info):
    
    #Check to see what the wanted info is and return the wanted info
    if wanted_info == 'password':
        return '1aJ7*'
    else:
        #If the user hasn't passed the right information, return nothing
        return
        
#----------------CLASSES----------------#
        
class Users:
    
    #---Attributes---#
    
    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
        
    def __str__(self):
        return f'\nUsername: {self.__username}\nPassword: {self.__password}\nEmail: {self.__email}'
    
    #---Modules---#
    
    
    