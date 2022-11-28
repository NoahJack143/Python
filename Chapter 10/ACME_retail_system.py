#Imports
#-----#
import retailitem as ri

#-----#

#A main function
def main():

    #A main function to call other functions within the main function
    def main_menu():
        
        #Before anything, try to open the file, inventory.dat, and try to pickle things.
        try:
            infile = open('inventory.dat', 'rb')
            #If that works, move things from the file into the dictionary
            inventory = pickle.load(infile)
            infile.close() #Close the file after unpickling items
        except:
            print('WARNING: Either the file inventory.dat is empty, or the file does not exist.')
            
        #A beginning statement
        print('Welcome to the ACME Main Menu.\n')
        
        #A statement before the options + the options
        print('Please select an action from the following:\n'+
              'Press 1 to access the inventory control system.\n'+
              'Press 2 to access the retail store.')
        
        #Loop for validation
        while True:
            
            #Ask the user for an option
            ui = input('Enter your choice: ')
            
            #Check for the user's input
            if ui == '1':
                
                #Try to open the file
                try:
                    infile = open('inventory.dat', 'rb')
                except:
                    print("Inventory file doesn't exist. Creating the file now.")
                    infile = open('inventory.dat', 'w')
                    infile.close()
                    infile = open('inventory.dat', 'rb')
                ISC()
                break
            elif ui == '2':
                RS()
                break
            else:
                print('\nPlease choose an option from the table.\n')
    
    #A function for the Inventory Control System
    def ICS():
        
        #A beginning statement
        print('Welcome to the ACME Inventory Control System.\n')
        
        #A statement before the options + the options
        print('Please select an action from the following:\n'+
              'Press 1 to display the current inventory.\n'+
              'Press 2 to add inventory items to the current inventory.\n'+
              'Press 3 to save the inventory.\n'+
              'Press 4 to exit.')
        
        #Loop for validation
        while True:
            
            #Ask the user to select an option
            ui = input('Select an action(1, 2, or 3. Press 4 to EXIT): ')
            
            #Check for the user's choice
            if ui == '1':
                display_inventory()
                break
            elif ui == '2':
                add_items()
                break
            elif ui == '3':
                save_inventory()
                break
            elif ui == '4':
                return
            else:
                print('\nPlease choose an option from the table.\n')
              
    #Function to show the inventory
    def display_inventory():
        
        #Try to load the contents from the file into a dictionary, check it's length, and move accordingly
        try:
            inventory = pickle.load(infile)
            print(inventory) #This is here for checking. Delete this later.
            if inventory == {}: #If there is nothing in the file, crash on purpose to load the statements
                p=p
        except:
            #If there is nothing within the list, print this statement
            print('There is nothing within the file.')
        else:
            #If there are items within the file, print every single key
            for key in inventory:
                print(f'Description: {inventory[key][0]\n'+
                      f'Units: {inventory[key][1]\n'+
                      f'Retail Price: {inventory[key][2]\n')
                
        return #return because the purpose of the function has been served
    
    #Function to add items to the inventory
    def add_items():
        
        #Try to load the contents from the file into a dictionary, then check it's length, and move accordingly
        try:
            inventory = pickle.load(infile)
            print(inventory) #This is here for checking. Delete this later.
            if inventory = {}:
                p=p
        except:
            #If there is nothing within the file, create an empty dictonary
            inventory = {}
        
        #Loop until the user no longer wants to
        while True:

            #Ask the user for information
            #Loop to check to see if the description alread exists
            while True:
                description = input('Enter an item description: ')
                if description in inventory:print('That description already exists');ui = input('Would you like to replace that item information? (y/n) ')
                if ui == 'y': break
                else: continue
            units = input(f'Enter the number of units for {description}: ')
            price = input(f'Enter the price per unit for {description}: ')
            
            #Create an object for that item
            item_info = ri.RetailItem(description, units, price)
            
            #Move the item info into the dictionary
            inventory[description] = item_info
            
            #Ask the user if they would like to continue
            cont = input('Would you like to continue? (y/n) ')
            
            #Check the user's input and move accordingly
            if cont == 'y':
                continue
            else:
                break
            
        #Once the user no longer wants to continue
        
        
            
        