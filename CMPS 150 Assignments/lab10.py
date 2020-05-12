# Author:         Austin Dugas 
# ULID/Section:   C00231110/003
# lab10.py

def main():

    # open the file
    infile = open("stringsNums.py",'r')
    
    # read 2 strings
    string1 = infile.readline().strip()
    string2 = infile.readline().strip()

    print("String     SubLength    Substring")
    print("---------------------------------")

    # while 2nd string is not '0'
    while string2 != '0':
        
        # call CheckAndReturn function twice
        origString = CheckAndReturn(string1)
        subLength = CheckAndReturn(string2)
            
        # finish processing and print
        subString = string1[0:subLength]
        print(format(origString,'11s'),format(subLength,'5d'),
              "       ",subString)

        # read 2 strings again
        string1 = infile.readline().strip()
        string2 = infile.readline().strip()

    # close the file
    print("---------------------------------")
    infile.close()

def CheckAndReturn(s):
    # use string methods to determine if all digits or alphanumeric
    # and return appropriate value
    if s.isdigit() == True:
        s = int(s)
        return s
    elif s.isalnum() == True:
        s = str(s)
        return s

main()
