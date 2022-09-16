import turtle


def square(x, y, width, color):
    
    #This is setting up turtle's location, speed, and beginning of the coloring.
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    
    #This is will turtle will start creating the square
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
        
    #Turtle will end when the task is done
    turtle.end_fill() #turtle will fill in the shape
    
def circle(x, y, radius, color):
    
    #Turtle will go to the desired spot and prepare the color
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    
    #Turtle will create the circle, fill it in with the desired color, and then end
    turtle.circle(radius)
    turtle.end_fill()
    
def line(startX, startY, endX, endY, color):
    
    #This is when turtle sets up by going to the desired location is selecting the desired color
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.pencolor(color)
    
    #Turtle will draw the line to the desired location
    turtle.goto(endX, endY)