from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for i in range(1,11):
            print(randint(1,self.sides))

dice = Die()
dice.sides = 10
dice.roll_die()