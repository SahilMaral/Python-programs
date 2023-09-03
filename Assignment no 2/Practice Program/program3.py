str = input("Enter a string: ")
no = len(str)
for i in range(0,no):
    if str[i] == 'A' or str[i] == 'a' or str[i] == 'E' or str[i] == 'e' or str[i] == 'I' or str[i] == 'i' or str[i] == 'O' or str[i] == 'o' or str[i] == 'U' or str[i] == 'u':
        print(str[i],"String has a vowels")
    else:
        print(str[i],"String is consonants")