class Restaurant:
    """A simple Attempt to represent restaurants"""
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        """Inistialising attributes restaurant_name, cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors

    def describe_restaurant(self):
        """Prints about restaurant"""
        print(f'\nRestaurant name is {self.restaurant_name.title()}')
        print(f'Here we make cuisine types of {self.cuisine_type.title()}')

    def show_flavors(self):
        """Prints flavors"""
        print('Following are the avaialable flavors: ')
        for flavor in self.flavors:
            print(f"--->{flavor.title()}")

res1 = Restaurant("KING'S","Ice_cream", 'strawberry', 'chocolate', 'raspberry')
res1.show_flavors()