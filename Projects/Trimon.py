#Welcome to Trimon!
#Trimon is an attempt to recreate Pokemon.

#Imports
import time
import turtle

#Start the game
def start_game():
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
        intro_msg = 'Are you a boy or are you a girl'
        for letter in intro_msg:
            print(letter, end='')
            time.sleep(.03)
        gender = input('? ')
        print(' ')
        if gender == 'boy':
            intro_msg = """It's great to know you're a boy."""
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
                USER_INPUT = 1
            time.sleep(1.2)
            print(' ')
            print(' ')
        elif gender == 'girl':
            intro_msg = """It's great to know you're a girl."""
            for letter in intro_msg:
                print(letter, end='')
                USER_INPUT = 1
                time.sleep(.03)
            time.sleep(1.2)
            print(' ')
            print(' ')
        elif gender != 'boy' and gender != 'girl':
            intro_msg = """Please enter either "boy" or "girl" """
            for letter in intro_msg:
                print(letter, end='')
                time.sleep(.03)
                USER_INPUT = 0
            time.sleep(1.2)
            print(' ')
            print(' ')
    #Extra information from the user that may or may not be used later on
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
    
    #Begin using turtle to create the map for the user
    turtle.pendown()
    turtle.penup()
    turtle.speed(0)
    #Constants for turtle
    X = -500
    Y = -500
    #Start by creating a grid for the map
    GRID_LOOP = 0
    while GRID_LOOP == 0:
        
        turtle.goto(X, Y)
        turtle.pendown()
        turtle.goto(X*-1, Y)
        turtle.goto(X, Y)
        Y += 3
        
start_game()
