import turtle

def commission(): #Program 4-1
    #commission accepts no arguments
    
    #Constants
    keep_going = "y"
    
    #Start the loop and set the condition to loop if "keep_going" == y
    while keep_going == 'y':
        #Input from the user
        sale = int(input("Enter the sale amount: "))
        commission_rate = int(input("Enter the commission rate: "))
        
        #Calculations
        commission = sale * commission_rate
        
        #Output for the user
        print("The commission is $", format(commission, '.2f'), sep = "")
        
        #Prompt the user if they want to calculate again by changing what "keep_going" stands for
        keep_going = input("Do you want to calculate another? (y/n) ")
        
def temperature(): #Program 4-2
    #temperature accepts no arguments
    
    #Constants
    MAX_TEMP = 102.5
    
    #Input from the user
    temperature = int(input("Please enter the current substance temperature in degrees celcius: "))
    
    #Start the loop with the condition of running only if the temperature is lower than the MAX_TEMP
    while MAX_TEMP < temperature:
        #Tell the user that the temperature is too high
        print("The temperature is too high.")
        print("Turn the thermostat down and wait for it to cool.")
        print("Then wait 5 minutes and measure again.")
        print(" ")
        
        #Input from the user to reasign a number to temperature
        temperature = int(input("Please enter the new temperature in degrees celcius: "))
    #Output for if the temperature is less than the MAX_TEMP
    print("The temperature is acceptable.")
    print("Measure again in 15 minutes.")

def infinite(): #Program 4-3
    #infinite accepts no arguments
    
    #Constants
    keep_going = "y"
    
    #Start the loop and set the condition to loop if "keep_going" == y
    while keep_going == 'y':
        #Input from the user
        sale = int(input("Enter the sale amount: "))
        commission_rate = int(input("Enter the commission rate: "))
        
        #Calculations
        commission = sale * commission_rate
        
        #Output for the user
        print("The commission is $", format(commission, '.2f'), sep = "")
        
        #The prompt has now been removed
        
def simple_loop1(): #Program 4-4
    #simple_loop1 accepts no arguments
    #This procedure will simply give a list of numbers
    
    #Text before the loop begins
    print("I will display the numbers 1-5")
    
    #Text for the user/ loop 1-5
    for num in [1, 2, 3, 4, 5]: #num stands for the data items after "in"
        print(num) #For every loop, an iteration will be outputed
        
def simple_loop2(): #Program 4-5
    #simple_loop2 accepts no arguments
    
    #Text before the loop
    print("I will output all odd numbers from 1-10")
    
    #Begin the loop like in the previous procedure
    for this_variable_can_be_ANYTHING_you_want_it_to_be in [1, 3, 5, 7, 9]:
        print(this_variable_can_be_ANYTHING_you_want_it_to_be)

def simple_loop3(): #Program 4-6
    #simple_loop3 accepts no arguments
    
    #Begin the loop and use strings instead of integers
    for remember_this_num_can_be_anything in ["Steve", "Tony", "Strange", "Thor"]:
        print(remember_this_num_can_be_anything)

def simple_loop1_update(): #Program 4-4 update
    #simple_loop1 accepts no arguments
    #it loops using the range() funcion

    for num in range(10): #num also represents the "Target Variable"
        print(num)
    #notice how the output contains 0, 1-9, and NOT 10
    #fix this by changing the range to "(10 + 1)"
        
def hello_world_loop(): #Program 4-7
    #hello world loop accepts no arguments
    #it outputs the phrase "Hello World!" 5 times
    
    for THIS_CAN_BE_ANYTHING in range(5): #The 5 represents what "THIS_CAN_BE_ANYTHING"'s value is and
        #how many loops there will be
        print("Hello World!")
        
def squares(): #Program 4-8
    #squares accepts no arguments
    #This procedure will output a table of numbers 1-10 and their squares
    
    #Text before the loop
    print("Number Square")
    print("-------------")
    
    #Begin the loop and calculate each square
    for RANDOM_VARIABLE in range(1,10+1): #"(1,10+1) represents numbers from 1 through 11
        #Calculations
        square = RANDOM_VARIABLE ** 2
        
        #Output in the table
        print(RANDOM_VARIABLE, '\t', square)
        
def speed_converter(): #Program 4-9
    #speed_converter accepts no arguments
    #it converts 60 through 130 kph in 10 kph increments
    
    #Constants to use
    start_speed = 60 #starting speed which is 60 kph
    stop_speed = 131 #last speed which is 130 kph
    increment = 10 #10 kph increments
    
    #Text before using the loop
    print("KPH\tMPH")
    print("--------------")
    
    #Begin the loop with calculations like the last procedure
    for KPH in range(start_speed, stop_speed, increment): #from 60 kph to 130 kph in 10 kph increments
        #Calculations
        MPH = KPH * .6241
        
        #Output inside the table
        print(KPH, '\t', format(MPH, '.1f'))
        
def user_squares1(): #Program 4-10
    #user_squares1 accepts no arguments
    
    #Text before the input from the user
    print("This program wil display a list of numbers (starting at 1) and their squares.")
    
    #Input from the user
    squares = int(input("How many squares? "))
    
    #Text before the loop
    print("Number\tSquare")
    print("--------------")
    
    #Begin the loop
    for RANDOM_NUMBER in range(1, squares + 1): #squares is within range() because
        #that's how many squares the user wants to be outputted
        #Calculations
        square = RANDOM_NUMBER ** 2
        
        #Output for the user inside the table
        print(RANDOM_NUMBER, '\t', square)
        
def user_squares2(): #Program 4-11
    #user squares2 accepts no arguments
    
    #Text before input from the user
    print("This program wil display a list of numbers and their squares.")
    
    #Input from the user
    starting_number = int(input("Enter the starting number: "))
    ending_number = int(input("Enter the ending number: "))
    print(" ")
    
    #Text before the loop
    print("Number\tSquare")
    print("-------------------")
    
    #Begin the loop with the inputs from the user
    for RANDOM_NUMBER in range(starting_number, ending_number + 1): #the loop will run through the strating number to the ending number
        #Calculations
        square = RANDOM_NUMBER ** 2
        
        #Output inside the table
        print(RANDOM_NUMBER, '\t', square)
        
def sum_numbers(): #Program 4-12
    #sum numbers accepts no numbers
    
    #Text before anything
    print("This program calculates the sum of 5 numbers you will enter.")
    
    #Set the accumulator variable, which accumulates total and reads in series and will eference the total at the end of the loop
    total = 0 #accumulator variable
    
    #Constant
    LOOPS = 5 #named constant for the number of prompts
    #Begin the loop
    for RANDOM_VARIABLE in range(LOOPS): #REMEMBER, the LOOPS represents the amount of loops and the value that RANDOM_VARIABLE represents/holds
        number = int(input("Please enter a number: "))
        total = total + number #Also the same as total += number
    
    #After the loop loops 5 times, it will end and read this output next
    print("The total of your", LOOPS, "numbers is: ", total)

def sum_numbers_assignment_operator(): #Program 4-12.1
    #sum numbers assignment operator accepts no numbers
    #this program uses an augmented assignment operator unlike the previous program
    
    
    #Text before anything
    print("This program calculates the sum of 5 numbers you will enter.")
    
    #Set the accumulator variable, which accumulates total and reads in series and will eference the total at the end of the loop
    total = 0 #accumulator variable
    
    #Constant
    LOOPS = 5 #named constant for the number of prompts
    #Begin the loop
    for RANDOM_VARIABLE in range(LOOPS): #REMEMBER, the LOOPS represents the amount of loops and the value that RANDOM_VARIABLE represents/holds
        number = int(input("Please enter a number: "))
        total += LOOPS #Uses an augmented assignment operator
    
    #After the loop loops 5 times, it will end and read this output next
    print("The total of your", LOOPS, "numbers is: ", total)

def property_tax(): #Program 4-13
    #property tax accepts no arguments
    #it prompts the usher for a lot number and loops whlie a lot number doesn't = 0
    #Use a while loop because the loop will loop CONTINUOUSLY unless stopped
    
    #Set the lot_number before starting the loop
    lot_number = 1 #lot_number = 1 because if it = 0 then the loop would never run
    #Other constant(s)
    PROP_TAX = .0065 #property tax
    #Begin the loop
    while lot_number != 0: #If the lot were to equal 0, then the loop would eventually end unless increased above 0 later on
        #Prompt the user to input a property value
        property_value = int(input("Please enter the property value: ")) #Value of user's property
        
        #Calculations
        property_tax = property_value * PROP_TAX
        
        #Output the total property tax owed and prompts for another lot
        print("Property tax: $", format(property_tax, '.2f'), sep = '')
        
        lot_number = int(input("Please enter a lot number (enter 0 to end): ")) #Used to tell if the user wants to end the program or continue
    #Once the user enters 0, the loop will end and run this text
    print(" ")
    print("Thank you for using the Cyberdyne Systems property tax calculator, all your rights reserved.")

def gross_pay(): #Program 4-14
    #gross pay accepts no arguments
    #it takes input from the user in the form of hours worked and pay rate
    #it calculates and outputs the gross pay
    #The following code will include a VALIDATION part that can tell if the user
    #inputted valid data
    
    #Use and If-Then-Else statement to check whether the user inputed valid data or not
    
    #Start with getting input from the user
    hours = int(input("Enter the number of hours worked for 1 week: ")) #Get hours worked
    pay_rate = int(input("Enter the hourly rate: ")) #Get pay rate
    
    #Calculations
    gross_pay = hours * pay_rate
    
    #Use if-then-else statements for validation
    if hours < 0 or pay_rate < 0 or gross_pay < 0:
        print("ERROR")
        print("Please input valid numbers.")
    else:
        print("Gross pay: $", format(gross_pay, ',.2f'), sep="")

def retail_no_validation(): #Program 4-15
    #retail no validatoin accepts no arguments
    #it uses a string sentinel varialbe to control the loop
    #it loops until the user no longer enters "y" or "Y" to continue
    #and outputs the retail price
    
    MARK_UP = 1.25 #named constant for markup percentage
    another = 'y' #set the sentinel variable to loop
    
    #process through the loop
    while another == 'y' or another == 'Y':
        #prompt the user for the wholesale price
        wholesale = float(input("Enter the wholesale cost: "))
        
        #Calculate retail price
        retail = wholesale * MARK_UP
        
        #Output the retail price
        print("Retail price: $", format(retail, ',.2f'), sep='')
        
        
        #Prompt to continue
        another = input('Do you want to enter another item?' +
                        '(Enter y for yes): ')
        
def retail_with_validation(): #Program 4-15
    #retail no validatoin accepts no arguments
    #it uses a string sentinel varialbe to control the loop
    #it loops until the user no longer enters "y" or "Y" to continue
    #and outputs the retail price
    #This procedure does have validation
    
    MARK_UP = 1.25 #named constant for markup percentage
    another = 'y' #set the sentinel variable to loop
    
    #process through the loop
    while another == 'y' or another == 'Y':
        #prompt the user for the wholesale price
        wholesale = float(input("Enter the wholesale cost: "))
        
        #Calculate retail price
        retail = wholesale * MARK_UP
        
        #Before outputting the results, validate their input using an if-then-else statement
        if wholesale >= 0:
            #Output the retail price
            print("Retail price: $", format(retail, ',.2f'), sep='')
        else:
            print("Sorry, but you've entered a negative number.")
            print("Next time, enter a positive number.")
            print(" ")
        #Prompt to continue
        another = input('Do you want to enter another item?' +
                        '(Enter y for yes): ')
        
#Nested loop: loop that is contained inside another loop
        
def test_score_averages(): #Program 4-17
    #test score averages accepts no arguments
    #this procedure will take a number of students, their test scores, and
    #their individual averages for test scores
    
    #Set an accumulator variable
    total = 0 #accumulater variable
    
    #Get input from the user
    students = int(input("How many studnets are there? "))
    tests = int(input("How many tests per student? "))
    
    #Begin the loop now because each student needs their own table
    for RANDOM_VARIABLE in range(1, students + 1): #loops through for each student
        #At the beginning of each loop, reset the accumulator variable to 0
        total = 0
        #Text above each table
        print("Student number", RANDOM_VARIABLE)
        print("-----------------")
        #Begin ANOTHER loop
        for test_number in range(1, tests + 1):
            #Get the score for each test, for each student, from the user
            print("Test number", test_number, end='')
            test_score = int(input(": ")) #Score / test
            total += test_score #Add test score to the accumulator
        #After the 2nd loop ends, this text will appear, and then the 1st loop will run again until all the students have been solved for
        #Calculations will come first though...
        average = total / tests #divide the accumulator by the amount of test
        
        #Now output the text for the user, and run though the loop again
        print("The average for student number", RANDOM_VARIABLE, "is: ", format(average, '.2f')) #RANDOM_VARIABLE represents the current student
        print(' ')
        
def rectangle_pattern(): #Program 4-18
    #rectangle pattern accepts no arguments
    
    #Prompt the user for the amount of rows and columns
    rows = int(input("Enter the number of rows to print: "))
    columns = int(input("Enter the number of columns to print: "))
    
    #Start the loop for rows first
    for RANDOM_VARIABLE in range(rows):
        #Start the loop for columns second
        for RANDOM_VARIABLE_TWO in range(columns):
            print("*", end='') #the """end='' """ allows each row of stars to ACTUALLY be a row
        print() #moves each row of stars below the previous row
        
def triangle_pattern(): #Program 4-19
    #triangle pattern accepts no arguments
    
    #Prompt the user for the size of the base of the triangle
    base = int(input("Enter the base size of the triangle: "))
    
    #Start the loops
    for row in range(1, base +1): #the "1" represents the top and the base+1 = the base
        for RANDOM_VARIABLE in range(row): #row is in range() because as we go down each row, the amount of stars on each row will increase
            print('*', end='') #the """end='' """ removes the "enter" between each star so they all line up on their respective rows
        print() #this space is here to move down to the next row
        
def stair_pattern(): #Program 4-20
    #stair pattern accepts no arguments
    
    #Prompt the user for the number of stairs
    stairs = int(input("Enter the number of stairs: "))
    
    #Start the loops
    for row in range(1, stairs + 1): #this loop will allow the target variable "row" to increase by 1 until it reachs the maximum stairs set by the user
        for RANDOM_VARIABLE in range(row): #This loop will repeat "row" amount of times
            print(" ", end='') #as "row" increased, the amount of spaces moved over will also increase
        print("@") #Lastly, this will print the desired character(s) that represent the stairs

def concentric_circles(): #Program 4-21
    #concentric circles accepts no arguments
    
    #Prompt the user for the amount of circles desired
    circles = int(input("Enter the number of circles: "))
    
    #Constants
    starting_radius = 20
    offset = 10
    animation_speed = 0
    
    #PRE settings for turtle
    turtle.speed(animation_speed)
    
    #start the loop
    for radius in range(starting_radius, circles * starting_radius, offset): #The radius starts at 20, then multiplies the desired circle amount by starting radius to get the next radius, and then increments by 10
        turtle.circle(radius)
        turtle.penup() #this is to avoid connecting the circles
        turtle.right(90) #turn right and left, otherwise the circles will have different center points
        turtle.forward(offset) #amount forward
        turtle.left(90) #turn left because turtle makes circles going counter clockwise
        turtle.pendown() #pen down to be able to draw the circle again
    #After the amount of circles desired have been created, the turtle will end
    turtle.done()
    concentric_circles()

def spiral_circles(): #Program 4-22
    #spiral circles accepts no arguments
    
    circles = 72 #number of circles to draw
    radius = 200 #radius of each circle
    angle = 5 #angle to turn after each circle
    
    turtle.speed(0) #turtle's speed
    #start the look
    for RANDOM_VARIABLE in range(circles):
        turtle.circle(radius)
        turtle.left(angle)
        
    turtle.done()

def starburst(): #Program 4-23
    #starburst accepts no arguments
    
    #Constants
    start_x = -200 # Starting X coordinate
    start_y = 0 # Starting Y coordinate
    num_lines = 36 # Number of lines to draw
    line_length = 400 # length of each line
    angle = 170 # Angle to turn
    
    #PRE settings for turtle
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    
    #Start the loop and draw 36 lines, tilt 170 degrees after each line
    for RANDOM_VARIABLE in range(num_lines):
        turtle.forward(line_length)
        turtle.left(angle)
