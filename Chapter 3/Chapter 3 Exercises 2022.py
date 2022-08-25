

def dotw(): #Day of the Week
    #Day of the Week accepts no arguments
    #This program will ask the user for a number between 1-7
    #and give feedback by giving a corresponding day in Spanish
    
    #Input from the user
    day = int(input("Enter a number between one and seven: "))
    
    #If statements for output
    if day == 1:
        print("The day is Lunes")
    elif day == 2:
        print("The day is Martes")
    elif day == 3:
        print("The day is Miecoles")
    elif day == 4:
        print("The day is Jueves")
    elif day == 5:
        print("THe day is Viernes")
    elif day == 6:
        print("The day is Sabado")
    elif day == 7:
        print("The day is Domingo")
    else:
        print("That's not a number between one and seven...")
        
def rn(): #Roman Numerals
    #Roman numerals accepts no arguments
    #roman numerals will take a number from the user and convert it
    #into a roman numeral
    
    #Input from the user
    number = int(input("Enter a number between one and ten: "))
    
    #If statements for output
    if number == 1:
        print("The corresponding roman numeral is I")
    elif number == 2:
        print("The corresponding roman numeral is II")
    elif number == 3:
        print("The corresponding roman numeral is III")
    elif number == 4:
        print("The corresponding roman numeral is IV")
    elif number == 5:
        print("The corresponding roman numeral is V")
    elif number == 6:
        print("The corresponding roman numeral is VI")
    elif number == 7:
        print("The corresponding roman numeral is VII")
    elif number == 8:
        print("The corresponding roman numeral is VIII")
    elif number == 9:
        print("The corresponding roman numeral is IX")
    elif number == 10:
        print("The corresponding roman numeral is X")
    else:
        print("ERROR")