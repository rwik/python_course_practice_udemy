#!/usr/bin/env python3
import string as st
import re
import difflib

s ="some text"
print(s.capitalize())

#translate
transTable = str.maketrans("abegiloprstz", "463611092572")
#print(s.translate(transTable))

#Pattern matches
test = "jksadgfjksdgfkjsd"
key = "jk"
for match in re.findall(key,test):
    print(match)

#differnce in texts
strng1 = "I know him"
strng2 = "I don't know him"

d = difflib.Differ()
result = d.compare(strng1,strng2)
#print('\n'.join(list(result)))



