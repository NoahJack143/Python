

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

def eq(): #loan_qualifier           #multiple "if" statements
    #loan qualifier is going to take input from the user
    #use multiple "if" statements, and then give a output
    #dependent on the "if" statements.
    
    #input from the user
    salary = int(input("Enter your annual salary: "))
    jobs = int(input("Enter the number of years at your current job: "))
    
    #IF statement #1
    if salary >= 30000:
        #IF statement #2
        if jobs >= 2:
            print("You qualify for the loan")
        #false statement #2
        else:
            print("You must have been on your current job for at least two "
                  "years to qualify.")
    #false statement #1
    else:
        print("You must earn at least $30,000 per year to qualify.")
        