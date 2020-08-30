import admin_tools

user01 = admin_tools.User('George', 'Costanza', 33,
                          'USA', 'accountant', 'english')
user02 = admin_tools.User('Ryan', 'Gosling', 75,
                          'Sweden', 'plumber', 'swedish')
user03 = admin_tools.User('Ariana', 'Grande', 19,
                          'Japan', 'veterinarian', 'english')
user04 = admin_tools.Admin('Joe', 'Exotic', 57,
                           'India', 'tiger king', 'french')

user01.desc()
user01.greet()

user02.desc()
user02.greet()

user03.desc()
user03.greet()

user04.desc()
user04.greet()

user04.privileges.show_privileges()
