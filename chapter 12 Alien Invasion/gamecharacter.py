import pygame


class Character:
    """A Character"""
    def __init__(self, samplegame):
        self.screen = samplegame.screen
        self.screen_rect =  samplegame.screen.get_rect()

        self.image = pygame.image.load('character.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)




