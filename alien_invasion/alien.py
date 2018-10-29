import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ alien class """

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image, and set rect property
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # every alien original location
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save alien correct location
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien"""
        self.screen.blit(self.image, self.rect)
