#START OF THE EXERCISE STAND IN FILE

def population(): #Exercise 13
    #population accepts no arguments
    #it prompts the user for the population, the perent of growsh per day, and
    #the amount of days for growing. It outputs a table that tells the growth
    #of the population per day. INCLUDES VALIDATIONS
    
    #Input from the user
    starting_population = int(input("Enter the starting population: "))
    percent = int(input("Enter the percent of daily growth: "))
    days = int(input("Enter the number of days to stimulate"))
    
    #Calculations before the loop
    percent /= 100
    
    #Input before the table
    print(" ")
    print("Day\t\tProjected Population")
    print("--------------------------------------")
    
    #VALIDATION
    if starting_population <= 0 or days <= 0:
        print("ERROR")
        print("Enter all positive numbers next time.")
    elif starting_population > 0 and days > 0:
        
        #Begin the loop
        for day in range(1, days + 1):
            #Data printed into the table
            print(day, '\t\t', starting_population)
            
            #Calculations
            starting_population = (starting_population * percent) + starting_population
        
def reverse_triangle(): #Exercise 14
    #reverse triangle accepts no arguments
    #it creates an upside down triangle
    
    #Ask the user for the bse size of the triangle:
    base = int(input("Enter the base size of the triangle: "))
    
    #Begin the loop right after
    for row in range(base, 0, -1):
        for column in range(row):
            print("*", end='')
        print()
        
#CHANGES WERE MADE