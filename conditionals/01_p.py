
#Write a program that takes an integer input from the user and checks whether it is even or odd.
number=int(input("Enter a number:"))
if number %2==0:
    print(f"The given number is even!")
else:
    print(f"The given number is odd!")

#leap year 
year=int(input("Enter a year: "))
if(year % 400 == 0)or(year % 4 == 0 and year % 100 != 0):
    print(year,"is a leap year")
else:
    print(year, "is Not a leap year!")

