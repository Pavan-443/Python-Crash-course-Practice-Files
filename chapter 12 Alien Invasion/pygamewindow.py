import sys
import pygame
from gamecharacter import Character

class Window:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 770))
        pygame.display.set_caption('Window')

        self.character = Character(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((75, 0, 130))

            self.character.blitme()

            pygame.display.flip()


if __name__ == '__main__':
    window = Window()
    window.run_game()
