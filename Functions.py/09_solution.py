#Generator Function with yield
def countdown(n):
    while n>0:
        yield n
        n=n-1
for number in countdown(5):
    print(number)
