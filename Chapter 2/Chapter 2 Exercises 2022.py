import turtle

def ex2_1():
    #The "Personal Information" accepts no arguments.
    #This exercise will receive information from the user
    #and will give the user the evaluated inforamation.
    #This exercise's output is personal information provided
    #by the user provides.
    
    #Input from the user
    name = input("Enter your first and last name: ")
    address_city_state_zip = input("Enter your address, city,"
    " state, and ZIP")
    phonenumber = input("Enter your phone number: ")
    college_major = input("Enter your projected college major: ")
    
    #Output for the user
    print(" ")
    print("Your name is: ", name)
    print("Your address, city, state, and ZIP are: ",
          address_city_state_zip)
    print("Your phone number is: ", phonenumber)
    print("Your projected college major", college_major)

def ex2_4():
    #The "Total Purchase" exercise accepts no arguments.
    #This exercise will take information from the user, make
    #some calculations, and then give the solutions to the
    #User. The output are going to be calculations the
    #program made.
    
    #Input from the user
    priceone = float(input("Please enter a price for your first item: "))
    pricetwo = float(input("Please enter a price for your second item: "))
    pricethree = float(input("Please enter a price for your third item: "))
    pricefour = float(input("Please enter a price for your fourth item: "))
    pricefive = float(input("Please enter a price for your fifth item: "))
    
    print(" ")
    #Calculations
    subtotal = priceone + pricetwo + pricethree + pricefour +pricefive
    tax = subtotal * .07
    total = subtotal + tax
    
    #Output for the users
    print("Subtotal:\t", end="$")
    print(format(subtotal, "6.2f"))
    print("Tax:\t\t",  end="$")
    print(format(tax, "6.2f"))
    print("Total:\t\t", end="$")
    print(format(total, "6.2f"))

def ex2_5():
    #The "Distance Traveled" exercise accepts no arguments
    #This exercise will take input from the user (Asking for mph traveled)
    #plug the input into an equation, and give three different information
    #bits to the user. The output is going to be three different
    #outputs from equations.
    
    #Input from the user
    mph = int(input("How fast are you driving? "))
    
    #Calculations
    sixhours = mph * 6
    tenhours = mph * 10
    fifteenhours = mph * 15
    
    #Output for the user
    print("At", mph, "miles per hour you will travel", sixhours, "miles in 6 hours.")
    print("At", mph, "miles per hour you will travel", tenhours, "miles in 10 hours.")
    print("At", mph, "miles per hour you will travel", fifteenhours, "miles in 15 hours.")
    
def ex2_6():
    #The "Sales Tax" exercise accepts no arguments
    #This exercise will take an integer (input) from the user, make calculations,
    #and give the output to the user. The output from this exercise is going to
    #be "purchase price was", "state tax amount is", "country tax amount is",
    #"total tax is", and "total sale is".
    
    #Input from the user
    saleamount = float(input("Enter the sale amount: "))
    
    #Calculations
    statetax = saleamount * .05
    countytax = saleamount * .025
    totaltax = statetax + countytax
    totalsale = totaltax + saleamount
    
    #Output for the user
    print("Your purchase price was:\t", end = "$")
    print(format(saleamount, "6.2f"))
    print("Your state tax amount is:\t", end = "$")
    print(format(statetax, "6.2f"))
    print("Your county tax amount is:\t", end = "$")
    print(format(countytax, "6.2f"))
    print("Your total tax is:\t\t", end = "$")
    print(format(totaltax, "6.2f"))
    print("Your total sale is:\t\t", end = "$")
    print(format(totalsale, "6.2f"))
    
def ex2_8():
    #The "Tip, Tax, and Total" exercise accepts no arguments
    #This exercise will take an integer (input) from the user, make calculations,
    #and give the output to the user. The output from this exercise are "sales was",
    #"tip amount is", sales tax amount is", and "total bill is".
    
    #Input from the user
    saleamount = float(input("Please enter the sale amount: "))
    
    #Calculations
    tipamount = saleamount * .18
    salestaxamount = saleamount * .07
    totalbill = tipamount + salestaxamount + saleamount
    
    #Output for the user
    print("The sale was:\t\t\t", end = "$")
    print(format(saleamount, "9.2f"))
    print("The tip amount is:\t\t", end = "$")
    print(format(tipamount, "9.2f"))
    print("The sales tax amount is:\t", end = "$")
    print(format(salestaxamount, "9.2f"))
    print("The total bill is:\t\t", end = "$")
    print(format(totalbill, "9.2f"))
    
def ex2_9():
    #The "Celsius to Fahrenheit Converter" exercise accepts no arguments
    #This exercise will take input from the user, make a calculation
    #, and give output back to the user. This exercise will give the user
    #their input converted into Farenheit.
    
    #Input from the user
    celsius = float(input("Please enter the degree Celsius: "))
    
    #Calculations
    fahrenheit = ((9/5) * celsius) + 32
    
    #Output
    print(celsius, "degrees celsius is ",
          fahrenheit, "degrees fahrenheit")
    
def cookie_monster():
    #The "Cookie Ingredient Adjuster" exercise accepts no arguments
    #This exercise will take input from the user, make some calculations
    #using integer division (//) to get the number of cups and modulus (%)
    #to get the number of ounces
    
    #Input from the user
    cookieamount = int(input("How many cookies do you want to make? "))
    
    #Calculations
    #Sugar
    totalsugar = cookieamount * .5
    cupsofsugar = totalsugar // 8
    ozofsugar = totalsugar % 8
    #Butter
    totalbutter = cookieamount * .3333
    cupsofbutter = totalbutter // 8
    ozofbutter = totalbutter % 8
    #Flour
    totalflour = cookieamount * .9166
    cupsofflour = totalflour // 8
    ozofflour = totalflour % 8
    
    #Output
    print("For ", cookieamount, "cookies you will need:")
    print(format(cupsofsugar, ".0f"), """cup(s)""", format(ozofsugar, ".0f"), "ounces of sugar.")
    print(format(cupsofbutter, ".0f"), """cup(s)""", format(ozofbutter, ".0f"), "ounces of butter.")
    print(format(cupsofflour, ".0f"), """cup(s)""", format(ozofflour, ".0f"), "ounces of flour.")

def class_demographics():
    #The "Male and Female Percentages" exercise accepts no arguments
    #This exercise will calculate the percentage of males and females in a class
    #The output will be the percentage of males and females in a class
    
    #Input
    femalestotal = int(input("Enter the number of females: "))
    malestotal = int(input("Enter the number of males: "))
    
    #Calculations
    totalstudents = femalestotal + malestotal 
    femalepercent = femalestotal / totalstudents
    malepercent = malestotal / totalstudents
    
    #Output
    print("The class consists of", format(femalepercent, ".0%"), "females and"
          , format(malepercent, ".0%"), "males.")
    
def turtleone():
    #The "turtleone" exercise accepts no arguments)
    #This exercise will use turtle to make 2 projects of our choice.
    #The output will be a compass and the olympics logo.
    
    #Presettings for turtle
    turtle.speed(8)
    turtle.pensize(7)
    
    #Executions
    turtle.penup()
    turtle.left(180)
    turtle.goto(-150, 0)
    turtle.pendown()
    turtle.pencolor("blue")
    turtle.circle(60)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pencolor("black")
    turtle.pendown()
    turtle.circle(60)
    turtle.penup()
    turtle.goto(150,0)
    turtle.pencolor("red")
    turtle.pendown()
    turtle.circle(60)
    turtle.penup()
    turtle.goto(75,-60)
    turtle.pencolor("green")
    turtle.pendown()
    turtle.circle(60)
    turtle.penup()
    turtle.goto(-75,-60)
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(60)
    turtle.done()
    
def turtletwo():
    #The "turtletwo" exercise accepts no arguments
    #This exercise will use turtle to create a compass
    #This exercise will output a compass
    
    #Presettings for turtle
    turtle.speed(8)
    turtle.pensize(7)
    
    #Executions
    turtle.penup()
    turtle.goto(0,90)
    turtle.pendown()
    turtle.goto(0,-90)
    turtle.penup()
    turtle.goto(-90,0)
    turtle.pendown()
    turtle.goto(90,0)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pensize(4)
    turtle.goto(-45,45)
    turtle.pendown()
    turtle.goto(45,-45)
    turtle.penup()
    turtle.goto(45,45)
    turtle.pendown()
    turtle.goto(-45,-45)
    turtle.penup()
    turtle.goto(-5,93)
    turtle.write("N", font=("arial", 16))
    turtle.goto(100,-10)
    turtle.write("E", font=("arial", 16))
    turtle.goto(-5,-120)
    turtle.write("S", font=("arial", 16))
    turtle.goto(-115,-10)
    turtle.write("W", font=("arial", 16))
    turtle.done()
    
    