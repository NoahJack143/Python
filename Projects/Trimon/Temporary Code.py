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
    c = 0 #Counter
    
    #boolean variable
    finish = False
    
    while not finish:
        #Create a list for the intro messages
        intro_msgs = [{"msg1": "Hi there!", "msg2": " "},{"msg1": "Welcome to the world of Trimon!","msg2": " "},{"msg1": "My name is Professor Computer","msg2": "Everyone calls me the Computer Professor!"},
                     {"msg1": "That's right! This world is widely inhabited","msg2": "by mysterious creatures called Trimon!"},{"msg1": "Trimon have mysterious powers. They come in many","msg2": "shapes and live in many different places."},
                      {"msg1": "You humans live happily with Trimon! Living and","msg2": "working together, we complement each other."},{"msg1": "We help each other out to","msg2": "accomplish difficult tasks."},
                      {"msg1": "Having Trimon battle one another is particulurly popular,","msg2": "and it depens the bonds between people and Trimon."},{"msg1": "And that is why I research Trimon.","msg2": " "},
                      {"msg1": "Well, that's enough from me...","msg2": "Could you tell me about yourself?"}]
        
        #Start a nested loop for every message       
        for x in intro_msgs:
            for letter in x['msg1']:
                print(letter, end='')
                time.sleep(.03)
            if x['msg2'] != ' ':
                print(' ')
            for letter in x['msg2']:
                print(letter, end='')
                time.sleep(.03)
            time.sleep(1.2)
            print(' ')
            print(' ')
            c += 1 #Increase the accumulator for every loop(printed message)
            if c == 10: #Check to see if the loop as looped enough times. If so, then break the while loop
                finish = True
   
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
        #Print if they're a boy
        elif gender == 'boy':
            intro_msg = "You're a boy, right? (yes/no"
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            CONFIRMATION = input(") ").lower()
            time.sleep(1.2)
            print(' ')
        #Print if the're a girl
        elif gender == 'girl':
            intro_msg = "You're a girl, right? (yes/no"
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            CONFIRMATION = input(") ").lower()
            time.sleep(1.2)
            print(' ')
        #Check their response
        if CONFIRMATION == 'yes':
            USER_INPUT = 1
        elif CONFIRMATION == 'no':
            USER_INPUT = 0
        else:
            intro_msg = 'Please enter either "yes" or "no".'
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            time.sleep(1.2)
            print(' ')
            print(' ')
            CONFIRMATION = 0
            
    #Add variables for validations
    USER_INPUT = 0
    CONFIRMATION = 'no'
    
    #Start another while loop to ask the user for their name
    while USER_INPUT == 0:
        #Validation variable
        length_requirement = 1
        #Ask the user for their name
        intro_msg = "I'd like to know your name."
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
        if len(USER_NAME) > 10:
            length_requirement = 0
            intro_msg = 'Please enter a name that is less than 11 letters.'
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            time.sleep(1.2)
            print(' ')
            print(' ')
        
        if length_requirement == 1: #If the user's name meets the length requirement, then ask them if they entered the name they really want
            intro_msg = "Your name is "
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
            
            #Check their response
            if CONFIRMATION == 'yes':
                USER_INPUT = 1
            elif CONFIRMATION == 'no':
                USER_INPUT = 0
            else:
                intro_msg = 'Please enter either "yes" or "no".'
                for letter in intro_msg:
                    print(letter, end='')
                    time.sleep(.03)
                time.sleep(1.2)
                print(' ')
                print(' ')
                CONFIRMATION = 0

    #Set a variable to validation
    CONFIRMATION = 0
    length_requirement = 1
    #Begin a loop for the rival
    while CONFIRMATION == 0:
        #Ask the user questions about their rival
        intro_msg = 'Now, please tell us more about the boy living right next to you.'
        for letter in intro_msg:
            print(letter, end='')
            time.sleep(.03)
        time.sleep(1.2)
        print(' ')
        print(' ')
        
        intro_msg = 'What might his name be? (1-10 letters'
        for letter in intro_msg:
            print(letter, end='')
            time.sleep(.03)
        RIVAL_NAME = input(') ')
        time.sleep(.5)
        print(' ')
        print(' ')
        
        #Validate the length of the rival's name
        if len(RIVAL_NAME) > 10:
            length_requirement = 0
        if length_requirement == 1:
            intro_msg = RIVAL_NAME
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            intro_msg = "is his name right? (yes/no"
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            CONFIRMATION = input(') ')
        #Check the response
        if CONFIRMATION == 'yes':
            CONFIRMATION = 1
        elif CONFIRMATION == 'no':
            CONFIRMATION = 0
        else:
            intro_msg = 'Please enter either "yes" or "no".'
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            time.sleep(1.2)
            print(' ')
            print(' ')
            CONFIRMATION = 0
        
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
