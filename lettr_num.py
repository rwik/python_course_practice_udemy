#!/usr/bin/env python3
#finds number of letters and digits

inp = input("Enter key: ")
digit = 0
letter = 0 
for i in inp:
    if i.isdigit():
        digit+=1        
    elif i.isalpha():
        letter+=1
    else:
        pass
print("Letter = ",letter)
print("Digit = ",digit)        
