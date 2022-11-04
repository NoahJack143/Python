def bd_main(): #Program 9-2
    #bd main accepts no arguments
    #it will call for other functions
    #and it will output the wanted
    #information
    
    #Create a dictionary for the birthdays
    birthdays = {}
    
    #Loop so the user can have multiple inputs
    while True:
        
        #Call for the menu, bd_menu()
        ui = bd_menu(birthdays)
        
        #Check to see if the user is done or not
        if ui == 'done':
            break
        else:
            birthdays, msg = ui(birthdays)
            print(msg)
        
        
def bd_menu(birthdays):
    #bd menu accepts one argument, a dictionary of birthdays
    #it will create a menu for the user and
    #will let them call another function
    
    #Create a list of the choices provided
    options = [bd_lookup,bd_add,
               bd_edit, bd_remove]
    
    #Print the options for the user
    print('Birthday Menu\n---------------\n'+
          '1) Lookup a Birthday\n2) Add a Birthday'+
          '\n3) Edit a Birthday\n4) Remove a Birthday'+
          '\n5) Quit\n---------------')
    
    #Ask the user for what they want to do
    ui = int(input('Which option would you like to choose? '))
    
    #Create an accumulator, and check for the user's input and validate their input
    c=1 #Checker
    for i in range(1,6):
        if ui == i:
            break
        else:
            c += 1
        if c==5:
            return 'done'
    ui = options[ui-1]
    
    return ui

def bd_lookup(birthdays):
    #bd lookup accepts one argument, a dictionary
    #it will find a name within the dictionary
    #if the name isn't in there, let the user know
    #if there is a name, print the name and birthday
    
    #Prompt the user for a name to search for
    name = input("\nWho's birthday would you like to look for? ")
    
    #Check to see if they're in the dictionary, if so get the birthday
    bday = birthdays.get(name, '0')
    
    #Return the information
    if bday != '0':
        return birthdays, f"\n{name}'s birthday is on {bday}.\n"
    return birthdays, f"\n{name}'s birthday isn't recorded.\n"
    
def bd_add(birthdays):
    #bd add accepts one argument, a dictionary
    #it will ask the user for a name and birthday
    #and it will add the information to the dictionary
    
    #Prompt the user for a name and a birthday
    name = input("\nWho's birthday would you like to add to the list? ")
    bday = input(f"What is {name}'s birthday? ")
    
    #Add the name into the dictionary
    birthdays[name] = bday
    
    #Return the dictionary
    return birthdays, f"\n{name}'s birthday was added to the list.\n"

def bd_edit(birthdays):
    #bd edit accepts one argument, a dictionary
    #it will ask the username for a name to edit
    #it will then edit that name based on what the user wants it to be
    #validation will be included
    
    #Prompt the user for a name to be editted
    name = input("\nWho's birthday would you like to change? ")
    
    #If their wanted name is within the dictionary, move accordingly
    if name in birthdays:
        #Prompt the user for the user's new birthday
        bday = input(f"What would you like {name}'s new birthday to be? ")
        
        #Change the birthday
        birthdays[name] = bday
    else:
        return birthdays, f"\n{name}'s birthday isn't recorded.\n"
    return birthdays, f"\n{name}'s birthday was changed.\n"

def bd_remove(birthdays):
    #bd remove accepts one argument, a dictionary
    #it will remove the requested birthday
    #it will tell the user if the birthday doesn't exist
    
    #Prompt the user for a birthday to be removed
    name = input("\nWho's birthday would you like to have removed? ")
    
    #Pop the name and check to see if they're in the dictionary o not
    popped_name = birthdays.pop(name, '0')
    if popped_name == '0':
        return birthdays, f"\n{name}'s birthday isn't recorded.\n"
    return birthdays, f"\n{name}'s birthday was removed.\n"

bd_main()
