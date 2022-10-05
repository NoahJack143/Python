#Welcome to Trimon!
#Trimon is an attempt to recreate Pokemon.

#Imports
import time
import turtle
import random

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
        #If the the rival's name is longer than 10 characters
        if len(RIVAL_NAME) > 10:
            length_requirement = 0
            CONFIRMATION = 'no'
            intro_msg = "The rival's name can not be longer than 10 letters."
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            time.sleep(1.2)
            print(' ')
            print(' ')
        #If the rival's name is equal to or less than 10, change the length_requirement
        elif len(RIVAL_NAME) <= 10:
            length_requirement = 1
            #If the length_requirement is met, then ask the user to confirm the rival's name
        if length_requirement == 1:
            intro_msg = RIVAL_NAME
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            intro_msg = "is his name right? (yes/no"
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            CONFIRMATION = input(') ').lower()
        #Check the response
        if CONFIRMATION == 'yes':
            CONFIRMATION = 1
        elif CONFIRMATION == 'no':
            CONFIRMATION = 0
        else:
            #If the user didn't type "yes" or "no", print this and make the confirmation = 0
            intro_msg = 'Please enter either "yes" or "no".'
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
            time.sleep(1.2)
            print(' ')
            print(' ')
            CONFIRMATION = 0
        
    #Create a new list to tell the user that they are now ready to begin their jouney
    intro_msgs = [{"msg1": "Now it's time for you to begin your journey.", "msg2": "", 'msg3': ''},{"msg1": "Be sure to catch lots of Trimon and fill the Tridex","msg2": "", 'msg3': ''},
                  {"msg1": "\t\t\t\t=== IMPORTANT ===", "msg2": "The size of the turtle screen is meant to be the initial size given to you when turtle first starts up.",
                   'msg3': 'Please do not change the size of the screen.'},{'msg1': 'Now enjoy the game!', 'msg2': '', 'msg3': ''}
                ]
    #Accumulator
    c = 0 #Counter
    finish = False

    #print every message accordingly, and change the times when necessary
    while not finish:   
        #Start a nested loop for every message       
        for x in intro_msgs:
            if c < 2: #If the loop hasn't looped more than or equal to 2 times, print these
                for letter in x['msg1']:
                    print(letter, end='')
                    time.sleep(.03)
                if x['msg2'] != '':
                    print(' ')
                if x['msg3'] != '' and x['msg2'] != '':
                    print(' ')
                for letter in x['msg2']:
                    print(letter, end='')
                    time.sleep(.03)
                time.sleep(1.2)
                print(' ')
                print(' ')
            elif c == 2: #If the loop has looped exactly 2 times, print these
                for letter in x['msg1']:
                    print(letter, end='')
                    time.sleep(.1)
                time.sleep(1.2)
                print(' ')
                for letter in x['msg2']:
                    print(letter, end='')
                    time.sleep(.1)
                time.sleep(1.2)
                print(' ')
                for letter in x['msg3']:
                    print(letter, end='')
                    time.sleep(.1)
                time.sleep(1.2)
                print(' ')
                print(' ')
            elif c > 2: #If the loop has looped more than 2 times, then print this
                for letter in x['msg1']:
                    print(letter, end='')
                    time.sleep(.03)
                time.sleep(1.2)
                print(' ')
                
            c += 1 #Increase the accumulator for every loop(printed message)
            if c == 4: #Check to see if the loop as looped enough times. If so, then break the while loop
                finish = True
    
def begin_turtle(): #Begin using turtle to create the map for the user
    #begin turtle accepts no arguments
    #it will create the map for the user and will change according to
    #whatever the user wants
    
    #PRE settings for turtle
    turtle.speed(0) #set turtle's speed
    turtle.hideturtle() #hide turtle
    turtle.delay(0) #make turtle have no delay
    turtle.screensize(400,300) #size of the screen
    turtle.pencolor('#000000') #This will be the normal pen color that is used
    
    #Variables for the starting x and y position
    x = -400
    y = -300
    
    #Accumulator
    c = 0 #Counter
    finish = False
    
    #Set the color for the grid
    turtle.pencolor('#d9d9d9')
    
    #Begin creating the grid for Trimon
    #Begin by creating the horizontal lines
    while not finish:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(-x,y)
        
        y += 30
        c += 1
        if c == 20:
            finish = True
    #Reset the accumulators
    c = 0 #Counter
    finish = False
    
    #Now make the vertical lines
    while not finish:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x,-y)
        
        x += 30
        c += 1
        if c == 25:
            finish = True
            
    #Make the surroundings
    #CREATE THE MODULE 'Trimon Objects' AND CREATE TREES, HOUSES, AND OTHER OBJECTS THAT WILL BE USED IN THE GAME
            
    turtle.done()
