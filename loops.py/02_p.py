#calculate sum of even numbers upto a given number n.
n=int(input("Enter a number: "))
sum_even=0
for c in range(1, n+1):
    if c % 2==0:
        sum_even+=1
print("Sum of even numbers is: ", sum_even)