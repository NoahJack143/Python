#Imports
import random

def IsValid(string): #Program EX1 #MAKE SURE STRING IS A STRING BEFORE SENDING: '123' #NOT: 123
    #IsValid accepts one argument
    #it iwll rtun True if the value passed to it is a string
    #containing only numbers and False if it has any characters other
    #than numbers
    
    if string.isnumeric():
        #the string only contains numbers
        return True
    else:
        #The string contains charcters other than numbers
        return False
        
def temp():
    days = ['mon', 'tue', 'wed', 'thur', 'fri']
    
    for day in days: #each iteration through the loop thsi will put out a day from the list of days
        print(day)
    
def numbers(): #Program EX2
    #numbers accepts no arugments
    #it will use the repetition operator *, change the list, numbers, to be [1,2,3,1,2,3,1,2,3]
    #and run the for loop again
    
    numbers = [1,2,3] * 3
    
    for num in numbers:
        print(num)
    
    for num in range(4): #keep in mind that range starts counting from 0
        print(num)
        
    len(numbers) #length will tell you how many elements are within the list
    

def sales_list(): #Program 7-1
    #sales list accepts no arguments
    #it will use the repetition character to create a list of 0s the
    #length of NUM_DAYS: list * NUM_DAYS:
    
    #Text before the question
    print('Enter the sales for each day')
    
    #Prompt the user constantly for the sales for each day
    day1 = int(input('Day #1:'))
    day2 = int(input('Day #2:'))
    day3 = int(input('Day #3:'))
    day4 = int(input('Day #4:'))
    day5 = int(input('Day #5:'))
    
    #Create the list
    NUM_DAYS = [day1, day2, day3, day4, day5]
    
    #Text before the loop
    print('\nHere are the vaues you entered:\n')
    
    #Create a loop for the numbers for each day
    for day in NUM_DAYS:
        print(day)
        
def sales_list_exapmle():
    
    NUM_DAYS = 5
    sales = [0] * NUM_DAYS
    index = 0
    
    print('Enter the sales for each day')
    
    while index < NUM_DAYS:
        print('Day #', index +1, ':', sep='', end='')
        sales[index] = float(input())
    
        index += 1
    
    print('\nHere are the values you entered:\n')
    for sale in sales:
        print(sale)
        
def in_list(): #Program 7-2
    #in list accepts no arguents
    #it creates a list of part numbers
    #V45, V65, V750, VFR1100
    #VTX1300 and prompts the user for a string to search for
    #and prints if the list contains the search string
    
    #Create the list containing the part names
    parts = ['V45', 'V65', 'V750', 'VFR1100', 'VTX1300']
    
    #Ask the user for a part to search for
    searching = input('Enter a string to search for: ')
    
    if searching in parts:
        print('Part number', searching, 'was found in the list of part numbers.')
    else:
        print('Part number not found.')
        
def list_append(): #Program 7-3
    #list appen accepts no arguments
    #it creates an empty list
    #and loops to append the list with input from the user
    #then propts to continue
    
    #Create a list that is empty
    list1 = []
    
    #User a boolean
    done = False
    
    #Loop to append the list with input from the user
    while not done:
        enter = input('Enter a name: ')
        list1.append(enter)
        continuE = input('Add another name? (y to continue) ')
        print('\n')
        if continuE == 'y':
            done = False
        else:
            done = True
    #Tell the user what they entered
    print('You entered the following names:')
    for name in list1:
        print(name)
        
def list_index(): #Program 7-4
    #list index accepts no arguments
    #creates a list of three food items
    #and prompts the uesr to replace of the items
    #it searches the list for the index of the item
    #and prompts the user with a replacement food
    
    #Create the list with the food items
    foods = ['burger', 'pizza', 'ice cream']
    
    #Ask the user for a food to search for in the list
    search = input('Enter the string to search for: ')
    
    #search for the item
    if search in foods:
        index = foods.index(search)
        print('Item found. Enter a new food item')
        replacement = input(': ')
        foods[index] = replacement
    else:
        print(search, 'was not found in the list. Check your spelling and try again.')
        
    #Tell the the user what the list looks like
    print('Here is the list: ', end='')
    print(foods)
    
def list_index_example():
    
    foods = ['burger', 'pizza', 'hotdog']
    
    search = input('Enter the string to search for: ')
    
    try:
        if foods.index(search) >= 0:
            index = foods.index(search)
            new_food = input('Item found. ENter a new food item: ')
            foods[index] = new_food
            
    except:
        print()
        print('The food item was not found. Please check your spelling.')
        
def list_insert(): #Program 7-5
    #list insert accepts no argments
    #it prints the origianl list of three names
    #it inserts a name in a list of names
    #at a specific index and prints the new list
    
    #Create a list of names
    names = ['Bruce', 'Steve', 'Tony']
    
    #Tell the user the list of names
    print('Here is the list before the insert method: ', names)
    
    #Insert a name intro the list
    names.insert(2, 'Sam')
    
    #Tell user the updated list
    print('Here is the list after the inset method: ', names)
    
def list_remove(): #Program 7-6
    #list index accepts no arguments
    #creates a list of three food items
    #and prompts the uesr to replace of the items
    #it searches the list for the index of the item
    #and removes the item from the list
    
    #Create the list with the food items
    foods = ['burger', 'pizza', 'ice cream']
    
    #Ask the user for a food to search for in the list
    search = input('Enter the string to search for: ')
    
    #search for the item
    if search in foods:
        foods.remove(search)
        print('\nItem removed.\n\n')
    else:
        print(search, 'was not found in the list. Check your spelling and try again.')
        
    #Tell the the user what the list looks like
    print('Here is the list: ', end='')
    print(foods)
    
def barista_pay(): #Program 7-7
    #barista pya accepts no arguments
    #it prompts the user for the number of employees, hours worked for each
    #employee and the hourly rate all employees are paid, then outputs
    #each employee's gross pay
    
    #Ask the user for the amount of employees
    emp = int(input('How many employees do you want to calculate pay for? '))
    
    #Create an empty list
    all_hours = []
    
    #Ask the user for the amount of hours each employee worked
    for hours in range(emp):
        print("Enter the hours worked by employee", hours, end='')
        worked = int(input(': '))
        all_hours.append(worked)
        
    #Prompt the user for the hourly rate for all employees
    hourly_rate = int(input("Enter the hourly rate for all employees: "))
    
    #Counter
    c = 1
    
    #Calculate and output eh gross pay for all the employees
    for worker in all_hours:
        gross_pay = hourly_rate * worker
        print('Gross pay for employee', c,':', gross_pay)
        c += 1
        
def list_total(): #Prgoram 7-8
    #list total accepts no arguments
    #it creates a list of numbers [2,4,6,8,10]
    #and loops to accumulate the total of all numbers
    #in the list
    
    #Create a list
    list1 = [2,4,6,8,10]
    
    #Variable
    sum1 = 0
    
    #Create a loop to get the sum of all the numbers
    for num in list1:
        sum1 += num
        
    #Print the sum for the user
    print('The sum of the numbers', list1, 'is:', sum1)
    
def list_avg(): #Program 7-9
    #list avg accepts no arguments
    #it creates a list of numbers [2.5, 7.3, 6.5, 4.0, 5.3]
    #and calculates the average of the numbers using len()
    
    #First create the list
    list1 = [2.5, 7.3, 6.5, 4.0, 5.3]
    
    #Create a variable
    sum1 = 0
    
    #Create a loop to get the sum of all the numbers
    for num in list1:
        sum1 += num
        
    #Find out the total amount of numbers in the list
    total_num = len(list1)
    
    #Find the average
    average = sum1 / total_num
    
    #print the average for the user
    print('The average of the numbers', list1, 'is:', format(average, ',.1f'))
    
#===================#
    
def list_function(): #Program 10
    #list function acepts no arguments
    #it creates a list [2,4,6,8,10]
    #it passes eh list to get_total
    #it prints the returned total
    
    #Create a list
    numbers = [2,4,6,8,10]
    
    #Call the function get_total
    sum1 = get_total(numbers)
    
    #print the total for the user
    print('The sum of the numbers', numbers, 'is:', sum1)
    
def get_total(numbers):
    #get total accepts one argument
    #get total accepts a list of numbers
    #it calculates and returns the total
    
    list1 = numbers
    
    #Variable
    sum1 = 0
    
    for num in list1:
        sum1 += num
    
    return sum1
    
#==============#
    
def list_return(): #Program 7-11
    #list return accepts no arguments
    #it calls get_values to create a list reference
    #and outputs the numbers in the list
    
    #Call for get_values to get a list
    list1 = get_values()
    
    #Print the list for the user
    print('You entered the numbers:', list1)
    
def get_values(): #For program 7-11
    #get values accepts no arguments
    #it will create an empty aggregator
    #and loops, prompting the user to enter a value
    #and appending that value to the list
    #and to if they want to add another value
    #it returns the reference to the list
    
    #create an empty list
    list1 = []
    
    #boolean variable
    done = False
    
    #Start asking the user to append numbers to the list
    while not done:
        #Prompt the user for a number
        num = int(input('Input a number: '))
        
        #Append that number into the list
        list1.append(num)
        
        #Ask the user if they want to continue
        keep_going = input('Would you like to add another? (y/n) ')
        
        #Check their response and go accordingly
        if keep_going.lower() == 'y':
            done = False
        else:
            done = True
    
    return list1

#=========================#

def test_calc(): #Program 7-12
    #test calc accepts no arguments
    #it will take student scores as an input and
    #calculate the average score with the lowerst score dropped.
    #it will call a lot of other functions
    
    #call for the function get_scores()
    scores = get_scores()
    
    #Make calculations to find the minimal
    low_score = min(scores)
    
    #Remove the lowest score in the list
    scores.remove(low_score)
    
    #Send the list to get_total to get the sum
    sum_of_scores = get_total(scores)
    
    total_numbers = len(scores)
    #Calculate the average
    average = sum_of_scores / total_numbers
    
    #print the lowest score and the average without the lowest score
    print(low_score, 'is the lowest score that was removed.')
    print(average, 'is the average of the scores.')
    
def get_scores(): #For prgoram 7-12
    #get_scores accepts no arguments
    #it will find all the scores and send it back to the
    #main function
    
    #Create a list
    scores = []
    
    #Boolean variable
    done = False
    
    #Create a while loop to ask the user for scores
    while not done:
        #Prompt the user for a score
        score = int(input('Enter a score: '))
        
        #Append that score to the list
        scores.append(score)
        
        #Propt the user to see if they want to keep going
        keep_going = input('Would you like to add another? (y/n) ')
        
        #Check their response and go accordingly
        if keep_going.lower() == 'y':
            done = False
        else:
            done = True
            
    #Return the list to the main function
    return scores

#+==========================

def list_writelines(): #Program 7-13
    #list writelines accepts no arguments
    #it writes the entire contents of the list
    #to the file cities.txt
    
    cities = ['Kansas City', 'Lawrence', 'WIchita', 'Manhatta']
    
    try:
        #open the file
        outfile = open('cities.txt', 'w')
        
        #write the list tot he file
        outfile.writelines(cities)
        
        #close the file
        print('All data written to cities.txt')
        outfile.close()
    except Exception as err:
        print(err)
        
def list_writelines(): #Program 7-14 #FIX THIS LATER
    #list writelines accepts no arguments
    #it writes the entire contents of the list
    #to the file cities.txt
    
    cities = ['Kansas City', 'Lawrence', 'WIchita', 'Manhatta']
    
    try:
        #open the file
        outfile = open('cities.txt', 'w')
        
        #write the list tot he file
        outfile.writelines(cities)
        
        #close the file
        print('All data written to cities.txt')
        outfile.close()
    except Exception as err:
        print(err)
        
def list_read(): #Prgoram 4-15
    #list read accepts no arguments
    #it reads from cities.txt and aggregates the data
    #to the list cities, stripping the \n fro each
    
    try:
        #open the file
        infile = open('cities.txt', 'r')
        
        #read the contents to a list
        cities = infile.readlines()
        
        #close the file
        infile.close()
    except:
        print('Error reading from the file.')
        
    #initialize index
    index = 0
    
    #strip the newline and reassign it to the list
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    print('Here is the information read from cities.txt.')
    print(cities)
    
def list_writes_numbers(): #PRogram 7-16
    #list write numbers accepts no arguments
    #it saves a list of integers [1,2,3,4,5,6,7]
    #to the file numberlist.txt
    
    #create list
    numbers = [1,2,3,4,5,6,7]
    
    #open the file
    outfile = open('numberlist.txt', 'w')
    
    #loop to write the numbers to the list
    for number in numbers:
        outfile.write(str(number) + '\n')
        
    #close the file
    outfile.close()
    print('All numbers saved to numberlist.txt')
    
def list_read_numbers(): #Program 7-17
    #list read numbers accepts no arguments
    #it reads integers from the fil numberlist.txt
    #and aggregates them to a list
    
    #intitialize the aggregator
    number = []
    
    try:
        #open the file
        infile = open('numberlist.txt', 'r')
        
        #loop to add each number to the list
        for num in infile:
            numbers.append(int(num.rstrip('\n')))
            
        #Close the file
        infile.close()
        
    except Exception as err:
        print(err)
    print('Here is the list created from numberlist.txt:')
    print(numbers)
    
def random_numbers(): #Program 7-18
    #random numbers accepts no arguments
    #it creates a 2d list with a maximum row index of 3
    #and a maximum column index of 2
    #it uses nested loops to fill the 2d list with a random number
    #from 1- 100
    
    #constants for row/cols loops
    ROWS = 3
    COLS = 4
    
    values = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    
    #loop to fill the list with random numbers
    for row in range(ROWS):
        for col in range(COLS): #for each row, fill all the columns
            values[row][col] = random.randint(1, 100)
            
    #output the list
    print(values)