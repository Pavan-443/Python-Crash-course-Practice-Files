class Restaurant:
    """A simple Attempt to represent restaurants"""
    def __init__(self, restaurant_name, cuisine_type):
        """Inistialising attributes restaurant_name, cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0

    def describe_restaurant(self):
        """Prints about restaurant"""
        print(f'\nRestaurant name is {self.restaurant_name.title()}')
        print(f'Here we make cuisine types of {self.cuisine_type.title()}')

    def open_restaurant(self):
        """prints that the restaurant is open"""
        print(f'The Restaurant {self.restaurant_name} is opened...')

    def display_numbersserved(self):
        """print numbers served in a restaurant"""
        print(f"\nno.of numbers served today is {self.numbers_served}")

    def set_number_served(self, no_served):
        """set numbers served to the given value"""
        self.numbers_served = no_served
    def increment_number_served(self, increment):
        self.numbers_served += increment



restau1 = Restaurant('king', 'chinese')
restau1.numbers_served = 85
restau1.describe_restaurant()
restau1.open_restaurant()
restau1.display_numbersserved()

restau1.set_number_served(97)
restau1.display_numbersserved()

restau1.increment_number_served(85)
restau1.display_numbersserved()