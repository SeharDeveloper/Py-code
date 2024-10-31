#Task: Count Words in a Sentence
#Takes a sentence as input from the user.
#Counts the number of words in the sentence.
#Prints the results
sentence=str(input("Enter a sentence here: "))
words=sentence.split()
length=len(sentence)
print(f"{sentence} has {length} letters")

    