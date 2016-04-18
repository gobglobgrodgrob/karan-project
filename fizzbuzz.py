'''
Created on 17/04/2016

@author: Nick
'''

"""
Write a 
"""


def fizzbuzz():
    for i in range(1, 101):
        if i%3==0 and i%5==0:
            print "FizzBuzz"
        elif i%3!=0 and i%5==0:
            print "Buzz"
        elif i%3==0 and i%5!=0:
            print "Fizz"
        else:
            print i

if __name__ == "__main__":
    fizzbuzz()
