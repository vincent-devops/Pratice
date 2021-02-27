import sys
import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        # ship.rect.centery -= 1
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # ship.rect.centery += 1
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)

def update_bullets(bullets, ai_settings, ship):
    bullets.update()
    for bullet in bullets.copy():
        # print(bullet.rect.centery)
        # print("ship -->", ship.rect.centery)
        # print("bullet-->", bullet.rect.centery)
        if bullet.rect.centerx >= ai_settings.screen_width:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    # 当按下一次空格键时，创建一颗子弹，并将其加入到编组bullets中
    # print("--start fire--")
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()