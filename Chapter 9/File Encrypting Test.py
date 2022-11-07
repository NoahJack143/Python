def encrypting_code(): #Exercise 3
    #encrypting_code accepts no arguments
    #it will take contents from a file, convert them to
    #the symbol representing each character from the contents
    #and then move those contents into another file
    
    #Create a dictionary for uppercase letter, numbers, and symbols
    code = {}
    num = 160
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    other = '''`1234567890-=~!@#$%^&*()_+,./<>?;':"[]{}|'''
    for i in range(0,3):
        if i == 1:
            alphabet = alphabet.upper()
        for letter in alphabet:
            code[letter] = chr(num)
            num += 1
        if i == 2:
            for letter in other:
                code[letter] = chr(num)
                num += 1
    
    #Prompt the user for a file to be opened. Validation will be included for this
    while True:
        file = input('Which file would you like to open? ')
        try:
            infile = open(file,'r')
        except:
            print('\nPlease open a file that exists.\n')
        else:
            break
    
    #Create a string for the contens from within the file
    contents = ''
    
    #Take everything from within the file and concatenate it to contents, then close the file and open the encryption file
    for line in infile:
        contents+=line
    infile.close()
    infile = open('Encrypted_Version','w')

    #Create a new string for the encrypted contents
    encrypted_contents = ''
    next_char = 0

    #Have a for loop and move the newly encrypted contentes to the string, encrypted_contents
    for char in range(len(contents)):
        if next_char != 1:
            old_value = contents[char]
            new_value = code.get(old_value,'00')
            if new_value == '00':
                if old_value == ' ': #This will run if the old_value is a ' '
                    encrypted_contents+=old_value
                else:
                    try:
                        if contents[char+1] == 'n': #This will run if the '\' is with an 'n'
                            encrypted_contents+='\n'
                            next_char = 1 #Skip the letter 'n' in order to not have extra code
                        else:
                            encrypted_contents+=old_value #This will run if the '\' is without an 'n'
                    except:
                        encrypted_contents+=old_value #This part will run if the '\' is at the end of contents
            else:
                encrypted_contents+=new_value #This will add the new value to encrypted_contents if the old_value isn't '\' or ' '
        else:
            next_char = 0
        
    #Move the encrypted content into the file, Encrypted_Version, and close the file
    infile.write(encrypted_contents)
    infile.close()
    
    #Tell the user that the contents have been put into the file
    print(f'\nThe contents from the file, {file}, have been encrypted and put into the file, Encrypted_Version')

def decrypting_code(): #For Exercise 3
    #decrypting code accepts no arguments
    #it will read the specific file created by
    #encrypting_code(), and decrypt the contents
    #from within the file
    
    #Create the same dictionary from the main function
    code = {}
    num = 160
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    other = '''`1234567890-=~!@#$%^&*()_+,./<>?;':"[]{}|'''
    for i in range(0,3):
        if i == 1:
            alphabet = alphabet.upper()
        for letter in alphabet:
            code[letter] = chr(num)
            num += 1
        if i == 2:
            for letter in other:
                code[letter] = chr(num)
                num += 1
    new_code = {}
    for character in code:
        value = code[character]
        new_code[value] = character
    
    
    #Open the file from the ecrypting_code() function
    infile = open('Encrypted_Version','r')
    
    #Create a string for the contens from within the file
    contents = ''
    
    #Take everything from within the file and concatenate it to contents, then close the file
    for line in infile:
        contents+=line
    infile.close()
    
    #Create a new string for the decrypted contents
    decrypted_contents = ''
    next_char = 0

    #Have a for loop and move the decrypted contentes to the string, decrypted_contents
    for char in range(len(contents)):
        if next_char != 1:
            old_value = contents[char]
            new_value = new_code.get(old_value,'00')
            if new_value == '00':
                if old_value == ' ': #This will run if the old_value is a ' '
                    decrypted_contents+=old_value
                else:
                    try:
                        if contents[char+1] == 'n': #This will run if the '\' is with an 'n'
                            decrypted_contents+='\n'
                            next_char = 1 #Skip the letter 'n' in order to not have extra code
                        else:
                            decrypted_contents+=old_value #This will run if the '\' is without an 'n'
                    except:
                        decrypted_contents+=old_value #This part will run if the '\' is at the end of contents
            else:
                decrypted_contents+=new_value #This will add the new value to decrypted_contents if the old_value isn't '\' or ' '
        else:
            next_char = 0
    
    #Print the decrypted_contents for the user
    print('Here is the decrypted message.\n')
    print(decrypted_contents)