import sys

import pygame


def check_events(ship):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = True
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = True
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False

def check_keydown_events(event, ship):
    """Respond to keypresses"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True

def check_keyup_events(event, ship):
    """Respond to releases"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def update_screen(bg_color, screen, ship):
    """Обновляеет отображение на экране и отображает новый экрын"""
    screen.fill(bg_color)
    ship.blitme()

    #Отображение последнего прорисованного экрана
    pygame.display.flip()
