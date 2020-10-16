class User:
    """Attempt to represent users"""
    def __init__(self, first_name, second_name, age, location):
        """initialising attributs name, age, location of user"""
        self.name = f'{first_name.title()} {second_name.title()}'
        self.age = age
        self.location = location


    def describe_user(self):
        """prints info about user"""
        print(f'\nName of the user is: {self.name}')
        print(f'Age of the user: {self.age}')
        print(f'Location of user is: {self.location}')

    def greet_user(self):
        """Greets the user"""
        print(f'Hii! {self.name}')

#user1 = User('mahesh', 'babu', 12, 'markapur')
#user2 = User('pavan', 'teja', 17, 'tirupati')
#user3 = User('Ramana', '', 36, 'singaripalli')

#user1.describe_user()
#user1.greet_user()
#user2.describe_user()
#user2.greet_user()
#user3.describe_user()
#user3.greet_user()