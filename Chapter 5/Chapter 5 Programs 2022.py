my_value = 10 #Global value

def message(): #Program 5-1
    #message accepts no arguments
    #it outputs one line: I am Iron Man.
    print("I am Iron Man.")

def main(): #Program 5-2
    #accepts no arguments
    #it prints, "I am inevitable."
    #it calls procedure message()
    #then prints, "Only one way to win..."
    
    print("I am inevitable.")
    message() #Calls for the previous function --- Program 5-2
    print("Only one way to win...")
    
#======================================#
    
def greeting():
    #Greetings for acme dryer
    
    print("Hello. We will present you with Acme Dryer diasassembly instruction.")
    
def step1():
    #Step #1
    
    print("Unplug the dryer and move it away from the wall.")
    
def step2():
    #Step #2
    
    print("Remove the si screws from the back of the dryer")
    
def step3():
    #Step #3
    
    print("Remove the back panel.")
    
def step4():
    #Step #4
    
    print("Pull the top of the dryer straight up.")
    
def step5():
    #Step #5
    
    print("Pull the front of the dryer off.")
    
def goodbye():
    #The goodbye function
    
    print("Thank you for using this program.")
    print(" ")
    
    
def acme_dryer(): #Program 5-3
    
    #Accumulater
    step = 0
    
    greeting() #Call for greeting()
    
    step = int(input("Please enter the step you are currently on. Enter 0 if you'd like to end this program: "))
    
    while step == 1 or step == 2 or step == 3 or step == 4 or step == 5: #Check for the step they are on and then call for the step
        print(" ")
        if step == 1:
            step1()
            print(" ")
            step = int(input("Please enter the step you are currently on. Enter 0 if you'd like to end this program."))
        elif step == 2:
            step2()
            print(" ")
            step = int(input("Please enter the step you are currently on. Enter 0 if you'd like to end this program."))
        elif step == 3:
            step3()
            print(" ")
            step = int(input("Please enter the step you are currently on. Enter 0 if you'd like to end this program."))
        elif step == 4:
            step4()
            print(" ")
            step = int(input("Please enter the step you are currently on. Enter 0 if you'd like to end this program."))
        elif step == 5:
            step5()
            print(" ")
            step = int(input("Please enter the step you are currently on. Enter 0 if you'd like to end this program."))
    print(" ")
    if step == 0: #Check if they entered 0
        goodbye()
    elif step < 0 or step > 5: #Check if they didn't enter numbers 0-5
        print(" ")
        print("Please enter a proper step number.")
        
#=================================================================#
        
def bad_scope(): #Program 5-4
    #bad scope accepts no arguments
    #it calls procedure get_name() to get someone's name
    #then outputs a message using tha tname
    #NOTE: The scope of the variable "name" in get_name will not allow this function to access that variable
    
    get_name()
    print("Hello", name) #this will throw an exception BECAUSE name only exists in the function get_name and not in the bad_scope function.
    
def get_name():
    #get name acepts no arguments
    #it prompts the user for their name
    
    name = input("Enter your name: ")
    
#======================================================================#
    
def texas():
    #texas accepts no arguments
    #it assigns the variable birds = 5000
    #then outputs a mesasge "Texas has <birds> birds."
    
    birds = 5000
    
    print("There are", birds, "birds in Texas.")
    
    
def kansas():
    #kansas accepts no arguments
    #it assigns the variable birds = 8000
    #then outputs a message "Kansas has <birds> birds."
    
    birds = 8000
    
    print("There are", birds, "birds in Kansas.")
    
def bird_calculator(): #Main function will only call for functions --- Program 5-5
    #bird calculator accepts no arguments
    #it calls the function texas()
    #then calls the function kansas()
    
    texas()
    
    kansas()
    
#===================================================#
    
def pass_arg(): #Program 5-6
    #pass args accepts no arguments
    #it assigns value = 5
    #it calls show_double, passing value
    
    value = 5
    show_double(value)
    
def show_double(RANDOM_VARIABLE):
    #show double accepts a value for numbr
    #it calculates that number * 2 and prints the result
    
    result = RANDOM_VARIABLE * 2
    print(RANDOM_VARIABLE, "* 2 =", result)
    
def main_for_5_6():
    pass_arg()
    show_double()
    
#====================================================#
    
def volume_conversion(): #Program 5-7
    #voluem conversion accepts no arguments
    #it calls intro() to display a greeting
    #it prompts the user for the number of cups
    #it calls cups_to_ounces, passing the value for cups
    
    intro() #Calls for intro()
    
    print(" ")
    cups = int(input("Please enter the number of cups to convert to oucnes: ")) #Prompt the user
    
    print(" ")
    cups_to_ounces(cups) #calls for cups_to_ounces()
    
def intro():
    #intro accepts no arguments
    #it displays a greetin message describing the program
    #and the conversion rate of cups to ounces
    
    print("Welcome to the cups to fluid ounces vonersion programs.")
    print("For your reference, 1 cup = 8 fluid ounces.")
    
def cups_to_ounces(cups):
    #cups_to_ounces accepts a value for cups
    #it converts the number of cups to the number of oucnes
    #and otputs the result
    
    #Calculations
    oz = cups * 2
    
    #Output
    print(cups, "cup(s) is equal to", oz, "fluid ounces.")
    
#==============================================================================#
    
def show_sum(): #Program 5-8
    #show sum accepts no arguments
    #it outputs a message "The sum of 12 and 45 is"
    #it calls sum_of_numbers(num1, num2) passings the values of 12 and 45
    
    sum_of_numbers(12, 45)
    
def sum_of_numbers(num1, num2):
    #sum of numbers accepts two arguments for num1 and num2
    #it adds the two numbers together
    #and prints the sum
    
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is", result)
    
#===========================================================================#
    
def get_name(): #Program 5-9
    #get name accepts no arguments
    #it prompts the user for their first then last name
    #it calls reverse_name(first, last) passings values
    #for first and last
    
    #Prompt the user for their first and last name
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")
    
    print("Your name reversed is ", end='')
    reverse_name(first, last)
    
    
def reverse_name(first, last):
    #reverse name accepts strings for first and last
    #it outputs the names in reverse order: last, first
    
    print(last, first)
    
#===========================================================#

def get_value(): #Program 5-10
    #get value accpets no argumetns
    #it assings value = 99 and outputs the value
    #it passes value to change_me
    #it outputs a message showing the value of value i this function
    
    value = 99
    print("I just assigned the variable value: ", value)
    change_me(value)
    
    #Output the value in this function
    print("The value in the function get_value is still: ", value)
    
def change_me(value):
    #change me accepts an integer for value
    #it reassigns the value to 0
    #and outputs a message with the new value in this vunction
    
    value = 0
    
    #output the value in this vunction
    print("The value in this fucntion change_me has been changed to: ", value)
    
#===================================================================#
    
def set_args(): #Program 5-11
    #set args accepts no arguments
    #it calls show_interest passing pincipal, rate, and periods as keywords
    
    show_interest(rate=0.01,  periods=10, principal=10000.0)
    
def show_interest(rate, periods, principal):
    #show interset accepts arguments for rate, periods, and princcipal
    #it calculates interest = principal*rate*periods
    #and outputs the result.
    
    interest = principal * rate * periods
    print("The simple interest will be $", format(interest, ',.2f'), sep='')
    
#=============================================================================#
    
my_value = 10 #global variable

def show_value(): #Program 5-13
    #show value receives no arguments
    #it prints the value of global my_value
    
    global my_value
    
    my_value += 1
    
    print("THe value of the global my_value is", my_value)
    
#====================================================================#
    
number = 0
    
def change_global(): #Program 5-14
    #changes_global accepts no arguments
    #it changes the alue of the global variable number
    #then calls global_variables_are_bad to print the variable
    
    global number
    number = int(input("What do you want to change the global to? "))
    global_variables_are_bad()
    
def global_variables_are_bad():
    #global variables are bad accepts no arguments
    #it prints the value of the globa variable number
    
    print("The value of the global variable number was changed in ", end='')
    print("change_global to the value of : ", number)
    
#================================================================#
    #Global constant for program 5-15
CONTRIBUTION_RATE = .05

def pay_me(): #Program 5-5
    #pay me accepts no arguments
    #it prompts the user for the gross pay and amount of bonuses
    #it calls show_pay, passing gross
    #and show_bonus, passing bonus
    
    #Prompt the user for information
    gross = int(input("Please enter the amount for gross pay: "))
    bonus = int(input("Please enter the amount of bonuses: "))
    
    
def show_pay(gross):
    #show pay accepts the float for gross
    #it calculates the contribution = gross * the global constant
    #it outputs the contribution for gros pay
    
    contribution_for_gross_pay = gross * CONTRIBUTION_RATE
    print("Contribution for gross pay: $", format(contribution_for_gross_pay, ',.2f'))
    
def show_bonus(bonus):
    #show_bonus acepts a float for bonus
    #it calculates the contribution = bonus * the global constant
    #it outputs the contribution for bonuses
    
    contribution_for_bonuses = bonus * CONTRIBUTION_RATE
    print("Contribution for bonuses: $", format(contribution_for_bonuses, ',.2f'))