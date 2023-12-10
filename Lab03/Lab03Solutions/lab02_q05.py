users = {
    "user1": "password1",
    "user2": "password2",
    'user3': "password3",
}


def accept_login(users, username, password):
    for x, y in users.items():
        if x == username and y == password:
            print("Login Successful.")
            break
    else:
        print("Login failed.")


accept_login(users, "user1", "password1")
