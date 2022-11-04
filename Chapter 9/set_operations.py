def so():
    #so2 accepts no arguments
    #this will be a shorter version of
    #so1
    
    #Collect all the message
    messages = ['\nThe following students are on the softball team:',
                '\nThe following students are on the basketball team:',
                '\nThe following students play both softball AND basketball:',
                '\nThe following students play either softball or basketball:',
                '\nThe following students play softball but not basketball:',
                '\nThe following students play basketball but not softball:',
                '\nThe following students play only one sport:']
    
    #Create two sets
    softball = set(['Jodi','Carmen','Aida','Alicia'])
    basketball = set(['Eva','Carmen','Alicia','Sarah'])
    
    #Create sets based on the two sets and the messages
    both_teams = softball & basketball
    either_teams = softball | basketball
    only_softball = softball - basketball
    only_basketball = basketball - softball
    only_one_sport = softball.symmetric_difference(basketball)
    
    #Create a list for each of the sets
    players = [softball, basketball,
               both_teams,either_teams,
               only_softball,only_basketball,
               only_one_sport]
    
    #Creat an accumulator, and create a nested for loop to print everything
    c=-1
    for msg in messages:
        c+=1
        print(msg)
        for name in players[c]:
            print(name)
            
so()