'''
Created on 14/04/2016

@author: Nick
'''

"""
Collatz Conjecture - Start with a number n > 1. Find the number of steps
it takes to reach one using the following process: If n is even, divide
it by 2. If n is odd, multiply it by 3 and add 1.
"""

def col(n, counter=0):
    assert type(n) == int and n >= 1
    while n != 1:       
        if n%2 == 0:
            n = n/2
            counter += 1

        elif n%2 == 1:
            n = (n*3) + 1
            counter += 1
    if n == 1:
        return counter
