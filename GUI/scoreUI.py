import pygame

class ScoreUI:
    def __init__(self, text:str, score:int):
        self.font = pygame.font.SysFont(None, 50)
        self.score = score
        self.text = text
        self.score_text = self.font.render(self.text, True, (255,255,255))

    def refresh_score(self):
        render_score = f'{self.text} {self.score}'
        self.score_text = self.font.render(render_score, True, (255,255,255))

