import users

class Admin(users.User):
    def __init__(self, first_name, second_name, age, location):
        """initializing variables from class User"""
        super().__init__(first_name, second_name, age, location)
        self.privilege = Privileges()


class Privileges:
    def __init__(self, *privileges):
        """Initializing attributes in this class"""

    def show_privileges(self):
        """prints privileges of admin"""
        print('following are the privileges enjoyed by an admin: ')
        for privilege in self.privileges:
            print(f">{privilege}")

#pavan = Admin('ji', 'ki', 'kl', 'ko')
#pavan.privilege.privileges = 'can chat', 'can edit'
#pavan.privilege.show_privileges()