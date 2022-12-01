#Imports will be here
#------#

#------#

#The Class will be created here
class RetailItem:
    
    #---Attributes---#
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price
        
    def __str__(self):
        return f'\nDescription: {self.__description}\nUnits: {self.__units}\nRetail Price: ${self.__price}'
        
    #---Methods---#
        
    def get_cart(self, EI): #Add something later that will accept arguem
        
        for amount in EI: return f'\n{amount} {self.__description}(s) <---> ${EI[amount]}'
    
    def get_description(self):
        return self.__description
    
    def get_units(self):
        return self.__units
    
    def get_price(self):
        return self.__price
    
    
    
