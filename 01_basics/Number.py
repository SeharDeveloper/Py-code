#Numbers in python
a=2
b=4

print(a**b) #Gives power (**)

c=13
print(a+(b*c)) #precendence of operators

# Defining boolean values
is_sunny = True
is_raining = False

# Boolean expressions
print(5 > 3)            # Output: True (5 is greater than 3)
print(3 == 3)           # Output: True (3 is equal to 3)
print(10 < 2)           # Output: False (10 is not less than 2)

# Combining booleans with "and" and "or" operators
print(is_sunny and is_raining)  # Output: False (both conditions must be True)
print(is_sunny or is_raining)   # Output: True (only one condition needs to be True)

# Negation with "not"
print(not is_sunny)      # Output: False (negates True to False)


#repr() is for developers (for debugging),

city = ('chakwal')
print(repr(city)) #output:'chakwal'

#str() is for users (for display)

cafe = ('Flipsee')
print(str(cafe)) #output : Flipsee

#print() outputs to the console.

print('SeharDeveloper') #SeharDeveloper

import math #This is the library for maths functions
a=math.floor(80.9)
print(a) #Iska output 80 hoga kiuu k ye function given value ka closest number return krta ha

a=math.floor(-80.9)
print(a) #Iska output -81 hoga 

fun = math.trunc(4.9)  # Removes the decimal part
print(fun) #output:4 ye decimal part ko truncate (remove) krta ha r 0 se close value return krta ha

# Decimal number
num = 10

octal=oct(num)
print(octal) #0o12 ye iska octal representation h

hexa=hex(num)
print(f"hexadecimal of {num}: {hexa}") # hexadecimal of 10: 0xa

binary=bin(num)
print(f"binary of {num}: {binary}") #binary of 10: 0b1010

import random
random_num = random.randint(10,90)
print(random_num) #it will display any random number


my_string = "hello"
random_char = random.choice(my_string)
print(random_char)  # Output will be a random character from 'hello'


my_list = ['12', '22', '43', '87']
shuffled_list = my_list[:]  # Make a copy of the original list
random.shuffle(shuffled_list)
print(shuffled_list)  # Output will be a shuffled version of my_list

