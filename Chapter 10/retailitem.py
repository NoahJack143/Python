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
        
    def get_cart(self, cart_info): #Add something later that will accept arguem
        
        return f'\n{cart_info[self.__description][1]} {self.__description}(s) <---> ${cart_info[self.__description][2]}'
    
    def get_description(self):
        return self.__description
    
    def get_units(self):
        return self.__units
    
    def get_price(self):
        return self.__price
    
    
    
