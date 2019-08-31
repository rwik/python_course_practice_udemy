#!/usr/bin/env python3
#dict = {'a':2 ,'b':4}
#print(dict)

def print_arr(inp):
    dict = {}
    for n in inp:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(print_arr('google'))    