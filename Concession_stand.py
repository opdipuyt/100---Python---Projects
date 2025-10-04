# 9 Concession stand program

menu = {"pizza": 3.00,
        "nachos":   3.54,
        "popcorn":  44.2,
        "cherry":    4.22,
        "apple":      12.33,
        "pretzel":    42.4,
        "soda"    :     4.00,
        "lemonade":   23.44

}

cart = []
total = 0

print("------------Menu------------")
for key,value in menu.items():
    print(f"{key:13}: ${value:.2f}")
print("----------------------------")

while True:
    food = input("Select in item (q to quit ) : ").lower()
    if food == "q":
        break
    elif  menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)

    print(food,)


print()
print(f"Total is : {total:.2f}")
