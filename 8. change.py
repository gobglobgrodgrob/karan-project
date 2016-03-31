'''
Created on 29/03/2016

@author: Nick
'''

""" The user enters a cost and then the amount of money given. The
program will figure out the change and the number of quarters, dimes,
nickels, pennies needed for the change.
"""

cost = float(input("Enter the cost of the item "))
money = float(input("Enter the amount of money given "))

change = money-cost

q=0
d=0
n=0
p=0

while int(change) >= 1:
    change -= 1
while round(change,1) >= 0.25:
    change -= 0.25
    q += 1
while 0.10 < round(change,2) <= 0.25:
    change -= 0.10
    d += 1
while 0.05 <= round(change,2) <= 0.10:
    change -= 0.05
    n += 1
while 0.01 <= round(change,2) < 0.05:
    change -= 0.01
    p += 1
print "Total change is " + str(q) + " quarters " + str(d) + " dimes " + str(n) + " nickles and " + str(p) + " pennies."
