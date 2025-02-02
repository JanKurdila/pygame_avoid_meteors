import pygame

ROZLISENIE = (580, 780)

POZADIE = pygame.image.load("IMAGES/pozadie.jpg")
RAKETA = pygame.image.load("IMAGES/raketa.png")
METEOR = pygame.image.load("IMAGES/meteor1.png")
SPEC_OBR = pygame.image.load("IMAGES/t.jpg")
RYCHLOST_PADU_METEORU = 0
METEOR_INKREMENT = 4
POCET_METEOROV = 0
POCET_ITERACII_METEOROV = 0 # aby som generoval pad špec. obrázka napr. po každej druhej iteraci meteorov

SURADNICE_RAKETY = (250, 685)
# SURADNICE_METEORU = (250, 30) už nepotrebujeme, lebo ich bude generovať funkcia

POZICIA_TEXTU_KONCA_HRY = (175, 400)

RYCHLEJSIA_RYCHLOST_PADU = 4

FPS = 25
STEP = 5

pygame.init()
FONT_HRY = pygame.font.SysFont("comicsans", 50)
FARBA_TEXTU = pygame.Color(255, 255, 255)
POZICIA_TEXTU = (280, 10)