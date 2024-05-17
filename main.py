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

def falling_meteor(meteor_y):
    meteor_y  += 3
    return meteor_y


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock() # Objekt

    window = pygame.display.set_mode(config.ROZLISENIE)
    pozadie = config.POZADIE
    raketa = config.RAKETA
    meteor = config.METEOR
    font_hry = config.FONT_HRY

    x = config.SURADNICE_RAKETY[0] # Inicializácia x-súradnice rakety
    y = config.SURADNICE_METEORU[1] # Inicializácia y-súradnice meteoru

    score = 0

    while True:
        score_text = config.FONT_HRY.render(f"SKÓRE: {score}", True, config.FARBA_TEXTU)
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu
        
        x = move_rocket(x)
        y = falling_meteor(y)

        window.blit(pozadie, (0, 0))
        # window.blit(raketa, config.SURADNICE_RAKETY) Tu musíme upraviť lebo nastáva phyb
        window.blit(raketa, (x, config.SURADNICE_RAKETY[1]))
        window.blit(meteor, (config.SURADNICE_METEORU[0], y))
        window.blit(score_text, config.POZICIA_TEXTU)

        pygame.display.update()

        clock.tick(config.FPS)