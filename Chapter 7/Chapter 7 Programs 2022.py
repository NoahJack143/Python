

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
    else:
        print(search, 'was not found in the list. Check your spelling and try again.')
        
    #Tell the the user what the list looks like
    print('Here is the list: ', end='')
    print(foods)