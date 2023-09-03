# accept cordinates from the user
x = int(input("Enter x cordinates: "))
y = int(input("Enter y cordinates: "))

# logic of code

if x > 0 and y > 0:
    print("Its lies in first quardrant")
elif x < 0 and y > 0:
    print("Its lies in second quardrant")
elif x < 0 and y < 0:
    print("Its lies in third quardrant")
elif x == 0 and y == 0:
    print("Its lies in origin")
else:
    print("Its lies in fourth quardrant")
