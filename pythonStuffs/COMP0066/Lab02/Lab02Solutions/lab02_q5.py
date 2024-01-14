def palindrome():
    word = input("Please input a word to check if it is a palindrome or not: ")
    list_1 = []
    list_2 = []

    for x in word:
        list_1.append(x)
        list_2.append(x)

    list_2.reverse()

    if list_1 == list_2:
        print(f"The word {word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")


palindrome()
