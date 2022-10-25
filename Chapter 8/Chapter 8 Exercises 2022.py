

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
    
    #List of dates and days
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                   'September', 'October', 'November', 'December']
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    
    #Create a boolean variable and a while loop
    cont = False
    while not cont:
        
        #Try block
        try:
            
            #Ask the user for the date
            date = input('\nEnter a date in the format mm/dd/yyyy: ')
            
            #Check to see if the format is formatted correctly and split the date if so
            if date[:1].isdigit() and date[3:4].isdigit() and date[6:].isdigit() and date[2] == '/' and date[5] == '/':
                date_splitted = date.split('/')
            else:
                t = b
            
            #Check to see if the month and date are valid
            if date_splitted[0] in months and date_splitted[1] in days:
                m = date_splitted[0]
                d = date_splitted[1]
                y = date_splitted[2]
            else:
                0/0
            
            #Check to see if the month and day and valid with each other
            if m == '02' and int(d) > 28:
                m += 1
            elif m =='04' or m == '06' or m == '09' or m == '11':
                if int(d) > 30:
                    m += 1
            
            #Check for the name of the month apply a name to m
            index = 0
            for month in months:
                if m == month:
                    m = month_names[index]
                else:
                    index += 1
            
        #If soemthing goes wrong, ask again and continue looping
        except NameError:
            print('\nCheck your formatting and make sure there are no letters.')
        except ZeroDivisionError:
            print('\nMake sure you month number and day number are actual month and day numbers.')
        except TypeError:
            print('\nMake sure that your day is appropriate according to your month.')
        #If something goes right, then print the outcome and stop looping
        else:
            print(f'\nThe date is: {m} {d}, {y}')
            cont = True