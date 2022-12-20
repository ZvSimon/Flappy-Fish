from math import pi
from time import time

import pygame

from fonctions import *


class Bird(pygame.sprite.Sprite):  # Sprite
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./ressources/bird.png")
        self.image = pygame.transform.scale(
            self.image,
            (80, 60)
        )  # taille de l'oiseau
        self.rect = (
            self.image.get_rect()
        )  # attribut qui vient de sprite, pour recuperer la hitbox
        self.rect.x = 300  
        self.rect.y = 300  # que le y qui bouge car défilement écran

        self.onjump = time()  # équation horraire utile
        self.vitesse_y = 0

    def jump(self):
        self.onjump = time()  # équation horraire  utile

    def update(self): #mettre a jour la position de l'oiseau.
        self.vitesse_y = vitesse_y(time() - self.onjump, vitesse, pi / 3)
        if self.rect.top <= 0:  # pour pas allez au dehors en haut
            self.rect.top += 1
        elif self.rect.bottom >= HEIGHT:  # pour pas aller en dehors en dessous
            self.rect.bottom += 1
        else:
            self.rect.y += self.vitesse_y // fps
