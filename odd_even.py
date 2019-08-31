#!/usr/bin/env python3
num_set = [1,2,3,4,5,6,7,8,9,0,66]
odd = even = 0
for i in num_set:
    if (i%2 != 0):
        odd=odd+1
    else:
        even=even+1
print("odd= ",odd)
print("even= ",even)

