import turtle

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
        
        #random can be used fo the trimon

            
