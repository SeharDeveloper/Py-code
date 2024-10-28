#Write a program to classify age group: child(<13), Teenager(13-19), Adult(20-59), Seniors(60+)
age=int(input("Enter your age:12"))
if age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age < 59:
    print("Adult")
else:
    print("Senior")