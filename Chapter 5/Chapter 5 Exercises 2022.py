import math

def sales_tax(): #Exercise 2
    #sales tax accepts no arguments
    #it will calculate sales tax using other functions
    #it will output the total sale and will validate all inputs
    
    sale_amount = sales_tax_input()
    
    print("Your purchase price was: \t $ \t", format(sale_amount, '9.2f'))
    
    state_tax = sales_tax_state(sale_amount)
    
    county_tax = sales_tax_county(sale_amount)
    
    print("Your state tax amount is: \t $ \t", format(state_tax, '9.2f'))
    
    print("Your county tax amount is: \t $ \t", format(county_tax, '9.2f'))
    
    total_tax, total_sale = sales_tax_totals(state_tax, county_tax, sale_amount)
    
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
    
    carbs, fat = calories_grams()
    
    print("Here is your calorie intake for the day.")
    
    carbs_intake = carbs_for_the_day(carbs)
    
    fat_intake = fat_for_the_day(fat)
    
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
    
    class_a = class_a_tickets()
    
    class_b = class_b_tickets()
    
    class_c = class_c_tickets()
    
    print(" ")
    
    tickets_income = total_income(class_a, class_b, class_c)
    
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
    
    total_square_feet, cost_of_gallons_of_paint = paint_estimator_input()
    
    print("The cost breakdown to paint", total_square_feet, "square feet is:")
    print("-------------------------------------------------------------------")
    
    total_cost_of_paint, total_labor_cost = paint_estimator_total_costs(total_square_feet, cost_of_gallons_of_paint)
    
    total_cost_of_job = paint_estimator_total_cost(total_cost_of_paint, total_labor_cost)
    
    
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
    