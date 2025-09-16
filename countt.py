text = "this is a sample line this is a test"
words = text.split()
counts = {}

for i in words:
    counts[i] = counts.get(i, 0) + 1

print(counts)
