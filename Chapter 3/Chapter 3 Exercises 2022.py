

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
        
def cm(): #color_mixer
    #color mixer accepts no arguments
    #This program will ask the user for two primary colors and will
    #give the user the mix of the two colors. If the user puts in
    #a non primary color, then there will be an ERROR message.
    
    #Input from the user
    color1 = input("Enter a primary color: ")
    color2 = input("Enter a second primary color: ")
    
    #If statements
    if (color1 == "red" and color2 == "blue") or (color1 =="blue" and color2 == "red"):
        print(" ")
        print("The secondary color is purple")
    elif (color1 == "red" and color2 == "yellow") or (color1 =="yellow" and color2 == "red"):
        print(" ")
        print("The secondary color is orange")
    elif (color1 == "yellow" and color2 == "blue") or (color1 =="blue" and color2 == "yellow"):
        print(" ")
        print("The secondary color is green")
    else:
        print(" ")
        print("ERROR")
        
def hcc(): #hotdog cookout companion
    #Hotdog Cookout Companion accepts no arguments
    #This program will ask the user for the amount of people attending
    #and the number of hotdogs each person will recieve. Using their input,
    #the program will calculate the minimum numer of packages of hotdogs and buns required,
    #the number of hotdogs left over, and hte number of hotdog buns left over.
    
    #Input from the user
    people_attending = int(input("How many people are attending?: "))
    hotdogs_per_person = int(input("How many hotdogs will each person get?: "))
    
    #PRE Calculations
    total_amount_of_hotdogs = people_attending * hotdogs_per_person
    minimum_hotdogs = total_amount_of_hotdogs // 10
    minimum_hotdog_buns = total_amount_of_hotdogs // 8
    
    #If statements + more Calculations
    if ((total_amount_of_hotdogs % 10) > 0) and ((total_amount_of_hotdogs % 10) <10):
        new_minimum_hotdogs = minimum_hotdogs + 1
    if new_minimum_hotdogs > minimum_hotdogs:
        #move the hotdog left over equation up here and change the left over hotdog equation below
    if ((total_amount_of_hotdogs % 8) > 0) and ((total_amount_of_hotdogs % 8) < 8):
        minimum_hotdog_buns = minimum_hotdog_buns + 1
        
    #POST Calculations
    hotdogs_left_over = (minimum_hotdogs*10) - total_amount_of_hotdogs
    hotdog_buns_left_over = (minimum_hotdog_buns*10) - total_amount_of_hotdogs
    
    #Output for the user
    print(" ")
    print("The minimum number of packages of hotdogs required are ", minimum_hotdogs, " packages")
    print("The minimum number of pakcages of hotdog buns required are ", minimum_hotdog_buns," packages")
    print("The number of hotdogs left over would be ", hotdogs_left_over)
    print("The number of hotdog buns left over would be ", hotdog_buns_left_over)
    