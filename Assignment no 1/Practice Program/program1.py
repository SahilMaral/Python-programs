# To take input form the user
amt = int(input("Enter your amount: "))
# logic code
ten = int(amt / 10)
amt %= 10
five = int(amt / 5)
amt %= 5
one = amt
# print the current of notes of ten,five,one
print("Currency of ten notes: ", ten)
print("Currency of five notes: ", five)
print("Currency of one notes: ", one)
