'''
Created on 29/03/2016

@author: Nick
'''

"""
Calculate the total cost of tile it would take to cover a floor plan of
width and height, using a cost entered by the user.
"""

currency = raw_input("Enter the currency")
cost = float(input("Enter cost per tile: "))
width = float(input("Enter width of room: "))
height = float(input("Enter height of room: "))

totalCost = lambda w,h,c: w*h*c

print ("Total cost to tile is " + currency + str(totalCost(width,height,cost)))
