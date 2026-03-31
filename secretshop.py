import os

print("---WELCOME TO THE SECRET SHOP!---\n\n")

items = [
    {"name": "Point Booster", "price": 1200},
    {"name": "Vitality Booster", "price": 1000},
    {"name": "Energy Booster", "price": 800},
    {"name": "Sacred Relic", "price": 3400},
    {"name": "Demon Edge", "price": 2200},
    {"name": "Reaver", "price": 2800},
    {"name": "Plate Mail", "price": 1400},
    {"name": "Hyperstone", "price": 2000},
    {"name": "Eaglesong", "price": 2800},
    {"name": "Ultimate Orb", "price": 2800}
]

cart = []
total = 0

# loop for buying
while True:

    os.system("cls")

    print("\nShop keeper: What do you want to buy?\n")

    i = 1
    for item in items:
        print(str(i) + ". " + item["name"] + " - " + str(item["price"]))
        i = i + 1

    print("0. Checkout")

    choice = int(input("\nEnter number: "))

    if choice == 0:
        break

    index = choice - 1

    if 0 <= index < len(items):
        selected_item = items[index]
        cart.append(selected_item)
        total = total + selected_item["price"]

        print("Added: " + selected_item["name"])
    else:
        print("Invalid choice!")

# show cart
print("\n--- YOUR CART ---")
for item in cart:
    print(item["name"] + " - " + str(item["price"]))

print("Total: " + str(total))

# payment
payment = int(input("\nEnter payment: "))

if payment < total:
    print("Not enough money!")
    print("Balance unpaid. Reset to 0.")
    total = 0
elif payment == total:
    print("Thank you for your purchase!")
else:
    change = payment - total
    print("Change: " + str(change))
    print("Thank you for buying!")