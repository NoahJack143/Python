#Program 10-13
#Import cellphone.py
import cellphone

def main():
    #main accepts no arguments
    #it will call use the class from cellphone
    #and do commands that the user
    #gives the program
    
    #Print the opening statement
    print('Welcome to the Galactic Phone Database.\n')
    
    #Ask the user for initializations
    manufact = input('Enter the phone manufacturer: ')
    model_num = input('Enter the phone model number: ')
    while True:
        try:
            retail_price = int(input(f'Enter the retail price for your {manufact}, model {model_num}: '))
            break
        except:
            print('\nPlease enter a proper retail price.\n')
    
    #Intialize the phone
    phone = cellphone.CellPhone(manufact, model_num, retail_price)
    
    #Tell the use the data they entered
    print('\nHere is the data you entered:')
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model: {phone.get_model()}')
    print(f'Retail Price: {phone.get_retail_price()}')
    