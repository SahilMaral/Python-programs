no = int(input("Enter a number: "))
sum = 0
temp = no
while(no > 0):
    rem = int(no % 10)
    sum += (rem * rem * rem)
    no /= 10

if(temp == sum):
    print("Number is armstrong")
else:
    print("Number is not armstrong")
