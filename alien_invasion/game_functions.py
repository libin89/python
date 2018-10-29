import sys
import pygame
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings, screen, ship, bullets):
    # create a bullet and add to group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def check_events(ai_settings, screen, ship, bullets):
    """respond keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)
            
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update screen's image, and switch to new screen"""
    # redraw screen every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    
    #redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    
        
    # let screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """ update bullet location and remove disappeared bullets"""
    # update bullets location
    bullets.update()
    # remove disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """ caculate alien counts in one line """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

    
def create_fleet(ai_settings, screen, aliens):
    """ create alien group """
    # create an alien and caclulate alien counts in one line
    # interval of aliens is alien's width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    # create a line aliens
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)
    
