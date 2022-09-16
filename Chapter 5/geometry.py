#Program 5-28

#This program allows the user to choose various
#geometry calculations from a menu. This program
#imports the circle and rectangle modules.
import circle
import rectangle

#Constants are for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# The main function.
def display_menu():
    #The display menu.
    choice = 0
    
    print("___________________________")
    print(" ")
    print("\tMENU")
    print("___________________________")
    print("Choice 1: Area of a circle")
    print("Choice 2: circumference_choice")
    print("Choice 3: Area of a rectangle")
    print("Choice 4: Perimeter of a rectangle")
    print("Choice 5: Quit")
    print("___________________________")
    print(" ")
    
def main():
    #The choice variables controls the loop
    #and holds the user's menu choice.
    
    choice = 0
    QUIT_CHOICE = 5
    
    while choice != QUIT_CHOICE:
        #display the menu.
        display_menu()
        
        #Get the user's choce
        choice = int(input("Enter your choice: "))
        
        #Perform the selected action.
        if choice == AREA_CIRCLE_CHOICE:
            redius = float(input("Enter the circle's radius: "))
            print('THe area is', circle.area(redius))
            print(' ')
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The circumference is', \
                  circle.circumference(radius))
            print(' ')
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("The area is", rectangle.area(width, length))
            print(' ')
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("The perimeter is", \
                  rectangle.perimeter(width, length))
            print(' ')
        elif choice == QUIT_CHOICE:
            print(' ')
            print("Exiting the program...")
        else:
            print(' ')
            print("Error: invalid selection.")
main()