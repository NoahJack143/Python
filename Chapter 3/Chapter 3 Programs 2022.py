

def ta(): #test_average
    
    #Presettings before recieving input
    highscore = 100
    
    #Inputs from the user
    first_score = int(input("Enter the first score: "))
    second_score = int(input("Enter the second score: "))
    third_score = int(input("Enter the third score: "))
    
    #Calculations
    average_score = (first_score + second_score + third_score) / 3
    
    #Displayed average for the user
    print("The average score is: ", format(average_score, ".2f"))
    
    #If the score is higher than the highscore + output
    if average_score > highscore:
        print("Congratulations!")
        print("That is a highscore!")
        
    #If the score is equal to the highscore + output
    if average_score == highscore:
        print("Wow!")
        print("You tied with the highscore!")
        
    #If the score is lower than the highscore + output
    if average_score < highscore:
        print("Sorry!")
        print("You didn't beat the highscore.")
        
def arp(): #auto_repair_payroll
    
    #Input from the user
    hours = int(input("How many hours have you worked? "))
    hourly_rate = int(input("What is your hourly rate? "))
    
    #Calculations
    normal_pay = hours * hourly_rate
    extra_hours = hours - 40
    overtime_pay = normal_pay * extra_hours * 1.5
    
    #If the worker has worked MORE than 40 hours
    if hours > 40:
        print("You will recieve ", format(overtime_pay, ".2f"), end = "$")
    #If the worker has worked LESS than 40 hours
    else:
        print("Your pay will be ", format(normal_pay, ".2f"), end = "$")