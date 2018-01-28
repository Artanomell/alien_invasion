import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_funcions


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()

    pygame.display.set_caption("Alien Invasion")

    bg_color = ai_settings.bg_color
    while True:
        game_funcions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        game_funcions.update_screen(ai_settings, screen, ship, bullets)
        # screen.fill(bg_color)
        # ship.blitme()

        # for event in pygame.event.get():
        # game_funcions.check_events(ship)
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        # pygame.display.flip()


run_game()
