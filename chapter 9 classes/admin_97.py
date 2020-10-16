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

class Admin(User):
    def __init__(self, first_name, second_name, age, location, *privileges):
        """initializing variables from class User"""
        super().__init__(first_name, second_name, age, location)
        self.privileges = privileges

    def show_privileges(self):
        """prints privileges of admin"""
        print('following are the privileges enjoyed by an admin: ')
        for privilege in self.privileges:
            print(f">{privilege}")

pavan = Admin('ji', 'ki', 'kl', 'ko')
pavan.privileges = 'can edit', 'can remove users', 'can do all legal things'
pavan.show_privileges()