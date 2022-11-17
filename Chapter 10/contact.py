#Program 10-18

#Create the class
class Contact:
    
    #---Attributes---#
    def __init__(self,name, phone_number,email_address):
        self.__name=name
        self.__phone_num=phone_number
        self.__email_address=email_address
        
    def __str__(self):
        return f'Name: {self.__name}\nPhone Number: {self.__phone_num}\nEmail: {self.__email_address}'
        
    #---Methods---#
        
    def set_name(self,name):
        self.__name=name
        
    def set_phone(self,phone_number):
        self.__phone_num=phone_number
        
    def set_email(self,email_address):
        self.__email_address=email_address
        
    def get_name(self,name):
        return self.__name
    
    def get_phone(self):
        return self.__phone_num
    
    def get_email(self):
        return self.__email_address
    