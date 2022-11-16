#The BankAccount class simulates a bank account

class BankAccount: #Program 10-7
    
    #the __init__ method accepts an argument for the account's balance.
    #it is assigned to the __balance attribute
    
    def __init__(self, bal):
        self.__balance = bal
        
    def __str__(self): #the default print statement when calling the object
        return 'The balance is $' + format(self.__balance, ',.2f')
        
    #the deposit method makes a deposit into the account
        
    def deposit(self, amount):
        self.__balance += int(amount)
        
    #the withdaraw method makes a withdrawl from teh account
        
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')
            
    #the get_balance method returns the accoutn balance
            
    def get_balance(self):
        return self.__balance
    
