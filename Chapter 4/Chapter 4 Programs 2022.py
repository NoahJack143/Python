import turtle

def gross_pay(): #program 4-14
    #it takes input from the user in the form of hours worked and pay rate
    #it calculates the gross pay
    
    #Input from the user
    hours = int(input("Enter the number of hours worked for 1 week: ")) #get horus worked
    
    pay_rate = int(input("Enter the hourly rate: ")) #Get pay rate
    
    gross_pay = hours * pay_rate
    
    #Output gross pay
    print("Gross pay: $", format(gross_pay, ",.2f"), sep = " ")
    
def retail_no_validation(): #program 4-15
    
    mark_up = 1.25 #named constant for markup percentage
    another = "y" #set the sentinel variable to loop
    
    #process through the loop
    while another == "y" or another == "Y":
        #prompt the user for the wholesale price
        wholesale = float(input("Enter the wholesale cost: "))
        
        #Calculate retail price
        retail = wholesale * mark_up
        
        #Output the retial price
        print("Retail price: $", format(retail, ',.2f'), sep=' ')
        
        #Prompt to continue
        another = input("Do you want to enter another item?" +
                        "(Enter y for yes): ")

def retail_with_validation(): #program 4-15.1
    
    mark_up = 1.25 #named constant for markup percentage
    another = "y" #set the sentinel variable to loop
    
    #process through the loop
    while another == "y" or another == "Y":
        #prompt the user for the wholesale price
        wholesale = float(input("Enter the wholesale cost: "))
        
        #while loop to check if they entered a valid number
        while wholesale < 0:
            whoesale = int(input("Please enter a valid wholesale price: "))
        #Calculate retail price
        retail = wholesale * mark_up
        
        #Output the retial price
        print("Retail price: $", format(retail, ',.2f'), sep=' ')
        
        #Prompt to continue
        another = input("Do you want to enter another item?" +
                        "(Enter y for yes): ")
        
#Nested loop: loop that is contained inside another loop
        
def test_score_averages(): #program 4-17
    #Input from the user
    students = int(input("How many students? "))
    tests = int(input("How many test per student? "))
    
    #loop for student
    for student in range(1, students + 1):
        
        #Accumulator for each student iteration
        total = 0
        
        #Student number + dashed line
        print("Student number", student)
        print("--------------")
        #loop for test
        for test in range(1, tests +1):
            print("Test number", student, ": ")
            score = float(input(": "))
            total += score
            
        #calculate average for each student
        average = total / tests
        print("The average for stund number", student, "is: ", format(average, '.2f'))
        print(' ') #FIX THIS LATER
        
def rectangle_pattern(): #program 4-18
    
    #Input from the user
    rows = int(input("Enter the number of rows to print: "))
    columns = int(input('Enter the number of rows to print: '))
    
    #start the loop
    for row in range(rows):
        
        #start the loops for columns
        for column in range(columns):
            print('*', end= ' ')
        print()
        
def triangle_pattern(): #program 4-19
    
    #Input from the user
    base = int(input("Enter the base size of the triangle: "))
    
    #Constants
    start = 1
    stop = base
    
    for rows in range(start, stop + 1):
        for col in range(rows):
            print('*', end=' ')
        print()
        
def stair_pattern(): #program 4-20
    
    #Input from the user
    stairs = int(input("Enter the number of stairs: "))
    
    #Constants
    start = 1
    stop = stairs
    
    for rows in range(start, stop + 1):
        print()
        for col in range(rows):
            print('', end = '')
        print('5')
        
def concentric_circles(): #program 4-21
    
    #input from the user
    num_circles = int(input("Enter the number of circles: "))
    
    #constant
    starting_radius = 20
    offset = 10
    radius = starting_radius
    
    #Turtle preset
    turtle.speed(1)
    
    for circle in range(num_circles):
        turtle.circle(radius)
        turtle.penup()
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.pendown()
        radius = radius + offset
    turtle.done()
    
def spiral_circles(): #program 4-22
    #constants
    circles = 36
    radius = 100
    angle = 10
    
    #turtle preset
    turtle.speed(10)
    
    #loop
    for spiral in range(circles):
        turtle.circle(radius)
        turtle.left(angle)
    turtle.done()
