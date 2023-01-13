import pygame

class Instructions:
    
    def __init__(self, text:str, position:tuple, size:int):
        self.font = pygame.font.SysFont('courier', size)
        self.text = text
        self.pos = position
        self.instruction = self.font.render(self.text, True, (255,255,255))
    
