# Author:         Austin Dugas 
# ULID/Section:   C00231110/003
# Lab #13

import random 
class Car:
   def __init__(self, symbolIn):
      self.__location = 0
      self.__symbol = symbolIn

   def GetLocation(self):
      return self.__location

   def GetSymbol(self):
      return self.__symbol

   def MoveCar(self):
      self.__location = self.__location + random.randint(1,5)   

   def DisplayCar(self):
      if (self.__location > 0):
         for i in range(self.__location):
            print('*',end="")
         print("|",self.__symbol)
      else:
         print("|",self.__symbol)    

def main():
    infile = open("lab13_data.py",'r')

    # create an empty list
    carList = []

    # read a symbol from the data file and strip it
    symbol = infile.readline().strip()

    # begin a sentinel-controlled loop based on the input NOT being "###"
    while symbol != "#":

        # create a car object using the symbol read from the file
        newCar = Car(symbol)

        # append the car object to the car list
        carList.append(newCar)

        # read the next symbol from the data file and strip it
        symbol = infile.readline().strip()

        
    # "race" the cars in the list ... five(5) times
    for i in range(5):
        # for each repetition of 'i' move and display each car object
        for i in range(len(carList)):
            carList[i].MoveCar()
            carList[i].DisplayCar()
        # between each race, print a blank line
        # this is to "visually" recognize where each of the 5 races begins/ends
        print()


    # finally, find a winner amongst the cars in the list of car objects
    # you may assume there are NO ties
    maxLocation = carList[0].GetLocation()
    indexOfMax = 0

    for i in range(len(carList)):
        if carList[i].GetLocation() > maxLocation:
            # fill in here the items that need to be updated
            # HINT:  same two variable set above, maxLocation & indexOfMax
            maxLocation = carList[i].GetLocation()
            indexOfMax = i

           
    print("Winner: ", carList[indexOfMax].GetSymbol())


main()   
