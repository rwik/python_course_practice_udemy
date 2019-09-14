#!/usr/bin/env python3
import collections

#counter A Counter is a container that tracks how many times equivalent values are added

print(collections.Counter(['a','b','d','a','d']))

c = collections.Counter("abcdaab")
for letter in "abcde":
    print("%s : %d" % (letter, c[letter]))

#named Tuple
bob = ("Bob", 30, "male")
print ("Name :", bob) 

#Normal and ordered dictionary. In ordered dictionary it keeps track of insertion order.
dict1 = collections.OrderedDict()#{}
dict1["z"] = 12
dict1["a"] = 13

for key , value in dict1.items():
    print(key,value)

    