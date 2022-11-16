#Program 10-8: account_test.py
#import the bankaccount module
import bankaccount as ba

def main(): #Program 10-8
    #main accepts no arguments
    #it takes input from the user for a starting balance
    #it uses the BankAccount class in bankaccount.py to create
    #an object savings, passing the starting balance
    #it takes input from the user for a pyacheck
    #it uses the desposit() method to deposit a paycheck
    #it takes the input from the user for a withdrawl and uses the withdraw() method
    #and outputs the final balance
    
    #Prompt the user of their starting balance
    BA = ba.BankAccount(int(input('Enter your starting balance: ')))
    
    #Ask the user for an amount that they would like to deposit
    while True:
        try:
            BA.deposit(int(input('Enter the amount of your paycheck to deposit: ')))
            break
        except:
            print("Error")
    print('Deposit completed\n')
    
    #Show the balance
    print(f'The balance is ${BA.get_balance()}')
    
    #Ask the user for an amount to withdraw
    while True:
        try:
            BA.withdraw(int(input('How much would you like to withdraw: ')))
            break
        except:
            print('Error')
    print('Withdrawl completed\n')
    
    #Show the remaining balance
    print(f'The balance is ${BA.get_balance()}')