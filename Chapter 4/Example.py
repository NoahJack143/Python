def loop_example():
    #loop example accepts no arguements
    #It takes input from the user for the number of loops
    #and loops until it reaches the user input
    
    number = int(input("Enter the number of loops to run: "))
    counter = 1 #prime the accumulator (This will stop the while loop)
    #without "counter" your loop will never stop
        
    while counter <= number: #while "number" is true     Step 1
        #run these lines of code
        print("This is loop number", counter )#     Step 2
        counter = counter + 1 #or counter += 1     Step 3 and loop back to Step 1
        
def loop_example2():
    #loop example accepts no arguements
    #It takes input from the user for the number of loops
    #and loops until it reaches the user input.
    
    #     This test uses 0 instead of 1 for the counter
    
    number = int(input("Enter the number of loops to run: "))
    counter = 0 #prime the accumulator (This will stop the while loop)
    #without "counter" your loop will never stop
        
    while counter < number: #while "number" is true     Step 1
        #run these lines of code
        print("This is loop number", counter )#     Step 2
        counter = counter + 1 #or counter += 1     Step 3 and loop back to Step 1
        
def loop_example3():
    #loop example accepts no arguements
    #It takes input from the user for the number of loops
    #and loops until it reaches the user input
    
    #This test uses a sentinel loop
    
    keep_going = "y" #prime the sentinel to "y"
    
        
    while keep_going == "y": #will run as long as keep_going == "y"
        number = int(input("Enter the number of loops to run: "))
        counter = 0
        while counter <= number: #while "number" is true
            print("This is loop number", counter )
            counter = counter + 1 #or counter += 1
        keep_going = input("Keep going? (y/n): ")
    
#iteration
#iteration 5 = loop will run 5 time
        
#range(2)
    #rage(0, 2)
#python starts counting from 0
    
def le2():
    #loop example 4 accepts no arguments
    #it uses a for loop to loop 5 times
    #and outputs a number
    
    for item in range(5):
        print(item)
        
def le3():
    #loop example 5 accepts no arguments
    #it uses a for loop to loop 5 times
    #and outputs a number
    
    for num in [1, 2, 3, 4]: #holds one value until it's done with the loop, then it holds the second value until it's done with the loop
    #and then when it gets to the end, it ends because there isn't anymore to reiterate
        print("I have holding the value", num)
        print("I will now release the value of num")
        
def le4():
    
    for num in range(1, 10+1):
        print(num)
        


def pc(): #procedure commission
    #Procedure commission accepts no arguments
    #This program will take input from the user and then run their input
    #through a loop and then give output
    
    #Sentinel for the loop to end and/or restart
    keep_going = "y"
    
    #Begin the loop
    while keep_going == "y":
        #Input from the user
        sale_amount = int(input("Enter the sale amount: "))
        commission_rate = int(input("Enter the percentage rate: "))
        
        #Calculations
        commission = sale_amount * (commission_rate / 100)
        
        #Output for the user
        print("The commission is $", format(commission, ",.2f"), sep= " ")
        
        #Ask the user if they want to run the calculations again
        keep_going = input("Do you want to calculate another? (y/n): ")
        
def pt(): #procedure temperature
    #procedure temperature accepts no arguments
    #This program will take a temp from the user and tell the user
    #whether they have an acceptable temp or not.
    
    #PRE variables before starting the loop
    max_temp = 102.5
    temp = 103
    
    #Starting the loop
    while temp > max_temp:
        degrees = int(input("Please enter the current substance temperature in degrees Celcius: "))
    
        #Pretty space
        print(" ")
    
        #If the temperature is NOT acceptable
        if degrees > max_temp:
            print("The temperature is too high.")
            print("Turn the thermostat down and wait fro it to cool.")
            print("Then wait 5 minutes and measure again.")
            print(" ")
        #If the temperature is acceptable
        elif degrees <= max_temp:
            print("The temperature is accpetable.")
            print("Measure again in 15 minutes")
            temp = 101
            
def pt2():
    
    #Named constant for the max temp
    max_temp = 102.5
    
    #Prompt the user for the temp
    temp = float(input("Please enter the current substance temperature in degrees Celcius: "))
    
    #The loop
    while temp > max_temp:
        print("\nThe temperature is too high.")
        print("Turn the thermostat down and wait for ti to cool.")
        print("Then wait 5 minutes and measure again.\n")
        temp = float(input("Please enter the new temperature in degrees Celcius: "))
    
    #Remind the user to check the temp again in 15 minutes
    print("The temperature is acceptable.")
    print("Measure again in 15 minutse.")
    
def sl(): #simple_looop 1
    #simple loop 1 accepts no arguments
    #it loops 5 times outputting each number
    
    #display header
    print("I wil display the numbers 1 - 5")
    
    #loop 1-5
    for num in [1, 2, 3, 4, 5]:
        print(num)
        
def sl2():
    #simple loop 2 accepts no arguments
    #it loops the odd numbers from 1-10
    
    print("I will output all odd numbers from 1-10")
    
    for num in [1, 3, 5, 7, 9]:
        print(num)
        
def sl3():
    #simple loop 3 accepts no arguments
    #it outputs names instead of numbers
    
    for name in ["Steve", "Tony", "Thor", "Wanda"]:
        print(name)
        
def sl4(): #simple_looop 1
    #simple loop 1 accepts no arguments
    #it loops 5 times outputting each number
    
    #display header
    print("I wil display the numbers 1 - 10")
    
    #loop 1-5
    for num in range(1,10+1):
        print(num)
        
def sl5(): #simple_looop 1
    #simple loop 1 accepts no arguments
    #it loops 5 times outputting each number
    
    #display header
    print("I wil display the numbers 1 - 5")
    
    #loop 1-5
    for count in range(1,6): #or "range(5)"
        print("Hello World!")
        
def psquare():
    #procedure squares accepts no arguments
    #will take a range of numbers and give their squared pair
    
    print("Number Square")
    print("-------------")
    for num in range(1, 10+1):
        print(num, '\t', num ** 2)
        
def speed_converter():
    #speed_converter accepts no arguments
    #takes a KPH and converts to MPH
    
    print("KPH" "\t" "MPH")
    print("--------------")
    for kph in [60, 70, 80, 90, 100, 110, 120, 130]:
        mph = kph * .6241
        print(kph, '\t', mph)
        
def speed_converter2():
    #speed_converter accepts no arguments
    #takes a KPH and converts to MPH
    
    #Constants
    start_speed = 60
    end_speed = 131
    increment = 10
    conversion_factor = 0.6214
    
    #Text for the top of the box
    print("KPH" "\t" "MPH")
    print("--------------")
    
    #Calculations + inside the box
    for kph in range(start_speed, end_speed, increment):
        mph = kph * conversion_factor
        print(kph, '\t', format(mph, ".1f"))
        
def user_squares():
    #PRE text
    print("This program will display a list of number")
    print("Starting at 1 and their squares.")
    
    #Input from the user
    end = int(input("How many squares? "))
    
    #Setting up the output
    print()
    print("Number\tSquare")
    print("--------------")
    
    #Calculations + output
    for number in range(1, end + 1):
        square = number**2
        print(number, '\t', square)
        
def user_squares2():
    #PRE text
    print("This program will display a list of number")
    print("Starting at a specified number and ending with another specified number and their squares.")
    
    #Input from the user
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    
    #Setting up the output
    print()
    print("Number\tSquare")
    print("--------------")
    
    #Calculations + output
    for number in range(start, end + 1):
        square = number**2
        print(number, '\t', square)
        
def sum_numbers():
    #sum_number accepts no arguments
    
    #PRE text
    print("This program calculates the sum of 5 numbers you will enter.")
    
    #Constants
    MAX = 5
    total = 0
    
    #Input from the user + loop
    for counter in range(MAX):
        number = int(input("Enter a number: "))
        total += number #Same as total = total + number
        
    print("The total of your", MAX, "numbers is: ", total)
    
def property_tax():
    #property_tax accepts no arguments
    
    #Constant
    lot = 1
    
    while lot != 0:
        lot = int(input("Please enter a lot number (ender 0 to end): "))
        property_value = int(input("Please enter the property value: "))
        tax = property_value *.0065
        print("Property tax: $", format(tax, '.2f'))
    
    print("Thank you for using the Cyberdyne Systems property tax calculator, all yoru rights reserved")
    