# Author:         Austin Dugas
# ULID/Section:   C00231110/003
# Lab #7
 
infile = open("fuel.py","r")
    
print()
print("    Fuel Type        Gallons     Bill")
print("-------------------------------------")  


# this is a count-controlled loop
              
for i in range (0,15,1): 
    # read and process data 
    word = infile.readline().strip()
    gallons = eval(infile.readline())
    if word == "S":
        word = "Super Unleaded"
        bill = gallons * 2.62
    elif word == "P":
        word = "Unleaded Plus"
        bill = gallons * 2.36
    elif word == "R":
        word = "Regular Unleaded"
        bill = gallons * 2.12
    elif word == "D":
        word = "Diesel"
        bill = gallons * 2.35

    # print each line of output
    print(format(word,'20s'),format(gallons,'7.2f'),format(bill,'8.2f'))  


infile.close()
