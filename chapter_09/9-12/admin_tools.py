from user_tools import User


class Admin(User):

    def __init__(self, first_name, last_name, age, country, profession, language):
        super().__init__(first_name, last_name, age, country, profession, language)
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(
            f'\nHere is your list of admin privleges: ')
        for priv in self.privileges:
            print(f'- {priv}')
