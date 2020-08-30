class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def desc(self):
        print(f"{self.name} is a {self.type} restaurant.")

    def open(self):
        print(f"{self.name} is now open.")


mcdo = Restaurant("McDonald's", 'fast-food')
domo = Restaurant("Domino's", 'pizza')
swch = Restaurant("Swiss Chalet", 'casual dining')

mcdo.desc()
domo.desc()
swch.desc()
