import pygame

# import tkinter as tk

from classes import World, Bird
from fonctions import *

pygame.init()


def main():
    son = pygame.mixer.Sound("son.wav") #mise du son 
    son2 = pygame.mixer.Sound("son2.wav")
    son2.play()
    pygame.mixer.music.set_volume(0.5)  # Met le volume à 0.5 (moitié)

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Fish")  # Nom de la fenetre

    player = Bird.Bird()
    monde = World.World(player)
    clock = pygame.time.Clock()
    run = True

    monde.nouveau_tuyau()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quitte quand tu mets on mets la croix
                run = False

            if event.type == pygame.KEYDOWN: # si on clique sur espace alors on saute, et un son s'active.
                if event.key == pygame.K_SPACE: 
                    player.jump()
                    son.play()
                    son2.stop()

         # si ca tourne True, alors le joueur a touché un tuyau
        run = not monde.update()
        monde.draw(win)
        clock.tick(fps)
        pygame.display.update()

    return monde.score, monde.debut
