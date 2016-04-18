'''
Created on 17/04/2016

@author: Nick
'''

"""

"""



def count_vowels(string):
    vowels = "aeiou"
    count = 0
    found = []
    for i in string:
        if i in vowels:
            count += 1
            found.append(i)
    print "Number of vowels in string = {}".format(count)
    print "Exact vowels found in string = {}".format(found)

string = raw_input("Enter a string ")

if __name__ == "__main__":
    count_vowels(string)
