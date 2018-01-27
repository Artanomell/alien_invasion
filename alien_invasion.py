import pygame
import sys

from settings import Settings
from ship import Ship
import game_funcions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_hight))
    ship = Ship(screen)

    pygame.display.set_caption("Alien Invasion")

    bg_color = ai_settings.bg_color
    while True:
        gf.check_events()
        for event in pygame.event.get():
            screen.fill(bg_color)
            ship.blitme()


        pygame.display.flip()

run_game()

