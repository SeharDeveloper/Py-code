#validate input
import random

name = input("Enter Your Name To Play The Game !!: ")
print(name)

if name == "NH":
    print(name + "!! You are not allowed to play the game. Get out!! Hurry up")
else:
    random_no = random.randrange(0, 100)
    userinput = int(input("Enter number to guess: "))

    if userinput > random_no:
        print(name + "!! Your number is greater than the random number⛥!!")
    elif userinput < random_no:
        print(name + "!! Your number is less than the random number!!")

    while userinput != random_no:
        userinput = int(input("Again Enter Random Number: "))
        
        if userinput > random_no:
            print(name + "!! Your number is greater than the random number⛥!!")
        elif userinput < random_no:
            print(name + "!! Your number is less than the random number!!")
    
    print("Congrats!! " + name + ", you guessed the right number.")
