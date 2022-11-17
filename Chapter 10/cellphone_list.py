#Program 10-14
#import cell phone
import cellphone as cp

def main():
    #main accepts no arguments
    #it calls phone_list() to generate a list of phones
    #then  calls display list, passing the list of objects, to display all data
    
    #Call make_list()
    phone_list = make_list()
    
    #Call for display_list() to shows the lists
    display_list(phone_list)
    
def make_list():
    #make list loops to prompts the user to enter data for
    #5 phones with attributes for mannufacturer, model, and retail price
    #it uses he CellPhone class in cellphone.py to create an object for phone
    #and appends it to a list
    
    #Create an empty list for all of the phones
    phone_list = []
    
    #Loop 5 times to get 5 different phones
    for i in range(1,6):
        #prompt the user for a manufacturer, model, and retail price
        manufact = input(f'\nEnter a manufacturer for phone #{i}: ')
        model = input(f'Enter a model for phone #{i}: ')
        while True:
            try:
                price = float(input(f'Enter a retail price for phone #{i}: '))
                break
            except:
                print('\nPlease enter a proper price.\n')
        #Create an object for every phone
        phone = cp.CellPhone(manufact, model, price)
        
        #Move every phone into the phone_list
        phone_list.append(phone)
        
    #Return the list
    return phone_list

def display_list(phone_list):
    #display list accepts an argument for phone list
    #it loops to output all of the attibutes for each object in phone_list
    #using the CellPhone class in cellphone.py
    
    #Text before the list of phones and information
    print('\nHere is the list of phones you entered:')
    
    #Loop 5 times for each phone
    for i in range(0,5):
        print(f'Manufacturer: {phone_list[i].get_manufact()}')
        print(f'Model: {phone_list[i].get_model()}')
        print('Retail Price: $'+str(format(phone_list[i].get_retail_price(),',.2f')));print()
        