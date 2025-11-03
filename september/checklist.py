  list1 = list(map(int, input("Enter the first list elements separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list elements separated by spaces: ").split()))

if len(list1) == len(list2):
    print("list is same length")
else:
    print("list is different length")

if sum(list1) == sum(list2):
    print("sum is same")
else:
    print("sum is different")
for item in list1:
    if item in list2:
        print("Common value found:", item)
        break
else:
    print("No common values found.")
