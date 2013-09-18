# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\emacs\.spyder2\.temp.py
"""

# Problem 1

import sys

first = int(sys.argv[1])
last = int(sys.argv[2])

# Function for 3n+1
def collatz(n):
    array = []
    while n > 1:
        array.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n *= 3
            n += 1
    if n == 1:
        array.append(1)
        # print array
        return len(array)
    elif n < 1:
        print "Please type a positive integer!"
    else:
        print "Invalid input."        

# Function to create chain of numbers till n = 1
def user_collatz(a, b):
    max_length = collatz(a)
    for i in range(a,b+1):
        if max_length < collatz(i):
            max_length = collatz(i)
    print a, b, max_length

user_collatz(first, last)