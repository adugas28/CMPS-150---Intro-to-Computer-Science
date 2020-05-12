# Author:           Austin Dugas
# ULID:             C00231110
# Course/Section:   CMPS 150 - Lecture Section # 003
# Assignment:       pa6
# Date Assigned:    Wednesday, October 30, 2019
# Date/Time Due:    Sunday, November 3, 2019 -- 11:55 pm
#
# Description:      Read data from a file until planet name is "DONE"
#                   Name of the data file is "planets.py"
#                   Each set of data is described in the specifications below.
#                   Produce a table of formatted output as seen in the sample output.
#                   Calculations needed are provided.
#                   Function requirements are specified below.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# Define a function that calculates the weight of a person on different planets
def PlanetWeight(planet,weight):
    if planet == "Mercury":
        newWeight = weight * .38
        return newWeight
    elif planet == "Venus":
        newWeight = weight * .91
        return newWeight
    elif planet == "Earth":
        newWeight = weight * 1.00
        return newWeight
    elif planet == "Mars":
        newWeight = weight * 1.03
        return newWeight
    elif planet == "Jupiter":
        newWeight = weight * 2.34
        return newWeight
    elif planet == "Saturn":
        newWeight = weight * .93
        return newWeight
    elif planet == "Uranus":
        newWeight = weight * .92
        return newWeight
    elif planet == "Neptune":
        newWeight = weight * 1.12
        return newWeight

# Define a function that calculates the age of a person on different planets
def PlanetAge(planet,years):
    if planet == "Mercury":
        newAge = years / .241
        return newAge
    elif planet == "Venus":
        newAge = years / .615
        return newAge
    elif planet == "Earth":
        newAge = years / 1.00
        return newAge
    elif planet == "Mars":
        newAge = years / 1.881
        return newAge
    elif planet == "Jupiter":
        newAge = years / 11.86
        return newAge
    elif planet == "Saturn":
        newAge = years / 29.46
        return newAge
    elif planet == "Uranus":
        newAge = years / 84.01
        return newAge
    elif planet == "Neptune":
        newAge = years / 164.8
        return newAge

# Define a function to format the output of the main
def OutputHeader():
    print("  Planet         Earth     Birth      Earth     Planet     Planet")
    print("   Name         Weight      Year        Age     Weight        Age")
    print("-----------------------------------------------------------------")

def PrintOutput(planet,weight,years,earthAge,newWeight,newAge):
    print(format(planet,'7s'),format(weight,'13d'),format(years,'10d'),
          format(earthAge,'10d'),format(newWeight,'10.2f'),format(newAge,'10.2f'))

def OutputEnd(weightAvg,pre2000,oldestName,oldestAge):
    print("-----------------------------------------------------------------")
    print()
    print("Sum:      ",weightAvg)
    print("Pre-2000: ",pre2000)
    print("Oldest:   ",oldestName,format(oldestAge,'6.2f'))

# Define the main function
def main():
    # Call the header function
    OutputHeader()
    
    # Open the input file
    infile = open("planets.py",'r')

    # Initialize the variables
    planet = infile.readline().strip()
    weight = eval(infile.readline())
    years = eval(infile.readline())

    # Initialize counters
    pre2000 = 0
    weightAvg = 0
    counter = 0
    oldestName = planet
    age1 = 0

    # Call the functions to get the calculations
    while planet != "DONE":
        earthAge = 2019 - years
        newWeight = PlanetWeight(planet,weight)
        newAge = PlanetAge(planet,earthAge)

        # Find the number of people born before 2000
        if years < 2000:
            pre2000 = pre2000 + 1

        # Find the oldest person after calculations
        if newAge > age1:
            age1 = newAge
            oldestName = planet
            oldestAge = age1

        # Find the sum of the weights
        weightAvg = weightAvg + weight

        # Update counter
        counter = counter + 1

        # Call the output function
        PrintOutput(planet,weight,years,earthAge,newWeight,newAge)

        # Update the variables from the file
        planet = infile.readline().strip()
        weight = eval(infile.readline())
        years = eval(infile.readline())

    # Calculate the average weight
    weightAvg = weightAvg / counter

    # Call the output ending function
    OutputEnd(weightAvg,pre2000,oldestName,oldestAge)

    # Close the file
    infile.close()

# Call the main
main()
        
