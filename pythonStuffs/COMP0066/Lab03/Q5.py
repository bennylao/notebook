def accept_login(user_dict, username, password):
    if username in user_dict and user_dict(username) == password:
        return True
    else:
        return False


if __name__ == "__main__":
    users = {"user1": "password1", "user2": "password2", "user3": "password3"}
    if accept_login(users, "wronguser", "wrongpassowrd"):
        print("login successful!")
    else:
        print("login failed...")
