# Author:         Austin Dugas
# ULID/Section:   C00231110/003
# lab8.py 

#****************** LAB Average  ******************
def LabAvg(): 

    infile1 = open("lab8_labGrades.py","r")
    num = eval(input("How many lab grades are in the file? "))

    print("Lab Grades: ", end='')
    sum = 0
    for i in range(num):
        grade = eval(infile1.readline())
        sum = sum + grade
        print(grade,end = ' ')

    infile1.close()

    print()
    avg = sum / num      # computes avg (number between 1 & 10)
    avg = avg / 10       # change the number to a percentage, labs are worth 10 points
    return avg  

#****************** PA Average  ****************** 
def PaAvg():
    infile2 = open("lab8_paGrades.py","r")
    num = eval(input("How many PA grades are in the file? "))

    print("PA Grades: ", end = '')
    sum = 0
    for i in range(num):
        grade = eval(infile2.readline())
        sum = sum + grade
        print(grade,end = ' ' )

    infile2.close()

    print()
    avg = sum / num
    avg = avg / 100
    return avg
    
#****************** EXAM Average  ****************** 
def ExamAvg():
    infile3 = open("lab8_examGrades.py","r")
    num = eval(input("How many exam grades are in the file? "))

    print("Exam Grades: ", end = '')
    sum = 0
    for i in range(num):
        grade = eval(infile3.readline())
        sum = sum + grade
        print(grade,end = ' ' )

    infile3.close()

    print()
    avg = sum / num
    avg = avg / 100
    return avg
    
#****************** MAIN/DRIVER  ******************

def main():

    # main will call each of your average functions to compute each component of overall class avg
    # call the function to compute your LAB average put the return value in the variable labAverage 

    print()
    labAverage = LabAvg()
    paAverage = PaAvg()
    examAverage = ExamAvg()

    # compute your OVERALL class average using the weights
    # provided on the lab instruction sheet 
    overallAverage = labAverage * 10 + paAverage * 20 + examAverage * 70
    
    # print results
    print()
    print("  Lab Average =", format(labAverage*100,'6.2f'), '%')
    print("   PA Average =", format(paAverage*100,'6.2f'), '%')
    print(" Exam Average =", format(examAverage*100,'6.2f'), '%')
    print("-------------")
    print("Class Average =", format(overallAverage,'6.2f'), '%')
    print()

main()
