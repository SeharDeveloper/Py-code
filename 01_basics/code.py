emotions = {"happy": "😊", "sad": "😢", "love": "❤️", "fire": "🔥"}
user = str(input("Enter a sentence: "))

for key, value in emotions.items():
    user = user.replace(key, value)

print(user)
