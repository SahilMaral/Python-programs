no1 = int(input("Enter a starting number: "))
no2 = int(input("Enter a ending number: "))
no = 1
for no in range(no1 , no2):
        for i in range(2 , no):
            if no % i == 0:
                break
        else:
            print(no," is prime number")



