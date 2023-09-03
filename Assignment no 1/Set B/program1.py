num = int(input("Enter a number: "))
even = 0 
odd = 0 
zero = 0
while num > 0:
    rem = int(num % 10)
    if rem == 0:
        zero += 1
    elif rem % 2 == 0:
        even += 1
    else:
        odd += 1
    num = int(num / 10)
print("The number of even digits is:", even)
print("The number of odd digits is:", odd)
print("The number of zero digits is:", zero)
