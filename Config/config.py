import pygame

ROZLISENIE = (580, 780)

POZADIE = pygame.image.load("IMAGES/pozadie.jpg")
RAKETA = pygame.image.load("IMAGES/raketa.png")
METEOR = pygame.image.load("IMAGES/meteor1.png")
RYCHLOST_PADU_METEORU = 0

SURADNICE_RAKETY = (250, 685)
# SURADNICE_METEORU = (250, 30) už nepotrebujeme, lebo ich bude generovať funkcia

FPS = 25
STEP = 5

pygame.init()
FONT_HRY = pygame.font.SysFont("comicsans", 50)
FARBA_TEXTU = pygame.Color(255, 255, 255)
POZICIA_TEXTU = (320, 10)