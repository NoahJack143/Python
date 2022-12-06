#Imports will be here
#------#
import retailitem as ri

#------#

#The Class will be created here
class CashRegister:
    
    #---Attributes---#
    
    def __init__(self, description, cart):
        self.__item = descriptionv #Create an object
        cart.append(description) #Add the item into the cart
        return cart #Return the updated shopping cart
        
    def __str__(self):
        #Print a message when called for
        return f'\nDescription: {self.__description}\nPrice: {self.__price}'
        
    #---Methods---#
    
    def purchase_item(description, cart):
        
        #Add the purchased item into the cart
        cart.append(description)
        
        #Return the cart
        return cart