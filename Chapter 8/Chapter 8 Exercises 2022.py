

#==========#

def sum_of_digits(): #Exercsise 2
    #sum of digits accepts no arguments
    #it will ask the user to enter a series of single digit numbers
    #it will then output the sum of the single digit numbers
    #validating will be used for the user input
    
    #Prompt the user for a series of single digit numbers without spaces
    ui = input('Enter a series of single digit numbers without spaces: ')
    
    #Create a boolean if needed variable and a checker
    if not ui.isdigit() or ui.isspace():
        cont = False
    else:
        cont = True
            
    #Check if needed
    while not cont:
        ui = input('Enter a series of single digit numbers WITHOUT spaces (no letters) ')
        
        #Check again
        if not ui.isdigit() or ui.isspace():
            cont = False
        else:
            cont = True
        
    #Get the sum of the numbers
    c = 0
    for number in ui:
        c += int(number)
    
    #Print the output
    print('The sum of your string is:', c)
    
#==========#
    
def date_converter(): #Exercise 3
    #date converter accepts no arguments
    #it will read a string in the format of 01/02/2007 and
    #will output the date if the string is formatted correctly
    
    #Ask the user for a date
    date = input('Enter a date in the format mm/dd/yyyy: ')
    
    #Create a boolean variable and a while loop
    cont = False
    while not cont:
        
        #Try block     #BE SURE TO CONVERT date[#] TO INTEGERS
        try:
        
            #Check to see if the characters are in the right spots
            if date[:1+1].isdigit() and date[2] == '/' and date[3:4+1].isdigit() and date[4] == '/' and date[5:].isdigit():
                t = 1
            else:
                t = b
             
             #Check to see if the month number and the days number are right
            if date[0] > 1 or date[0] < 0 or date[1] < 0 or date[0] == 1 and date[1] > 2 or date[3] > 2 and date[4] > 1 or date[3] < 0 or date[4] < 0:
                t = b
            else: 
                t = 1
                
            #Check to see if the month and the amount of days match
            if date[0] == 0 and date[1] == 2 and date[3] < 3 and date[4] > 8:
                t = b
            else:
                t = 1
        except: #If something fails
            cont = False
        else: #If all works
            cont = True
    
    #print the date that the user entered
    if date[0] == 0 and date[1] == 1