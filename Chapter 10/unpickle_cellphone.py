#Program 10-17
#Imports
import pickle
import cellphone

def main():
    #main receives no arguments
    #it opens the file cellphones.dat to read binary
    #it loops until end_of_file to retreive each object
    #EOFError exception raised should set end_of_file to true
    #and calls display_data passing each object
    
    #Open the file
    infile = open('cellphone.dat', 'rb')
    
    #Loop until nothing else is to be read in the file
    while True:
        try:
            phone = pickle.load(infile)
            
            display_data(phone)
            
        except:
            break
    
    #Close the file when you are done
    infile.close()
    
def display_data(phone):
    #display_data receives an argument for phone
    #it uses the CellPhone class in cellphone.py to print the attributes
    #for the object
    
    #Print everything for that object
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model: {phone.get_model()}')
    print('Retail Price: $'+str(format(phone.get_retail_price(),',.2f')));print()
        
