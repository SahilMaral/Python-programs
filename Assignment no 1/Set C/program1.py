no = int(input("Enter a number of lines: "))
for i in range(1, no + 1):
    for j in range(1, no - i + 1):
        print(" ",end = " ")
    for j in range(1, i + 1):
        print(j,end=" ")
    for j in range(j-1, 0,-1):
        print(j, end=" ")
    print()