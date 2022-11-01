

def gas_prices(): #Exercise 14
    #gas prices 1 accepts no arguments
    #it will call on the function gas_prices_info(),
    #gain information from it, then it will find the
    #average gas price for each year, the
    #highest and lowest price for each year,
    #the prices from highest to lowest, and
    #the prices from lowest to highest.
    #There will be FOUR outputs
    
    #call for the function, gas_prices_info
    average_prices, lowest_prices, highest_prices = gas_prices_info()
    
    #Print the average prices
    year = 1993
    for price in average_prices:
        print(f'The average price in {year} was {price}.')
        year += 1
    print()
    
    for msg in lowest_prices:
        print(msg)
        
    print()
    for msg in highest_prices:
        print(msg)
    
        
    #Print the highest to lowest prices
    
def gas_prices_info(): #For Exercise 14
    #gas prices info accepts no arguments
    #it will pull information from the file,
    #GasPrices.txt
    
    #open the file
    infile = open('GasPrices.txt', 'r')
    
    #Create a two dimensional list that will contain all the years
    gasprices_in_years = [[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']]
    gasprices_unsorted = [''] #WON'T BE SORTED
    lowest_to_highest = ['']
    highest_to_lowest = ['']
    dates_unsorted = ['']
    
    #Create two accumulators, read the first line in the file, have a while loop
    #and add each price to their respective variable
    current_year = 1993
    year = 0
    line = infile.readline()
    while line != '':
        if line[6:9+1] == str(current_year):
            gasprices_in_years[year][0] += line[11:].replace('\n',' ') #LATER ON BE SURE TO ADD IN THE ANOTHER LIST THAT CONTAINS THE DATES
            dates_unsorted[0] += line[:10+1].replace(':',' ')
            gasprices_unsorted[0] += line[11:].replace('\n',' ') #Prices will not be sorted into years
            lowest_to_highest[0] += line[11:].replace('\n',' ')
            highest_to_lowest[0] += line[11:].replace('\n',' ')
            line = infile.readline()
        else:
            current_year += 1
            year += 1
    infile.close()
    
    #Reset one of the accumulators, and split all of the prices in their respective years in their respective years
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
    #loop for the total amount prices within the text file, and append the average
    #gas prices per year into the new list
    average_gasprices_in_years = []
    year = 0
    gas_price = 0
    total = 0

    while year < 21: #for i in range(0,1087): <-- ME
        try:
            total += float(gasprices_in_years[year][0][gas_price]) #THE YEAR 2013 IS NOT BEING READ
            gas_price += 1
        except:
            average = total/gas_price
            average_gasprices_in_years.append(format(average, '.2f'))
            year += 1
            gas_price = 0
            total = 0
            average = 0
            
    #HIGHEST AND LOWEST GAS PRICES
        
    #Create two empty lists for the highest and lowest gas prices per year. Have a loop and use max and min to find
    #the highest and lowest prices.
    highest_prices = []
    lowest_prices = []
    current_year = 1993
    for year in range(0,21):
        high_price = max(gasprices_in_years[year][0])
        low_price = min(gasprices_in_years[year][0])
        highest_prices.append(high_price)
        lowest_prices.append(low_price)
        #Add the year for each price
        highest_prices[year] = f'The highest price for {current_year} is: ' + highest_prices[year]
        lowest_prices[year] = f'The lowest price for {current_year} is: ' + lowest_prices[year]
        current_year += 1
        
    #LIST OF PRICES FROM LOWEST TO HIGHEST  
    
    infile = open('lowest_to_highest_gas_prices.txt', 'w')
    lowest_to_highest_prices = ['']
    lowest_to_highest.sort()
    for price in lowest_to_highest:
        price_index = gasprices_unsorted.index(price)
        date = dates_unsorted[price_index]
        lowest_to_highest_prices[0] += f'{date}:{price} '
    lowest_to_highest_prices = lowest_to_highest_prices[0].split()
    #Move the dates and their gas prices into a new list called, 'lowest_to_highest_gas_prices.txt'
    for line in lowest_to_highest_prices:
        infile.write(line + '\n')
    infile.close()
        
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
    
    #Return the listst that will be outputted by the main function
    return average_gasprices_in_years, lowest_prices, highest_prices