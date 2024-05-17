import pygame
import sys
from Config import config
import random

def move_rocket(x_coordinate):
    """Funkcia na zistenie pohybu rakety"""

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x_coordinate > 10: # Aby raketa nešla za ľavý okraj
            x_coordinate -= config.STEP # Pohyb rakety vľavo
    if keys[pygame.K_RIGHT]:
        if x_coordinate < 480: # Aby raketa nešla za pravý okraj
            x_coordinate += config.STEP  # Pohyb rakety vpravo
    return x_coordinate

def generate_meteor():
    """Funkcia bude generovať meteor na náhodnom mieste"""

    return {'x': random.choice(range(10, 440, 50)),
            'y': random.choice(range(-10, -500, -50))
           }

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock() # Objekt

    window = pygame.display.set_mode(config.ROZLISENIE)
    pozadie = config.POZADIE
    raketa = config.RAKETA
    meteor_image = config.METEOR # Musíme premenovať meteor na napr. meteor_image, lebo nižšie používame cyklus for meteor in meteory:
    font_hry = config.FONT_HRY

    x = config.SURADNICE_RAKETY[0] # Inicializácia x-súradnice rakety

    score = 0
    meteory = []

    for i in range(5):
        meteory.append(generate_meteor())

    while True:
        score_text = font_hry.render(f"SKÓRE: {score}", True, config.FARBA_TEXTU)
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu
        
        x = move_rocket(x)
        
        window.blit(pozadie, (0, 0))
        window.blit(raketa, (x, config.SURADNICE_RAKETY[1]))

        for meteor in meteory:
            window.blit(meteor_image, (meteor['x'], meteor['y']))
            meteor['y'] += 2  # Pád meteoru   # predtým sme mali def falling_meteor
        
        window.blit(score_text, config.POZICIA_TEXTU)

        pygame.display.update()

        clock.tick(config.FPS)
