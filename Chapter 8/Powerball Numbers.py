

def pb_main(): #Exercise 13
    #pb main accepts no arguments
    #it is the main function that will have outputs
    #and will call on other functions
    
    #Call for the function, pb_frequency, and get back the frequency of the numbers and the available lottery numbers
    frequency, lotto_numbers = pb_frequency()
    
    #Copy the frequency list, and sort the new list from greatest to least
    frequency_sort = []
    for element in frequency:
        frequency_sort.append(element)
    frequency_sort.sort()
    frequency_sort.reverse()
    
    #Create an empty list, run a nested for loop, find the top ten highest frequencies the first time and then the top ten lowest frequencies,
    #then find the position of those frequencies in the frequency list, change their position to anythying so they aren't used again,
    #then use that as an index for the lotto_numbers list, and append the result to the frequencies list
    frequencies = []
    for loop in range(0,2):
        if loop == 1:
            frequency_sort.reverse() #Reverse the list the second time through
        for num in range(0,9+1):
            current_frequency = frequency_sort[num]
            position = frequency.index(current_frequency)
            frequency[position] = -1
            currently_occuring_number = lotto_numbers[position]
            frequencies.append(currently_occuring_number) #Append every number to the same list
            
    #Reverse the list back to greatest to least, and then print the most occuring numbers and their frequency
    frequency_sort.reverse()
    print('Here are the 10 most frequently occuring numbers:')
    for num in range(0,9+1):
        print(frequencies[num], 'with a frequency of', frequency_sort[num])
    #Reverse the list back to least to greatest, and then print the most occuring numbers and their frequency
    frequency_sort.reverse()
    print('\nHere are the 10 least frequently occuring numbers:')
    for num in range(10,19+1):
        print(frequencies[num], 'with a frequency of', frequency_sort[num-10])
    
    
def pb_frequency(): #For Exercise 13
    #pb_frequency accepts no arguments
    #it will find how often each number occurs
    
    #open the file
    infile = open('pbnumbers.txt', 'r')
    
    #Move the first 15 characters of every line into a string, and then split that string
    contents = ''
    for line in infile:
        contents = contents + line[:15]
    contents = contents.split()
    
    #Create a list of all the possible lottery numbers
    lotto_numbers = ['01','02','03','04','05','06','07','08','09']
    for num in range(10,69+1):
        lotto_numbers.append(str(num))
        
    #Create an empty list, find out how often every number appears within contents, and then append the frequency
    #to the list
    frequency = []
    for num in lotto_numbers:
        frequency_count = contents.count(num)
        frequency.append(frequency_count)
    
    #return the list to the main function
    return frequency, lotto_numbers