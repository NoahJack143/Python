#Welcome to Trimon!
#Trimon is an attempt to recreate Pokemon.

#Imports
import time
import turtle

#Main function to call to start the game
def Trimon(): #Main function to use
    
    #Beginning of the game messages
    start_game()
    
    #Begin using turtle to show graphics for the user
    begin_turtle()

#=============Separator for each individual function that will be called for by Trimon()=============#
    
#Functions that will be used in the main function
def start_game(): #This function will contain all the messages that will appear in the beginning of the game.
    #start_game accepts no arguments
    #start game will print everything that is said in the beginning of the
    #Generation 5 pokemon games
    
    #accumulators
    c = 0 #c = counter
    
    #boolean variable
    finish = False
    
    while not finish:
        #Create a list for the intro messages
        intro_msg = [{"name": "Hi there!"},{"name": "Welcome to the world of Trimon!"},{"name": "My name is Professor Computer"},
                     {"name": "That's right! This world is widely inhabited"},{"name": "Trimon have mysterious powers. They come in many"},{"name": "You humans live happily with Trimon! Living and"},
                     {"name": "Welcome to the world of Trimon!"},{"name": "Welcome to the world of Trimon!"},{"name": "Welcome to the world of Trimon!"},
                     {"name": "Welcome to the world of Trimon!"},{"name": "Welcome to the world of Trimon!"},{"name": "Welcome to the world of Trimon!"},
                     {"name": "Welcome to the world of Trimon!"},{"name": "Welcome to the world of Trimon!"},{"name": "Welcome to the world of Trimon!"},
                     {"name": "Welcome to the world of Trimon!"},{"name": "Welcome to the world of Trimon!"},{"name": "Welcome to the world of Trimon!"},]
        intro_msg2 = [{"name": 'Everyone calls me the Computer Professor!'},{"name": "by mysterious creatures called Trimon!"},{"name": "shapes and live in many different places."},
                      {"name": "working together, we complement each other."},{"name": 'Everyone calls me the Computer Professor!'},{"name": 'Everyone calls me the Computer Professor!'},
                      {"name": 'Everyone calls me the Computer Professor!'},{"name": 'Everyone calls me the Computer Professor!'},{"name": 'Everyone calls me the Computer Professor!'},
                      {"name": 'Everyone calls me the Computer Professor!'},{"name": 'Everyone calls me the Computer Professor!'},{"name": 'Everyone calls me the Computer Professor!'},
                      {"name": 'Everyone calls me the Computer Professor!'},{"name": 'Everyone calls me the Computer Professor!'},{"name": 'Everyone calls me the Computer Professor!'},
                      {"name": 'Everyone calls me the Computer Professor!'},{"name": 'Everyone calls me the Computer Professor!'},{"name": 'Everyone calls me the Computer Professor!'},]
        #Start a loop for every message       
        for x in intro_msg:
            c += 1
            if c == 1 or c == 2:
                for letter in x['name']:
                    print(letter, end='')
                    time.sleep(.03)
                time.sleep(1.2)
                print(' ')
                print(' ')
            else:
                for y in intro_msg2:
                    for letter in y['name']:
                        print(letter, end='')
                        time.sleep(.03)
                    print(' ')
                    for letter in y['name']:
                        print(letter, end='')
                        time.sleep(.03)
                    time.sleep(1.2)
                    print(' ')
                    print(' ')

            
 
     
    intro_msg = "You humans live happily with Trimon! Living and"
    intro_msg2 = "working together, we complement each other."
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    print(' ')
    for letter in intro_msg2:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
    intro_msg = "We help each other out to"
    intro_msg2 = "accomplish difficult tasks."
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    print(' ')
    for letter in intro_msg2:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
    intro_msg = "Having Trimon battle one another is particulurly popular,"
    intro_msg2 = "and it depens the bonds between people and Trimon."
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    print(' ')
    for letter in intro_msg2:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
    intro_msg = "And that is why I research Trimon."
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
    intro_msg = "Well, that's enough from me..."
    intro_msg2 = "Could you tell me about yourself?"
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    print(' ')
    for letter in intro_msg2:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
    USER_INPUT = 0
    CONFIRMATION = 'no'
    
    #Ask the user to tell you if they're a boy or a girl
    while USER_INPUT == 0:
        
        #The beginning of the question
        intro_msg = 'Are you a boy or a girl? (boy/girl'
        for letter in intro_msg:
            print(letter, end='')
            time.sleep(.03)
        gender = input(') ').lower()
        print(' ')
        
        #If they didn't choose either of the options
        if gender != 'boy' and gender != 'girl':
            intro_msg = """Please enter either "boy" or "girl" """
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
                USER_INPUT = 0
                CONFIRMATION = 'no'
            time.sleep(1.2)
            print(' ')
            print(' ')
        
        elif gender == 'boy':
            intro_msg = "You're a boy, right? (yes/no"
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            CONFIRMATION = input(") ").lower()
            time.sleep(1.2)
            print(' ')
        
        elif gender == 'girl':
            intro_msg = "You're a girl, right? (yes/no"
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            CONFIRMATION = input(") ").lower()
            time.sleep(1.2)
            print(' ')
        
        if CONFIRMATION == 'yes':
            USER_INPUT = 1
        else:
            USER_INPUT = 0
            
    USER_INPUT = 0
    CONFIRMATION = 'no'
    
    #Start another while loop to ask the user for their name
    while USER_INPUT == 0:
        
        intro_msg = "I'd like to konw your name."
        intro_msg2 = "Please tell me. (Must be from 1-10 letters"
        for letter in intro_msg:
            print(letter, end='')
            time.sleep(.03)
        print(" ")
        for letter in intro_msg2:
            print(letter, end='')
            time.sleep(.03)
        USER_NAME = input(') ')
        time.sleep(1.2)
        print(' ')
        
        #ADD A CHECKER FOR THE AMOUNT OF LETTERS THERE ARE IN THE USERS NAME LATER
        
        intro_msg = "Your name is " #ADD AN IF STATEMENT LATER WHEN THE CHECKER IS ADDED AND INDENT EVERYTHING NEEDED
        for letter in intro_msg:
            print(letter, end='')
            time.sleep(.03)
        for letter in USER_NAME:
            print(letter, end='')
            time.sleep(.03)
        intro_msg = '? (yes/no'
        for letter in intro_msg:
            print(letter, end='')
            time.sleep(.03)
        CONFIRMATION = input(') ').lower()
        time.sleep(1.2)
        print(' ')
        print(' ')
        
        if CONFIRMATION == 'yes':
            USER_INPUT = 1
        else:
            USER_INPUT = 0
            
    #End the questions for now...
            
    intro_msg = "So your name's "
    intro_msg2 = "by mysterious creatures called Trimon"
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    for letter in USER_NAME:
        print(letter, end='')
        time.sleep(.03)
    print(' ')
    for letter in intro_msg2:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
            
        
            
    
    intro_msg = 'Now, please tell us more about the boy living right next to you.'
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
    RIVAL_NAME = 'none'
    intro_msg = 'What might his name be'
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    RIVAL_NAME = input('? ')
    time.sleep(.5)
    print(' ')
    print(' ')
    
    intro_msg = """Now it's time for you to begin your journy."""
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
    intro_msg = 'Be sure to catch lots of Trimon and fill the tridex'
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
def begin_turtle(): #Begin using turtle to create the map for the user
    turtle.pendown()
    turtle.penup()
    turtle.speed(0)
    #Constants for horizontal lines
    X = -600
    Y = -600
    #Start by creating a grid for the map
    for variable in range (60):
        
        #Horizontal lines + Constants
        turtle.goto(X, Y)
        turtle.pendown()
        turtle.goto(X*-1, Y)
        turtle.goto(X, Y)
        turtle.penup()
        Y += 25
    
    #Constants for vertical lines
    X = -600
    Y = -600
    for variable in range(60):
        
        #Vertical lines
        turtle.goto(X, Y)
        turtle.pendown()
        turtle.goto(X, Y*-1)
        turtle.goto(X, Y)
        turtle.penup()
        X += 25
        
    turtle.done()
