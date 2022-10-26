# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 08:37:15 2022

@author: TOBBY
"""

#write a program to return fizz is it is divisible by 3
# buzz if divisible by 5
#fizzbuzz if divisible by both 5 and 3

def FizzBuzz(input):
    if input % 5 == 0 and input % 3 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input
print(FizzBuzz())