# Author:           Austin Dugas
# ULID:             C00231110
# Course/Section:   CMPS 150 - Lecture Section #3
# Assignment:       pa7
# Date Assigned:    Friday, November 15, 2019
# Date/Time Due:    Thursday, November 21, 2019 -- 11:55 pm
#
# Description:      Read data from a file until card string is "EXIT"
#                   Name of the data file is "cards.py"
#                   Each set of data is a single line of string data.
#                   Produce a table of formatted output as seen in the sample output.
#                   Follow the table with the list of invalid cards.
#                   Function requirements are specified below.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# This function checks the beginning value of the string
def Beginning(card):
    if card[0] == "4":
        return "V"
    elif card[0] == "5":
        return "M"
    elif card[0] == "3" and card[1] == "7":
        return "A"
    elif card[0] == "6":
        return "D"
    else:
        return "I"

# The print functions
def PrintHeader():
    print("Card Number          Card Type          Chars")
    print("---------------------------------------------")

def PrintEnd(listInvalid):
    print("---------------------------------------------")
    print()
    print("List of Invalid Strings")
    print("---------------------------------------------")
    print(listInvalid)

def PrintBody(listVisa, listMC, listAE, listDiscover):
    for i in range(0,len(listAE)):
        print(format(listAE[i],'16s'), "    American Express",
              format(len(listAE[i]),'4d'))
    for i in range(0,len(listDiscover)):
        print(format(listDiscover[i],'16s'), "    Discover",
              format(len(listDiscover[i]),'12d'))
    for i in range(0,len(listMC)):
        print(format(listMC[i],'16s'), "    MasterCard",
              format(len(listMC[i]),'10d'))
    for i in range(0,len(listVisa)):
        print(format(listVisa[i],'16s'), "    Visa",
              format(len(listVisa[i]),'16d'))

# The main function
def main():
    # Open file
    infile = open("cards.py",'r')

    # Read file
    card = infile.readline().strip()

    # Create empty lists
    listInvalid = []
    listVisa = []
    listMC = []
    listAE = []
    listDiscover = []

    # Create Boolean variable
    x = True

    # Call the function that prints the header
    PrintHeader()

    # Loop through the file
    while card != "EXIT":

        # Call the function that checks the brand of the string
        brand = Beginning(card)

        # Check all conditions for validity of card and append appropriate lists
        if brand == "V" and len(card) >= 10 and len(card) <= 16 and card.isdigit() == True:
            listVisa.append(card)
            x = True
        elif brand == "M" and len(card) >= 10 and len(card) <= 16 and card.isdigit() == True:
            listMC.append(card)
            x = True
        elif brand == "A" and len(card) >= 10 and len(card) <= 16 and card.isdigit() == True:
            listAE.append(card)
            x = True
        elif brand == "D" and len(card) >= 10 and len(card) <= 16 and card.isdigit() == True:
            listDiscover.append(card)
            x = True
        else:
            x = False

        # Append the invalid list
        if x == False:
            listInvalid.append(card)

        # Read the next string
        card = infile.readline().strip()

    # Call the function to print the main body
    PrintBody(listVisa, listMC, listAE, listDiscover)

    # Call the end print function
    PrintEnd(listInvalid)

    # Close the file
    infile.close()

# Call the main function
main()
    
    
