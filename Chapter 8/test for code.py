#Code Decoder
alpha='abcdefghijklmnopqrstuvwxyz'
code=input('Code: ').lower()
decoded=''
for letter in code:
    try:
        ind=alpha.index(letter)
        new_ind=alpha[(ind+10)]
    except IndexError:
        new_ind=alpha[((ind+10)-26)]
    except:
        new_ind=letter
    decoded+=new_ind
print(decoded.upper())
