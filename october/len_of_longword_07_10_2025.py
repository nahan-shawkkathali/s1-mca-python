words = ["apple", "banana", "cherry"]
max_length = 0

for word in words:
    if len(word) > max_length:
        max_length = len(word)

print(max_length)
