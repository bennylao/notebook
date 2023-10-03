def sort_three_numbers():
    a = int(input("Enter the first unique number: "))
    b = int(input("Enter the second unique number: "))
    c = int(input("Enter the third unique number: "))

    # if a > b and a > c:
    #     print(a)
    #     if b > c:
    #         print(b)
    #         print(c)
    #     else:
    #         print(c)
    #         print(b)
    # elif b > a and b > c:
    #     print(b)
    #     if a > c:
    #         print(a)
    #         print(c)
    #     else:
    #         print(c)
    #         print(a)
    # else:
    #     print(c)
    #     if a > b:
    #         print(a)
    #         print(b)
    #     else:
    #         print(b)
    #         print(a)

    number_list = [a, b, c]
    for i in range(len(number_list)):
        for j in range(len(number_list)-1):
            if number_list[j] < number_list[j+1]:
                temp = number_list[j]
                number_list[j] = number_list[j+1]
                number_list[j+1] = temp
    for x in range(len(number_list)):
        print(number_list[x])


def verify_password():
    # pre-stored password
    existing_password = "testing123"
    user_input_password = input("Please enter your password: ")
    if user_input_password == existing_password:
        print("Password accepted!")
    else:
        print("Wrong password")


def calculate_ucl_grade():
    grade_percentage = int(input("Please input your percentage score: "))
    if grade_percentage >= 70:
        print("Distinction")
    elif 50 <= grade_percentage < 70:
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    sort_three_numbers()
    verify_password()
    calculate_ucl_grade()
