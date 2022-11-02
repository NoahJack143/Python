#MAIN MENU FUNCTION
def m(): #MAIN MENU
    #m accepts no arguments
    #it will call other functions
    
    print('\n' * 100)
    print('MAIN MENU\n---------------\n'+
          '2) Sum of Digits\n3) '+
          'Date Converter\n4) Morse Code\n5) '+
          'Telephone Number Translator\n6) '+
          'Average Number of Words\n12) '+
          'Igplay Atinlay\n13) '+
          'Powerball Lottery\n14) '+
          'Gas Prices\n---------------')
    
    #Prompt the user for an main function to call
    try:
        ui = int(input('Which main function would you like to call? '))
    except:
        print('Enter a number...')
    else:
        print('\n' * 100)
        
        #Check to see if the user input is any of the option
        if ui == 2:
            sum_of_digits()
        elif ui == 3:
            date_converter()
        elif ui == 4:
            morse_code()
        elif ui == 5:
            phone_converter()
        elif ui == 6:
            avg_num_words()
        elif ui == 12:
            igpay_atinlay()
        elif ui == 13:
            pb_main()
        elif ui == 14:
            gas_prices()
        else:
            print('Please choose an option from the table.')
    

#====Imports=====#

#==========#

def sum_of_digits(): #Exercsise 2
    #sum of digits accepts no arguments
    #it will ask the user to enter a series of single digit numbers
    #it will then output the sum of the single digit numbers
    #validating will be used for the user input
    
    #Prompt the user for a series of single digit numbers without spaces
    ui = input('Enter a series of single digit numbers without spaces: ')
    
    #Create a boolean if needed variable and a checker
    if not ui.isdigit() or ui.isspace():
        cont = False
    else:
        cont = True
            
    #Check if needed
    while not cont:
        ui = input('Enter a series of single digit numbers WITHOUT spaces or letters.')
        
        #Check again
        if not ui.isdigit() or ui.isspace():
            cont = False
        else:
            cont = True
        
    #Get the sum of the numbers
    c = 0
    for number in ui:
        c += int(number)
    
    #Print the output
    print('The sum of your string is:', c)
    
#================================================================================#
    
def date_converter(): #Exercise 3
    #date converter accepts no arguments
    #it will read a string in the format of 01/02/2007 and
    #will output the date if the string is formatted correctly
    
    #List of dates and days
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                   'September', 'October', 'November', 'December']
    months = ['01','02','03','04','05','06','07','08','09','10','11','12'] #You could combine months and days into one list to make this shorter
    days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16',
            '17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    
    #Create a boolean variable and a while loop
    cont = False
    while not cont:
        
        #Try block
        try:
            
            #Ask the user for the date
            date = input('\nEnter a date in the format mm/dd/yyyy: ')
            
            #Check to see if the format is formatted correctly and split the date if so
            if date[:1].isdigit() and date[3:4].isdigit() and date[6:].isdigit() and date[2] == '/' and date[5] == '/':
                date_splitted = date.split('/')
            else:
                t = b
            
            #Check to see if the month, day, and year are all valid
            if date_splitted[0] in months and date_splitted[1] in days and len(date_splitted[2]) == 4:
                m = date_splitted[0]
                d = date_splitted[1]
                y = date_splitted[2]
            else:
                0/0
            
            #Check to see if the month and day and valid with each other
            if m == '02' and int(d) > 28:
                m += 1
            elif m =='04' or m == '06' or m == '09' or m == '11':
                if int(d) > 30:
                    m += 1
            
            #Check for the name of the month apply a name to m
            index = 0
            for month in months:
                if m == month:
                    m = month_names[index]
                else:
                    index += 1
            
        #If soemthing goes wrong, ask again and continue looping
        except NameError:
            print('\nCheck your formatting and make sure there are no letters.')
        except ZeroDivisionError:
            print('\nMake sure you month number and day number are actual month and day numbers.' +
                  '\nAlso make sure that your year has 4 digits.')
        except TypeError:
            print('\nMake sure that your day is appropriate according to your month.')
        #If something goes right, then print the outcome and stop looping
        else:
            print(f'\nThe date is: {m} {d}, {y}')
            cont = True
            
#================================================================================#
            
def morse_code(): #Exercise 4
    #morse code accepts no arguments
    #morse code will take input from the user and change
    #their message into morse code
    
    #Create lists for the morse code and create variables for the alphabet and numbers
    alphabet_list = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••', '--',
              '-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••']
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers_list = ['•----', '••---', '•••---', '••••-', '•••••', '-••••', '--•••', '---••', '----•', '-----']
    numbers = '1234567890'
    
    #Ask the user to input a message to be encoded
    message = input('Enter a mesage to encode to morse code: ')

    #Boolean variable and while loop to keep asking for a valid code
    cont = False
    while not cont:

        #try block
        try:
            
            #copy the message and then strip the old message
            message2 = message
            message = message.split()
            
            #Check to see if the message is valid
            for word in message:
                if word.isalnum():
                    t = 1
                else:
                    t = b
            
            #Check to see if the character is a number or letter and print the right morse code
            for letter in message2:
                if letter.isalpha():
                    index = alphabet.find(letter.lower())
                    morse_code = alphabet_list[index]
                    message2 = message2.replace(letter, morse_code + ' ')
                elif letter.isdigit():
                    index = numbers.find(letter)
                    morse_code = numbers_list[index]
                    message2 = message2.replace(letter, morse_code + ' ')
                elif letter == ' ':
                    message2 = message2.replace('  ', ' / ')
                else:
                    t = b
               
        #If something went wrong
        except NameError:
            message = input('Enter only numbers and letters: ')
        #If everything worked
        else:
            print(message2)
            cont = True
            
#================================================================================#
            
def phone_converter(): #Exercise 5
    #phone converter accepts no arguments
    #get input from thw user, convert the phone number, and output the convertted number
    #Create a two dimensional list with all of the letters and the alphabet
    numpad = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    #Boolean variable with while loop
    cont = False
    while not cont:
        #try block
        try:
            #Ask the user for a number and copy their message
            tpn = input('Enter a telephone number in the form of XXX-XXX-XXXX: ')
            #Check to see if the phone number is valid
            if tpn[:2+1].isalnum() and tpn[3] == '-' and tpn[4:6+1].isalnum() and tpn[7] == '-' and tpn[8:].isalnum() and len(tpn) == 12:
                t = 1
            else:
                t = b
            #Check for every character in the tpn and move on accordingly + Accumulator
            for character in tpn:
                index = 0
                for group in numpad:
                    if not character.isalpha():
                        break
                    elif character.lower() in group:
                        tpn = tpn.replace(character, str(index))
                        break
                    else:
                        index += 1      
        #Run the excepts after the loop is over
        except NameError:
            print('There is an issue with your input.')
        else: #If everything works, output the new phone number
            print('Here is your convereted telephone number:', tpn)
            cont = True
            
#================================================================================#
            
def avg_num_words(): #Exercise 6
    #avg num words accepts no arguments
    #it will read froma file and will calculate the total
    #number of words, total number of sentences, and average
    #number of words per sentence in the document
    #A WORD IS CONSIDERED ANYTHING SEPARATED BY A SPACE
    
    #create a try block
    try:
        
        #open the file
        file = 'text.txt'
        infile = open(file, 'r')
        
        #Put every thing from the file and put it into a list
        contents = ''
        for line in infile:
            contents += line
        
        #Split the text base on the new lines to find the amount of sentences
        sentences = contents.split('\n')
        
        #Find out how many sentences there are in total
        index_s = 0
        for sentence in sentences:
            index_s += 1
        
        #Split the text base on spaces to find out how many words there are
        contents = contents.replace('\n', ' ') #Take out the new lines
        words = contents.split(' ') #Split every single word by splitting the spaces
        
        #Find out how many words there are in total
        index_w = 0
        for word in words:
            index_w += 1
        
        #Calculate the average words per sentence
        average = index_w / index_s
    
    #If there is a problem, run the exception
    except:
        print('There was a problem with the file or the calculations')
    else:
        print('The file',file,'has',index_w,'words.\n' +
              'There are',index_s,'total sentences.\n' +
              'The average number of words per sentence is:',format(average, '.2f'))

#================================================================================#
        
def igpay_atinlay(): #Exercise 12             #ADD VALIDATION
    #igpya_atinlay accepts no arguments
    #it will convert english words into "Pig Latin"
    #it will output the user's message in "Pig Latin"
    
    #Get a message from the user
    message = input('Enter a message to convert to pig latin: ')
    
    cont = False #Boolean Variable
    while not cont: #Used to validate the user's input
        if message.isalpha():
            #Separate every word in the user's message
            message = message.split()
            
            #Create an empty list for the converted words
            new_message = []
            
            #Make a loop that will look at every word
            index = 1
            for word in message:
                word = word[1:].upper() + word[0].upper() + 'AY '
                new_message.append(word)
                
            #Print the new message
            print('\nHere is your new message in pig latin: ')
            for word in new_message:
                print(word, end='')
            cont = True
        else:
            message = input('\nOnly enter letters to be converted to pig latin: ')
        
#================================================================================#
        
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
    
    #Create an empty list, run a nested for loop, find the top ten highest frequencies the first time and then the top ten lowest frequencies,
    #then find the position of those frequencies in the frequency list, change their position to anythying so they aren't used again,
    #then use that as an index for the lotto_numbers list, and append the result to the frequencies list
    frequencies = []
    for loop in range(0,2):
        frequency_sort.reverse() #Reverse the list twice
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

#================================================================================#

def gas_prices(): #Exercise 14
    #gas prices 1 accepts no arguments
    #it will call on the function gas_prices_info(),
    #gain information from it, and then output the average
    #gas prices per year, the lowest price for each year
    #and the highest price for each year
    
    #call for the function, gas_prices_info
    average_prices, lowest_prices, highest_prices = gas_prices_info()
    
    #Print the average prices
    year = 1993
    for price in average_prices:
        print(f'The average price in {year} was {price}')
        year += 1
    print()
    
    #Print the lowest and the highest prices per year
    for msg in lowest_prices:
        print(msg)
    print()
    for msg in highest_prices:
        print(msg)
    
def gas_prices_info(): #For Exercise 14
    #gas prices info accepts no arguments
    #it will pull information from the file,
    #GasPrices.txt, find the average of the gas prices
    #per year, find the highest and lowest prices
    #for each year, create a file that sorts the
    #gas prices from lowest to highest, and it will
    #create a file that sorts the gas prices from
    #highest to lowest
    
    #open the file
    infile = open('GasPrices.txt', 'r')
    
    #Create a two dimensional list that will contain all the years and four other lists
    gasprices_in_years = [[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']] #WILL BE SORTED
    gasprices_unsorted = [''] #WON'T BE SORTED
    lowest_to_highest = [''] #WON'T BE SORTED
    highest_to_lowest = [''] #WON'T BE SORTED
    dates_unsorted = [''] #WON'T BE SORTED
    
    #Create two accumulators, read the first line in the file, have a while loop,
    #and add parts of the current line into all of the lists created so far
    current_year = 1993
    year = 0
    line = infile.readline()
    while line != '':
        if line[6:9+1] == str(current_year): #If there are any gas prices left to read in the current year
            gasprices_in_years[year][0] += line[11:].replace('\n',' ')
            dates_unsorted[0] += line[:10+1].replace(':',' ')
            gasprices_unsorted[0] += line[11:].replace('\n',' ')
            lowest_to_highest[0] += line[11:].replace('\n',' ')
            highest_to_lowest[0] += line[11:].replace('\n',' ')
            line = infile.readline() #Read the next line in the file
        else: #If there are no more gas prices left to be read in the current year
            current_year += 1 #Increase the current year to check its gas prices
            year += 1 #Move to the next year in the list gasprices_in_years
    infile.close()
    
    #Reset one of the accumulators, and split all of the prices in their respective years. Split the other lists as well
    year = 0
    for prices in gasprices_in_years:
        gasprices_in_years[year][0] = gasprices_in_years[year][0].split()
        year += 1
    dates_unsorted = dates_unsorted[0].split()
    gasprices_unsorted = gasprices_unsorted[0].split()
    lowest_to_highest = lowest_to_highest[0].split()
    highest_to_lowest = highest_to_lowest[0].split()
        
    #AVERAGE GAS PRICES
        
    #Create an empty list for the avg of the gas prices per year, create 3 accumulators
    #loop for each of the years, and append the average to the list, average_gasprices_in_years
    #gas prices per year into the new list
    average_gasprices_in_years = [] #List for the averages
    year = 0 #Will tell the current year for the loop and the list, gasprices_in_years
    gas_price = 0 #Reads each gas price in the years
    total = 0

    while year < 21: #<-- Kyle #for i in range(0,1087): <-- ME
        try:
            total += float(gasprices_in_years[year][0][gas_price]) #THE YEAR 2013 IS NOT BEING READ
            gas_price += 1
        except:
            average = total/gas_price
            average_gasprices_in_years.append(format(average, '.2f')) #Append the average the newest list
            year += 1 #Increase the accumulator
            gas_price = 0 #Reset the accumulator
            total = 0 #Reset the accumulator
            average = 0 #Reset the average for the next year
            
    #HIGHEST AND LOWEST GAS PRICES
        
    #Create two empty lists for the highest and lowest gas prices per year. Have a loop and use max and min to find
    #the highest and lowest prices for each year
    highest_prices = []
    lowest_prices = []
    current_year = 1993
    for year in range(0,21): #Loop for all of the years
        high_price = max(gasprices_in_years[year][0])
        low_price = min(gasprices_in_years[year][0])
        highest_prices.append(high_price)
        lowest_prices.append(low_price)
        #Add the year for each lowest and highest price
        highest_prices[year] = f'The highest price for {current_year} is: ' + highest_prices[year]
        lowest_prices[year] = f'The lowest price for {current_year} is: ' + lowest_prices[year]
        current_year += 1
        
    #LIST OF PRICES FROM LOWEST TO HIGHEST  
    
    #Create or write in a file called, lowest_to_highest_gas_prices.txt, create an empty list for the
    #file that's being written in, sort the lowest_to_highest list that was created in the beginning(contains
    #unsorted prices), and loop for every price in the list, lowest_to_highest.
    infile = open('lowest_to_highest_gas_prices.txt', 'w')
    lowest_to_highest_prices = ['']
    lowest_to_highest.sort()
    for price in lowest_to_highest:
        price_index = gasprices_unsorted.index(price) #Find the index of the price in the list, gasprices_unsorted, and label it 'price_index'
        date = dates_unsorted[price_index] #Find the date in the list, dates_unsorted, using the previously found index, price_index
        lowest_to_highest_prices[0] += f'{date}:{price} ' #concatenate the formatted string and the text from within the newly created list
    lowest_to_highest_prices = lowest_to_highest_prices[0].split() #Split the information
    #Move the dates and their gas prices into a new list called, 'lowest_to_highest_gas_prices.txt'
    for line in lowest_to_highest_prices:
        infile.write(line + '\n')
    infile.close()
    
    #Do the same thing that was done for the lowest to highest prices, but instead find the highest to lowest prices
    #All the comments would appear to be the same for all of the steps excpet for the names of the created lists, the
    #new file, and the list used to sort the prices.
    infile = open('highest_to_lowest_gas_prices.txt', 'w')
    highest_to_lowest_prices = ['']
    highest_to_lowest.sort()
    highest_to_lowest.reverse()
    for price in highest_to_lowest:
        price_index = gasprices_unsorted.index(price)
        date = dates_unsorted[price_index]
        highest_to_lowest_prices[0] += f'{date}:{price} '
    highest_to_lowest_prices = highest_to_lowest_prices[0].split()
    #Move the dates and their gas prices into a new list called, 'lowest_to_highest_gas_prices.txt'
    for line in highest_to_lowest_prices:
        infile.write(line + '\n')
    infile.close()
    
    #Return the lists that will be outputted by the main function
    return average_gasprices_in_years, lowest_prices, highest_prices

m()