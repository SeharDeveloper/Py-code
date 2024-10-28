#write a program that classifies a number 1-10(small), 11-50(medium), 51-100(large)out of range
number=int(input("Enter a number"))

if number < 10:
    print("Small")
elif number < 50:
    print("Medium")
elif number < 100:
    print("Large")
else:
    print("Out of range")

