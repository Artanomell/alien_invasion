import sys

import pygame


def check_events():
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
