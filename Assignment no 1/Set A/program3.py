no = int(input("Enter a number: "))
i = 1
sum = 0
while(i < no):
    if(no % i == 0):
        sum += i
    i += 1

if(sum == no):
    print("Number is perfect")
else:
    print("Number is not perfect")