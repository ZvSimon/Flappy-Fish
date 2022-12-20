import pygame


class Platform(pygame.sprite.Sprite):  # pour créer un rectangle qui soit une surface ( code couleur etc)
    def __init__(self, width, height, color):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
