#Password Strength Checker
password=str(input("Enter password"))
char=int(input("characters: "))
if char <= 6:
    print("weak")
elif 6 < char > 10:
    print("Medium")
else:
    print("Strong")