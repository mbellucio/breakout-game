import pygame

class BallUI:

    def __init__(self, ball_image:str):
        self.image = pygame.image.load(ball_image)
        