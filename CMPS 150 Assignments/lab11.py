#  Author:          Austin Dugas
#  ULID/Section:    C00231110/003
#  lab11.py 

import random

def Swap(list1):
    temp = list1[0]
    list1[0] = list1[len(list1)-1]
    list1[len(list1)-1] = temp
    return list1

def Reverse(list1):
    newList = []
    for i in range(len(list1) - 1, -1, -1):
        newList.append(list1[i])
    return newList

def main():
    # create an empty list
    list1 = []

    # set up a counting loop to append 15 random integers
    # to the list, ranging from 1 to 25 (inclusive)
    for i in range(0,15):
        list1.append(random.randint(0,25))

    # print the list
    print(list1)
    print()

    # generate one more random integer in the same range
    # append it to list ONLY IF it is not already in the list
    # you are NOT allowed to use the builtin method/function 'in' or 'not in'
    newInt = random.randint(0,25)
    print("newInt =",newInt)

    for i in range(0,len(list1)):
        if newInt == list1[i]:
            x = False
            break
        elif newInt != list1[i]:
            x = True

    if x == False:
        print(newInt, "is already in the list ... not added!")
    elif x == True:
        print(newInt, "is NOT in the list ... it has been added!")
        list1.append(newInt)

    # print the list
    print()
    print(list1)
    print()

    # call function to swap the first & last element, pass the list as a parameter
    swapList = Swap(list1)
    
    # print the list
    print(swapList)

    # call function to reverse the list, the function must return the reversed list
    revList = Reverse(list1)

    # print the list
    print(revList)


main()
