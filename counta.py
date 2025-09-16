names = ["Anu", "Meena", "rani", "anand"]
count = 0

for name in names:
    for char in name.lower():
        if char == 'a':
            count =count+ 1

print(count)
