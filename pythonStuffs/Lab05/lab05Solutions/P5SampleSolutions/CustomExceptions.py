# Exceptions

class DuplicateUsernameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class UnderageError(Exception):
    pass


class InvalidEmailError(Exception):
    pass


# A class for a user's data

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


example_list = [("jane", "jane@example.com", 21), ("bob", "bob@example", 19), ("jane", "jane2@example.com", 25),
                ("steve", "steve@somewhere", 15), ("joe", "joe", 23), ("anna", "anna@example.com", -3), ]

directory = {}

for username, email, age in example_list:
    try:
        if username in directory:
            raise DuplicateUsernameError()
        if age < 0:
            raise InvalidAgeError()
        if age < 16:
            raise UnderageError()
        email_parts = email.split('@')
        if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
            raise InvalidEmailError()
    except DuplicateUsernameError:
        print("Username '%s' is in use." % username)
    except InvalidAgeError:
        print("Invalid age:%d" % age)
    except UnderageError:
        print("User %s is underage." % username)
    except InvalidEmailError:
        print("'%s' is not a valid email address." % email)

    else:
        directory[username] = User(username, email)
