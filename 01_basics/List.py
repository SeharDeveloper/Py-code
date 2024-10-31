#indexing
my_list = [10, 20, 30]
print(my_list[0])  # Output: 10

#Negative indexing
my_list = [10, 20, 30]
print(my_list[-1])  # Output: 30

#Slicing
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40]

#Modifying Lists
#changing elements
my_list = [10, 20, 30]
my_list[1] = 50
print(my_list)  # Output: [10, 50, 30]

#Append: Add an element to the end of the list.
my_list = [10, 20]
my_list.append(30)
print(my_list)  # Output: [10, 20, 30]

#Insert: Insert an element at a specific index.
my_list = [10, 20]
my_list.insert(1, 30)
print(my_list)  # Output: [10, 30, 20]

#Remove : Removes the first occurrence of a specified element.
my_list = [10, 20, 30, 20]
my_list.remove(20)
print(my_list)  # Output: [10, 30, 20]

#Pop: Remove an element at a specific index and return its value
my_list = [10, 20, 30]
removed_value = my_list.pop(1)
print(my_list)  # Output: [10, 30]
print(removed_value)  # Output: 20

#Del : Remove an element at a specific index without returning its value.
my_list = [10, 20, 30]
del my_list[1]
print(my_list)  # Output: [10, 30]

#clear() Removes all elements from the list.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []

# extend(): Adds the elements of another iterable to the end of the list.
my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

#index(element, start=0, end=None): Returns the index of the first occurrence of a specified element.
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1

#count(element): Returns the number of occurrences of a specified element.
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2

#sort(key=None, reverse=False): Sorts the list in ascending order (by default) or descending order.
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

# reverse(): Reverses the order of the elements in the list.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

#copy(): Returns a shallow copy of the list.
my_list = [1, 2, 3]
copied_list = my_list.copy()
print(copied_list)  # Output: [1, 2, 3]

#List Comprehension 
new_list = [expression for item in iterable if condition] #Syntax
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

#lists
#indexing me pehly digit 0 se start hota ha..
Shopping_list = ['Shirts', 'Trousers', 'Shoes', 'Makeup']
print(Shopping_list)
print(Shopping_list[1]) #specifies the index and returns indexed value
print(Shopping_list[1:3]) #index start hoga 1 se r 3 tk jaye pr 3 include nhi hoga
print(Shopping_list[:2])#index 2 se start hoga r last tk jye ga
Shopping_list [3] = "Jwellery" #index number 3 pr value ko is value se replace kr de ga
print(Shopping_list)
#-->Shopping_list[1:2] =  "Heels"
#--->print(Shopping_list) #yahan Heels ka hr letter alg alg display hoga r trouser se Heel replace ho jye ga
Shopping_list[1:2] = ["Heels"]
print(Shopping_list) #pura word trouser ki jgha heels as it is a jye ga kiu k braces lgi haiun
Shopping_list[1:1]
print(Shopping_list) #prints nothing coz 1 se index start ha r end pont b 1 hi ha to kuch b print nhi hua

squared_num = [x ** 2 for x in range(10)] #square function ha jo 2 ka sqr btye ga jis ki range 10 numbers haiun 
print(squared_num)
#indexing
my_list = [10, 20, 30]
print(my_list[0])  # Output: 10

#Negative indexing
my_list = [10, 20, 30]
print(my_list[-1])  # Output: 30

#Slicing
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40]

#Modifying Lists
#changing elements
my_list = [10, 20, 30]
my_list[1] = 50
print(my_list)  # Output: [10, 50, 30]

#Append: Add an element to the end of the list.
my_list = [10, 20]
my_list.append(30)
print(my_list)  # Output: [10, 20, 30]

#Insert: Insert an element at a specific index.
my_list = [10, 20]
my_list.insert(1, 30)
print(my_list)  # Output: [10, 30, 20]

#Remove : Removes the first occurrence of a specified element.
my_list = [10, 20, 30, 20]
my_list.remove(20)
print(my_list)  # Output: [10, 30, 20]

#Pop: Remove an element at a specific index and return its value
my_list = [10, 20, 30]
removed_value = my_list.pop(1)
print(my_list)  # Output: [10, 30]
print(removed_value)  # Output: 20

#Del : Remove an element at a specific index without returning its value.
my_list = [10, 20, 30]
del my_list[1]
print(my_list)  # Output: [10, 30]

#clear() Removes all elements from the list.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []

# extend(): Adds the elements of another iterable to the end of the list.
my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

#index(element, start=0, end=None): Returns the index of the first occurrence of a specified element.
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1

#count(element): Returns the number of occurrences of a specified element.
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2

#sort(key=None, reverse=False): Sorts the list in ascending order (by default) or descending order.
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

# reverse(): Reverses the order of the elements in the list.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

#copy(): Returns a shallow copy of the list.
my_list = [1, 2, 3]
copied_list = my_list.copy()
print(copied_list)  # Output: [1, 2, 3]

#List Comprehension 
new_list = [expression for item in iterable if condition] #Syntax
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

#lists
#indexing me pehly digit 0 se start hota ha..
Shopping_list = ['Shirts', 'Trousers', 'Shoes', 'Makeup']
print(Shopping_list)
print(Shopping_list[1]) #specifies the index and returns indexed value
print(Shopping_list[1:3]) #index start hoga 1 se r 3 tk jaye pr 3 include nhi hoga
print(Shopping_list[:2])#index 2 se start hoga r last tk jye ga
Shopping_list [3] = "Jwellery" #index number 3 pr value ko is value se replace kr de ga
print(Shopping_list)
#-->Shopping_list[1:2] =  "Heels"
#--->print(Shopping_list) #yahan Heels ka hr letter alg alg display hoga r trouser se Heel replace ho jye ga
Shopping_list[1:2] = ["Heels"]
print(Shopping_list) #pura word trouser ki jgha heels as it is a jye ga kiu k braces lgi haiun
Shopping_list[1:1]
print(Shopping_list) #prints nothing coz 1 se index start ha r end pont b 1 hi ha to kuch b print nhi hua

squared_num = [x ** 2 for x in range(10)] #square function ha jo 2 ka sqr btye ga jis ki range 10 numbers haiun 
print(squared_num)


