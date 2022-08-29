import turtle

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
        
def hcc(): #Hotdog Cookout Companion
    #Hotdog cookout companion accepts no arguments
    #hcc will take input from the use and tell the user how many hotdogs and buns they need to buy,
    #and the scripts will tell the user how many hotdogs and buns will be left over.
    #Input from the user
    people = int(input("Enter the amount of people attending: "))
    hotdogs_per_person = int(input("Enter the amount of hotdogs each person will get: "))
    
    #PRE Calculations
    total_hotdogs = people * hotdogs_per_person
    mim_hotdog_packs = total_hotdogs // 10
    mim_bun_packs = total_hotdogs // 8
    
    #POST 1 Calculations
    if (total_hotdogs % 10) > 0 and (total_hotdogs % 10) < 10:
        mim_hotdog_packs = mim_hotdog_packs + 1
    if (total_hotdogs % 8) > 0 and (total_hotdogs % 8) < 8:
        mim_bun_packs = mim_bun_packs + 1
        
    #POST 2 Calculations
    hotdogs_left_over = (mim_hotdog_packs * 10) - total_hotdogs
    buns_left_over = (mim_bun_packs * 8) - total_hotdogs
    
    #Output for the user
    print(" ")
    print("You will need to buy", mim_hotdog_packs, "packages of hotdogs")
    print("You will need to buy", mim_bun_packs, "packages of buns")
    print("There will be", hotdogs_left_over, "hotdogs left over")
    print("There will be", buns_left_over, "buns left over")

def tc(): #Time Calculator
    #Time Calculator accepts no arguments
    #Time Calculator will take input from the user and depending on the amount, the
    #program will either give the output in seconds, minutes and seconds, hours and
    #minutes and seconds, or days, hours, minutes, and seconds
    
    #Input from the user
    user_input = int(input("Enter a positive number of seconds: "))
    
    #Calculations 1
    if user_input >= 86400:
        days = user_input // 86400
        hours = (user_input - (days * 86400)) // 3600
        minutes = ((user_input - (days * 86400)) - (hours * 3600)) // 60
        seconds = (((user_input - (days * 86400) - (hours * 3600) -(minutes * 60)))) // 1
    elif user_input >= 3600:
        days = user_input // 86400
        hours = (user_input - (days * 86400)) // 3600
        minutes = ((user_input - (days * 86400)) - (hours * 3600)) // 60
        seconds = (((user_input - (days * 86400) - (hours * 3600) -(minutes * 60)))) // 1
    elif user_input >= 60:
        days = user_input // 86400
        hours = (user_input - (days * 86400)) // 3600
        minutes = ((user_input - (days * 86400)) - (hours * 3600)) // 60
        seconds = (((user_input - (days * 86400) - (hours * 3600) -(minutes * 60)))) // 1
    elif user_input >= 0:
        days = user_input // 86400
        hours = (user_input - (days * 86400)) // 3600
        minutes = ((user_input - (days * 86400)) - (hours * 3600)) // 60
        seconds = (((user_input - (days * 86400) - (hours * 3600) -(minutes * 60)))) // 1
    else:
        print(" ")
        print("ERROR")
        
    #Extra space for prettiness
    print(" ")
        
    #Output for the user
    if user_input >= 86400:
        print("After", user_input, "seconds have passed,", days, "days,", hours, "hours,",
              minutes, "minutes,", "and", seconds, "seconds would've passed.")
    elif user_input >= 3600:
        print("After", user_input, "seconds have passed,", hours, "hours,",
              minutes, "minutes,", "and", seconds, "seconds would've passed.")
    elif user_input >= 60:
        print("After", user_input, "seconds have passed,", minutes, "minutes", "and", seconds, "seconds would've passed.")
    elif user_input >= 0:
        print("After", user_input, "seconds have passed,", seconds, "seconds would've passed.")
    else:
        print(" ")

def fd(): #February Days
    #February Days accepts no arguments
    #This program will take prompt the user for a year, and the output will tell
    #the user whether or not that year is a leap year
    
    #Input from the user
    year = int(input("Enter a year: "))
    
    #Calculations + Output
    if (year % 4) == 0:
        print(year, "is a leap year. There are 29 days in the month of February.")
    elif (year % 4) != 0:
        print(year, "is not a leap year. There are 28 days in the month of February.")
    else:
        print("ERROR")

def sfa(): #sir_fix_alot
    #sir_fix_alot accepts no arguments
    #This program will take multiple inputs from the user, and if the input is constantly False
    #, then the output will be get a new router. However, if even one of the inputs from the user True,
    #then the output will be Netflix and Chill.
    
    #PRE text just for fun
    print("ROUTER PROBLEM MANUAL")
    print("""ANSWER THE FOLLOWING QUESTIONS WITH EITHER "YES" OR "NO" """)
    print(" ")
    
    #Question 1 + possible output
    print("Reboot your computer and try to reconnect to the router...")
    print(" ")
    answer1 = input("Did that fix the problem?: ")
    if answer1 == "YES":
        print(" ")
        print("Great! Go enjoy your Netflix show!")
    #Question 2 + possible output
    elif answer1 == "NO":
        print(" ")
        print("Reboot your computer again and try to reconnect to the router...")
        print(" ")
        answer2 = input("Did that fix the problem?: ")
        if answer2 == "YES":
            print(" ")
            print("Great! Go enjoy your Netflix show!")
        #Question 3 + possible output
        elif answer2 == "NO":
            print(" ")
            print("Check your cables and make sure that they are firmly attached...")
            print(" ")
            answer3 = input("Did that fix the problem?: ")
            if answer3 == "YES":
                print(" ")
                print("Great! Go enjoy your Netflix show!")
            #Question 4 + possible outputs
            elif answer3 == "NO":
                print(" ")
                print("Move your router to a location that is closer to your computer...")
                print(" ")
                answer4 = input("Did that fix the problem?: ")
                if answer4 == "YES":
                    print(" ")
                    print("Great! Go enjoy your Netflix show!")
                #Question 5 + remaining outputs
                elif answer4 == "NO":
                    print(" ")
                    print("Your final solution would be to get a new router.")
                    if answer4 == "YES":
                        print(" ")
                        print("Great! Go enjoy your Netflix show!")
                else:
                    print(" ")
                    print("ERROR")
                    print("ENTER THE REQUESTED RESPONSES NEXT TIME")
            else:
                print(" ")
                print("ERROR")
                print("ENTER THE REQUESTED RESPONSES NEXT TIME")
        else:
            print(" ")
            print("ERROR")
            print("ENTER THE REQUESTED RESPONSES NEXT TIME")
    else:
        print(" ")
        print("ERROR")
        print("ENTER THE REQUESTED RESPONSES NEXT TIME")
        
def rs(): #Restaurant Selector
    #Restaurant Selector accepts no arguments
    #This script will prompt the user for questions about foods they can or can't eat.
    #Then, the script will give the user their restaurant options.
    
    #Input from the user
    vegetarian = input("Is anyone a vegetarian? ").lower()
    vegan = input("Is anyone vegan? ").lower()
    gluten_free = input("Is anyone gluten-free? ").lower()
    
    #PRE Text output
    print(" ")
    print("Here are your restaurant choices:")
    
    #If statements + output
    if vegetarian == "yes" and vegan == "yes" and gluten_free == "yes":
        print("Corner Cafe")
        print("The Chef's Kitchen")
    elif vegetarian == "yes" and vegan == "yes" and gluten_free == "no":
        print("Search for another restaurant to satisfy the group.")
    elif vegetarian == "yes" and vegan == "no" and gluten_free == "no":
        print("Main Street Pizza Company")
        print("Mama's Fine Italian")
    elif vegetarian == "no" and vegan == "yes" and gluten_free == "yes":
        print("Search for another restaurant to satisfy the group.")
    elif vegetarian == "no" and vegan == "yes" and gluten_free == "no":
        print("Search for another restaurant to satisfy the group.")
    elif vegetarian == "no" and vegan == "no" and gluten_free == "yes":
        print("Search for another restaurant to satisfy the group.")
    elif vegetarian == "no" and vegan == "no" and gluten_free == "no":
        print("Search for another restaurant to satisfy the group.")
    
def httm(): #hit_the_target()
    #hit the target accepts no arguments
    screenwidth = 600  #screen width
    screenheight = 600  #screen height
    targetleftx = 100  #Target's lower left corner x
    targetlefty = 250  #Target's lower left corner y
    targetwidth = 25  #Target's width
    targetfactor = 30  #Arbitrary force factor
    projectilespeed = 1  #Projectile's animation speed
    north = 90  #Angle of north direction
    south = 270  #Angle of south direction
    east = 0  #Angle of east direction
    west = 180  #Angle of west direction
    
    #Presettings to create the target
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(targetleftx, targetlefty)
    turtle.pendown()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.penup()
    turtle.goto(0,0)
    turtle.showturtle()
    
    #Ask the user for input
    projectile_angle = int(input("Enter the projectile's angle (1-359): "))
    force = int(input("Enter the launch force (1-10): "))
    
    #Speed of animation
    turtle.speed(1)
    
    #Angle of projection
    turtle.setheading(projectile_angle)
    
    #Force of projection
    turtle.forward(force * 35)
    
    #Space between the input and the output
    print(" ")
    
    #Check to see if they hit the target. If not, give hints
    if turtle.xcor() > 100 and turtle.xcor() < 125 and turtle.ycor() > 250 and turtle.ycor() < 275:
        print("You hit!")
    elif turtle.xcor() < 100 and turtle.ycor() < 250:
        print("You missed!")
        print("Try using more power and a greater angle next time!")
    elif turtle.xcor() > 125 and turtle.ycor() < 250:
        print("You missed!")
        print("Try using more power and a lesser angle next time!")
    elif turtle.xcor() > 125 and turtle.ycor() > 275:
        print("You missed!")
        print("Try using lesser power and a lesser angle next time!")
    elif turtle.xcor() < 100 and turtle.ycor() > 275:
        print("You missed!")
        print("Try using lesser power and a greater angle next time!")

    turtle.done()