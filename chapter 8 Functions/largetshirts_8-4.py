def make_shirt_anysize(size, text):
    """Info about shirt"""
    print(f'\nsize of T-shirt is {size}')
    print(f"Text that to be displayed on T-Shirt is '{text}'")

def makeshirt_medium(size='Medium', text='I love Python'):
    """Info about medium T-shirts"""
    print(f'\nsize of T-shirt is {size}')
    print(f"Text that to be displayed on T-Shirt is '{text}'")

def makeshirt_large(size='large', text='Python is interesting'):
    """Info about large shirts"""
    print(f'\nsize of T-shirt is {size}')
    print(f"Text that to be displayed on T-Shirt is '{text}'")

makeshirt_medium()
makeshirt_large()
make_shirt_anysize('medium', 'PYHTON')
