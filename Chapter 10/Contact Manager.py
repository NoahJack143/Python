#Program 10-19
#Imports
import contact as c

#The main function to call
def main():
    #main accepts no arguments
    #it calls load_contancts to get the dictionary (CHECK TO SEE IF DICTIONARY IS MADE OR IS EMPTY AND
    #MOVE ACCORDINGLY). Call appropriate functions based on the return value for the menu from, get_menu_choice().
    #Finally save the contacts when the user quits
    
    #Call on load_contacts to get the dictionary
    mycontacts = load_contacts()
    
def load_contancts():
    #load contacts accepts no arguments
    #it opens the <file name> = contacts.dat, as READ BINARY ('rb'). Unpickles the file into the dictionary
    #contact_dct and handles any IO exceptions. Returns the dictionary
    
    #Read the file and get the dictionary
    infile = open('contacts.dat', 'rb')
    
    #Create an empty dictionary
    mycontacts = {}
    
    #For every single key, move it into the new dictionary
    key = pickle.load(infile)
    mycontacts[key] =
    
def get_menu_choice():
    #get menu choice accepts no arguments
    #it will present the user with a menu and returns a choice
    
def look_up(mycontacts):
    #look_up accepts one argument, a dictionary
    #it will prompt the user for a name, prints the name the object for name in dictionary, or
    #'That name is not found' if it isn't in the dictionary.
    
def add(mycontacts):
    #add accepts one argument, a dictionary
    #it will prompt the user for a name, phone, and email and create an object with those attributes
    #If the name doesn't exist, add it to the dictionary with the name as the key and the object as the value
    #If the name already exists, say that it already exists and ask the user if they want to change it(call change)
    
def change(mycontacts,name):
    #change accepts two arguments, a dictionary and a name(from add)
    #prompts the user for a name to change (unless called on by add) It will search the dictionary for the name
    #and prompts the user for new values for the attributes phone and email and changs them. Inform the user if
    #the name wansn't found
    
def delete(mycontacts):
    #delete accepts on argument, a dictionary
    #it will prompt the user for aname to delete and searches the dictionary for it and deltes it. If it doesn't appear
    #tell the user
    
def save_contacts(mycontacts):
    #save contacts accepts one argument, a dictionary
    #it will open the file <file name> as BINARY WRITE ('wb'). It will pickle the dictionary into the file, and then close the file
    #ie: for key in dictionary: pickle.dump(key, <file name>)
    