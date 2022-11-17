#Program 10-13

#Create a class
class CellPhone:
    
    #---Attributes---#
    def __init__(self, manufacturer, model_number, retail_price):
        self.manufact = manufacturer #Assign the attribute
        self.model_num = model_number #Assign the attribute
        self.retail_price = retail_price #Assign the attribute
        
    def __str__(self, manufact, model_num, retail_price):
        print(f'{manufact}, {model_num}, costs ${retail_price}.')
        
    #---Instance methods---#
    
    #Changing the manufacturer
    def set_manufact(self, manufacturer):
        self.manufact = manufacturer
    
    #Changing the model
    def set_model(self, model):
        self.model_num = model
        
    #Changing the price
    def set_retail_price(self, price):
        self.retail_price = price
    
    #Return the phone's manufacturer
    def get_manufact(self):
        return self.manufact
    
    #Return the phone's model number
    def get_model(self):
        return self.model_num
    
    #Return the phone's retail price
    def get_retail_price(self):
        return self.retail_price