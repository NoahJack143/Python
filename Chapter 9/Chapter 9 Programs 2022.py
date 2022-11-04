import pickle

#Dictionaries
#Sets
#Serializing Objects

#dictionary = {key1:val1, key2:val2}

#phonebook['Jenny'] = '8675309' #Adds another key and value

#for key in phonebook:
    #print(key)
#will print every key

#for key in phonebook:
    #print(phonebook[key])
#will print the value for each key

#phonebook.clear() #Clears the phonebook

def write_main(): #Program 9-4
    #pickle_main accepts no arguments
    #it opens the file info.dat for binary writing
    #i loops and calls save_data to prompt the user for information
    #to add user data to a dictionary
    #and prompts the user to continue
    
    #primt the loop
    again = 'y'
    
    #open the file for binary writing
    outfile = open('info.dat', 'wb')
    
    #loop to get data until the user wants to stop
    while again.lower() == 'y':
        #get and save data
        save_data(outfile)
        
        #prmopt the user to continue
        again = input("Enter more data: (y/n: ")
    
    #data entry finished, close the file
    outfile.close()

def read_main():#Program 9-5
    #ead main accepts no arguments
    #it opens info.dat as a binary read file
    #it loops to the end of the file and unpickles the data
    
    #primt the loop
    end_of_file = False
    
    #open the file
    infile = open('info.dat','rb')
    
    #loop to the end of the file
    while not end_of_file:
        try:
            #unpickle and display the next object
            person = pickle.load(infile)
            display_data(person)
        except EOFError:
            #end of the file error reached, change the loop flag
            end_of_file = True
            
    #All datae, read close the file
    infile.close()
    
def display_data(person):
    #display data accepts person as a dictionary unpickled from the file
    #it displyas the information for that person
    
    print('Name: ',person['name'])
    print('Age: ', person['age'])
    print('Weight: ', person['weight'])
    
def save_data(file):
    #save data accepts fie as an argument
    #it creates an empty dictionary and prompts the user for inforattion
    #to add keys/values for name, age, and weight
    #it pickles the data to write to info.dat
    
    #Create an empty dicitonary
    person = {}
    
    #get data for name, age, weight, and pickle the data
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))
    
    #pickle the dictionary
    pickle.dump(person, file)