#Grade calculator
grade =float(input("Enter marks(0-100)"))
if 90<=grade <= 100:
    print("A")
elif 80<= grade <89:
    print("B")
elif 70<=grade < 79:
    print("C")
elif 60<=grade < 69:
    print("D")
else:
    print("F")
