#print the multiplication table for the given number upto 10 , but skip the fifth iteration
number=int(input("Table of: "))
for i in range(1, 11):
    if i==5:
        continue
    print(number, 'x', i, "=", number*i)
