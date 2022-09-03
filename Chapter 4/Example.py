def loop_example():
    #loop example accepts no arguements
    #It takes input from the user for the number of loops
    #and loops until it reaches the user input
    
    number = int(input("Enter the number of loops to run: "))
    counter = 1 #prime the accumulator (This will stop the while loop)
    #without "counter" your loop will never stop
        
    while counter <= number: #while "number" is true     Step 1
        #run these lines of code
        print("This is loop number", counter )#     Step 2
        counter = counter + 1 #or counter += 1     Step 3 and loop back to Step 1
        
def loop_example2():
    #loop example accepts no arguements
    #It takes input from the user for the number of loops
    #and loops until it reaches the user input.
    
    #     This test uses 0 instead of 1 for the counter
    
    number = int(input("Enter the number of loops to run: "))
    counter = 0 #prime the accumulator (This will stop the while loop)
    #without "counter" your loop will never stop
        
    while counter < number: #while "number" is true     Step 1
        #run these lines of code
        print("This is loop number", counter )#     Step 2
        counter = counter + 1 #or counter += 1     Step 3 and loop back to Step 1
        
def loop_example3():
    #loop example accepts no arguements
    #It takes input from the user for the number of loops
    #and loops until it reaches the user input
    
    #This test uses a sentinel loop
    
    keep_going = "y" #prime the sentinel to "y"
    
        
    while keep_going == "y": #will run as long as keep_going == "y"
        number = int(input("Enter the number of loops to run: "))
        counter = 0
        while counter <= number: #while "number" is true
            print("This is loop number", counter )
            counter = counter + 1 #or counter += 1
        keep_going = input("Keep going? (y/n): ")
    
#iteration
#iteration 5 = loop will run 5 time
        
#range(2)
    #rage(0, 2)
#python starts counting from 0
    
def le2():
    #loop example 4 accepts no arguments
    #it uses a for loop to loop 5 times
    #and outputs a number
    
    for item in range(5):
        print(item)
        
def le3():
    #loop example 5 accepts no arguments
    #it uses a for loop to loop 5 times
    #and outputs a number
    
    for num in [1, 2, 3, 4]: #holds one value until it's done with the loop, then it holds the second value until it's done with the loop
    #and then when it gets to the end, it ends because there isn't anymore to reiterate
        print("I have holding the value", num)
        print("I will now release the value of num")
        
def le4():
    
    for num in range(1, 10+1):
        print(num)
         
