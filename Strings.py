
#Slicing
name = "Leiutenant"
First_char = name[0]
print(First_char) #Output:L--> Jo char display krana ho kisi word ka uska index de gy

post = "lieutenant"
slice_name = post[:]
print(slice_name) #output:lieutenant--->slicing with [:] gives you the whole string.

num_list = '0123456789'
slice_list = num_list[1:7:3] #num_list[start:stop:step]
print(slice_list) #output:14


area = "Naran, Kaghan"
index = area.find("Kaghan")
print(index) #find() returns 7

area = "Naran, Kaghan"
index = area.find("kaghan")
print(index) #find() returns -1 coz index is not found

name = "Sehar"
skill = "Artist"
print(f"{name} is an {skill}") #output: Sehar is an Artist 

digit_list = '123456789'
option1 = digit_list[:]  #output: 123456789
print(option1)

option2 = digit_list[0:5]  # 12345
print(option2)

option3 = digit_list[0:4:1]  # 1234
print(option3)

option4 = digit_list[1:2:3]  # 2
print(option4)

#{}--->place holders
name = "Sehar"
painting = "Queen Elizabeth"
request = "I requested {} for {} portrait."
accept = request.format(name, painting)
print(accept) #I requested Sehar for Queen Elizabeth portrait.

#.join 
Fruits = ['orange', 'apple', 'guava']
basket = ', '.join(Fruits)
print(basket) #Output: orange, apple, guava

#len()
text = "Hello, world!"
length = len(text)
print(length) #The string "Hello, world!" has 13 characters, including spaces and punctuation.

#printing each letter
portait = 'Queen Elizabeth'
for letter in portait:
     print(letter)

#.count
letters = 'abcdefghijklmnopqrstuvwxyz'
print('The letter k appears', letters.count('k'), 'time(s)')

Place = "I requested, \"Please Dont go\""
print(Place)

name='Queen Elizabeth'
print(name)

name = "Queen\Elizebath"
print(name)

name = 'Haleema\nSehar'
print(name) #next line 


name = r'Haleema\nSehar'
print(name) #output: Haleema\nSehar

name = r"c:\user\pwd"
print(name) #widely used method to overcome backslash problem