no = int(input("Enter a two or more digit number: "))
sum = 0
while(no > 0):
    rem = no % 10
    sum += int(rem)
    no /= 10
print("sum of digit is: ", sum)