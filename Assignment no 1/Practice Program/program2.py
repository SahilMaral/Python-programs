# Accepting salary from the user
salary = int(input("Enter a salary: "))
# login code
if salary <= 250000:
    tax = 0
elif salary >= 250000 and salary <= 500000:
    tax = 10
else:
    tax = 20
sum = (salary * tax) / 100
print("Income tax of salary is: ", sum)
