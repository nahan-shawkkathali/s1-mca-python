word = input("Enter a word: ")
if len(word) >= 3 and word[-3:] == "ing":
    word = word + "ly"
else:
    word = word + "ing"

print(word)
