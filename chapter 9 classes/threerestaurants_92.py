class Restaurant:
    """an attempt to represent restaurants"""
    def __init__(self, restaurant_name, cuisine_type):
        """initialising attributes restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """prints info about restaurant"""
        print(f'\nRestaurant name is {self.restaurant_name.title()}')
        print(f'Here we make cuisine types of {self.cuisine_type.title()}')

    def open_restaurant(self):
        """prints whether restaurant is open or not"""
        print(f'The Restaurant {self.restaurant_name} is opened...')

restaurant1 = Restaurant('grand inn', 'chinese')
restaurant2 = Restaurant("king's dhaba", 'biryani')
restaurant3 = Restaurant('kohinoor', 'Indian')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()