# accept amout form the user
cost = int(input("Enter a product cost: "))
selling = int(input("Enter selling price: "))

if cost > selling:
    print("Loss is: ", cost - selling)
elif cost == selling:
    print("There will be no loss and no profit")
else:
    print("Profit is: ", selling - cost)
