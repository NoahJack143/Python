#Imports
#-----#
import retailitem as ri
import CashRegister as cr
import ACME_Password_TEST as pt
import time
import pickle

#-----#

#Notes
#-----#

#OPEN AND CLOSE THE FILES EVERYTIME A FILE IS USED, PER FUNCTION

#-----#

#---------------------------Main Menu Functions---------------------------#

#A main function to call other functions within the main function
def main_menu():
    
    #Create a variable to check if the user wants to continue
    m = 'open'
    
    #Loop until the user chooses to leave the program
    while True:
        
        #Before anything, try to open the file, inventory.dat, and try to pickle things.
        try:
            infile = open('inventory.dat', 'rb')
            #If that works, move things from the file into the list
            inventory = pickle.load(infile)
            infile.close() #Close the file after unpickling items
        except:
            print('WARNING: Either the file inventory.dat is empty, or the file does not exist.')
            time.sleep(3) #This is here to give the user time to read
            
        #A beginning statement
        print('\n\n\nWelcome to the ACME Main Menu.\n')
        
        #A statement before the options + the options
        print('\tMenu Options\n'+
              '--------------------------------\n'+
              'Press 1 to access the inventory control system.\n'+
              'Press 2 to access the retail store.\n'+
              'Press 3 to access the password menu.\n'+
              'Press 4 to exit the main menu.\n'+
              '--------------------------------')
        
        #Loop for validation
        while True:
            
            #Ask the user for an option
            ui = input('Enter your choice: ')
            
            #Check for the user's input
            if ui == '1':
                
                #Before anything, send the user a code for them to crack before they get into the system
                print('\nBefore you can get into the Inventory Control System, you must configure this code to get the password.')
                time.sleep(2) #This is here to give the user time to read
                
                #Have a bot checker
                cont = pt.bot_passer()
                time.sleep(1.5) #This is here to give the user time to read
                
                #Check to see if the user can continue or not
                if cont:
                    #Check to see if the file exists. Create it if it doesn't
                    try:
                        infile = open('inventory.dat', 'rb')
                        infile.close()
                    except:
                        print("Inventory file doesn't exist. Creating the file now.")
                        infile = open('inventory.dat', 'w')
                        infile.close()
                    ICS()
                    break
                else:
                    #If the user got the password wrong, break out
                    break
            
            #If the user choose option 2, open the Retail Store
            elif ui == '2':
                RS()
                break
            
            #If the user chooses option 3, ask them for the admin password, and then move them to the password editting menu
            elif ui == '3':
                
                #Before anything, ask the user the admin password, and then check the password and move accordingly
                print('Before you can enter the Password Menu, you must enter the admin password.')
                ui = input('Enter the admin password: ')
                if ui == '1aJ7':
                    #If they get the password right, send them to the password menu
                    PM()
                    break
                
                #If they don't get the password right, tell them and send them back
                print('Sorry, but the password you entered is wrong.')
                break
            
            #If the user chooses option 4, exit the main menu
            elif ui == '4':
                m='exit'
                break
                
            #VALIDATION                
            else:
                print('\nPlease choose an option from the table.\n')
                time.sleep(2) #This is here to give the user time to read
        
        #Check to see if the user chose to exit
        if m == 'exit':
            #Print a closing message
            print('\nGoodbye.')
            time.sleep(1.5) #This is here to give the user time to read
            break
                
                
#---------------------------Inventory Control System Functions---------------------------#
                
#A function for the Inventory Control System
def ICS():
    
    #Before anything, load the information from the file into the list. VALIDATION WILL BE HERE
    try:
        infile = open('inventory.dat','rb')
        inventory = pickle.load(infile)
        infile.close()
    except:
        inventory = []
    
    #Create a loop here to loop until the players chooses option #4
    while True:
        
        #A beginning statement
        print('\n\n\nWelcome to the ACME Inventory Control System.\n')
        
        #A statement before the options + the options
        print('\tMenu Options\n'+
              '--------------------------------\n'
              'Press 1 to display the current inventory.\n'+
              'Press 2 to add inventory items to the current inventory.\n'+
              'Press 3 to save the inventory.\n'+
              'Press 4 to exit.\n'
              '--------------------------------')
        
        #Loop for validation
        while True:
            
            #Ask the user to select an option
            ui = input('Select an action(1, 2, or 3. Press 4 to EXIT): ')
            
            #Check for the user's choice
            if ui == '1':
                inventory = display_inventory()
                break
            elif ui == '2':
                inventory = add_items(inventory)
                break
            elif ui == '3':
                inventory = save_inventory(inventory)
                break
            elif ui == '4':
                inventory = exitting_ISC()
                break
            else:
                print('\nPlease choose an option from the table.\n')
                time.sleep(2) #This is here to give the user time to read
            
        #Check to see if the user chose option #4
        if inventory == 'exit':
            print() #make code purty
            break
    
    #Once the user chooses to exit return the to main menu
    #Before leaving have a message
    for i in 'Exiting':
        print(i,end=''); time.sleep(.02)
    for i in '...':
        print(i,end=''); time.sleep(.8)
    return
          
#Function to show the inventory
def display_inventory():
    
    #Open the file, move the contents into a list, and clos the file
    infile = open('inventory.dat', 'rb')
    inventory = pickle.load(infile)
    infile.close()
    
    #Try to load the contents from the file into a list, check it's length, and move accordingly
    try:
        if len(inventory) < 1:
            p=p
    except:
        #If there is nothing within the list, print this statement
        print('\nThere are no items in the inventory.')
        time.sleep(3) #This is here to give the user time to read
    else:
        #Print a message before display everything
        print('\nHere are items within the inventory:')
        
        #If there are items within the file, print every single key
        for key in inventory:
            print(key)
            #print(key.get_name()) <-- this is to check for a description asked by the user
            
        #Find out how long to let the reader read the inventory
        if len(inventory) > 3:
            wait = int(len(inventory) / 2)
        else:
            wait = len(inventory)
        
        time.sleep(wait) #This is here to give the user time to read
            
    #return because the purpose of the function has been served
    return inventory

#Function to add items to the inventory
def add_items(inventory):
    
    #Loop until the user no longer wants to
    while True:
        
        #Reset the User Input every loop and a boolean variable
        change_object = False
        ui = 1
        
        #Ask the user for information
        #Loop to check to see if the description alread exists
        while True:
            
            #Get information from the user. VALIDATION IS HERE
            description = input('\nEnter an item description: ')
            for item in inventory:
                if description == ri.RetailItem.get_description(item):
                    print('\nThat description already exists');ui = input('Would you like to replace that item information? (y/n) ');print() #make code purty
            if ui == 'y': change_object = True; break
            elif ui == 1: break
            else: continue
        #VALIDATION
        while True:
            try:
                units = int(input(f'Enter the number of units for {description}: '))
                price = float(input(f'Enter the price per unit for {description}: (0.00) '))
                if units <= 0 or price <= 0:
                    p=p
            except:
                print('\nEither the entry for units or the entry for retail price was not a number.')
                time.sleep(2)
            else:
                break
        
        #Create an object for that item
        item_info = ri.RetailItem(description, units, price)
        
        #Check for previous options and move accordingly
        if change_object:
            for i in range(len(inventory)):
                if ri.RetailItem.get_description(inventory[i]) == description:
                    inventory[i] = ri.RetailItem(description, units, price)
        else:
            #Append the item info into the list
            inventory.append(item_info)
        
        #Ask the user if they would like to continue
        cont = input('\nWould you like to add another item? (y/n) ')
        
        #Check the user's input and move accordingly
        if cont == 'y':
            continue
        else:
            #Tell the user to save the inventory before viewing
            print('\nWARNING: Be sure you save the inventory before adding more items or viewing the inventory IF you want keep the previously made changes.')
            time.sleep(3)
            break
    
    #Return because this function's purpose has been served
    return inventory

#Function for saving the changes made to the file
def save_inventory(inventory):
    
    print() #make code purty
    
    #Open the file, dump the info, and tell the user if this was successful
    try:
        infile = open('inventory.dat','wb') #open file
        pickle.dump(inventory, infile)
        infile.close() #close file
        
        #Before telling the user the results, print a message
        #Before leaving have a message
        for i in 'Saving inventory':
            print(i,end=''); time.sleep(.02)
        for i in '...':
            print(i,end=''); time.sleep(.8)
            
        #Tell the user the success
        print('\n\nThe changes have been successfully saved.')
    except:
        print('\nThere was a problem trying to save the data.')
    time.sleep(3) #This is here to give the user time to read
    
    #Return because the purpose has been served
    return inventory
    

def exitting_ISC():
    
    #Return the key word to leave the inventory
    return 'exit'

#---------------------------Retail Store Functions---------------------------#

def RS():
    
    #Before anything, create a list that will contain the objects that the user wants to buy
    cart = []
    cart_info = {} #A dictionary to hold specific information within the cart
    
    #Set a boolean variable for the menu
    leave = False
    
    #Continue until the user no longer wants to
    while True:
        
        #Print an opening message for the user when they enter the "store"
        print('\n\n\nWelcome to the ACME PoS retail system\n')
        
        #Print another message and then list options for the user
        print('Please choose from the following items:\n'+
              '1 - View Cart\n2 - Display items for sale\n'+
              '3 - Purchase item\n4 - Empty cart and start over\n'+
              '5 - Check out\n6 - EXIT to main menu\n')
        
        #Loop until the user chooses to quit
        while True:
            
            #Ask the user for an option
            ui = input('Please enter a selection: ')
            
            #Check the user's input
            if ui == '1':
                cart, cart_info = view_cart(cart, cart_info)
                break
            elif ui == '2':
                display_items()
                break
            elif ui == '3':
                cart, cart_info = purchase_item(cart, cart_info)
                break
            elif ui == '4':
                cart, cart_info = empty_cart(cart, cart_info)
                break
            elif ui == '5':
                cart, cart_info = check_out(cart, cart_info)
                break
            elif ui == '6':
                leave = True
                print() #make code purty
                break
            else:
                print('\nPlease choose an option from the table.\n')
                time.sleep(2) #This is here to give the user time to read
            
        #Check to see if the user wants to leave
        if leave:
            #Before leaving have a message
            for i in 'Exiting':
                print(i,end=''); time.sleep(.02)
            for i in '...':
                print(i,end=''); time.sleep(.8)
            break
        
def view_cart(cart, cart_info):
    
    #Check to see if the cart is empty and move accordingly
    if len(cart) < 1:
        print('\nYour cart is empty!')
        time.sleep(2) #This is here to give the user time to read
    else:
            
        #Print a message, and then display the cart
        print('Here are the items within your cart')
        for item in cart:
            print(ri.RetailItem.get_cart(item, cart_info))
            
        #Find out how long to let the reader read the inventory
        if len(cart) > 3:
            wait = int(len(cart) / 2)
        else:
            wait = len(cart)
        
        time.sleep(wait) #This is here to give the user time to read
    
    #Return because this function's purpose has been served
    return cart, cart_info

def display_items():
    
    #Simply call for the function, display_inventory()
    display_inventory()
    
    #Return because this function's purpose has bee served
    return

def purchase_item(cart, cart_info):
    
    #Call for display_items() to show the inventory
    display_items()

    #Open the file, move the contents, and close the file
    infile = open('inventory.dat', 'rb') #Open file
    inventory = pickle.load(infile) #Create inventory
    infile.close() #Close file
    
    #Loop until the user no longer wants to purchase items
    while True:
        
        #Loop until the user selects a real item
        while True:
            
            #Reset the boolean variable
            existence = False
            
            #Ask the user for an item to purchase
            wanted_item = input('\nWhich item would you like to purchase? ')
            
            #Check to see if the wanted item is even in the inventory
            for item in inventory:
                if wanted_item == ri.RetailItem.get_description(item):
                
                    #If so, get the description, price, and units of that item
                    WI_description = item
                    WI_price = float(ri.RetailItem.get_price(item))
                    WI_units = int(ri.RetailItem.get_units(item))
                    existence = True
                    break

            if not existence:
                
                #Tell the user their item doesn't exist in the inventory
                print('\nThe wanted item is not in stock.\nChoose another.')
                time.sleep(2) #This is here to give the user time to read
                print() #make code purty
            else:
                
                #If the item does exist, check to see if it's already in the cart
                if wanted_item in cart_info and cart_info[wanted_item][1] != WI_units:
                    
                    #If the item is already in the cart, then add to the info
                    cart_info[wanted_item][1] = cart_info[wanted_item][1] + 1
                    cart_info[wanted_item][2] = cart_info[wanted_item][2] + WI_price
                    
                elif wanted_item in cart_info and cart_info[wanted_item][1] == WI_units:
                    
                    #If the item's units in the cart_info == to the item's units in the object
                    if wanted_item[-1] == 's':print(f'\nYou are currently carrying all of the {wanted_item} in stock\n')
                    else:print(f'\nYou are currently carrying all of the {wanted_item}s in stock\n')
                    time.sleep(2) #This is here to give the user time to read
                    
                else:
                    #If the item isn't in the cart, create a key for it
                    cart_info[wanted_item] = [] #Create a list for the key
                    cart_info[wanted_item] += [wanted_item, 1, WI_price] #Add things into that list within the dictionary
                    #Add the item to the normal cart as well
                    cart.append(WI_description)
            break
        
        #Ask the user if they want to purhcse another item
        cont = input('Would you like to purchse another item? (y/n) ')
        
        if cont == 'y':
            continue
        else:
            break
    
    #Return the cart and it's info
    return cart, cart_info
    
def empty_cart(cart, cart_info):
    
    #Have a try block to check for items in the cart
    try:
        
        #Check to see if there's anything in the cart in the first place
        if len(cart) < 1: p=p
    
    except:
        #If there isn't anything in the cart, tell the user
        print('Your cart is already empty!'); time.sleep(2); return cart, cart_info
    else:
        #If there is, empty the cart and tell the user
        cart = []; cart_info = {}
        
        #Before telling the user about the cart, print a message
        for i in 'Emptying Cart':
            print(i,end=''); time.sleep(.02)
        for i in '...':
            print(i,end=''); time.sleep(.8)
            
        #Print the results
        print('Cart successfully emptied.'); return cart, cart_info
    
def check_out(cart, cart_info):
    
    #Open the file, inventory.dat, load the contents, and then close the file
    infile = open('inventory.dat', 'rb') #Open the file
    inventory = pickle.load(infile) #Load the contents
    infile.close()
    
    #Create a try block for checking purposes
    try:
        
        #Create an accumulator for the total price
        total_price = 0
        
        #Add up everything inside the user's cart
        for item in cart_info:
            #Add the price to the accumulator
            total_price += cart_info[item][2]
            
        #Check to see if nothing was added, and then move accordingly
        if total_price == 0:p=p
            
    except:
        #If the cart is empty, tell the user
        print('Your cart is empty!')
        time.sleep(2) #This is here to give the user time to read
    
    else:
        print() #make code purty
        
        #If the cart isn't empty, show the cart's contents to the user
        cart, cart_info = view_cart(cart, cart_info)
            
    #Show the final price that the user must pay for the items
    print('\nThe price of all your items is ', format(total_price, '.2f'), sep = '$')
    #Ask the user if they would like to buy all the items, if any, in their cart
    confirmation = input('Would you like to purchase the items in your cart? (y/n) ')
    
    #Check for the user's response and move accordingly
    if confirmation == 'y':
        
        #For all the items within the cart, remove the amount of units in stock by the amount bought
        for item in cart:
            units_left = int(ri.RetailItem.get_units(item)) - cart_info[ri.RetailItem.get_description(item)][1]
            
            #Check to see if there are any items left in stock
            if units_left == 0:
                
                #Remove the item from the inventory if there is none left
                for i in range(len(inventory)):
                    if ri.RetailItem.get_description(inventory[i]) == ri.RetailItem.get_description(item):
                        del inventory[i]
                        break
            
            else:
                #If there are items left, find where the item is at in the inventory, then replace it when a new object
                for i in range(len(inventory)):
                    if ri.RetailItem.get_description(inventory[i]) == ri.RetailItem.get_description(item):
                        inventory[i] = ri.RetailItem(ri.RetailItem.get_description(inventory[i]),units_left,ri.RetailItem.get_price(inventory[i]))
                        
        #Next, empty the cart and cart_info
        cart = []; cart_info = {}
        
        print() #make code purty
        
        #Before purchasing the items, print a message
        for i in 'Scanning items':
            print(i,end=''); time.sleep(.02)
        for i in '...':
            print(i,end=''); time.sleep(.8)
            
        #Finally, tell the user that they have finally bought the items and return the cart
        print('\n\nThe items within the cart were bought successfully.\nHappy shopping!')
        time.sleep(3) #This is here to give the user time to read
        infile = open('inventory.dat', 'wb')
        pickle.dump(inventory, infile)
        infile.close()
        return cart, cart_info
            
    else:
        #If the user decides to keep shopping, then just return the cart
        print('The items within the cart were not purchsed.\nHappy shopping!')
        time.sleep(3) #This is here to give the user time to read
        
        #Without the user knowing, save the new inventory information into the file, inventory.dat
        infile = open('inventory.dat', 'wb')
        pickle.dump(inventory, infile)
        infile.close()
        return cart, cart_info
                
#If the user chooses option 3, take them to the Password Menu
def PS():
    
    #To make sure that the username file exists in the first place
    infile = open('users.dat', 'wb')
    infile.close()
    
    #Open the file that has all of the users, load the list, and then close the file
    infile = open('users.dat', 'rb')
    user_list = pickle.load(infile)
    infile.close()
    
    #Set a boolean variable for the menu
    leave = False
    
    #Continue until the user no longer wants to
    while True:
        
        #A beginning statement
        print('\n\n\nWelcome to the ACME Password Menu.\n')
        
        #A statement before the options + the options
        print('\tMenu Options\n'+
              '--------------------------------\n'+
              'Press 1 to show all of the users.\n'+
              'Press 2 to add a user.\n'+
              'Press 3 to delete a user.\n'+
              'Press 4 to exit the main menu.\n'+
              '--------------------------------')
        
        #Loop until the user chooses to quit
        while True:
            
            #Ask the user for an option
            ui = input('Please enter a selection: ')
            
            #Check the user's input
            if ui == '1':
                #cart, cart_info = view_cart(cart, cart_info)
                break
            elif ui == '2':
                #display_items()
                break
            elif ui == '3':
                #cart, cart_info = purchase_item(cart, cart_info)
                break
            elif ui == '4':
                leave = True
                print() #make code purty
                break
            else:
                print('\nPlease choose an option from the table.\n')
                time.sleep(2) #This is here to give the user time to read
            
        #Check to see if the user wants to leave
        if leave:
            #Before leaving have a message
            for i in 'Exiting':
                print(i,end=''); time.sleep(.02)
            for i in '...':
                print(i,end=''); time.sleep(.8)
            break
        
def show_users(user_list):
    
    #Add a try block to checking purposes
    try:
        
        #Check to see if the list has anything insdide of it
        if len(user_list) < 1:
            p=p
        
        #If there are things inside of it, print everything
        for user in user_list:
            print(user)
            
        time.sleep(2) #This is here to give the user time to read
        
        #Return once done
        return user_list
    
    except:
        #If there is nothign within the list tell the user
        print('There are no contacts within the list')
        return user_list
    
    
    
    
#Call the main function
main_menu()