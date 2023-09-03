no = int(input("Enter a number: "))
temp = no
sum = 0
while(no > 0):
    rem = int(no % 10)
    sum = sum * 10 + rem
    no /= 10

# print(sum)
if(temp == sum):
    print("Number is palindrome")
else:
    print("Number is not palindrome")