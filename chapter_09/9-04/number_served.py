class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.served = 0

    def desc(self):
        print(f"{self.name} is a {self.type} restaurant.")

    def open(self):
        print(f"{self.name} is now open.")

    def set_served(self, num):
        self.served = num

    def incr_served(self, num):
        self.served += num


restaurant = Restaurant("Al Fresco", 'italian')
restaurant.desc()
print(f"This restaurant has served {restaurant.served} customers.")

restaurant.set_served(15)
print(f"This restaurant has served {restaurant.served} customers.")

restaurant.incr_served(32)
print(f"This restaurant has served {restaurant.served} customers.")
