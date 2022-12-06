#Imports
#-----#
import retailitem as ri
import CashRegister as cr
import ACME_Password_TEST as pt
import time
import pickle
import random as r

#import smtplib, ssl #MIGHT BE USED LATER
#-----#

#Notes
#-----#

#OPEN AND CLOSE THE FILES EVERYTIME A FILE IS USED, PER FUNCTION

#-----#

#---------------------------Main Menu Functions---------------------------#

#A main function to call other functions within the main function
def main_menu():
    #main menu accepts no arguments
    #This is the main function that will call all of the other
    #"main" functions (They're really just menus for other functions)
    
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
            #Check to the file, users.dat, as well
            try:
                infile = open('users.dat', 'rb')
                user_list = pickle.load(infile)
                infile.close()
            except:
                print('\n\n\nWARNING: Either the file, inventory.dat, is empty, or the file does not exist.'+
                      '\nWARNING: Either the file, users.dat, is empty, or the file does not exist.')
                time.sleep(5) #This is here to give the user time to read
            else:
                print('\n\n\nWARNING: Either the file, inventory.dat, is empty, or the file does not exist.')
                time.sleep(5) #This is here to give the user time to read
            
        #A beginning statement
        print('\n\n\nWelcome to the ACME Main Menu.\n')
        
        #A statement before the options + the options
        print('\tMenu Options\n'+
              '--------------------------------\n'+
              'Press 1 to access the inventory control system.\n'+
              'Press 2 to access the retail store.\n'+
              'Press 3 to access the user control menu.\n'+
              'Press 4 to exit the main menu.\n'+
              '--------------------------------')
        
        #Loop for validation
        while True:
            
            #Ask the user for an option
            ui = input('Enter your choice: ')
            
            #Check for the user's input
            if ui == '1':
                
                #Before anything, open the file, users.dat, and get the dictionary from there
                try:
                    infile = open('users.dat', 'rb')
                    user_list = pickle.load(infile)
                    infile.close()
                except:
                    print('\nThe file, users.dat, does not exist. Please choose option 3 from the menu before accessing the Inventory Control System.')
                    time.sleep(3) #This is here to give the user time to read
                    break
                else:
                
                    #Set boolean variables
                    passs = False
                    found = False
                    break_out = False
                    
                    #Ask the user for a username and password.
                    print('\nLogin Credentials\n-------------')
                    username = input('Username: ')
                    password = input('Password: ')
                    
                    #Check the username first to see if there is a username in the users_list that matches it
                    for user in user_list:
                        if username == user_list[user][1]:
                            #Check for the password if the username matches
                            if password == user_list[user][2]:
                                #If everything works, print a message
                                print('\nYou have the right username and password.')
                                time.sleep(2) #This is here to give the user time to read
                                passs = True
                                #Get the email if the username and password are right
                                email = user_list[user][3]
                            else:
                                #if the password is incorrect
                                print('\nThe password you entered is incorrect.')
                                time.sleep(2) #This is here to give the user time to read
                                break_out = True
                            found = True
                    if break_out: break
                    #Check to see if the user got anything right. Move accordingly
                    if not found:
                        print('\nThe username you entered does not exist.')
                        time.sleep(2) #This is here to give the user time to read
                        break
                    elif passs:

                        #If they get the username and password right, have a bot checker to see if the user is a bot.
                        print('\nBefore entering the Inventory Control System, please answer the question to see if you are a human.\n')
                        time.sleep(2) #This is here to give the user time to read
                        
                        #Have a bot checker
                        cont = pt.bot_checker2()
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
                print('\nBefore you can enter the Password Menu, you must enter the admin password.')
                ui = input('Enter the admin password: ')
                if ui == pt.admin_information('password'):
                    #If they get the password right, send them to the password menu
                    print('\nCorrect!')
                    time.sleep(1) #This is here to give the user time to read
                    UCM()
                    break
                
                #If they don't get the password right, tell them and send them back
                print('\nSorry, but the password you entered is wrong.')
                time.sleep(2) #This is here to give the user time to read
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
    #ISC accepts no arguments
    #This is the main function/menu for all of the inventory
    #editting options
    
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
                inventory = display_inventory(inventory)
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
def display_inventory(inventory):
    #display inventory accepts one arugment, a list
    #if there are items in the inventory, it will
    #display them
    
    try:
        #If the file loads correcly, check the length of the list
        if len(inventory) < 1:
            p=p
    except:
        #If there is nothing within the list, print this statement
        print('\nThere are no items in the inventory.')
        time.sleep(3) #This is here to give the user time to read
        #Create the inventory if it doesn't exist
        inventory = []
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
    #add_items accepts one argument, a list
    #it will ask the user to add items into the inventory
    
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
                units = int(input(f'Enter the number of units for {description}: (0) '))
                price = float(input(f'Enter the price per unit for {description}: (0.00) '))
                if units <= 0 or price <= 0:
                    p=p
            except:
                print('\nEither the entry for units or the entry for retail price was not a number or was not formatted correctly.')
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
            print('\nWARNING: Be sure you save the inventory before adding more items to the inventory IF you want keep the previously made changes.')
            time.sleep(5)
            break
    
    #Return because this function's purpose has been served
    return inventory

#Function for saving the changes made to the file
def save_inventory(inventory):
    #save_invenotry accepts one argument, a list
    #it will save the changes made in the inventory
    
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
    #exitting ISC accepts no arguments
    #it returns the key word to exit the ISC menu
    
    #Return the key word to leave the inventory
    return 'exit'

#---------------------------Retail Store Functions---------------------------#

def RS():
    #RS accepts no arguments
    #it is the main function/menu for the retail store,
    #and it will call other functions based on the user's
    #choice
    
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
    #view_cart accepts two arguments, a list and a dictionary
    #it will show all of the items within the user's cart, if
    #there are any
    
    #Check to see if the cart is empty and move accordingly
    if len(cart) < 1:
        print('\nYour cart is empty!')
        time.sleep(2) #This is here to give the user time to read
    else:
            
        #Print a message, and then display the cart
        print('\nHere are the items within your cart')
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
    #display_items accepts no arguments
    #it will simply call the function, display_inventory(inventory)
    
    #Open the file, inventory.dat and get it's contents
    try:
        infile = open('inventory.dat','rb')
        inventory = pickle.load(infile)
        infile.close()
    except:
        print('\nThe inventory is empty.')
        time.sleep(3) #This is here to give the user time to erad
    else:
        #Simply call for the function, display_inventory(inventory)
        display_inventory(inventory)
    
    #Return because this function's purpose has been served
    return

def purchase_item(cart, cart_info):
    #purchase_item accepts two arguments, a list and a dictionary
    #if there are items in the inventory, it will ask the user
    #for items they would like to purchase, and adds them to the
    #cart and add the information of those items into the cart_info
    
    #Call for display_items() to show the inventory
    display_items()
    
    #VALIDATION
    try:
        #Open the file, move the contents, and close the file
        infile = open('inventory.dat', 'rb') #Open file
        inventory = pickle.load(infile) #Create inventory
        infile.close() #Close file
    except:
        #Return the cart and it's info
        return cart, cart_info
    else:
    
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
                #Return the cart and it's info
                return cart, cart_info
    
def empty_cart(cart, cart_info):
    #emtpy_cart accepts two argumenets, a list and dictionary
    #if there are items in the user's cart, it will
    #make cart = [] and cart_info = {}
    
    #Have a try block to check for items in the cart
    try:
        
        #Check to see if there's anything in the cart in the first place
        if len(cart) < 1: p=p
        else: print() #make code purty
    
    except:
        #If there isn't anything in the cart, tell the user
        print('\nYour cart is already empty!'); time.sleep(2); return cart, cart_info
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
    #check out accepts two arguments, a list and a dictoinary
    #if there are items in the inventory and items in the cart, it will ask
    #the user if they would like to check out. If so, it will make cart = []
    #and cart_info = {}, and it will affect the inventory
    
    try:
        #Open the file, inventory.dat, load the contents, and then close the file
        infile = open('inventory.dat', 'rb') #Open the file
        inventory = pickle.load(infile) #Load the contents
        infile.close()
    except:
        print("\nThere are no items in the inventory, so you can't check out anything.")
        time.sleep(2.5) #This is here to give the user time to read
        return cart, cart_info
    else:
    
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
                
#---------------------------User Control Menu Functions---------------------------#
        
def UCM():
    #UCM accepts no arguments
    #UCM is the main function/menu that will call other functions
    #based on the user's choice
    
    #Set a boolean variable in the very beginning
    there = False
    
    #Check to see if the acount exists, and if it does, check for the admin account
    try:
        infile = open('users.dat', 'rb')
        user_list = pickle.load(infile)
        infile.close()
        for user in user_list:
            if user == 'Noah (ADMIN)':
                there = True
                break
        if not there:
                   
            #Create the user_list <--- really a dictionary
            user_list = {}; print() #make code purty
            
            #Create the admin account and move it into the file
            new_user = pt.Users('Noah (ADMIN)', '1aJ7*', 'noahjack143@gmail.com')
            user_list['Noah (ADMIN)'] = [new_user, 'Noah (ADMIN)', '1aJ7*', 'noahjack143@gmail.com']
            infile = open('users.dat', 'wb')
            pickle.dump(user_list, infile)
            infile.close()
            for i in 'The admin user, Noah (ADMIN), was not found. Creating it now':
                print(i,end=''); time.sleep(.02)
            for i in '...':
                print(i,end=''); time.sleep(.8)
    
    except:
        #If the file doesn't exist in the first place
        
        #Create the user_list <--- really a dictionary
        user_list = {}; print() #make code purty
        
        #Create the admin account and move it into the file
        new_user = pt.Users('Noah (ADMIN)', '1aJ7*', 'noahjack143@gmail.com')
        user_list['Noah (ADMIN)'] = [new_user, 'Noah (ADMIN)', '1aJ7*', 'noahjack143@gmail.com']
        infile = open('users.dat', 'wb')
        pickle.dump(user_list, infile)
        infile.close()
        for i in 'The file, users.dat, was not found. Creating it now':
            print(i,end=''); time.sleep(.02)
        for i in '...':
            print(i,end=''); time.sleep(.8)
        print() #make code purty
        for i in 'The admin user, Noah (ADMIN), was not found. Creating it now':
            print(i,end=''); time.sleep(.02)
        for i in '...':
            print(i,end=''); time.sleep(.8)
    
    #Set a boolean variable for the menu
    leave = False

    #Continue until the user no longer wants to
    while True:
        
        #A beginning statement
        print('\n\n\nWelcome to the ACME User Control Menu.\n')
        
        #A statement before the options + the options
        print('\tMenu Options\n'+
              '--------------------------------\n'+
              'Press 1 to show all of the users.\n'+
              'Press 2 to add a user.\n'+
              'Press 3 to save the user list.\n'+
              'Press 4 to delete a user.\n'+
              'Press 5 to exit the main menu.\n'+
              '--------------------------------')
        
        #Loop until the user chooses to quit
        while True:
            
            #Ask the user for an option
            ui = input('Please enter a selection: ')
            
            #Check the user's input
            if ui == '1':
                show_users(user_list)
                break
            elif ui == '2':
                user_list = add_users(user_list)
                break
            elif ui == '3':
                user_list = save_users(user_list)
                break
            elif ui == '4':
                user_list = delete_users(user_list)
                break
            elif ui == '5':
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
    #show users accepts one argument, a dictionary
    #it display the names within the dictionary to the user, if any
    
    #Add a try block to checking purposes
    try:
        
        #Check to see if the list has anything insdide of it
        if len(user_list) < 1:
            p=p
        
        #If there are things inside of it, print everything
        for user in user_list:
            print(user_list[user][0])
            
        #Find out how long to let the reader read the user list
        if len(user_list) > 3:
            wait = int(len(user_list) / 2)
        else:
            wait = len(user_list)
        
        time.sleep(wait) #This is here to give the user time to read
        
        #Return once done
        return user_list
    
    except:
        #If there is nothign within the list tell the user
        print('\nThere are no users within the list of users')
        time.sleep(2) #This is here to give the user time to read
        return user_list
    
def add_users(user_list):
    #add users accepts one argument, a dictionary
    #for every time the user wants to, it will ask the user
    #for a name, a password, and a email for the user. It
    #will then add the information to the dictionary
    
    #Loop until the user no longer wants to add users
    while True:
        
        #Create/reset the boolean variable
        duplicate = False
        
        #Ask the user for a username, password, and email
        #Loop until the user gets a non duplucated username
        while True:
            
            #Loop until the user chooses a username different from the admin username
            while True:
                #Input from the user
                username = input('\nUsername: ')
                
                #Check to see if the user is trying to delete the admin account
                if username == 'Noah (ADMIN)':
                    print('You can not have the same username as the admin account.')
                    time.sleep(2) #This is here to give time for the user to read
                    continue
                
                else:
                    break
                
            #Check to see if that username is already in the list
            for user in user_list:
                if username == user_list[user][0]:
                    duplicate = True
                
            #Check to see if the username already exists
            if not duplicate:
                break
            else:
                #Ask the user if they would like to replace that username
                print(f'\nThe username, {username}, alread exists.')
                replace = input(f'Would you like to replace the username, {username}? (y/n) ')
                
                #Check the response
                if replace != 'y':
                    continue
                else:
                    #Ask for the admin password
                    cont = input('\nEnter the admin password to continue: ')
                    #Reset the boolean variable
                    replace = False
                    
                    #Check to see if the password is right and move accordingly
                    if cont == pt.admin_information('password'):
                        print() #make code purty
                        break
                    
                    else:
                        #If not, tell the user to that the password is wrong
                        print('The password was wrong. Please choose a different username.')
                        time.sleep(2) #This is here to give the user time to read
                        continue
                    
        
        #Loop until the password is strong
        while True:
            #Input from the user
            password = input('Password: ')
            #Create a bunch of boolean variables
            uppercase = False; lowercase = False; number = False; symbol = False; space = False
            #Loop through all the letters in the password and check them
            for char in password:
                if char.isupper(): uppercase = True
                elif char.islower(): lowercase = True
                elif char.isdigit(): number = True
                elif not char.isalnum(): symbol = True
                elif char == ' ': space = True
            
            #Check to see for the requirements. Make sure that there isn't a space. Move accordingly
            if space:
                print('There can not be a space in your password.')
                continue
            elif uppercase and lowercase and number and symbol:
                break
            else:
                print('\nYour password is too weak. Be sure to include an uppercase and a lowercase letter, a number, and a symbol.\n')
                time.sleep(2) #This is here to give the user time to read
                continue
        
        #Loop until the email is an actual email
        while True:
            
            #Input from the user
            email = input('Email: ')
            #Create a bunch of boolean variables
            space = False; atsign = False; period = False; letter_or_number = False
            #Loop for every character in the email and check them
            for char in email:
                if char.isalnum(): letter_or_number = True
                elif char == '@': atsign = True
                elif char == '.': period = True
                elif char == ' ': space = True
            
            #Check the the requirements. Make sure there aren't any spaces. Move accordingly
            if space:
                print('There can not be a space in your email.')
                continue
            elif atsign and period and letter_or_number:
                break
            else:
                print('\nYour email could not be created. Be sure to have everything that an normal email has.\n')
                time.sleep(2) #This is here to give the user time to read
                continue
        
        #Ask the user if they would like to add this User to the user_list
        print(f'\nUsername: {username}\nPassword: {password}\nEmail: {email}')
        cont = input('\nAre you sure you would like to add this user to the user list? (y/n) ')
        
        if cont == 'y':
            #Create an object for the given information
            new_user = pt.Users(username, password, email)
            #Add the new user to the dictionary of users
            user_list[username] = [new_user, username, password, email]
            #Print a message
            print('\nThe user has been created successfully.')
                
        else:
            #Print a message
            print('\nThe user will not be created.')
            
        #Ask the user if they would like to create another user
        cont = input('\nWould you like to create another user? (y/n) ')
        
        #Check the response and move accordingly
        if cont == 'y':
            continue
        else:
            return user_list
        
def save_users(user_list):
    #save users accepts on argument, a dictionary
    #if the file, users.dat, exists, it will save
    #the dictionary to that file
    
    #Have a try block
    try:
        
        #Open the file, put the user_list into the file, then close the file
        infile = open('users.dat','wb')
        pickle.dump(user_list, infile)
        infile.close() ; print() #make code purty
        
        #Print a fancy message
        for i in 'Saving new users':
            print(i,end=''); time.sleep(.02)
        for i in '...':
            print(i,end=''); time.sleep(.8)
            
        #Tell the user if this was successful
        print('\n\nThe new users were saved successfully.')
        time.sleep(2) #This is here to give the user time to read
        
        #Return when done
        return user_list
    
    except:
        #If some error occured, tell the user
        print('An error occured when trying to save the new users.')
        time.sleep(2) #This is here to give the user time to read
        return user_list
        
def delete_users(user_list):
    #delete_users accepts one argument, a dictionary
    #it will display the users within the user list, and it will
    #ask the user for users to delete.
    
    #Print a message before displaying the users
    print('Here is a list of the users:\n')
    
    #Display the list of users
    for user in user_list:
        print(user_list[user][0])
        
    #Find out how long to let the reader read the user list
    if len(user_list) > 3:
        wait = int(len(user_list) / 2)
    else:
        wait = len(user_list)
    
    time.sleep(wait) #This is here to give the user time to read
       
    #Loop until the user no longer wants to
    while True:
        
        #Create a boolean variable to start with
        existence = False
        
        #Ask the user for a user to delete
        wanted_user = input('\nWhat is the username of the user you would like to delete? ')
        
        #Check to see if the user is even in the user_list
        for user in user_list:
            if wanted_user == user_list[user][1]:
                existence = True
                break
        
        #If the user is in the user_list, continue with the function
        if not existence:
            #Tell the user
            print('\nPlease enter the username of user that exists.')
            time.sleep(2) #This is here to give the user time to read
            continue
        else:
            
            #Then ask the user if they would like to really delete it
            cont = input(f'\nWould you like to delete the user, {wanted_user}? (y/n) ')
            
            #Check the responsed and move accordingly
            if cont == 'y' and wanted_user != 'Noah (ADMIN)':
                for user in user_list:
                    if wanted_user == user_list[user][1]:
                        del user_list[user]
                        print('\nUser successfully deleted.')
                        time.sleep(2) #This is here to give the user time to read
                        break
            else:
                #If they change their mind, move along
                if wanted_user != 'Noah (ADMIN)':print(f'The user, {wanted_user}, will not be deleted.')
                else:print('\nYou can not delete the admin account, Noah (ADMIN)')
                time.sleep(3) #This is here to give the user time to read

        #Ask the user if they would like to delete another user
        cont = input('\nWould you like to delete another user? (y/n) ')
        
        #Check the response and move accordingly
        if cont == 'y':
            continue
        else:
            print('\nWARNING: Be sure to save the users list before leaving the Password Menu.')
            time.sleep(5) #This is here to give the user time to read
            break
    
    #Return the user list
    return user_list
    
#Call the main function
main_menu()