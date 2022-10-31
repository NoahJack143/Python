

def gas_prices1(): #Exercise 14 Part 1
    #gas prices 1 accepts no arguments
    #it will call on the function gas_prices_info(),
    #gain information from it, then it will find the
    #average gas price for each year, the
    #highest and lowest price for each year,
    #the prices from highest to lowest, and
    #the prices from lowest to highest.
    #There will be FOUR outputs
    
    #call for the function, gas_prices_info
    print('hi')
    
def gas_prices_info(): #For Exercise 14
    #gas prices info accepts no arguments
    #it will pull information from the file,
    #GasPrices.txt
    
    #open the file
    infile = open('GasPrices.txt', 'r')
    
    #Create a two dimensional list that will contain all the years
    gasprices_in_years = [[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']]
    
    #Create two accumulators, read the first line in the file, have a while loop
    #and add each price to their respective variable
    current_year = 1993
    year = 0
    line = infile.readline()
    while line != '':
        if line[6:9+1] == str(current_year):
            gasprices_in_years[year][0] += line[11:].replace('\n',' ') #LATER ON BE SURE TO ADD IN THE ANOTHER LIST THAT CONTAINS THE DATES
            line = infile.readline()
        else:
            current_year += 1
            year += 1
    
    #Reset one of the accumulators, and split all of the prices in their respective years
    year = 0
    for prices in gasprices_in_years:
        gasprices_in_years[year][0] = gasprices_in_years[year][0].split()
        year += 1
        
    #AVERAGE GAS PRICES
        
    #Create an empty list for the avg of the gas prices per year, create 3 accumulators
    #loop for the total amount prices within the text file, and append the average
    #gas prices per year into the new list
    average_gasprices_in_years = []
    year = 0
    gas_price = 0
    total = 0
    for i in range(1,1065):
        try:
            total += float(gasprices_in_years[year][0][gas_price])
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
    for year in range(0,19):
        high_price = max(gasprices_in_years[year][0])
        low_price = min(gasprices_in_years[year][0])
        highest_prices.append(high_price)
        lowest_prices.append(low_price)
    
    for i in range(0,19):
        date = gasprices_in_years[i][0].index(highest_prices[i])
        print(date)
            
        
        
        
        
gas_prices_info()