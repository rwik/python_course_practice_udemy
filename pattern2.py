#!/usr/bin/env python3
print("Print alphabets ")
lastNumber = 6
asciiNumber = 65
for i in range(0, lastNumber):
    for j in range(0, i+1):
        character  = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber+=1
    print(" ")