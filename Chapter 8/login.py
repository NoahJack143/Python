#This is a module for the Chapter 8 Programs 2022

def get_login_name(first, last, idnumber): #Program 8-3
    #get login name accpets arguments for first, last, and id number
    #it creates separate substrings of the FIRST 3 letters of both the first
    #nae and the last name and the LAST 3 letters of id number
    #it concatenates the srings in the order of first, last, id
    #and returns the newly generated login
    
    new_login = first[:2+1] + last[:2+1] + idnumber[-3:]
    
    return new_login

def valid_password(password): #Program 8-6
    #valid password accpets a string for password
    #it tests the following conditions
    #it password at least 7 characters
    #does password have at elsat one uppercase
    #does password have atleast one lowercase
    #does password have at elast one digit (numeric)
    #if the password meets all conditions is_valid is true
    #valid_password returns is_valid

    #Check or requirements and return True or False
    if password.islower() or password.isupper():
        return False
    if len(password) < 7:
        return False
    if password.isalpha():
        return False
    return True