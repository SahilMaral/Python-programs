binary = int(input("Enter a binary number: ")) 
bits = list(str(binary))
decimal = 0 
counter = 0 
for i in reversed(bits):
    decimal += 2**counter * int(i) 
    counter += 1
print("The decimal equivalent is:", decimal)
