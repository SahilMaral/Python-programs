string = input("Enter a string: ")
if len(string) < 2:
    print("")
else:
    print(string[:2] + string[-2:])
