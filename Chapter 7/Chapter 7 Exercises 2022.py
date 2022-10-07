#Imports
import random

#==============================================#

def m(): #Exercise 0
    #m accepts no arguments
    #it will call for other MAIN FUNCTIONS
    
    #Text before and inside the table
    print('Main Function caller\n---------------------\n' +
    '2) Lotter Number Generator\n3) Rainfall Statistics\n5) Charge Account Validation\n' +
    "7) Driver's License Exam\n11) Tic Tac Toe\n12) White Elephant Exchange\n" +
    "13) Magic 8 Ball\n14) Expense Pie Chart\n15) 1994 Weekly Gas Graph\n" +
    "----------------------")
    
    #Prompt the user for an main function to call
    ui = int(input('Which main function would you like to call? '))
    print('\n\n\n\n\n\n\n')
    
    #List of options
    options = [2,3,5,7,11,12,13,14,15]
    
    #Check to see if the user input is any of the option
    if ui == 2:
        lottery()
    elif ui == 3:
        rainfall()
    else:
        print('Please choose an option from the table.')
        
#==========================================================#
        
def lottery(): #Exercise 2
    #lottery accepts no arguments
    #it will generate a seven-digit- lottery number.
    #it should generate seven random numbers, each in the range of 0 through
    #0, and assign each number to a list element. Then write another loop
    #that displays the contents of the list
    
    #Create a try block incase something fails
    try:
    
        #Create an accumulator
        c = 0
        
        #Create an empty list
        lot_nums = []
        
        #Tell the user that you are generating the lottery numbers
        print('Generating lotto numbers...')
        
        #Create a while loop
        while c != 7:
            #Generate a random number
            number = random.randint(0,9)
            
            #Put the number into a list
            lot_nums.append(number)
            
            #Increase the counter
            c += 1
        
        #Tell the user something before showing the lottery numbers they drew
        print('your lotto numbers are:')
        
        #After breaking out of the loop, write another loop to display the numbers
        for num in lot_nums:
            print(num)
    #Use this except incase something goes wrong
    except:
        print('An error has occured with the lottery machine.\n' +
              'Please try again later.')

#=============================================================#
        
def rainfall(): #Exercise 3
    #rainfall accepts no arguments
    #it will let the user enter the total INCHES of rainfall for each of 12 months
    #into a list. Then, it will calculate and display the total rainfall
    #for the year, the average monthly rainfall, the months with the
    #highest and lowest amount
    #USER VALIDATIONS AND HANDLE EXCEPTIONS
    
    #Create a list of the months
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July'
              , 'August', 'September', 'October', 'November', 'December']
    
    #Create an empty list for the next bit of questions
    rainfall = []
    
    #Ask the user to tell the inches of rainfall for each month
    for month in months:
        #Ask the user for input
        print('Enter the rainfall for', month, end='')
        inches = int(input(': '))
        
        #Append the input into the created list
        rainfall.append(inches)
    
    #After for loop is over, copy the list
    #rainfall2 = X , rainfall = Y
    rainfall2 = []
    
    for element in rainfall:
        rainfall2.append(element)
    
    
    #sort the numbers in list X
    rainfall2.sort()
    
    #Accumulator and counter variables
    c = 0
    index = -1
    
    #read the first element in list X and see where it is located in list Y
    minimum = rainfall2[0] #Find the minimum
    
    for num in rainfall: #Loop through all the elemnts in list Y
        
        if minimum == num: #If minimum matches, then index will = the location of that element in list Y
            index = c
            
        c += 1 #Increase the counter every time

    min_month = months[index] #Find the month with the least rainfall
    
    #Reverse the order of the numbers in list X
    rainfall2.reverse()
    
    #Accumulator counter variables
    c = 0
    index = -1
    
    #read the first element in list X and see where it is located in list Y
    maximum = rainfall2[0] #Find the minimum
    
    for num in rainfall: #Loop through all the elemnts in list Y
        
        if maximum == num: #If minimum matches, then index will = the location of that element in list Y
            index = c

        c += 1 #Increase the counter every time

    max_month = months[index] #Find the month with the least rainfall
    
    #Once the maximum and minimum have been found, find the total rainfall
    #for the year and the average rain per month
    
    #TOTAL RAINFALL
    
    #Variable
    total_rain = 0
    
    #Loop for each year
    for rain in rainfall:
        total_rain += rain
        
    #AVERAGE RAIN P/ MONTH
        
    average_rain = total_rain / 12
    
    #Once all is said and done, print everything that has been found
    print()
    print(min_month, 'had the least rain with', minimum, 'inches of rain.')
    print(max_month, 'had the most rain with', maximum, 'inches of rain.')
    print('Total rain for the year:', format(total_rain, ',.2f'), 'inches')
    print('Average rain per month:', format(average_rain, ',.2f'), 'inches')