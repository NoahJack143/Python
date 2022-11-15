import ranodm

#comments to explain your class
#more comments to explain your class
#Capitols are used for standard naming
class CookieCutter:
    #a class should begin with the __init__() #__ is a double underline
    #it receives two arguments for name and number
    
    #------------Data Attributes------------#
    def __init__(self, name, number): #Always use the key word self, which refers to itself. This could recieve multiple things
        #all of your initial attributes
        self.name = name
        self.number = number
        
    #---------------Methods------------------#
    #change name changes the name attribute
    #change number changes the number attribute
    
    def change_name(self, name): #Be sure to have self
        self.name = name
        
    def change_number(self, number): #Be sure to have self
        self.number = number