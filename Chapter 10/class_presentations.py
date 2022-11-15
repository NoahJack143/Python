#Class Dog
#Class Car

class Dog:
    #the Dog class accepts values for anme, age, and the coat color
    #the str method prints the dog's vitals aka: the state of the object
    #the speak method prints what the says 'SAYS'
    
    #class attributes
    species = 'Canis familiaris' #common name for all dogs aka: all instances
    
    def __init__(self, name, age, coat):
        self.name = name #Create an attrbute for the name for the object
        self.age = age #Same thing but for age
        self.coat = coat #Same thing but for coat
        
    def __str__(self): #printing something will resort to this
        #str returns a string with the state of the object
        #displaying the name, age, and coat of the dog
        return f'{self.name} is {self.age} years old and has a {self.coat} coat color.'
    
    def speak(self, sound):
        #speak accepts an argument for the string sound
        #and return a string with the dogs name and what it 'says'
        return f'{self.name} said {sound}'

class Car:
    #the object of the Car class has attributes for
    #the year, make, model, color, and mileage
    #str prints the vehicle's vitals/specs
    #method add_miles to add miles to the car's mileage
    
    #------------------Attributes------------------#
    def __init__(self, year, make, model, color, mileage):
        self.year=year #assign the attribute
        self.make=make #assign the attribute
        self.model=model #assign the attribute
        self.color=color #assign the attribute
        self.mileage=mileage #assign the attribute
        
    #----------------------Instance methods--------------#
    def __str__(self): #return a string witht eh vitals of the vehicle
        return f'The {self.year} {self.color} {self.make} {self.model} has {self.mileage} miles.'
    
    def add_miles(self, miles):
        #add miles accepts a numeric value for miles
        #it adds the miles to the total mileage
        #and returns a message
        
        self.mileage+=miles
        print(f'{miles} miles have been added to the mileage.')