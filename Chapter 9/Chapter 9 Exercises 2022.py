

def encrypting_code(): #Exercise 3
    #encrypting_code accepts no arguments
    #it will take contents from a file, convert them to
    #the symbol representing each character from the contents
    #and then move those contents into another file
    
    #Create a dictionary for uppercase letter, numbers, and symbols
    code_upper = {'A':'B','B':'C','C':'D','D':'E','E':'F','F':'G','G':'H','H':'I','I':'J','J':'K','K':'L','L':'M',
            'M':'N','N':'O','O':'P','P':'Q','Q':'R','R':'S','S':'T','T':'U','U':'V','V':'W','W':'X','X':'Y','Y':'Z','Z':'A',
                  '1':'2','2':'3','3':'4','4':'5','5':'6','6':'7','7':'8','8':'9','9':'0','0':'1',
                  '!':'@','@':'#','#':'$','$':'%','%':'^','^':'&','&':'*','*':'(','(':')',')':'!',
                  '`':'~','~':"`",',':'<','<':',','.':">",">":',','/':'?','?':'/',';':":",":":';',"'":'"','"':"'",
                  '[':"{","{":'[',']':"}","}":']','-':"_","_":'-','=':"+","+":'='
            }
    code={} #Create a dictionary to add in lowercase letters
    for key in code_upper: #Have a for loop to add everything to a single dictionary
        value = code_upper[key]
        code[key] = value
        if key.isalnum():
            code[key.lower()] = value.lower()
    
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
    
    #Take everything from wtihin the file and concatenate it to contents, then close the file and open the encryption file
    for line in infile:
        contents+=line
    infile.close()
    infile = open('Encrypted_Version','w')
    
    #temporily change the new lines in the contents.
    #print(contents)
    #contents = contents.replace('\n','|')
    #print(contents)
    
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
        
    #Move the encrypted content into the file, Encrypted_Version
    infile.write(encrypted_contents)
    
    #Close the file
    infile.close()
    
def test_file():
    #test file accepts no arguments
    #it will let the user create a file
    
    #Rewrite or create a file
    file = input('What would you like to call the file? ')
    
    infile = open(file,'w')
    
    #Prompt the user what they would like to be inside the file
    contents = input('What message would you like to put in the file? ')
    
    infile.write(contents)
    
    infile.close()