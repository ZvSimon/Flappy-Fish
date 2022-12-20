import pygame

from classes import Platform as pf
from constantes import *


class Tuyau(pygame.sprite.Group):  # classe comme si on avait une liste de sprite
    def __init__(self, hauteur1, hauteur2):
        super().__init__()

        platform = pf.Platform(epaisseur_tuyau, hauteur1, GREEN) #tuyaux du haut
        platform.rect.y = 0
        platform.rect.x = WIDTH
        self.add(platform)
        platform = pf.Platform(
            int(epaisseur_tuyau * 1.3), hauteur_tuyau_initiale // 6, BLACK_GREEN #tuyaux haut embouchures
        )
        platform.rect.y = hauteur1
        platform.rect.x = WIDTH - (int(epaisseur_tuyau * 1.3) - epaisseur_tuyau) // 2
        self.add(platform)
        platform = pf.Platform(
            int(epaisseur_tuyau * 1.3), hauteur_tuyau_initiale // 6, BLACK_GREEN # tuyaux  du bas embouchures
        )
        platform.rect.y = HEIGHT - hauteur_tuyau_initiale // 6 - hauteur2  
        platform.rect.x = WIDTH - (int(epaisseur_tuyau * 1.3) - epaisseur_tuyau) // 2
        self.add(platform)
        platform = pf.Platform(epaisseur_tuyau, hauteur2, GREEN)# tuyaux du bas  
        platform.rect.y = HEIGHT - hauteur2
        platform.rect.x = WIDTH
        self.add(platform)
