class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def desc(self):
        print(f"{self.name} is a {self.type} restaurant.")

    def open(self):
        print(f"{self.name} is now open.")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def list_flavors(self):
        print('Available flavors: ')
        for flavor in self.flavors:
            print(f'- {flavor}')
