import re


class UserNameNotUniqueException(Exception):
    def __init__(self, username):
        super().__init__(f"Username '{username}' is in use.")


class AgeIsNotPositiveIntegerException(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age:{age}")


class UserUnderAgeException(Exception):
    def __init__(self, username):
        super().__init__(f"User {username} is under age.")


class EmailNotValidException(Exception):
    def __init__(self, email):
        super().__init__(f"'{email}' is not a valid email address.")


def check_user_list(users_list):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    existing_users = []
    for user in users_list:
        username = user[0]
        email = user[1]
        age = user[2]
        try:
            if any(username == member[0] for member in existing_users):
                raise UserNameNotUniqueException(username)
            elif age <= 0 or not isinstance(age, int):
                raise AgeIsNotPositiveIntegerException(age)
            elif age < 16:
                raise UserUnderAgeException(username)
            elif not re.fullmatch(regex, email):
                raise EmailNotValidException(email)
            else:
                existing_users.append((username, age))
        except UserNameNotUniqueException as e:
            print(e)
        except AgeIsNotPositiveIntegerException as e:
            print(e)
        except UserUnderAgeException as e:
            print(e)
        except EmailNotValidException as e:
            print(e)
    return existing_users


if __name__ == '__main__':
    users = [("jane", "jane@example.com", 21),
             ("bob", "bob@example", 19),
             ("jane", "jane2@example.com", 25),
             ("steve", "steve@somewhere", 15),
             ("joe", "joe", 23),
             ("anna", "anna@example.com", -3)]

    valid_users = check_user_list(users)
    print(valid_users)
