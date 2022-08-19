

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
    cookieamount = float(input("How many cookies do you want to make? "))
    
    #Calculations
    #Sugar
    totalsugar = cookieamount * .5
    cupsofsugar = totalsugar // 8
    ozofsugar = totalsugar % 8
    #Butter
    totalbutter = cookieamount * .3333
