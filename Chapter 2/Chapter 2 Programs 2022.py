import turtle

def comment_example():
    #comment_example receives no arguments
    #it explains how to create a function header
    #and outputs or returns "Hello World!"
    print("Hello World!")
    
def program2_1():
    #program 2 1 receives no arguments
    #it outputs three messages using apostrophes instead
    #of quotation marks.
    print("Kate Austen")
    print("123 Full Circle Drive")
    print("Asheville, NC 28899")
    
def program2_2(): #double quote output
    print("Kate Austen")
    print("123 FUll Circle Drive")
    print("Asheville, NC 28899")
    
def program2_3(): #display apostrophe
    print()
    print("Don't fear!")
    print("I'm here!")
    
def program2_4():
    print("""Your assignment is to read "Hamlet" by tomorrow.""")
    #or
    print('Your assignment is to read "Hamlet" by tomorrow.')
    
def program2_5(): #This function displays a person's name and address
    #program 2 1 receives no arguments
    #it outputs three messages using apostrophes instead
    #of quotation marks.
    print("Kate Austen")
    print("123 Full Circle Drive")
    print("Asheville, NC 28899")
    
def program2_6():
    #program 2 1 receives no arguments
    #it outputs three messages using apostrophes instead
    #of quotation marks.
    print("Kate Austen") #Display the Name
    print("123 Full Circle Drive") #Display the address
    print("Asheville, NC 28899") #Display the city, state, and ZIP
    
def program2_7(): 
    room_number = 503 #applying a variable to "room_number"
    print("I am staying in room number")
    print(room_number)
    
def program2_8():
    top_speed = 160
    distance_traveled = 300
    print("The top speed is")
    print(top_speed)
    print("The distance traveled is")
    print(distance_traveled)
    
def program2_9(): #A msg and a variable on the same line
    room_number = 503
    print("I am staying in room number", room_number)
    
def program2_10(): #Multiple strings in a single print command
    dollars = 2.75
    print("I have", dollars, "in my account.")
    dollars = 99.5
    print("But now I have", dollars, "in my account!")
    
def program2_11():
    #commas are used for cocatination
    #plus signs are for string
    firstname = "Noah"
    lastname = "Jackson"
    print(firstname + " " + lastname)
    
def program2_12():
    #grabbing input from the user and then using their input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print("Hello", first_name, last_name)
    
def program2_13():
    #Input from user
    first_name = input("What is your name? ")
    age = input("What is your age? ")
    income = input("What is your income? ")
    #or income = float(input("What is your income? "))
    #generally better ^
    
    #Outputted information
    print("Here is the data you entered:")
    print("Name:", first_name)
    print("Age:", age)
    print("Income:", float(income))
    #or print("Income:", float(income))
    
def program2_14():
    salary = float(input("What is your salary? "))
    bonus = float(input("How much was your bonus? "))
    final_amount = salary + bonus
    
    print("Your total amount is", final_amount)
    
def program2_15():
    original_price = float(input("What was the original price of the item? ")) #original price the user inputs
    discount = original_price * 0.2 #finding the discount
    final_price = original_price - discount #finding the final price
    
    print("The final price is: ", final_price) #The output price the user will receive
    
def program2_16(): #getting the average from inputs
    #collect data from the user
    firsttestscore = float(input("Enter the first test score: "))
    secondtestscore = float(input("Enter the second test score: "))
    thirdtestscore = float(input("Enter the third test score: "))
    
    #adding the three inputs that the user put in
    finalscore = firsttestscore + secondtestscore + thirdtestscore
    
    #diving the "finalscore" by the total amount of inputs
    averagescore = finalscore / 3
    #could also be "averagescore = (firsttestscore + secondtestscore+ thirdtestscore) / 3"
    
    #output message that the user will recieve (Their final score)
    print("Your average score is: ", averagescore)
    
def program2_17():#Time converter
    #Get input from the user
    totalseconds = float(input("Enter the number of seconds: "))
    
    #Get the number of remaining seconds
    seconds = totalseconds % 60
    
    #Get the number of remaining seconds
    minutes = (totalseconds // 60) % 60
    
    #Get the number of hours
    hours = totalseconds // 3600
    
    #Output the results
    print("Here is the time in hours, minutes, and in seconds: ")
    print("Hours: ", hours)
    print("Minutes: ", minutes)
    print("Seconds: ", seconds)
    
def program2_18(): #future value equation
    
    #F = what you want your money to be
    #R = interest rate
    #N = numbe of years that the money will accrue interest
    #P = the amount that will need to be deposited
    
    #User will input values here
    F = float(input("Enter the desired future value: "))
    R = float(input("Enter the annual interest rate: "))
    N = float(input("Enter the number of years the money will grow: "))
    
    #Solve for the bottom of the equation
    denominator = (1+R) ** N
    
    #Devide the numerator by the denominator
    P = F / denominator
    
    #The equation could also be "P = F / ((1 + R) ** N)"
    
    #The output information the user will get
    print("You will need to deposit: ", P)
    
#integer + integer = integer
#float + integer = float

#split commands with \
    
def program2_18b(): #future value equation with decimals
    
    #F = what you want your money to be
    #R = interest rate
    #N = numbe of years that the money will accrue interest
    #P = the amount that will need to be deposited

    F = float(input("Enter the desired future value: "))
    R = float(input("Enter the annual interest rate: "))
    N = float(input("Enter the number of years the money will grow: "))
    
    denominator = (1+R) ** N
    P = F / denominator
    
    #Making the output number have only 2 decimals
    print("You will need to deposit: ", format(P, ".2f"))
    
#Inside ".2f", the "f" is the type
    
def program2_19():
    amountdue = float(input("Enter the amount due: "))
    
    monthlypayment = amountdue / 12
    
    print("Your monthly payment is", monthlypayment)
    
def program2_20():
    amountdue = float(input("Enter the amount due: "))
    
    monthlypayment = amountdue / 12
    
    print("Your monthly payment is ", end= "$")
    print(format(monthlypayment, ".2f"))
    
def program2_21(): #future value equation
    
    #F = what you want your money to be
    #R = interest rate
    #N = numbe of years that the money will accrue interest
    #P = the amount that will need to be deposited

    F = float(input("Enter the desired future value: "))
    R = float(input("Enter the annual interest rate: "))
    N = float(input("Enter the number of years the money will grow: "))
    
    denominator = (1+R) ** N

    P = F / denominator

    print("You will need to deposit: ", end="$")
    print(format(P, ".2f"))
    
def program2_21b(): #future value equation
    
    #F = what you want your money to be
    #R = interest rate
    #N = numbe of years that the money will accrue interest
    #P = the amount that will need to be deposited

    F = float(input("Enter the desired future value: "))
    R = float(input("Enter the annual interest rate: "))
    N = float(input("Enter the number of years the money will grow: "))
    
    denominator = (1+R) ** N

    P = F / denominator

    print("You will need to deposit: $" + str(format(P, ".2f")))
    #Could be "print("You will need to depost $", format(P, ".2f", sep= " "))
    
def program2_22():
    
    #Values
    no1 = 127.90
    no2 = 3465.15
    no3 = 3.78
    no4 = 264.82
    no5 = 88.08
    no6 = 800.00
    
    #Output Values
    print(format(no1, "7.2f"))
    print(format(no2, "7.2f"))
    print(format(no3, "7.2f"))
    print(format(no4, "7.2f"))
    print(format(no5, "7.2f"))
    print(format(no6, "7.2f"))
    
#Stick to variables and not just random numbers
#Random numbers will only be understood by the writer
#Not the user
#Instead, use a constant (Name that has a variable applied to it)
    
def orion2_21():
    #The Function orion uses Named Constants to stablish
    #each star location, it's name, and to draw the
    #constellation using the turtle to draw
    
    #Setup turtle
    turtle.setup(500, 500)
    turtle.penup()
    turtle.hideturtle()
    
    #Use named constants for each star
    left_shoulder_x = -70
    left_shoulder_y = 200
    
    right_shoulder_x = 80
    right_shoulder_y = 180
    
    left_beltstar_x = -40
    left_beltstar_y = -20
    
    middle_beltstar_x = 0
    middle_beltstar_y = 0
    
    right_beltstar_x = 40
    right_beltstar_y = 20
    
    left_knee_x = -90
    left_knee_y = -180
    
    right_knee_x = 120
    right_knee_y = -140
    
    turtle.pendown()
    turtle.dot()
    turtle.write("Alrilam")
    turtle.goto(right_beltstar_x, right_beltstar_y)
    turtle.dot()
    turtle.write("Mintaka")
    turtle.goto(right_knee_x, right_knee_y)
    turtle.dot()
    turtle.write("Rigel")
    turtle.goto(right_beltstar_x, right_beltstar_y)
    turtle.goto(right_shoulder_x, right_shoulder_y)
    turtle.dot()
    turtle.write("Meissa")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(left_beltstar_x, left_beltstar_y)
    turtle.dot()
    turtle.write("Alritak")
    turtle.goto(left_shoulder_x, left_shoulder_y)
    turtle.dot()
    turtle.write("Betelgeuse")
    turtle.goto(left_beltstar_x, left_beltstar_y)
    turtle.goto(left_knee_x, left_knee_y)
    turtle.dot()
    turtle.write("Saiph")
    
    turtle.done()
    
    TEST TEST