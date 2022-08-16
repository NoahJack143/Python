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