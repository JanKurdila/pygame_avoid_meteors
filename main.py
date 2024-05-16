import pygame
import sys
from Config import config

if __name__ == "__main__":
    pygame.init()

    window = pygame.display.set_mode(config.ROZLISENIE)
    pozadie = config.pozadie
    raketa = config.raketa

    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu

        window.blit(pozadie, (0, 0))
        window.blit(raketa, config.suradnice_rakety)

        pygame.display.update()