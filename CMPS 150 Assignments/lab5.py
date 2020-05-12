# Author:         Austin Dugas  
# ULID/Section:   C00231110/003
# Lab #5

# Part I
# ask the user to enter the x coordinate (it can be a float)
x = eval(input("Enter the x coordinate: "))

# ask the user to enter the y coordinate (it can be a float)
y = eval(input("Enter the y coordinate: "))

# check for the origin, x-axis OR y-axis, then all 4 quadrants
if x == 0 and y == 0:
    print("This point is the origin")
elif x == 0 or y == 0:
    print("This point is on an axis")
elif x > 0 and y > 0:
    print("This point is in Quadrant I")
elif x < 0 and y > 0:
    print("This point is in Quadrant II")
elif x < 0 and y < 0:
    print("This point is in Quadrant III")
else:
    print("This point is in Quadrant IV")

# Part II
# print a blank line
print()

# pounds/kilograms table

print(" Pounds     Kilograms")
print("---------------------")

pounds = 5
kilograms = pounds * .453592
print(format(pounds, '6d'), format(kilograms, '12.2f'))

pounds = 10
kilograms = pounds * .453592
print(format(pounds, '6d'), format(kilograms, '12.2f'))

pounds = 15
kilograms = pounds * .453592
print(format(pounds, '6d'), format(kilograms, '12.2f'))
