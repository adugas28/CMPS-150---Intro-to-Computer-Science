# Author:           Austin Dugas
# ULID:             C00231110
# Course/Section:   CMPS 150 - Lecture Section #3
# Assignment:       pa9
# Date Assigned:    Monday, December 2, 2019
# Date/Time Due:    Saturday, December 7, 2019 -- 11:55 pm
# 
# Description:      Read data from a file and create a list of Dog objects using an
#                   existing class definition
#                   Display a menu of options and repeat until the user quits
#                   Process and display the dog records using the menu
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# *************************
# CLASS SECTION
# *************************

# The Dog class
class Dog ():
    def __init__(self, inName, inServ, inDays):
        # inServ = Boarding ($40 per day)
        # inServ = Grooming ($25 --> days set to 1)
        # inServ = Daycare ($16 per day)
        self.__name = inName
        self.__service = inServ
        self.__days = inDays

        if inServ == 'Boarding':
            self.__rate = 40
        elif inServ == 'Grooming':
            self.__rate = 25
        else:
            self.__rate = 16

    def GetName (self):
        return self.__name        

    def GetService (self):
        return self.__service

    def GetRate (self):
        return self.__rate

    def GetDays (self):
        return self.__days

    def GetBalance (self):
        return self.__rate * self.__days

# *************************
# FREE FUNCTION SECTION
# *************************

# The function that displays the menu
def DisplayMenu():
    print("*****************************************************")
    print("Welcome to Bow-Wow Boarding. Please choose an option:")
    print("*****************************************************")
    print("1. Add a dog and service")
    print("2. Display all dogs")
    print("3. Search for client and display balance")
    print("4. Quit")
    user = eval(input("Enter your selection: "))
    return user

# The function that displays the table of dogs
def PrintTable(dogList):
    count = 0
    balance = 0
    print()
    print()
    print("Name           Service      Days    Balance")
    print("-------------------------------------------")
    for i in range(len(dogList)):
        print(format(dogList[i].GetName(),'13s'), format(dogList[i].GetService(),'14s'),
              format(dogList[i].GetDays(),'1d'), format(dogList[i].GetBalance(),'10d'))
        count = count + 1
        balance = balance + dogList[i].GetBalance()
    print("-----------------------------------------------")
    print("Totals:", format(count,'7d'), "dogs                $", format(balance,'3d'))

# This function searches the list of dogs for the given name
def FindDog(dogList, nameSearch):
    index = -1
    for i in range(len(dogList)):
        if dogList[i].GetName() == nameSearch:
            index = i
        elif dogList[i].GetName() != nameSearch:
            continue
    return index

# This function prints the information of individual dog records
def PrintOneRecord(dogList,nameSearch):
    print("Record found:")
    print("----------------------")
    for i in range(len(dogList)):
        if dogList[i].GetName() == nameSearch:
            print("Name:", dogList[i].GetName())
            print("Service:", dogList[i].GetService())
            print("Days:", dogList[i].GetDays())
            print("Balance: $", dogList[i].GetBalance())

# *************************
# MAIN FUNCTION 
# *************************

# The main function
def main():

    # Open the file
    infile = open("DogRecords.py",'r')

    # Read the file
    dogName = infile.readline().strip()
    service = infile.readline().strip()
    days = eval(infile.readline())

    # Create an empty list
    dogList = []

    # Append the list
    while dogName != "DONE":
        dog = Dog(dogName, service, days)
        dogList.append(dog)

        # Read the next line in the file
        dogName = infile.readline().strip()
        service = infile.readline().strip()
        days = eval(infile.readline())

    # Close the file
    infile.close()

    # Call the function that displays the menu
    user = DisplayMenu()

    # Satisfy the user input
    while user != 4:
        if user == 1:
            # Ask the user for input
            newName = input("Enter dog's name: ")
            newService = input("Enter the service type (Boarding/Grooming/Daycare): ")

            # Grooming can only be one day
            if newService == "Grooming":
                newDays = 1
            else:
                newDays = eval(input("Enter num of days: "))

            # Create an object for the new dog
            newDog = Dog(newName, newService, newDays)

            # Append the dog list
            dogList.append(newDog)

            # Make a space in between the table when it repeats
            print()
            print()

            # Display the menu again
            user = DisplayMenu()

        elif user == 2:
            # Call the function to print the talbe of dogs
            PrintTable(dogList)

            # Make a space in between the table when it repeats
            print()
            print()

            # Display the menu again
            user = DisplayMenu()

        elif user == 3:
            # Ask the user for input
            nameSearch = input("Enter the name of the dog: ")

            # Call the function to search the list for the given dog name
            found = FindDog(dogList,nameSearch)

            # Process search result
            if found != -1:
                print()
                # Call the function that prints the record of dog requested
                PrintOneRecord(dogList,nameSearch)
            else:
                print()
                print("Sorry, we don't have a dog with that name.")

            # Make a space in between the table when it repeats
            print()
            print()

            # Display the menu again
            user = DisplayMenu()

        # Check for bad user input
        else:
            print()
            print("Invalid selection")

            # Make a space in between the table when it repeats
            print()
            print()

            # Display the menu again
            user = DisplayMenu()

    # End the program if 'quit' is selected
    if user == 4:
        print()
        print("****************************")
        print("Thank you for your business.")
        print("****************************")
            
# Call the main function
main()





    
