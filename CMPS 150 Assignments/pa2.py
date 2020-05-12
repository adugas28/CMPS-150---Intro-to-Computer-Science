# Author:           Austin Dugas
# ULID:             C00231110
# Course/Section:   CMPS 150 - Lecture Section # 003
# Assignment:       pa2
# Date Assigned:    Thursday, September 19, 2019
# Date/Time Due:    Tuesday, September 24, 2019
#
# Description:      Ask for 2 sets of data.
#                   Each set of data will have a user name and their pet's weight.
#                   Calculate the amount of antibiotic needed for their pet.
#                   Produce a table of formatted output.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# Ask the user for inputs
print()
client1 = input("Enter client #1: ")
petWeight1 = eval(input("Enter pet weight: "))
print()
client2 = input("Enter client #2: ")
petWeight2 = eval(input("Enter pet weight: "))

# Calculate the pill dosage needed for each pet
petWeight1 = int(petWeight1)
petWeight2 = int(petWeight2)
pillDosage1 = petWeight1 * 10
pillDosage2 = petWeight2 * 10

# Calculate the liquid dosage needed for each pet
liqDosage1 = (pillDosage1 / 250) * 5
liqDosage2 = (pillDosage2 / 250) * 5

# Print output
print()
print()
print("Client       Pet Weight    Dosage (ml)")
print("--------------------------------------")
print(format(client1, '12s'),format(petWeight1, '10d'), format(liqDosage1, '9.3f'))
print(format(client2, '12s'),format(petWeight2, '10d'), format(liqDosage2, '9.3f'))
