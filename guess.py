#!/usr/bin/env python3
import random
number = random.randint(1,10)
guess = ""
while guess != -1:
    guess = (int(input("Your guess= ")))
    if(guess == number):
        print("corect")
        break
    elif (guess<number):
        print("lesser")
    elif (number == -1):
        break
    else:
        print("higher")