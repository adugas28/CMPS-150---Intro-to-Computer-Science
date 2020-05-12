# Author:           Austin Dugas
# ULID:             C00231110
# Course/Section:   CMPS 150 - Section 3
# Assignment:       pa5
# Date Assigned:    Thursday, October 24, 2019
# Date/Time Due:    Monday, October 28, 2019 -- 11:55 pm
# 
# Description:      Read player data from a file until number of times at bat is -1
#                   Input file name is "pa5_baseball.py"
#                   Each set of data is described in the specifications below.
#                   Produce a table of formatted output as seen in the sample output.
#                   Calculations needed are provided.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# Initialize inputs from file
infile = open("pa5_baseball.py",'r')

name = infile.readline().strip()
number = eval(infile.readline())
position = infile.readline().strip()
atBats = eval(infile.readline())
hits = eval(infile.readline())
walks = eval(infile.readline())

# Set max and min values and set counters for team average
maxWalks = walks
maxName = name
minAtBats = atBats
minName = name
hitsAvg = 0
atBatsAvg = 0

# Print header for outputs
print("    Name                      Number  Position     At Bats  Hits   Walks    BatAvg   OnBaseAvg")
print("----------------------------------------------------------------------------------------------")

# Calculate batting averages and on base averages
while name != "Done":
    batAvg = hits / atBats
    onBaseAvg = (hits + walks) / atBats
    if walks > maxWalks:
        maxWalks = walks
        maxName = name
    if atBats < minAtBats:
        minAtBats = atBats
        minName = name
    atBatsAvg = atBats + atBatsAvg
    hitsAvg = hits + hitsAvg
    print(format(name,'17s'),format(number,'16d'),"  ",format(position,'12s'),format(atBats,'6d'),
          format(hits,'6d'),format(walks,'6d'),format(batAvg,'10.4f'),format(onBaseAvg,'10.4f'))

    name = infile.readline().strip()
    number = eval(infile.readline())
    position = infile.readline().strip()
    atBats = eval(infile.readline())
    hits = eval(infile.readline())
    walks = eval(infile.readline())

# Calculate the team batting average
teamBatAvg = hitsAvg / atBatsAvg

# Print outputs
print("----------------------------------------------------------------------------------------------")
print()
print("Max Walks:   ",maxName,",",maxWalks)
print("Min At Bats: ",minName,',',minAtBats)
print("Team Bat Avg:",format(teamBatAvg,'6.4f'))

# Close the file
infile.close()
    
