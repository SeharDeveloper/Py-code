#Transportataion Mode selection
distance=str(input(f"Enter distance: "))
 
if distance == "3km":
    print(f"Walk")
elif distance <= "15km":
    print(f"Bike")
else:
    print(f"Car")


