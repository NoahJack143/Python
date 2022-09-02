def loop1(): #Ths is an example of a while loop (Pretest loop that tests the condition)
    #loop1 accepts no arguments
    #It loops through 10 times calculating a running
    #total and outputs the total as it processes
    
    #constants
    loop_end = 10 #constant for the ax iterations
    counter = 0 #accumulator to create a counted loop
    total = 0 #variable (also a type of accumulator) for running total
    
    #Start the loop
    while counter < loop_end:
        #increment the accumulator (counter)
        counter = counter + 1 #this is the same as counter += 1
        
        #as long as counter is less than 10, these lines will execute
        print("The loop has run", counter, "times.")
        total = total + counter
        
        #output a message with the running total
        print("The total of numbers 1 - 10 for this iteration is: ", total)
        
        #the loop statements are over, so it will return to the while statement
        #to test the condition again
loop1()

def loop2(): #for loop example
    #loop2 accepts no arguments
    #it calculates a running total of a fixed set of numbers 1-10
    #and outputs the total
    
    #constants
    loop_begin = 1
    loop_end = 10
    total = 0
    
    #the for loop is a different iteration than the other loop
    #num localizes "for" and is managed by the for loop
    #num can be ANYTHING YOU WANT IT TO BE
    #range makes the loop through the numbers from "loop_begin" to "loop_end"
    for num in range(loop_begin, loop_end + 1): #for loop to iterate from 1 - 10
        #as long as values remain between 1 (loop_begin) - 10 (loop_end), iterate
        
        total = total + num#whatever value it is hold by "num". "num" takes numbers from range (1-10 in this scenario).
        #Keep a running total of values from 1- 10. As the loop loops, the num will move to the next number from 1-10.
        #The first time the loop runs through, num = 1, the second time, num = 2, the third time, num = 3, and so on so forth.
        
        print("The loop has iterated", num, "times.")
        
        #loop statements are finished, return to the for loop start
        print("The total for this iteration of all numbers 1-10 is: ", total)
        
        #loop statements are finished, return to the for loop start. If any numbers remain, continue.
loop2() #Adding this to the bottom of your script will allow the scrip to run from just pressing the "run" button. Otherwise
#you'll have to press the "run" button AND type "loop2()" in the interactive part