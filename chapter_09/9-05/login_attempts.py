class User:

    def __init__(self, first_name, last_name, age, country, profession, language):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.country = country
        self.prof = profession
        self.lang = language
        self.login_attempts = 0

    def desc(self):
        print(f'''
Name: {self.fname} {self.lname}
Age: {self.age}
Residence: {self.country}
Profession: {self.prof}
Preferred Language: {self.lang}
        ''')

    def greet(self):
        print(f"Hello {self.fname}, thank you for registering to our website.")

    def incr_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user01 = User('George', 'Costanza', 33, 'USA', 'accountant', 'english')
user02 = User('Ryan', 'Gosling', 75, 'Sweden', 'plumber', 'swedish')
user03 = User('Ariana', 'Grande', 19, 'Japan', 'veterinarian', 'english')

user01.desc()
user01.greet()

user02.desc()
user02.greet()

user03.desc()
user03.greet()

user02.incr_login_attempts()
user02.incr_login_attempts()
user02.incr_login_attempts()
user02.incr_login_attempts()
user02.incr_login_attempts()
user02.incr_login_attempts()
user02.incr_login_attempts()
user02.incr_login_attempts()
user02.incr_login_attempts()

print(f"\nUser {user02.fname} {user02.lname} has attempted to login {user02.login_attempts} times.")
print(f"The password will now be reset.")

user02.reset_login_attempts()

print(f"Current login attempts: {user02.login_attempts}")
