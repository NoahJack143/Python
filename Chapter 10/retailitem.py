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
        return f'\nDescription: {self.__description}\nUnits: {self.__units}\nRetail Price: {self.__price}'
        
    #---Methods---#
        
    #def get_name(self,name):
    
    
        