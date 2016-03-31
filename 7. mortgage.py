'''
Created on 29/03/2016

@author: Nick
'''

""" Calculate the monthly payments of a fixed term mortgage over given
Nth terms at a given interest rate. Also figure out how long it will
take the user to pay back the loan. For added complexity, add an option
for users to select the compounding interval (Monthly, Weekly, Daily,
Continually).
"""

term = int(input("Enter the term period in number of months: "))
rate = float(input("Enter the interest rate in %: "))
loan = float(input("Enter the loan amount: "))

monthly_rate = rate/1200
payment = (monthly_rate / (1 - (1 + monthly_rate)**(-term))) * loan

print "Monthly payments: " + str(round(payment, 2))
