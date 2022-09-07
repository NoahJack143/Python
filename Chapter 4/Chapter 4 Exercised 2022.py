import turtle

def bug_collector(): #Exercise 1
    #bug collector accepts no arguments
    #it asks the user for the amount of bugs they collected within 5 days
    #, it will validate their input, and output the amount they collected and
    #if they're a good collector or a bad collector
    
    #Constants
    total = 0 #Accumulator Variable
    days = 5 #The amount of days they have to collect bugs
    checker = 1 #This is needed for the validation part of the loop
    
    #Text before the loop
    print("Welcome to Bug Masters bug collection system.")
    print(' ')
    
    #Begin the loop
    for day in range(1, days + 1): #"day" stands for the current day
        
        if checker > 0: #The loop will only run and continue of "checker" > 0. Used for validation
            
            #Input from the user to find out how many bugs they collected on one day
            print("How many bugs did you collect on day", day, end='')
            bugs = int(input("? "))
            
            #Check to see if their input in valid or not by using an if-then-else statement
            
            if bugs < 0: #If the answer ISN'T valid, then the loop would end
                print(" ")
                print("Please enter a valid number of bugs next time.")
                checker = -1 #This is here to make the loop end
                
            elif bugs >= 0: #If the answer IS valid, then the calculation will happen AND the loop will continue to run
                #Calculations
                total += bugs
                
    if checker > 0: #These texts will only output if the user's output have all been valid
        
        #Once the loop is over, this text will run
        print(" ")
        print("Great job, you collected", format(total, ','), "bugs this week. ", end='')
        
        #Another If-then-else statement to see if they're a good catcher or not
        if total >= 0 and total <= 50:
            print("You're an average catcher.")
        elif total > 50 and total <= 100:
            print("You're an accomplished catcher.")
        elif total >100:
            print("You're a master catcher!")
    else:
        print("Have a good day.") #This text will only output if the user's output weren't valid

def distance_traveled(): #Exercise 4
    #distance traveled accepts no arguments
    #asks the user for the speed of the vehicle and how far the vehilce traveled
    #and outputs the distance traveled for each hour passed.
    #it also will validate all of the inputs.
    
    #Gather input from the user for hours traveled and the speed of the vehicle
    speed = int(input("Enter the speed of the vehicle in MPH: "))
    hours = int(input("Enter how many hours the vehicle traveled: "))
    
    #Create a space between the input and the table OR a space between the input and a invalid output
    print(" ")
    
    #Check to see if both of the inputs are valid
    if speed < 0 or hours < 0: #If EITHER of the input are invalid
        print("Sorry, but at least one of the numbers you provided isn't valid")
    elif speed >= 0 and hours >= 0: #If BOTH of the input are valid
        #print the text before the table
        print("Hour\t\tDistance Traveled")
        print("_________________________________")
        
        #Begin the loop to output all the hours and distances
        for hour in range(1, hours + 1):
            
            #Calculation before outputting any text
            distance_traveled = hour * speed
            
            #Print the information into the table
            print(hour, '\t\t\t', format(distance_traveled, '5'))
            
def pennies(): #Exercise 7
    #pennies accepts no arguments
    #it prompts the user for an amount of days they want to use to double their
    #pennies. The output will be a table
    
    #Start with getting input from the user
    days = int(input("How many days do you want to accure pennies? "))
    
    #Then set up a constant for the amount of pennies
    pennies = 1.0
    salary = pennies
    
    #Validate the user's input before starting the loop(s)
    if days > 0: # If the user's input IS valid
        #Start by printing the text above the table
        print("Day\t\tSalary")
        print("------------------------")
        
        #Begin the loop(s)
        for day in range(1, days + 1):
            
            #Print the output
            print(day, '\t\t', '$', format(salary / 100, '5,.2f'))
            
            #Make calculations before outputting text AFTER the first loop
            salary = salary * 2
            
    elif days <= 0: #This text will only output if the input is invalid
        print(" ")
        print("Sorry, but you entered an invalid amount of days")
            
def hogwarts_tuition():
    #hogwarts tuition accepts no arguments
    #it will output the semester tuition amount for the next 5 years
    
    #Constant(s) / accumulator variable to makes things clear
    tuition = 16000 #the cost per semester is 16000
    
    #Text above the table before the loop
    print("Year\t\tTuition Cost")
    print("----------------------------")
    
    #Begin the loop
    for year in range(1, 5 + 1):
        
        #Make calculations before outputting text
        tuition = (tuition * .03) + tuition
        
        #Output text into the table
        print(year, '\t\t', '$', format(tuition, '5,.2f'))
        
def population(): #Exercise 13
    #population accepts no arguments
    #it prompts the user for the population, the perent of growsh per day, and
    #the amount of days for growing. It outputs a table that tells the growth
    #of the population per day. INCLUDES VALIDATIONS
    
    #Input from the user
    starting_population = int(input("Enter the starting population: "))
    percent = int(input("Enter the percent of daily growth: "))
    days = int(input("Enter the number of days to stimulate"))
    
    #Calculations before the loop
    percent /= 100
    
    #Input before the table
    print(" ")
    print("Day\t\tProjected Population")
    print("--------------------------------------")
    
    #VALIDATION
    if starting_population <= 0 or days <= 0:
        print("ERROR")
        print("Enter all positive numbers next time.")
    elif starting_population > 0 and days > 0:
        
        #Begin the loop
        for day in range(1, days + 1):
            #Data printed into the table
            print(day, '\t\t', starting_population)
            
            #Calculations
            starting_population = (starting_population * percent) + starting_population
        
def reverse_triangle(): #Exercise 14
    #reverse triangle accepts no arguments
    #it creates an upside down triangle
    
    #Ask the user for the bse size of the triangle:
    base = int(input("Enter the base size of the triangle: "))
    
    #Begin the loop right after
    for row in range(base, 0, -1):
        for column in range(row):
            print("*", end='')
        print()
        
def stair_pattern2(): #Exercise 15
    #stair pattern 2 accepts no arguments
    #it creates stairs using any symbol and has that same symbol along the left margin
    
    #Prompt the user for the number of stairs
    stairs = int(input("Enter the number of stairs: "))
    
    #Start the loops
    for row in range(1, stairs + 1): #sets the loop with a range
        print("@", end='') #prints the symbols along the left margin
        for RANDOM_VARIABLE in range(row): #Next loop to make the stair case
            print(" ", end='') #makes the spaces needed between the symbols on each row
        print("@") #prints the symbol on the furthest right of each row
        
def turtle_graphics(): #Exercise 16
    #turtle graphics accepts no arguments
    #it will ask the user for the number of squares to draw and
    #outputs the amount of squares the user requested for
    
    #Input from the user
    squares = int(input("How many squares do you want to be drawn? "))
    
    #Constants
    MOVE = 10 #This is how far turtle will move initially
    TURN = 90 #This is the rotation degrees for turtle
    
    #PRE settings for turtle
    turtle.hideturtle()
    turtle.speed(0)
    
    #Validation
    if squares <= 0:
        print(" ")
        print("Please enter a positive number next time.")
    elif squares > 0:
        #Begin the loop
        for square in range(1, squares + 1):
            #Start using turtle
            turtle.left(TURN)
            turtle.forward(MOVE)
            turtle.left(TURN)
            turtle.forward(MOVE)
            turtle.left(TURN)
            turtle.forward(MOVE)
            turtle.left(TURN)
            turtle.forward(MOVE)
            
            #Increase the amount of spaces turtle moves forward for each loop
            MOVE += 10
        #End when turtle is done
        turtle.done()
        
def hypnotic_pattern(): #Exercise 18
    #hypnotic pattern accepts no arguments
    #it asks the user for the amount of patterns to draw and then
    #outputs the pattern
    
    #Input from the user
    patterns = int(input("How many patterns do you want? "))
    
    #Constants
    MOVE = 2 #This is how far turtle's first line will be
    TURN = 90 #This is the amount of degrees turtle will turn
    
    #PRE settings for turtle
    turtle.hideturtle()
    turtle.speed(0)
    
    #Validation
    if patterns <= 0:
        print(" ")
        print("Sorry, but you entered an invalid amount of patterns")
    elif patterns > 0:
        #Begin the loop
        for pattern in range(1, patterns + 1):
            #Start making the pattern
            turtle.left(TURN)
            turtle.forward(MOVE)
            MOVE += 3
            turtle.left(TURN)
            turtle.forward(MOVE)
            MOVE += 3
            turtle.left(TURN)
            turtle.forward(MOVE)
            MOVE += 3
            turtle.left(TURN)
            turtle.forward(MOVE)
            MOVE += 3
            #The pattern will repeat how ever many times the user wants turtle to
        #This is when turtle is done
        turtle.done()