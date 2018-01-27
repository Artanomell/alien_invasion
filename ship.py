import pygame
import settings


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.centerx < self.screen_rect.centerx + 470:
            self.rect.centerx += 1
        if self.moving_left and self.rect.centerx > self.screen_rect.centerx - 470:
            self.rect.centerx -= 1
