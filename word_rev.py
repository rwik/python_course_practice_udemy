#!/usr/bin/env python3
def rev_str(inp):
    str = ""
    length = len(inp)
    for i in range(length,0,-1):
        str = str + inp[i]
    return str    
str = input("Enter a string:")
print(rev_str(str))