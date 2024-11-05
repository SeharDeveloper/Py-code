
item_prices = {
    "Apples": 2.5,
    "Bread": 1.8,
    "Milk": 1.2,
    "Eggs": 2.0,
    "Rice": 3.0,
    "Sugar": 1.5
}


grocery_list = {}

num_items = int(input("How many items do you want to buy? "))

for _ in range(num_items):
    item_name = input("Enter item name: ")

    if item_name in item_prices:
        grocery_list[item_name] = item_prices[item_name]
        print(f"Added {item_name} - ${item_prices[item_name]}")
    else:
        print(f"Item '{item_name}' is not available.")


total_cost = sum(grocery_list.values())


print("\nYour grocery list:")
for item, price in grocery_list.items():
    print(f"- {item}: ${price}")

print(f"\nTotal cost: ${total_cost}")
