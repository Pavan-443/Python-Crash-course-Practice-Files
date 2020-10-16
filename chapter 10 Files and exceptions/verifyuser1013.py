import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def check_username():
    """checks whether the given user name is stored"""
    name = get_stored_username().title()
    username = input("What is your name? ")
    if username.title() == name:
        return None
    else:
        return username.title()


def get_new_username():
    """Prompt for a new username."""
    username = check_username()
    filename = 'username.json'
    if username:
        with open(filename, 'w') as f:
            json.dump(username.title(), f)
    return username.title()


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


# username1 = get_stored_username()
# qn = input(f'Is this your name?{username1} (Y/N):')
#
# if qn.lower().strip() == 'n':
#     changedusername = get_new_username()
#     if changedusername.lower() == username1.lower():
#         greet_user()
#     else:
#         print(f"From now onwards I will remember your name, {changedusername}")
#
# elif qn.lower().strip() == 'y':
#     greet_user()
#
# else:
#     print("Please Enter whether y/n")