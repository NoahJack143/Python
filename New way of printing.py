def valid():
    manufact = input('Enter a phone manufacturer: ')
    model = input('Enter a phone model: ')
    price = input('ENter a price: ')
    valid = False
    while not valid:
        try:
            price = float(price)
            valid = True
        except:
            valid = False
            print('Be a try hard. Try again')
            prince = input('Enter a price: ')
            
    print('You have a', manufact, 'model', model, 'that retails for ' + str(price) + '.')
    #f' stands for format #{} finds that variable #f' is called an f string
    print(f"You have a {manufact} model {model} that retails for ${price}.") #Python under 3.6 won't be able to run this

