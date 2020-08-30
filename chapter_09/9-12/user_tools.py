class User:

    def __init__(self, first_name, last_name, age, country, profession, language):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.country = country
        self.prof = profession
        self.lang = language

    def desc(self):
        print(f'''
Name: {self.fname} {self.lname}
Age: {self.age}
Residence: {self.country}
Profession: {self.prof}
Preferred Language: {self.lang}
        ''')

    def greet(self):
        print(f"Hello {self.fname}, thank you for visiting our website.")
