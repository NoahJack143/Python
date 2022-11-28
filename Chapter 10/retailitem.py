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
        
    #---Methods---#
        
    def display(self, description, units, price):
        return f'\n Description: {description}\nUnits: {units}\nRetail Price: {price}\n'
    
    
        