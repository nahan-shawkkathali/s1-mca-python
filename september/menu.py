while True:
    print("\nMENU")
    print("1) Occurrence of word")
    print("2) Character frequency")
    print("3) Display factors of a given number")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        text = input("Enter a line of text: ")
        word = input("Enter the word to count: ")
        count = text.split().count(word)
        print("The word '" + word + "' occurred " + str(count) + " times.")

    elif choice == '2':
        text = input("Enter a line of text: ")
        freq = {}
        for char in text:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        print("Character frequencies:")
        for char, count in freq.items():
            print("'" + char + "':", count)

    elif choice == '3':
        num = int(input("Enter a number: "))
        print("Factors of", num, "are:", end=" ")
        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end=" ")
        print()

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
