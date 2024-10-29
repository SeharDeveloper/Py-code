#reverse a string using loop
str_name=str(input("Enter string "))
reversed_str=""

for char in str_name:
    reversed_str=char+reversed_str
print(reversed_str)