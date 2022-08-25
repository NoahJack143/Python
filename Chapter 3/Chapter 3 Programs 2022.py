import turtle

def ta(): #test_average
    
    #Presettings before recieving input
    highscore = 100
    
    #Inputs from the user
    first_score = int(input("Enter the first score: "))
    second_score = int(input("Enter the second score: "))
    third_score = int(input("Enter the third score: "))
    
    #Calculations
    average_score = (first_score + second_score + third_score) / 3
    
    #Displayed average for the user
    print("The average score is: ", format(average_score, ".2f"))
    
    #If the score is higher than the highscore + output
    if average_score > highscore:
        print("Congratulations!")
        print("That is a highscore!")
        
    #If the score is equal to the highscore + output
    if average_score == highscore:
        print("Wow!")
        print("You tied with the highscore!")
        
    #If the score is lower than the highscore + output
    if average_score < highscore:
        print("Sorry!")
        print("You didn't beat the highscore.")
        
def arp(): #auto_repair_payroll
    
    #There are things wrong in this! FIX THEM!!
    
    #Input from the user
    hours = int(input("How many hours have you worked? "))
    hourly_rate = int(input("What is your hourly rate? "))
    
    #Calculations
    normal_pay = hours * hourly_rate
    extra_hours = hours - 40
    overtime_pay = normal_pay * extra_hours * 1.5
    
    #If the worker has worked MORE than 40 hours
    if hours > 40:
        print("You will recieve ", format(overtime_pay, ".2f"), end = "$")
    #If the worker has worked LESS than 40 hours
    else:
        print("Your pay will be ", format(normal_pay, ".2f"), end = "$")
        
def en(): #even_number
    #even number accepts no arguments
    #it takes input from the user
    #and returns if the numer was even
    
    number = int(input("Please enter an even number: "))
    
    #use modulus (% --> 4%2)  to determine if the number was even or odd
    if number % 2 == 0:
        print("The number is even!")
        #you could then perform the calculation
    else:
        print("I said to enter an even number!")
        #do not perform the calculation
        
def pv(): #password_verifier
    #pv is going to take a password from the user
    #and if the password is wrong, then the
    #user will recieve "invalidation"
    
    #Input from the user
    password = input("Please enter the password: ")
    
    #If statement, to see if the password is right or wrong, and then give output
    if password == "prospero":
        print("Password accepted.")
    else:
        print("Password is invalid.")
        
def pv2(): #password_verifier1.2
    #Convert their input and change it it to lower case
    
    #Input from the user
    password = input("Please enter the password: ")
    
    #If statement, to see if the password is right or wrong, and then give output
    if password.lower() == "prospero":
        print("Password accepted.")
    else:
        print("Password is invalid.")
        
def sn(): #sort_names
    #This procedure is going to recieve names
    #and then list them alphabetically
    
    #Input from the user
    first_name = input("""Enter the first name (last, first): """)
    last_name = input("""Enter the second name (last, first): """)
    
    #Output for the user before sorting the names
    print("Here are the names, sorted alphabetically.")
    
    #Check to see which name has a higher value than the other
    #compare and output the names from greatest to least
    if first_name < last_name:
        print(first_name)
        print(last_name)
    else:
        print(last_name)
        print(first_name)
    
def ron(): #range_of_numbers      #elif
    #range of numbers accepts no arguments
    #it will prompt the user for a number from 1 to 10
    #and output if the number if <> 5
    #and output if the number is out of range.
    #This assumes that the user doesn't enter a number below
    #1 and a non-numeric number
    
    #Get input from the user
    number = int(input("Enter a number from 1 to 10: "))
    
    #Check if the number if greater than 10
    #the program will check each "if", "elif", and "else" statements in order
    #from top to bottom. If everything else wasn't right, then the "else" statement
    #will output
    if number > 10:
        print("Only enter number between 1 and 10")
    elif number <= 5:
        print("Your number was between 1 and 5")
    else:
        print("Your number was between 6 and 10")
        
#if <condition:
    #statements here
#   if <condition:
        #more statements here
#    else:
        #if the second condition failed
#else:
    #If the first condition failed

def eq(): #loan_qualifier              #multiple "if" statements
    #loan qualifier accepts no arguments
    #loan qualifier is going to take input from the user
    #use multiple "if" statements, and then give a output
    #dependent on the "if" statements.
    
    #input from the user
    salary = int(input("Enter your annual salary: "))
    jobs = int(input("Enter the number of years at your current job: "))
    
    #IF statement #1
    if salary >= 30000:
        print("Your salary meets the requirements.")
        #IF statement #2
        if jobs >= 2:
            print("Your years worked also meets the requirement.")
            print("You qualify for the loan.")
        #false statement #2
        else:
            print("You must have been on your current job for at least two "
                  "years to qualify.")
    #false statement #1
    else:
        print("You must earn at least $30,000 per year to qualify.")

#elif is used to check mulitple conditions ------
#else is used if all the conditions fail ------
        
def g(): #grader
    #grader accepts no arguments
    #grader will take input from the user and tell them what letter grade they have
    #this will output their letter grade correlation to their pecentage
    
    #Input from the user
    grade = int(input("What is your current grade? "))
    
    #If statements
    if grade >= 90:
        print("Your grade is A.")
    elif grade >=80:
        print("Your grade is B.")
    elif grade >=70:
        print("Your grade is C.")
    elif grade >=60:
        print("Your grade is D.")
    else:
        print("Your grade is F.")
        
def g2(): #grader2.0
    #grader2.0 accepts no arguments
    #grader will take input from the user and tell them what letter grade they have
    #this will output their letter grade correlation to their pecentage
    
    #Input from the user
    grade = int(input("What is your current grade? "))
    
    #You can also group the "if" and "else" together
    #if grade >= 90:
    #   print("Your grade is A.")
    #else:
    #
    #If statements
    if grade >= 60:
        if grade >= 70:
            if grade >= 80:
                if grade >= 90:
                    print("Your grade is A.")
                else:
                    print("Your grade is B.")
            else:
                print("Your grade is C.")
        else:
            print("Your grade is D.")
    else:
        print("Your grade is F.")
        
#"or" needs one or the other to be True
#True and False = True
#"and" needs both to be True in order to be True
#True and True = True
#True and False = False
        
def eq2(): #loan_qualifier1.2              #"and" statement
    #loan qualifier accepts no arguments
    #loan qualifier is going to take input from the user
    #loan qualifier is going to use "and" to check if both
    #expressions are true. If not, then the output will be "else".
    
    #input from the user
    salary = int(input("Enter your annual salary: "))
    jobs = int(input("Enter the number of years at your current job: "))
    
    #If statement with "and"
    if salary >= 30000 and jobs >= 2:
        print("You qualify for the loan.")
    else:
        print("""You're are missing one of the qualifications""")
        
def eq3(): #loan_qualifier1.3              #"or" statement
    #loan qualifier accepts no arguments
    #loan qualifier is going to take input from the user
    #loan qualifier is going to use and "if" statement with an "or"
    #statement to see if only one of the expressions is true.
    #If even one of the expressions is true, then the output will be true
    #If both of the expressions are false, then the output will be "else"
    
    #input from the user
    salary = int(input("Enter your annual salary: "))
    jobs = int(input("Enter the number of years at your current job: "))
    
    #IF statement #1
    if salary >= 30000 or jobs >= 2:
        print("You qualify for the loan.")
    else:
        print("""You're missing both of the qualifications""")
    
#Boolean variable: references one of two values, True or False (bool)

def htt(): #hit_the_target()
    #hit the target accepts no arguments
    screenwidth = 600  #screen width
    screenheight = 600  #screen height
    targetleftx = 100  #Target's lower left corner x
    targetlefty = 250  #Target's lower left corner y
    targetwidth = 25  #Target's width
    targetfactor = 30  #Arbitrary force factor
    projectilespeed = 1  #Projectile's animation speed
    north = 90  #Angle of north direction
    south = 270  #Angle of south direction
    east = 0  #Angle of east direction
    west = 180  #Angle of west direction
    
    #Presettings to create the target
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(targetleftx, targetlefty)
    turtle.pendown()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.penup()
    turtle.goto(0,0)
    turtle.showturtle()
    
    #Ask the user for input
    projectile_angle = int(input("Enter the projectile's angle (1-359): "))
    force = int(input("Enter the launch force (1-10): "))
    
    #Speed of animation
    turtle.speed(1)
    
    #Angle of projection
    turtle.setheading(projectile_angle)
    
    #Force of projection
    turtle.forward(force * 28)
    
    #Check to see if they hit the target
    if turtle.xcor() > 100 and turtle.xcor() < 125 and turtle.ycor() > 250 and turtle.ycor() < 275:
        print("You hit!")
    else:
        print("You missed!")
    
    turtle.done()