command = ""
while command != "quit":
    command = input("> ").lower()  # Assign the input to command and convert to lowercase
    if command == "start":
        print("Car started, ready to go...")
    elif command == "stop":
        print("Car stopped")
    elif command == "quit":
        print("Program finished...")
        break
    elif command == "help":
        print("""
start - car started, ready to go
stop - car stopped
quit - exits the game                
        """)
    else:
        print("I don't understand!")

    