import turtle
import time

def turtle_position_test():
    #this function is here to test the position of turtle
    #this will help with the barriers that are going to be used in the game
    #Refer back to Chapter 3 Exercises 2022 --- hit_the_target
    
    turtle.goto(5, 5) #Feel free to change this to see whether the if statement with work
    if turtle.xcor == 5 and turtle.ycor == 5: #This will test to see if turtle is inside the barrier or not
        print("Hello there")
    elif turtle.xcor != 5 or turtle.ycor != 5: #Same with this line
        print("Tutle is not within or on the barrier")
        
#=============================================================#
        
        #random can be used fo the trimon that the user will encounter
        
#=============================================================#

            
def test():
    if len(name) > 8:
        c = True
    c = False
    
#=======================================#
    
def message_test():
    #message test accepts no arguments
    #it will test if the message works

    intro_msgs = [{"msg1": "Now it's time for you to begin your journey.", "msg2": "", 'msg3': ''},{"msg1": "Be sure to catch lots of Trimon and fill the Tridex","msg2": "", 'msg3': ''},
                  {"msg1": "\t\t\t\t=== IMPORTANT ===", "msg2": "The size of the turtle screen is meant to be the initial size given to you when turtle first starts up.",
                   'msg3': 'Please do not change the size of the screen.'},{'msg1': 'Now enjoy the game!', 'msg2': '', 'msg3': ''}
                ]
    #Accumulator
    c = 0 #Counter
    finish = False
    second_msg = False

    #print every message accordingly, and change the times when necessary
    while not finish:   
        #Start a nested loop for every message       
        for x in intro_msgs:
            if c < 2:
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
            elif c == 2:
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
            elif c > 2:
                for letter in x['msg1']:
                    print(letter, end='')
                    time.sleep(.03)
                time.sleep(1.2)
                print(' ')
                
            c += 1 #Increase the accumulator for every loop(printed message)
            if c == 4: #Check to see if the loop as looped enough times. If so, then break the while loop
                finish = True

