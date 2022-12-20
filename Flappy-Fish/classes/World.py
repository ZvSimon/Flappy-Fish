from random import randint
from time import time

import pygame

from classes import Tuyau as ty
from constantes import *
from fonctions import retourner_temps


class World:  # tout draw et tout update
    def __init__(self, player):

        self.tuyau_actif = []
        self.player = player
        self.sprite_actif = pygame.sprite.Group(self.player)
        self.background = pygame.image.load("./ressources/ciel.png")

        self.score = 0
        self.t = time()
        self.delai = time()
        self.debut = time()
        self.last = (hauteur_tuyau_initiale, hauteur_tuyau_initiale)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        minutes, secondes = retourner_temps(time() - self.debut)

        for tuyau in self.tuyau_actif:
            tuyau.draw(screen)
        self.sprite_actif.draw(screen)

        screen.blit(
            pygame.font.Font(None, 75).render(
                f"{self.score}",
                1, (0, 0, 0)
            ),
            (50, 50)
        )

        screen.blit(
            pygame.font.Font(None, 75).render(
                f"{minutes}:{secondes}",
                1, (0, 0, 0)
            ),
            (WIDTH - 150, 50)
        )

    def nouveau_tuyau(self):
        # hauteur 1 on le randam, on prends la pos d'avant H1 .
        hauteur1 = randint(self.last[0] - 30, self.last[0] + 30)

        ecart = self.score % 12 \
            if (self.score // 12) % 2 \
            else 12 - self.score % 12

        hauteur2 = HEIGHT - hauteur1 * 2 - (ecart * 8)

        # définir un ecart minimum
        if HEIGHT - hauteur2 - hauteur1 < 200:
            hauteur2 -= 150

        # raccourcir les tuyaux s'ils sortent du ch
        if HEIGHT - hauteur2 > HEIGHT:
            hauteur1 -= 20
            hauteur2 += 20

        self.tuyau_actif.append(ty.Tuyau(hauteur1, hauteur2))
        self.last = hauteur1, hauteur2

    def update(self):  # tout les delais entre tuyaux va rajouter un tuyau
        if time() - self.delai >= delai_entre_tuyau:
            self.nouveau_tuyau()
            self.delai = time()

        if (time() - self.t - 2.2) / (self.score + 1) > delai_entre_tuyau:
            # il mets 3,7 s a atteindre la fin du premier, un tuyau se créer tout les s (constantes)
            self.score += 1

        self.sprite_actif.update() #liste de groupe de sprite
        for tuyau in self.tuyau_actif:
            for sprite in tuyau:
                if sprite.rect.x == -300: #si position x == 300 alors on tue le tuyau , car en largeur il compte 300.
                    tuyau.empty()
                sprite.rect.x -= (vitesse + self.score) // fps 
            if pygame.sprite.spritecollide(self.player, tuyau, False): # si colision alors mort.
                self.player.kill()
                return True

        return False
