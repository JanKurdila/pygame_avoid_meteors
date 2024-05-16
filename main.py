import pygame
import sys
from Config import config

def move_rocket(x_coordinate):
    "Funkcia na zistenie pohybu rakety"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x_coordinate > 10: # Aby raketa nešla za ľavý okraj
            x_coordinate -= config.STEP # Pohyb rakety vľavo
    if keys[pygame.K_RIGHT]:
        if x_coordinate < 480: # Aby raketa nešla za pravý okraj
            x_coordinate += config.STEP  # Pohyb rakety vpravo
    return x_coordinate

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock() # Objekt

    window = pygame.display.set_mode(config.ROZLISENIE)
    pozadie = config.POZADIE
    raketa = config.RAKETA

    x = config.SURADNICE_RAKETY[0] # Inicializácia x-súradnice rakety

    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu
        
        x = move_rocket(x)

        window.blit(pozadie, (0, 0))
        # window.blit(raketa, config.SURADNICE_RAKETY) Tu musíme upraviť lebo nastáva phyb
        window.blit(raketa, (x, config.SURADNICE_RAKETY[1]))

        pygame.display.update()

        clock.tick(config.FPS)