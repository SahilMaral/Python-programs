num = int(input("Enter a number: ")) 
last = num % 10
first = num
while first > 9:
    first = int(first / 10)
sum = first + last 
print("The sum of first and last digit is:", sum)
