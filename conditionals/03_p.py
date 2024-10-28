#simple program to take input from user and displays it on the screen
print("Welcome to SEHAR's Wardrobe\nHere are the items for you. What do you want?")
name = input("Please enter your name: ")

wardrobe = {
    "Jeans": 50, "Suit Salwar": 75, "Saari": 100, "Coat": 150, "Short": 35,
    "Skirt": 45, "Cap": 20, "Sweater": 80, "T-Shirt": 25, "Trouser": 40,
    "Bracelet": 15
}

print(name + "! Our wardrobe includes:")
for item, price in wardrobe.items():
    print(f"- {item}: {price}$")

while True:
        print("What would you like?\n")
        order = input()
        print(order + " Okay!")
        if order in wardrobe:
              price = wardrobe[order]
              print("Price for this item is = " +    str(price))
              quantity = int(input("How much quantity of " + order + " do you want? "))
              total = price * quantity
              print("\nThe total charge for " + str(quantity) + " " + order + "s is = " + str(total) + "$")
        break
else:
    print("Sorry Dear!, 😔 We ran out of " + order)
    
    
    
goodbye = ("\nThank you🌟!for your Order " + name + "! See you Later !!")
print(goodbye)
