

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

gas_prices()