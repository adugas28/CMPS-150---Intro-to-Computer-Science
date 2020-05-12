def Max(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    i = 5
    j = 2
    k = Max(i, j)

    print("The maximum between",i,"and",j,"is",k)

main()
