#Program 10-16
#Imports
import pickle
import cellphone as cp

def main():
    #main receives no arguments
    #it opens a file called cellphones.dat
    #and loops until the user enters a 'n' to continue
    #each iterations of the loop the user is prompted
    #to enter phone data: manufacturer, model, and retail price(validation)
    #an object is created using the CellPhone class in cellphone.py
    #with the attributes manufact, model, and retail_price
    #the object is pickled to the file cellphones.dat
    
    #Create an object file
    infile = open('cellphone.dat', 'wb')
    
    #Loop until the user no longer wants to continue
    while True:
        #Gain information from the user
        manufact = input('Enter the phone manufacturer: ')
        model = input('Enter the phone model: ')
        while True:
            try:
                price = float(input('Enter the phone retail price: '))
                break
            except:
                print('\nEnter a valid price.\n')
                
        #Create an object using the information given and the CellPhone class from cellphone.py
        phone = cp.CellPhone(manufact, model, price)
        
        #Dump every phone into the file
        pickle.dump(phone,infile)
        
        #Ask if the user if they want to continue
        cont = input('\nEnter another phone? (y/n) ')
        if cont.lower() != 'y':break
    
    #Close the file
    infile.close()
    
    #Print a final message
    print('\nAll data has been written to cellphones.dat')
    
    