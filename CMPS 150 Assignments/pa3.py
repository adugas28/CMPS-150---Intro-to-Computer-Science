# Author:           Austin Dugas
# ULID:             C00231110
# Course/Section:   CMPS 150 - 003
# Assignment:       pa3
# Date Assigned:    Thursday, September 27, 2019
# Date/Time Due:    Tuesday, October 1, 2019 -- 11:55 pm
#
# Description:      Ask user for 3 sets of data.
#                   Each set of data will have a package type and weight.
#                   Calculate the cost for the shipping packages.
#                   Produce a table of formatted output.
#
# Certification of Authenticity:
# I certify that this assignemt is entirely my own work.

# Ask the use for package type and weight
packageType1 = input("Enter package #1 type - N (non-perishable) or P (perishable): ")
packageWeight1 = eval(input("Enter package #1 weight: "))
print()
packageType2 = input("Enter package #2 type - N (non-perishable) or P (perishable): ")
packageWeight2 = eval(input("Enter package #2 weight: "))
print()
packageType3 = input("Enter package #3 type - N (non-perishable) or P (perishable): ")
packageWeight3 = eval(input("Enter package #3 weight: "))
print()

# Set conditions for caculations
if packageType1 == "P":
    if packageWeight1 > 8:
        cost1 = 5.95 + 19.95
    elif packageWeight1 <= 8 and packageWeight1 > 5:
        cost1 = 5.95 + 9.95
    elif packageWeight1 <= 5 and packageWeight1 > 2:
        cost1 = 5.95 + 5.95
    elif packageWeight1 <= 2 and packageWeight1 >= 0:
        cost1 = 5.95 + 2.95
    else:
        print("NA")
elif packageType1 == "N":
    if packageWeight1 > 8:
        cost1 = 1.95 + 9.95
    elif packageWeight1 <= 8 and packageWeight1 > 5:
        cost1 = 1.95 + 7.95
    elif packageWeight1 <= 5 and packageWeight1 > 2:
        cost1 = 1.95 + 3.95
    elif packageWeight1 <= 2 and packageWeight1 >= 0:
        cost1 = 1.95 + 1.95
    else:
        print("NA")
else:
    print("Invalid input!")

if packageType2 == "P":
    if packageWeight2 > 8:
        cost2 = 5.95 + 19.95
    elif packageWeight2 <= 8 and packageWeight2 > 5:
        cost2 = 5.95 + 9.95
    elif packageWeight2 <= 5 and packageWeight2 > 2:
        cost2 = 5.95 + 5.95
    elif packageWeight2 <= 2 and packageWeight2 >= 0:
        cost2 = 5.95 + 2.95
    else:
        print("NA")
elif packageType2 == "N":
    if packageWeight2 > 8:
        cost2 = 1.95 + 9.95
    elif packageWeight2 <= 8 and packageWeight2 > 5:
        cost2 = 1.95 + 7.95
    elif packageWeight2 <= 5 and packageWeight2 > 2:
        cost2 = 1.95 + 3.95
    elif packageWeight2 <= 2 and packageWeight2 >= 0:
        cost2 = 1.95 + 1.95
    else:
        print("NA")
else:
    print("Invalid input!")

if packageType3 == "P":
    if packageWeight3 > 8:
        cost3 = 5.95 + 19.95
    elif packageWeight3 <= 8 and packageWeight3 > 5:
        cost3 = 5.95 + 9.95
    elif packageWeight3 <= 5 and packageWeight3 > 2:
        cost3 = 5.95 + 5.95
    elif packageWeight3 <= 2 and packageWeight3 >= 0:
        cost3 = 5.95 + 2.95
    else:
        print("NA")
elif packageType3 == "N":
    if packageWeight3 > 8:
        cost3 = 1.95 + 9.95
    elif packageWeight3 <= 8 and packageWeight3 > 5:
        cost3 = 1.95 + 7.95
    elif packageWeight3 <= 5 and packageWeight3 > 2:
        cost3 = 1.95 + 3.95
    elif packageWeight3 <= 2 and packageWeight3 >= 0:
        cost3 = 1.95 + 1.95
    else:
        print("NA")
else:
    print("Invalid input!")

# Set conditions for package type output
if packageType1 == "N":
    packageType1 = "Non-Perishable"
else:
    packageType1 = "Perishable"

if packageType2 == "N":
    packageType2 = "Non-Perishable"
else:
    packageType2 = "Perishable"

if packageType3 == "N":
    packageType3 = "Non-Perishable"
else:
    packageType3 = "Perishable"

# Print output
print("Package Type        Weight      Shipping Charge")
print("-----------------------------------------------")
print(format(packageType1, '14s'), format(packageWeight1, '10.2f'), format(cost1, '16.2f'))
print(format(packageType2, '14s'), format(packageWeight2, '10.2f'), format(cost2, '16.2f'))
print(format(packageType3, '14s'), format(packageWeight3, '10.2f'), format(cost3, '16.2f'))
