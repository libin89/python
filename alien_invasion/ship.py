import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """ inintialize ship and set a location """
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image and get shape
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # lay every new ship in the middle of screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # property center save float numeric
        self.center = float(self.rect.centerx)
        
        # moving flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """change ship location"""
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
            if self.rect.centerx > self.screen.get_width():
                self.rect.centerx = self.screen.get_width()
        elif self.moving_left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
            if self.rect.centerx < 0:
                self.rect.centerx = 0
            
    def blitme(self):
        """ draw ship in assigned location """
        self.screen.blit(self.image, self.rect)
