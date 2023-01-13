import pygame

class Background:

    def __init__(self, background_image:str, position:tuple):
        self.background = pygame.image.load(background_image)
        self.bg = self.background.get_rect()
        self.position = position
