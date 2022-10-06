#Trimon Objects is a module that will contain functions for objects that will be used in Trimon
#such as houses, trees, and other things.

#Imports
import turtle

#This will be used for the trees in Trimon
def tree(x, y):
    #tree accepts no arguments
    #tree will create a tree for user at certain coordinates
    #given by the user
    
    #Set up turtle
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)
    turtle.penup()
    
    #Go to the specific location given by the user
    turtle.goto(x, y)
    
    #Setup turtle for the base of the tree and put the pen down
    turtle.color('#a85c0a')
    turtle.begin_fill()
    turtle.pendown()
    
    #Begin drawing the wood for the tree.
    turtle.setheading(0)
    for x in range(2):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
    turtle.penup()
    
    #End the filling
    turtle.end_fill()
    
    #Go to where the leaves will be for the tree
    turtle.goto(x, y+10)
    
    #Setup turtle for the leaves of the tree and put the pen down
    turtle.color('#20ab0a')
    turtle.begin_fill()
    turtle.pendown()
    
    #Begin drawing the wood for the tree.
    turtle.setheading(200)
    turtle.forward(12)
    turtle.setheading(80)
    turtle.forward(20)
    turtle.setheading(280)
    turtle.forward(20)
    turtle.setheading(160)
    turtle.forward(12)
    
    #End the color filling
    turtle.end_fill()
    
    #Lift the pen to end the function
    turtle.penup()
    
    turtle.done()