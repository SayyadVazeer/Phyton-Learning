menu = {
    "popcorn": 5.00,
    "soda": 2.50,
    "nachos": 4.50,
    "hotdog": 3.75,
    "candy": 1.50,
    "icecream": 3.00,
    "pretzel": 2.75,
    "waterbottle": 1.00}

cart =[]
total = 0

print("------* MENU *------")
for key, value in menu.items():
    print(f"{key:12} - ${value:.2f}")
print("--------------------")

while True:
    food = input("Select an Food (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print()
print("---* Your Order *---")
for food in cart:
    total += menu.get(food)
    print(f"{food:12} - ${menu.get(food):.2f}")
print()
print(f"Your Total is ${total:.2f}")