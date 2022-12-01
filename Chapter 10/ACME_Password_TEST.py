#Imports
#-----#
import pickle
import random

#-----#

def main():
    
    #Try to open the files and read them, if an Error occurs, create the files and exit
    try:
        infile = open('words.dat', 'rb')
    except:
        print('The file, words.dat, does not exist...')
    else:
        #Create the list of words
        words = pickle.load(infile)
        
        #Create a list for the three words
        random_words = []
        
        #Create a list for the colors of the rainbow
        rainbow_colors = ['red','orange','yellow','green','blue','purple']
        
        #Loop until there are proper values in the color_values list
        while True:
            
            #Create values for the colors
            color_values = [0,0,0,0,0,0]
            #Pick three random words and append them to the list
            for i in range(0,3):
                random_words.append(words[random.randint(0,len(words))])
                
            #Put the three random words into a single string
            string = '' #Create an empty string first
            for i in random_words:
                string+=i
                
            #For every letter in the string, find out if they match any of the first letters of the colors in the rainbow
            #If so, add an amount to the colors value
            for letter in string:
                for color in rainbow_colors:
                    if letter[0] == color[0]:
                        index = rainbow_colors.index(color)
                        color_values[index] += 1
            
            #Check to see if there are two maxes in the list, if so, repeat this process.
            color_values_sorted = list(sorted(color_values, reverse=True))
            if color_values_sorted[0] == color_values_sorted[1]:
                continue
            else:
                break
        
        #Find out where the maximum value is at in the unsorted value list
        color = rainbow_colors[color_values[color_values_sorted[0]]]
        
        print(color)