#Fruit ripeness checker
fruit=str(input("Fruit name:"))
colour=str(input(f"Colour of {fruit} is "))

if colour == "Green":
    print(f"{fruit} is Unripe")
elif colour == "Yellow":
    print(f"{fruit} is ripe")
else:
    print(f"{fruit} is overripe")
