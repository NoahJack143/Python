#Program 10-19
#Imports
import contact as c
import pickle

#The main function to call
def main():
    #main accepts no arguments
    #it calls load_contancts to get the dictionary (CHECK TO SEE IF DICTIONARY IS MADE OR IS EMPTY AND
    #MOVE ACCORDINGLY). Call appropriate functions based on the return value for the menu from, get_menu_choice().
    #Finally save the contacts when the user quits
    
    #Create an accumulator for validations
    q=0
    
    #Call on load_contacts to get the dictionary
    mycontacts = load_contacts()
        
    #Loop until the user no longer wants to
    while True:
        
        #Call for get_menu_choice() to get the choice from the user
        function = get_menu_choice()
        
        #Call for the function that the user chose
        mycontacts = function(mycontacts)
        
        #Check to see something that resembles stopping was returned
        if mycontacts == 'done':break
        
def load_contacts():
    #load contacts accepts no arguments
    #it opens the <file name> = contacts.dat, as READ BINARY ('rb'). Unpickles the file into the dictionary
    #contact_dct and handles any IO exceptions. Returns the dictionary
    
    #Read the file and get the dictionary
    try:
        infile = open('contacts.dat', 'rb')
    except:
        print('The file does not exist.')
        return
    
    #Get the dictionary from the file using pickle
    try:
        mycontacts = pickle.load(infile)
    except EOFError:
        print('The contact dictionary is currently empty, so please add a contact.')
        mycontacts = {}
        add(mycontacts) #Add something to the dictionary
    
    #Close the file
    infile.close()
    
    #Return the dictionary to the main function
    return mycontacts
    
def get_menu_choice():
    #get menu choice accepts no arguments
    #it will present the user with a menu and returns a choice
    
    print('\nCONTACT MENU\n---------------\n'+
          '1) Look Up Contact\n2) '+
          'Add A Contact\n' +
          '3) Change A Contact\n4) '+
          'Delete A Contact\n5) '+
          'Save Contacts And Exit\n'+
          '---------------')
    
    #Prompt the user for an main function to call with validation
    while True:
        try:
            ui = float(input('What would you like to do? '))
        except:
            print('\nEnter a number...\n')
        else:
            try:
    
                #Check to see if the user input is any of the option
                if ui == 1:
                    function = look_up
                elif ui == 2:
                    function = add
                elif ui == 3:
                    function = change
                elif ui == 4:
                    function = delete
                elif ui == 5:
                    function = save_contacts
                else:
                    f
            except:
                print('\nPlease choose an option from the table.\n')
            else:
                print('\n'*1)
                return function
    
def look_up(mycontacts): #----------Perfected----------#
    #look_up accepts one argument, a dictionary
    #it will prompt the user for a name, prints the name the object for name in dictionary, or
    #'That name is not found' if it isn't in the dictionary.
    
    #Set ui before you prompt the user (if you do)
    ui = 'n'
    
    #Ask the user for a contanct (name) to search up
    name = input('What is the name of the contact that you would like to search up? ')

    #See if the desired contact is an actual contact, and move accordingly
    try:
        print(mycontacts[name])
    except:
        print('\nThe requested contact does not exist.')
        ui=input('Would you like to add that contact? (y/n) ') #See if the user wants to add the contact that doesn't exist
        if ui == 'y': add(mycontacts); return mycontacts #If the user wants to add a contact, let em.
        
    return mycontacts
    
def add(mycontacts): #----------Perfected----------#
    #add accepts one argument, a dictionary
    #it will prompt the user for a name, phone, and email and create an object with those attributes
    #If the name doesn't exist, add it to the dictionary with the name as the key and the object as the value
    #If the name already exists, say that it already exists and ask the user if they want to change it(call change)
    
    #Set an accumulator
    q=0
    
    #Loop until the user says otherwise
    while True:
        
        #Set ui to be soemthing before asking the user
        ui = 'n'
        
        #Text before asking the user
        print('\nAdd A Contact\n-------------')
        
        #Ask the user for a name, phone, and email. If the name is in the dictionary, print accordingly
        while True:
            if q == 3:q=0;print('\nToo many failed attempts occured.\n');return mycontacts#Return to the menu if too many failed attempts occured
            name = input('\nName: ')
            if name in mycontacts:print('That name is already a contact.');ui=input('Would you like to change it? (y/n)');q+=1 #If a taken name is entered, see if user wants to change it
            else:break
            if ui == 'y':change(mycontacts);return mycontacts #Change the contact if the user wants to
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        
        #Create an object for the contact
        contact = c.Contact(name, phone_number, email)
        
        #Move the contact into the dictionary. Let the user know if successful
        mycontacts[name] = contact
        print('\nContact successfully added.')
        
        #Ask the user if they would like to add another
        cont = input('\nWould you like to add another contact? (y/n) ')
        if cont != 'y': break
    
    #Return  the contact list
    return mycontacts
    
def change(mycontacts): #----------Perfected----------#
    #change accepts two arguments, a dictionary and a name(from add)
    #prompts the user for a name to change (unless called on by add) It will search the dictionary for the name
    #and prompts the user for new values for the attributes phone and email and changs them. Inform the user if
    #the name wansn't found
    
    #Set an accumulator
    q=0
    
    #Loop until the user no longer wants to
    while True:
        
        #Text before asking the user
        print('\nChange A Contact\n----------------')
        
        #Ask the user for a name to search for. Validate to see if the name is in the list
        while True:
            name = input('\nWhat is the name of the contact you would like to change? ')
            if name in mycontacts:q=0;break
            elif q==3:q=0;print('\nToo many failed attempts occured.\n');return mycontacts#Return to the menu if too many failed attempts occured
            else:print('\nPlease choose a name that is in the contact list.');q+=1
        
        #Ask the user for a new name, phone number, and email to replace the wanted contact. Make sure the new name... is a new name
        while True:
            nname = input('New Name: ')
            if nname not in mycontacts:q=0;break
            elif q==3:q=0;print('\nToo many failed attempts occured.\n');return mycontacts#Return to the menu if too many failed attempts occured
            else:print("\nChoose a name that isn't taken up.\n");q+=1 #Increate accumulator for validations
        phone = input('New Phone Number: ')
        email = input('New Email: ')
            
        #Create a new contact based on the new information from the user
        contact = c.Contact(nname, phone, email)
        
        #Delete the wanted username, and insert the new username. Let the user know if this was successful
        del mycontacts[name]
        mycontacts[nname] = contact
        print('\nContact successfully changed.')
        
        #Ask the user if they would like to change another contact
        cont = input('\nWould you like to change another contact? (y/n) ')
        if cont != 'y': break
    
    #Return the contacts
    return mycontacts
    
def delete(mycontacts): #----------Perfected----------#
    #delete accepts on argument, a dictionary
    #it will prompt the user for a name to delete and searches the dictionary for it and deltes it. If it doesn't appear
    #tell the user
    
    #Set an accumulator
    q=0
    
    #Loop until the user no longer wants to
    while True:
        
        #Text before asking the user
        print('\nDelete A Contact\n-------------')
        
        #Ask the user for a contact name to delete. Check to see if the name even is in the contact dictionary
        while True:
            name = input('\nWhat is the name of the contact that you would like to delete? ')
            if name not in mycontacts:print("\nThe wanted name isn't in the contact dictionary.\n");q+=1 #Increate accumulator for validations
            else:q=0;break
            if q==3:q=0;print('\nToo many failed attempts occured.\n');return mycontacts#Return to the menu if too many failed attempts occured
            
        #Delete the contact that is wanted to be deleted. If successful, let the user know
        del mycontacts[name]
        print('\nContact successfully deleted.')
        
        #Ask the user if they want to delete another
        cont = input('\nWould you like to delete another contact? (y/n) ')
        if cont != 'y': break
    
    #Return the list
    return mycontacts
    
    
def save_contacts(mycontacts):
    #save contacts accepts one argument, a dictionary
    #it will open the file <file name> as BINARY WRITE ('wb'). It will pickle the dictionary into the file, and then close the file
    #ie: for key in dictionary: pickle.dump(key, <file name>)
    
    #Open the file and binary write in it
    infile = open('contacts.dat','wb')
    
    #Dump the dictionary into the file
    pickle.dump(mycontacts,infile)
    
    #Close the file
    infile.close()
    
    #Change mycontacts to 'done'
    mycontacts = 'done'
    
    #Tell the user the successfulness and then say goodbye
    print('\nContacts successfully saved.')
    print('\nUntil next time.\nBye-Bye.')
    
    #Return mycontacts
    return mycontacts
    
main()