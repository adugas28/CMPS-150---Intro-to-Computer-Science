# Author:           Austin Dugas         
# ULID:             C00231110
# Course/Section:   CMPS 150 - Section 003
# Assignment:       pa1
# Date Assigned:    Wednesday, September 11, 2019
# Date/Time Due:    Sunday, September 15, 2019 -- 11:55 pm
#
# Description:      This program will return on an investment.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# Ask user for input
name = input("Enter your name: ")
billAmount = eval(input("Enter your bill amount (i.e. a restaurant bill): "))
gratuity = eval(input("Enter your gratuity percentage (i.e. 20): "))

# Calculate the subtotal of the bill
tax = .085
subTotal = (billAmount * tax) + billAmount

# Calculate the gratuity for the bill
newGratuity = subTotal * (gratuity / 100)

# Calculate the final total
total = subTotal + newGratuity

#Print output
print()
print("-------------------------------------------")
print("Report for", name)
print("-------------------------------------------")
print("Charges: ", billAmount)
print("Tax:     ", tax * 100)
print("Gratuity:", newGratuity)
print("Total:   ", total)


                  
