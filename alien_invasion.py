import pygame
import sys

from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_hight))
    ship = Ship(screen)

    pygame.display.set_caption("Alien Invasion")

    bg_color = ai_settings.bg_color
    while True:
        for event in pygame.event.get():
            screen.fill(bg_color)
            ship.blitme()
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

run_game()

