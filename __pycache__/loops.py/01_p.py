#for loop using list--->basic programming practise
#Number List Printer: [1, 2, 3, 4, 5]
my_list=[1, 2, 3, 4, 5]
for num in range(6):
    print(num)
#[1, 2, 3, 4, 5]loop use kar ke is list ke numbers ka total nikaalna hai.
my_items=[1,2,3,4,5]
total=0
for num in my_items:
   total+=num#total=num+1
print("Total is: ", total)
#[1, 2, 3, 4, 5, 6]. Tumne sirf even numbers ko print karna hai
list1=[1,2,3,4,5,6]
for i in list1:
    if i %2==0:
        print(i)
#["apple", "banana", "apple", "orange"]count karna hai ke total kitni items hain.  
list2=["apple", "banana", "apple", "orange"]
count =0
for item in list2:
    count+=1
print("Total items in list:", count)
#["Ali", "Sara", "Ahmed"]har name ke sath "Hello" print karna hai, jaise "Hello Ali".
list2=["Ali", "Sara", "Ahmed"]
for i in list2:
    print("Hello ", i)
#[1, 2, 3, 4, 5]number ka square nikaal ke print karna hai.
list4=[1,2,3,4,5]
square=0
for i in list4:
    square=i**2
    print("Square is ",square)
#loop use karke is list ko reverse order mein print karna hai.
list3=["Ali", "Ahmad", "Sara"]
for i in range(len(list3) -1,-1,-1):
    print(list3 [i])
# loop use karke numbers 1 se 10 tak print karne hain.
num=0
for i in range(1,11):
    print(i)
#Find Maximum in List.
list1=[3, 5, 2, 8, 6]
max_number=list1[0]
for number in list1:
    if number>max_number:
        max_number=number
print("maximum number is ", max_number)
#Alphabet Printer
import string
alphabet_list=list(string.ascii_lowercase)
print(alphabet_list)