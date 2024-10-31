#Tuple ek immutable collection hai jo ordered items ko parentheses () mein store karti hai aur modify nahi ho sakti
my_tuple=(12,45,19,'Hello!')
print(my_tuple)

#Immutable: You cannot change the items after the tuple is created.
#Ordered: Tuples maintain the order of elements.
#Allows Duplicates: Tuples can have multiple items with the same value.
#Can Store Different Data Types

#indexing
my_tuple=(12,45,19,'Hello!')
print(my_tuple.index(45)) #1s

my_tuple=(12,45,19,'Hello!')
print(my_tuple[:]) #12,45,19,Hello! 

my_tuple=(12,45,19,'Hello!')
print(my_tuple[1:2]) #(45,)

my_tuple=(12,45,19,'Hello!')
print(my_tuple[1]) #45

#combining tuple
tuple_1=(12,45,19,'Sehar')
tuple_2=('a','b')
combined_tuple=tuple_1+tuple_2
print(combined_tuple)#(12, 45, 19, 'Sehar', 'a', 'b')
#repetition
repeated=tuple_1*2
print(repeated)#(12, 45, 19, 'Sehar', 12, 45, 19, 'Sehar')

#count-->Ye method tuple ke andar kisi specific value ka count batata hai.
tuple_3=(1,2,3,2,2,1,3)
print(tuple_3.count(2)) # is ki output 3 hogi kiuu k 2 is me 3times h

#len()
my_tuple=(12,45,19,'Hello!')
length=len(my_tuple)
print(length) # 4

#tuples are immutable, meaning their contents cannot be changed once assigned, 
# and they cannot be assigned values directly.
#(12, 45, 19, 'Hello!') = class_1
#print(class_1)

#If ka use kr k check krty haiun k element tuple me available h ya nhi
my_tuple = (12, 45, 19, 'Hello!')
if 45 in my_tuple:
    print("45 is in the tuple.")
else:
    print("45 is not in the tuple.") #45 is in the tuple.

#If ka use kr k tuples ko compare krty haiun like 2 tuples same haiun ya nhi
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
if tuple1 == tuple2:
    print("The tuples are equal.")
else:
    print("The tuples are not equal.") #The tuples are equal.
 
#If statement me items ki length find kr skty haiun
my_tuple = (12, 45, 19, 'Hello!')
if len(my_tuple) > 3:
    print("The tuple has more than 3 elements.")
else:
    print("The tuple has 3 or fewer elements.")#The tuple has more than 3 elements.

#Accessing elements conditionally
my_tuple = (12, 45, 19, 'Hello!')
if my_tuple[0] == 12:
    print("The first element is 12.")
else:
    print("The first element is not 12.")
