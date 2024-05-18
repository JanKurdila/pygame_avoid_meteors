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
        if x_coordinate < config.ROZLISENIE[0] - config.RAKETA.get_width() - 10:  # Aby raketa nešla za pravý okraj
            x_coordinate += config.STEP  # Pohyb rakety vpravo
    return x_coordinate

def generate_meteor(meteor_image):
    """Funkcia bude generovať meteor na náhodnom mieste"""
    return {'x': random.choice(range(10, config.ROZLISENIE[0] - meteor_image.get_width(), 50)),
            'y': random.choice(range(-10, -500, -50)),
            'mask': pygame.mask.from_surface(meteor_image)}

def is_collision(mask1, mask2, mask1_coordinate, mask2_coordinate):
    """Funkcia zistí či nastala kolízia meteoru a rakety"""
    x_off = mask2_coordinate[0] - mask1_coordinate[0]
    y_off = mask2_coordinate[1] - mask1_coordinate[1]
    return mask1.overlap(mask2, (x_off, y_off)) is not None

def generate_special_item(special_image):
    """Funkcia bude generovať špeciálny objekt na náhodnom mieste"""
    return {
        'x': random.choice(range(10, config.ROZLISENIE[0] - special_image.get_width(), 50)),
        'y': random.choice(range(-10, -500, -50)),
        'mask': pygame.mask.from_surface(special_image)
    }

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()  # Objekt

    window = pygame.display.set_mode(config.ROZLISENIE)
    pozadie = config.POZADIE
    raketa = config.RAKETA
    meteor_image = config.METEOR  # Musíme premenovať meteor na napr. meteor_image, lebo nižšie používame cyklus for meteor in meteory:
    special_image = config.SPEC_OBR
    font_hry = config.FONT_HRY

    # Ideme riešiť kolíziu rakety a meteoru
    maska_rakety = pygame.mask.from_surface(raketa)

    x = config.SURADNICE_RAKETY[0]  # Inicializácia x-súradnice rakety

    score = 0
    meteory = []
    special_items = []

    koniec_hry = False   # Ukončenie hry
    

    while True:
        keys = pygame.key.get_pressed()
        score_text = font_hry.render(f"SKÓRE: {score}", True, config.FARBA_TEXTU)

        if len(meteory) == 0:
            config.RYCHLOST_PADU_METEORU += 1
            config.POCET_METEOROV += config.METEOR_INKREMENT
            for i in range(config.POCET_METEOROV):
                meteory.append(generate_meteor(meteor_image))
            config.POCET_ITERACII_METEOROV += 1

        if config.POCET_ITERACII_METEOROV % 3 == 0:
            special_items.append(generate_special_item(special_image))
            config.POCET_ITERACII_METEOROV += 1  # Zabezpečí, že sa špeciálny objekt objaví iba každé dve iterácie

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        x = move_rocket(x, keys)

        window.blit(pozadie, (0, 0))
        window.blit(raketa, (x, config.SURADNICE_RAKETY[1]))

        if not koniec_hry:
            for meteor in meteory[:]:
                window.blit(meteor_image, (meteor['x'], meteor['y']))
                meteor['y'] += config.RYCHLOST_PADU_METEORU
                if meteor['y'] > config.ROZLISENIE[1]:
                    score += 1
                    meteory.remove(meteor)
                if is_collision(maska_rakety, meteor['mask'], (x, config.SURADNICE_RAKETY[1]), (meteor['x'], meteor['y'])):
                    koniec_hry = True

            for item in special_items[:]:
                window.blit(special_image, (item['x'], item['y']))
                item['y'] += config.RYCHLEJSIA_RYCHLOST_PADU  
                if item['y'] > config.ROZLISENIE[1]:
                    special_items.remove(item)
                if is_collision(maska_rakety, item['mask'], (x, config.SURADNICE_RAKETY[1]), (item['x'], item['y'])):
                    score += 10
                    special_items.remove(item)
                
        if koniec_hry:
            text_na_konci_hry = font_hry.render(f"GAME OVER", True, config.FARBA_TEXTU)
            window.blit(text_na_konci_hry, config.POZICIA_TEXTU_KONCA_HRY)

        window.blit(score_text, config.POZICIA_TEXTU)

        pygame.display.update()
        clock.tick(config.FPS)
