#Welcome to Trimon!
#Trimon is an attempt to recreate Pokemon.

#Imports
import time
import turtle

#Functions that will be used in the main function
def start_game(): #This function will contain all the messages that will appear in the beginning of the game.
    intro_msg = 'Hello!'
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
    intro_msg = 'Welcome to the world of Trimon!'
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
    intro_msg = 'This world is populated with lots of Trimon that are ready to be caught by you!'
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    
    intro_msg = 'Before you can start your jounry, you must first tell us if you are a boy or a girl.'
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    time.sleep(1.2)
    print(' ')
    print(' ')
    USER_INPUT = 0
    
    #Ask the user to tell you if they're a boy or a girl
    while USER_INPUT == 0:
        
        #The beginning of the question
        intro_msg = 'Are you a boy or are you a girl'
        for letter in intro_msg:
            print(letter, end='')
            time.sleep(.03)
        gender = input('? ')
        print(' ')
        
        #Their first choice
        if gender == 'boy':
            intro_msg = """It's great to know you're a boy."""
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
                USER_INPUT = 1
            time.sleep(1.2)
            print(' ')
            print(' ')
        
        #Their second choice
        elif gender == 'girl':
            intro_msg = """It's great to know you're a girl."""
            for letter in intro_msg:
                print(letter, end='')
                USER_INPUT = 1
                time.sleep(.03)
            time.sleep(1.2)
            print(' ')
            print(' ')
            
        #If they didn't choose either of the options
        elif gender != 'boy' and gender != 'girl':
            intro_msg = """Please enter either "boy" or "girl" """
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
                USER_INPUT = 0
            time.sleep(1.2)
            print(' ')
            print(' ')
    
    #Continue the questions that appear in the beginning of the game
    intro_msg = 'Now, please tell me your name'
    for letter in intro_msg:
        print(letter, end='')
        time.sleep(.03)
    USER_NAME = input('. ')
    time.sleep(.5)
    print(' ')
    print(' ')
    
    intro_msg = 'Great!'
    for letter in intro_msg:
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
    X = -800
    Y = -800
    #Start by creating a grid for the map
    for variable in range (110):
        
        #Horizontal lines + Constants
        turtle.goto(X, Y)
        turtle.pendown()
        turtle.goto(X*-1, Y)
        turtle.goto(X, Y)
        turtle.penup()
        Y += 15
    
    #Constants for vertical lines
    X = -800
    Y = -800
    for variable in range(110):
        
        #Vertical lines
        turtle.goto(X, Y)
        turtle.pendown()
        turtle.goto(X, Y*-1)
        turtle.goto(X, Y)
        turtle.penup()
        X += 15
        
        
def Trimon(): #Main function to use
    
    #Beginning of the game messages
    
    
    #Begin using turtle to show graphics for the user
    begin_turtle()
