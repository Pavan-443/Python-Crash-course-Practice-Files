class Restaurant:
    """A simple Attempt to represent restaurants"""
    def __init__(self, restaurant_name, cuisine_type):
        """Inistialising attributes restaurant_name, cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints about restaurant"""
        print(f'\nRestaurant name is {self.restaurant_name.title()}')
        print(f'Here we make cuisine types of {self.cuisine_type.title()}')

    def open_restaurant(self):
        """prints that the restaurant is open"""
        print(f'The Restaurant {self.restaurant_name} is opened...')

res1 = Restaurant('king', 'chinese')
print(res1.restaurant_name)
print(res1.cuisine_type)

res1.describe_restaurant()
res1.open_restaurant()