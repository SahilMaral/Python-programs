str1 = input("Enter a string: ")
no = {}
for i in str1:
    if i in no:
        no[i] += 1
    else:
        no[i] = 1
print("Count of all characters: " + str(no))
