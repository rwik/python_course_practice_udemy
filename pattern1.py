#!/usr/bin/env python3
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

count = 5
for i in range(count):
    for j in range(i):
        print("*",end = "") #end = "" disables newline
    print("")    
print("*****")
for i in range(count,0,-1):#range([start,] stop [, step]) -> range object
    for j in range(i):
        print("*",end = "") #end = "" disables newline
    print("") 
