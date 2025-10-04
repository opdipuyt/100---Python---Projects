#7  shopping cart program

foods = []
prices = []
total = 0
while True:
    food  = input("Enter a food to buy ( q to quite): ")
    if food.lower() == "q":
        break
    else:
        prince =float(input(f"Enter the price of a {food} : $"))
        foods.append(food)
        prices.append(prince)

print("-----Your cart ------")

for food in foods:
    # print(food, end=" ")
    print(food)

for price in prices:
    total += price
print()
print(f"Your total is : ${total}")
