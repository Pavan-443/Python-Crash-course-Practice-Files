class User:
    """Attempt to represent users"""
    def __init__(self, first_name, second_name, age, location):
        """initialising attributs name, age, location of user"""
        self.name = f'{first_name.title()} {second_name.title()}'
        self.age = age
        self.location = location
        self.login_attempts = 0


    def describe_user(self):
        """prints info about user"""
        print(f'\nName of the user is: {self.name}')
        print(f'Age of the user: {self.age}')
        print(f'Location of user is: {self.location}')

    def greet_user(self):
        """Greets the user"""
        print(f'Hii! {self.name}')

    def increment_login_attempts(self):
        """Increments the login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets login attempts to 0"""
        self.login_attempts = 0

user1 = User('pavan', 'teja', 17, 'kalikiri')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)