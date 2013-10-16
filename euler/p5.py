"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from sys import maxint

def is_divisible(x):
    'is divisible by numbers from 1 to 20'
    for i in range(1, 21):
        if x % i != 0:
            return False
    return True

def p():
    for x in xrange(1, maxint):
        if is_divisible(x):
            return x
    return -1

print p()