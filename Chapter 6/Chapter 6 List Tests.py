#THIS IS A TEST FOR LISTS

def test1(): #Test 1
    #test 1 accepts no arguments
    #thi si the first etest
    
    dpm = [31, 28]
    for num in dpm:
        print('hi')
        
def test2(): #test 2
    #test 2 accepts no arguments
    
    counter = 1
    
    for num in range(1, 31 + 1):
        print(counter)
        counter += 1
        
    counter = 1
    
    for num in range(1, 28 + 1):
        print(counter)
        counter += 1
        
#==========================================#
        
def test3(): #test 3
    #test3 accepts no arguments
    
    #Call for function
    month, month2= months()
    
    for day in month:
        print('hi')
    
def months():
    #months accepts no arguments
    #assign ranges to months
    jan = [1, 31 + 1]
    feb = [1, 28 + 1]
    
    return [jan, feb]

#+==============================================#

def test4(): #test 4
    #test3 accepts no arguments
    
    #Call for function
    month, month2= months()
    
    for day in range[month]:
        print('hi')
    
def months():
    #months accepts no arguments
    #assign ranges to months
    jan = [32]
    feb = [29]
    
    return [jan, feb]