

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

    