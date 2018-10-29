import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    # initialize game and create a window object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(ai_settings, screen)
    # create bullet group
    bullets = Group()
    # create a alien group
    aliens = Group()

    # create alien group
    gf.create_fleet(ai_settings, screen, aliens)

    # create an object to help track time
    clock = pygame.time.Clock()
    
    # start game mianloop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        clock.tick(ai_settings.frames_per_second)
        
run_game()
