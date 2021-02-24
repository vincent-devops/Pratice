import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # ship.rect.centery -= 1
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                # ship.rect.centery += 1
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False