#Imports for Chapter 5
import math
import random
import My_Graphics
import turtle

def sales_tax(): #Exercise 2
    #sales tax accepts no arguments
    #it will calculate sales tax using other functions
    #it will output the total sale and will validate all inputs
    
    sale_amount = sales_tax_input()
    
    print("Your purchase price was: \t $ \t", format(sale_amount, '9.2f'))
    
    state_tax = sales_tax_state(sale_amount) #Call sales tax state to get the state tax
    
    county_tax = sales_tax_county(sale_amount) #Call sales tax county to get the county tax
    
    print("Your state tax amount is: \t $ \t", format(state_tax, '9.2f'))
    
    print("Your county tax amount is: \t $ \t", format(county_tax, '9.2f'))
    
    total_tax, total_sale = sales_tax_totals(state_tax, county_tax, sale_amount) #sales tax totals to get the total tax amount and the total sale amount
    
    print("Your total tax is: \t\t $ \t", format(total_tax, '9.2f'))
    
    print("Your total sale is: \t\t $ \t", format(total_sale, '9.2f'))
    
def sales_tax_input(): #For Exercise 2
    #sales tax input accepts no arguments
    #this will prompt the user for the sale amount
    #this will also validate their answer
    
    LOOP = 0 #Accumulator
    
    sale_amount = int(input("Enter the sale amount: ")) #Input
    
    while LOOP == 0: #While loop for validation
        if sale_amount >= 0:
            LOOP = 1
        elif sale_amount < 0:
            LOOP = 0
            print("Please enter a valid sale amount", end='')
            sale_amount = int(input(": "))
    
    return sale_amount #return their input

def sales_tax_state(sale_amount): #For Exercise 2
    #sales tax state accepts one argument
    #it will make a calculation and return the product
    
    state_tax = sale_amount * .05
    
    return state_tax

def sales_tax_county(sale_amount): #For Exercise 2
    #sales tax county accepts one argument
    #it will make a calculation and return the product
    
    county_tax = sale_amount * .025
    
    return county_tax

def sales_tax_totals(state_tax, county_tax, sale_amount): #For Exercise 2
    #sales tax totals accepts three arguments
    #it will calculate the total tax and the total sale
    
    total_tax = state_tax + county_tax
    
    total_sale = total_tax + sale_amount
    
    return total_tax, total_sale

#=====================================================================================#

def calories(): #Exercise 6
    #calories accepts no arguments
    #it will calculate the amount of calories someone has taken in for a day
    #it will use a minimum of three functions and outputs the user's calorie intake
    
    carbs, fat = calories_grams() #Call calories grams to get information from the user
    
    print("Here is your calorie intake for the day.")
    
    carbs_intake = carbs_for_the_day(carbs) #Prompt the user for the amount of carbs they consumed
    
    fat_intake = fat_for_the_day(fat) #Prompt the user for the amount of fats they consumed
    
    print("You consumed", carbs_intake, "calories worth of carbs today. Nice work...")
    
    print("You consumed", fat_intake, "calories worth of fats today. Nice work...")
    
def calories_grams(): #For Exercise 6
    #calories accepts no arguments
    #it will prompt the user for the amount of carbs and fat they've taken in for the day
    
    carbs = int(input("How many grams of carbs did you consume? "))
    
    fat = int(input("How many grams of fat did you consume? "))
    
    return carbs, fat

def carbs_for_the_day(carbs): #For Exercise 6
    #carbs for the day accepts one argument
    #it will calculate the amount of carbs the user has taken in for the day
    
    carbs_intake = carbs * 4
    
    return carbs_intake

def fat_for_the_day(fat): #For Exercise 6
    #fat for the day accepts one argument
    #it will calculate the amount of fat the user has taken in for the day
    
    fat_intake = fat * 9
    
    return fat_intake

#=====================================================================================#

def stadium_seating(): #Exercise 7
    #stadium seating accepts no arguments
    #it will calculate the amount spent based on the tickets that were bought
    
    class_a = class_a_tickets() #Call class a tickets to get the total amount of class a seat tickets were bought
    
    class_b = class_b_tickets() #Call class b tickets to get the total amount of class b seat tickets were bought
    
    class_c = class_c_tickets() #Call class c tickets to get the total amount of class c seat tickets were bought
    
    print(" ")
    
    tickets_income = total_income(class_a, class_b, class_c) #Call total_income to get the total cost for all the tickets combined
    
    print("The total income sales from tickets is: $", format(tickets_income, ',.2f'), sep='')
    
def class_a_tickets(): #For Exercise 7
    #class a tickets accepts no arguments
    #it will prompt the user for the amount of class a tickets bought
    #it will also validate the users inputs
    
    LOOP = 0
    
    class_a = int(input("Enter the number of Class A tickets sold: "))
    
    while LOOP == 0:
        if class_a >= 0:
            LOOP = 1
        elif class_a < 0:
            LOOP = 0
            class_a = int(input("Enter a valid number of Class A tickets sold: "))
            
    return class_a

def class_b_tickets(): #For Exercise 7
    #class a tickets accepts no arguments
    #it will prompt the user for the amount of class b tickets bought
    #it will also validate the users inputs
    
    LOOP = 0
    
    class_b = int(input("Enter the number of Class B tickets sold: "))
    
    while LOOP == 0:
        if class_b >= 0:
            LOOP = 1
        elif class_b < 0:
            LOOP = 0
            class_a = int(input("Enter a valid number of Class B tickets sold: "))
            
    return class_b

def class_c_tickets(): #For Exercise 7
    #class a tickets accepts no arguments
    #it will crompt the user for the amount of class c tickets bought
    #it will also validate the users inputs
    
    LOOP = 0
    
    class_c = int(input("Enter the number of Class C tickets sold: "))
    
    while LOOP == 0:
        if class_c >= 0:
            LOOP = 1
        elif class_a < 0:
            LOOP = 0
            class_c = int(input("Enter a valid number of Class C tickets sold: "))
            
    return class_c

def total_income(class_a, class_b, class_c): #For Exercise 7
    #total income accepts 3 arguments
    #it will calculate the total income for selling all of the tickets
    
    #Find the total amount for each tickets
    class_a_total = class_a * 20
    
    class_b_total = class_b * 15
    
    class_c_total = class_c * 10
    
    #Find the total income
    total_income = class_a_total + class_b_total + class_c_total
    
    #Return the total income
    return total_income

#====================================================================================#

def paint_estimator(): #Exercise 8
    #paint estimator accepts no arguments
    #it will determine the square feet of wall space t be painted and
    #the price f the paint per gallon
    #this will use a minimum of three functions
    
    total_square_feet, cost_of_gallons_of_paint = paint_estimator_input() #Call paint estimator to get the total square feet the cost of gallons of paint
    
    print(" ")
    print("The cost breakdown to paint", total_square_feet, "square feet is:")
    print("-------------------------------------------------------------------")
    
    total_cost_of_paint, total_labor_cost = paint_estimator_total_costs(total_square_feet, cost_of_gallons_of_paint) #Call paint estimator total costs to get the total costs
    
    total_cost_of_job = paint_estimator_total_cost(total_cost_of_paint, total_labor_cost) #Call paint estimator total cost to get the final cost
    
    print("Total cost of paint: $", format(total_cost_of_paint, '.2f'), sep='')
    
    print("Total labor cost: $", format(total_labor_cost, '.2f'), sep='')
    
    print("Total cost of the job is: $", format(total_cost_of_job, '.2f'), sep='')
    
    
def paint_estimator_input(): #For Exercise 8
    #paint estimator input accepts no arguments
    #it will prompt the user for the some information and return them
    #it will also validate their answers
    
    LOOP = 0 #Accumulator
    
    total_square_feet = int(input("Please enter the total square feet to be painted: "))
    
    cost_of_gallons_of_paint = int(input("How much is each gallon of paint? "))
    
    #Get input from the user
    while LOOP == 0:
        if total_square_feet >= 0 and cost_of_gallons_of_paint >= 0:
            LOOP = 1
        elif total_square_feet < 0 or cost_of_gallons_of_paint < 0:
            LOOP = 0
            print("ERROR")
            total_square_feet = int(input("Please enter a valid total square feet to be painted: "))
            cost_of_gallons_of_paint = int(input("Please enter a valid price for each gallon of paint: "))
            
    #return the inputs
    return total_square_feet, cost_of_gallons_of_paint

def paint_estimator_total_costs(total_square_feet, cost_of_gallons_of_paint): #For Exercise 8
    #paint estimator total costs accepts two arguments
    #it will calculate the total costs for paint and labor
    
    #Find the total cost for paint
    gallons_of_paint = math.ceil(total_square_feet / 112)
    
    total_cost_of_paint = gallons_of_paint * cost_of_gallons_of_paint
    
    #Find the total cost for labor
    total_hours_of_work = gallons_of_paint * 8
    
    total_labor_cost = total_hours_of_work * 35
    
    return total_cost_of_paint, total_labor_cost
    
def paint_estimator_total_cost(total_cost_of_paint, total_labor_cost): #For Exercise 8
    #paint estimator total cost accepts two arguments
    #it will calculate the total cost for the job
    
    total_cost_of_job = total_cost_of_paint + total_labor_cost
    
    return total_cost_of_job
    
#=========================================================================================#

def math_quiz(): #Exercise 11
    #math quiz accepts no arguments
    #this will createa a simple test for the user to solve.
    #once the user solves, correct or incorrect, the user will be asked if they want to continue.
    
    #Start the loop before everything to get different integers each time
    continue1 = 'y'
    while continue1 == 'y':
        
        num1, num2 = get_numbers() #Call for get_numbers and get the random integers
        
        answer = num1 + num2 #Find the sum of the two random integers
        
        #Text for the user before the loop and input from the user
        print("Solve:")
        print(" ")
        print("\t\t", num1)
        print("+\t\t", num2)
        print(" ")
        user_answer = int(input("Answer: "))
        #Check their answer
        if user_answer == answer:
            print("Correct!")
        elif user_answer != answer:
            print("WRONG!! The answer is:", answer)
        print(" ")
        
        #Prompt the user to see if they want to continue
        continue1 = input("Do you want another problem? (y/n) ")
        
    
def get_numbers(): #For Exercise 11
    #get numbers accepts no arguments
    #it will generate two random integers from 1-200 and will return them to math_quiz
    
    num1 = random.randint(1, 200)
    
    num2 = random.randint(1, 200)
    
    return num1, num2

#===============================================================================#

def time_loop(): #Exercise 13
    #time loop accepts no arguments
    #it loops 1-10, calls falling_distance passing time, 1-10 in seconds
    #due to there being no inputs from the user, there will be no validation
    
    #Constants
    gravity = 9.8
    
    #PRE text above the table
    print("Here is the distance an object will fall for 10 seconds")
    print("----------------------------------------------------------")
    
    #Start a for loop that will contain time in range
    for time in range(1, 10+1):
        distance = falling_distance(time) #Call for time
        
        print(time, "sec \t\t", format(distance, '.2f'), end='m') #print the distance for each second
        print(" ")
    
def falling_distance(time): #For Exercise 13
    #falling distance accepts one argument
    #it will calculate the distance fallen
    
    #Constants
    g = 9.8
    t = time
    
    #Calculations
    acceleration = g * t**2
    distance = acceleration * .5
    
    #Return distance
    return distance

#===============================================================================#

def game(): #Exercise 21
    #game accepts no arguments
    #it will allow the computer to play a game of rock, paper, scissors, lizard, spock with the user
    #it will output the winner each time
    
    #Begin a while loop to loop the game
    LOOP = 0
    
    while LOOP == 0:
        player_choice1 = player_choice() #Call for player choice to get the players choice
        
        print(" ")
        print(" ")
        
        comp_choice = computer_choice() #Call for computer choice to get the computers choice
        
        dominator = winner(player_choice1, comp_choice) #Call for winner to find out whether the computer won or the user won
        
        print(" ")
        print(dominator)
        
        print(" ")
        again = input("Play again? (y/n) ")
        
        if again == 'y':
            LOOP = 0
        elif again != 'y':
            LOOP = 1
        
def player_choice(): #For Exercise 21
    #player choice accepts no arguments
    #it prompts the user for their choice in the game and returns it to the main function
    #it will validate the users answser and will prompt the user again if their answer isn't valid
    
    LOOP = 0 #Accumulator
    
    while LOOP == 0: #Validate and recieve the user input
        pc = input("Type your weapon of choice (rock, paper, scissors, lizard, spock) ").lower()
        
        if pc == "rock" or pc == 'paper' or pc == 'scissors' or pc == 'lizard' or pc == 'spock':
            print(" ")
            print("You chose.... ", pc, end='.')
            LOOP = 1
        else:
            print("Choose a proper choice.")
            print(" ")
            LOOP = 0
    
    return pc
    
def computer_choice(): #For Exercise 21
    #computer choice accepts no arugments
    #it will find out the computer's choice for the game
    #no validation is needed here
    
    cc = random.randint(1, 5)
    
    if cc == 1:
        cc = 'rock'
    elif cc == 2:
        cc = 'paper'
    elif cc == 3:
        cc = 'scissors'
    elif cc == 4:
        cc = 'lizard'
    elif cc == 5:
        cc = 'spock'
    
    return cc

def winner(player_choice1, comp_choice): #For Exercise 21
    #winner accepts two arguments
    #it will decide whether the computer or the user wins in the game
    #no validation is needed here
    
    #Changing the arguments
    pc = player_choice1
    cc = comp_choice
    
    print("The computer chose....", cc, end='.')
    print(" ")
    #Start checking the results
    if pc == 'rock' and cc == 'rock':
        champion = "It's a tie!"
    elif pc == 'rock' and cc == 'paper':
        champion = "The computer wins! Paper covers rock."
    elif pc == 'rock' and cc == 'scissors':
        champion = "You win! Rock crushes scissors."
    elif pc == 'rock' and cc == 'lizard':
        champion = "You win! Rock crushes lizard."
    elif pc == 'rock' and cc == 'spock':
        champion = "The computer wins! Spock vaporizes rock."
    elif pc == 'paper' and cc == 'rock':
        champion = "You win! Paper covers rock."
    elif pc == 'paper' and cc == 'paper':
        champion = "It's a tie!"
    elif pc == 'paper' and cc == 'scissors':
        champion = "The computer wins! Scissors cuts paper."
    elif pc == 'paper' and cc == 'lizard':
        champion = "The computer wins! Lizard eats paper."
    elif pc == 'paper' and cc == 'spock':
        champion = "You win! Paper disproves spock."
    elif pc == 'scissors' and cc == 'rock':
        champion = "The computer wins! Rock crushes scissors."
    elif pc == 'scissors' and cc == 'paper':
        champion = "You win! Scissors cuts paper."
    elif pc == 'scissors' and cc == 'scissors':
        champion = "It's a tie!"
    elif pc == 'scissors' and cc == 'lizard':
        champion = "You win! Scissors decapitates lizard."
    elif pc == 'scissors' and cc == 'spock':
        champion = "The computer wins! Spock smashes scissors."
    elif pc == 'lizard' and cc == 'rock':
        champion = "The computer wins! Rock crushes lizard."
    elif pc == 'lizard' and cc == 'paper':
        champion = "You win! Lizard eats paper."
    elif pc == 'lizard' and cc == 'scissors':
        champion = "The computer wins! Scissors decapitates lizard."
    elif pc == 'lizard' and cc == 'lizard':
        champion = "It's a tie!"
    elif pc == 'lizard' and cc == 'spock':
        champion = "You win! Lizard poisons spock."
    elif pc == 'spock' and cc == 'rock':
        champion = "You win! Spock vaporizes rock."
    elif pc == 'spock' and cc == 'paper':
        champion = "You win! Spock eats paper."
    elif pc == 'spock' and cc == 'scissors':
        champion = "You win! Spock smashes scissors."
    elif pc == 'spock' and cc == 'lizard':
        champion = "The computer wins! Lizard poisons spock."
    elif pc == 'spock' and cc == 'spock':
        champion = "It's a tie!"
        
    return champion

#=====================================================================#

def draw_snowman(): #Exercise 23
    #draw snowman accepts no arguments
    #draw snowman will use a variety of functions... to draw a snowman
    #the output will be a snowman
    
    turtle.hideturtle() #This is to hide turtle
    
    draw_base() #Calls for draw base to create the largest snowball for the snowman
    
    draw_mid_section() #Calls for draw mid section to create the second largest snowball for the snowman
    
    draw_head() #Calls for draw head to create the third largest snowball for the snowman
    
    draw_face() #Calls for draw face to create the face for the snowman and the pipe for the snowman
    
    draw_hat() #Calls for draw hat to create the hat that will go on top of the snowman
    
    draw_arms() #Calls for draw arms to create the sticks that will act as the snowman's arms
    
    turtle.hideturtle() #Hides turtle again
    
    turtle.done() #Turtle is done when turtle is done
    
def draw_base(): #For Exercise 23
    #draw base accpets no arguments
    #this is for the base of the snowman
    #this will return the turtle commands to the main function
    
    My_Graphics.circle(0, -170, 140, 'blue')
    
def draw_mid_section(): #For Exercise 23
    #draw mid section accepts no arguments
    #this snowman will create the middle section of the snowman
    #it will return the turtle comands to the main function
    
    My_Graphics.circle(0, 70, 100, 'blue')
    
def draw_head(): #You get the idea by now
    #draw head accepts no arguments
    #it will draw the head of the snowman and send it back to the main function
    
    My_Graphics.circle(0, 237, 67, 'blue')
    
def draw_face(): #I don't have to explain what exercise this function is for
    #draw face accepts no arguments
    #it will draw the face of the snowman (with a pipe) and sent it back to the main function
    
    My_Graphics.circle(-25, 250, 15, 'black')
    
    My_Graphics.circle(25, 250, 15, 'black')
    
    My_Graphics.line(-25, 215, 25, 215, 'black')
    
    My_Graphics.line(15, 215, 85, 185, 'brown')
    
    My_Graphics.square(85, 185, 10, 'brown')
    
    My_Graphics.line(85, 185, 115, 215, 'gray')
    
    My_Graphics.circle(115, 215, 3, 'white')
    
    My_Graphics.line(115, 215, 145, 225, 'gray')
    
    My_Graphics.circle(145, 225, 3, 'white')
    
    My_Graphics.line(145, 225, 165, 230, 'gray')
    
    My_Graphics.circle(165, 230, 3, 'white')
    
    My_Graphics.line(165, 230, 185, 233, 'gray')
    
def draw_hat(): #You know where this is contributing to
    #draw hat accepts no arguments
    #it creates the hat for the snowman and returns it to the main function
    
    My_Graphics.square(-55, 300, 35, 'red')
    
    My_Graphics.square(25, 300, 35, 'red')
    
    My_Graphics.square(-20, 302, 50, 'red')
    
def draw_arms(): #Last one...
    #draw darms accepts no arguments
    #it creates arms for the snowman and returns it to the main function
    
    #Snowman's left arm
    My_Graphics.line(90, 50, 130, 160, 'black')
    
    My_Graphics.line(130, 160, 130, 200, 'black')
    
    My_Graphics.line(130, 160, 150, 130, 'black')
    
    #Snowman's right arm
    My_Graphics.line(-90, 50, -150, 110, 'black')
    
    My_Graphics.line(-150, 110, -165, 160, 'black')
    
    My_Graphics.line(-165, 160, -185, 140, 'black')
    
    My_Graphics.line(-165, 160, -170, 180, 'black')
    
#==============================================================================#
    
def checkerboard(): #Exercise 25
    #checkerboard accepts no arguments
    #it creates a checkerboard using loops
    #Nothing was mentioned about calling another function besides the module My_Graphics
    
    color = 1 #1 = black. 2 = white
    
    for RANDOM_VARIABLE in range(-120, 180, 60): #This is for the rows
        for ANOTHER_VARIABLE in range(-120, 180, 60): #This is for the columns
            if color == 1:
                My_Graphics.square(RANDOM_VARIABLE, ANOTHER_VARIABLE, 60, 'black') #Calls for My_Graphics.square when the previous color was white or when this is the first box
                color = 2
            elif color == 2:
                My_Graphics.square(RANDOM_VARIABLE, ANOTHER_VARIABLE, 60, 'white') #Calls for My_Grpahics.sqare when the previous color was black
                color = 1
                
    turtle.hideturtle() #Hards turtle in the end
    turtle.done() #Turtle is done when turtle is done.