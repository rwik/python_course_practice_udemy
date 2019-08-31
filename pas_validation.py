#!/usr/bin/env python3
import re 
#regex lib
pwd = (input("Enter your pass: "))

if (len(pwd)>8 and re.search("[a-z]",pwd) and re.search("[A-Z]",pwd)):
    print("valid pass")
else:
    print("Invalid pass")    