import pygame
import sys
from Config import config
import random

def move_rocket(x_coordinate, keys):
    """Funkcia na zistenie pohybu rakety"""
    if keys[pygame.K_LEFT]:
        if x_coordinate > 10:  # Aby raketa nešla za ľavý okraj
            x_coordinate -= config.STEP  # Pohyb rakety vľavo
    if keys[pygame.K_RIGHT]:
        if x_coordinate < 480:  # Aby raketa nešla za pravý okraj
            x_coordinate += config.STEP  # Pohyb rakety vpravo
    return x_coordinate

def generate_meteor(meteor_image):
    """Funkcia bude generovať meteor na náhodnom mieste"""
    return {'x': random.choice(range(10, 440, 50)),
            'y': random.choice(range(-10, -500, -50)),
            'mask': pygame.mask.from_surface(meteor_image)}

def is_collision(mask1, mask2, mask1_coordinate, mask2_coordinate):
    """Funkcia zistí či nastala kolízia meteoru a rakety"""
    x_off = mask2_coordinate[0] - mask1_coordinate[0]
    y_off = mask2_coordinate[1] - mask1_coordinate[1]
    if mask1.overlap(mask2, (x_off, y_off)):  # Funkcia overlap zisťuje prekrytie masiek
        return True
    return False

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()  # Objekt

    window = pygame.display.set_mode(config.ROZLISENIE)
    pozadie = config.POZADIE
    raketa = config.RAKETA
    meteor_image = config.METEOR  # Musíme premenovať meteor na napr. meteor_image, lebo nižšie používame cyklus for meteor in meteory:
    font_hry = config.FONT_HRY

    # Ideme riešiť kolíziu rakety a meteoru
    maska_rakety = pygame.mask.from_surface(raketa)

    x = config.SURADNICE_RAKETY[0]  # Inicializácia x-súradnice rakety

    score = 0
    meteory = []

    while True:
        keys = pygame.key.get_pressed()
        score_text = font_hry.render(f"SKÓRE: {score}", True, config.FARBA_TEXTU)

        if len(meteory) == 0:
            config.RYCHLOST_PADU_METEORU += 1
            config.POCET_METEOROV += config.METEOR_INKREMENT
            for i in range(config.POCET_METEOROV):
                meteory.append(generate_meteor(meteor_image))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        x = move_rocket(x, keys)

        window.blit(pozadie, (0, 0))
        window.blit(raketa, (x, config.SURADNICE_RAKETY[1]))

        for meteor in meteory[:]:
            window.blit(meteor_image, (meteor['x'], meteor['y']))
            meteor['y'] += config.RYCHLOST_PADU_METEORU
            if meteor['y'] > config.ROZLISENIE[1]:
                score += 1
                meteory.remove(meteor)
            if is_collision(maska_rakety, meteor['mask'], (x, config.SURADNICE_RAKETY[1]), (meteor['x'], meteor['y'])):
                print("GAME OVER")

        window.blit(score_text, config.POZICIA_TEXTU)

        pygame.display.update()
        clock.tick(config.FPS)
