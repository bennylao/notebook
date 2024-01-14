def check_palindrome(string):
    is_palindrome = True
    for i in range(int(len(string) / 2)):
        if string[i] != string[-i - 1]:
            is_palindrome = False
    print(is_palindrome)


if __name__ == "__main__":
    check_palindrome("test")
    check_palindrome("noon")
    check_palindrome("madam")
