

def file_test():#Test for file in a for loop
    #file test accepts no arguments
    #this will be the first test
    
    infile = open('steps.txt', 'r')
    
    for line in infile:
        print(line)