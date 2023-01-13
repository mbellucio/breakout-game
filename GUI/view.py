import pygame, sys
from GUI.paddleUI import PaddleUI
from GUI.background import Background
from GUI.view_settings import ViewSettings
from GUI.ballUI import BallUI
from GUI.scoreUI import ScoreUI
from GUI.instructions import Instructions


class View:

    def __init__(self, scorepoint:int):
        pygame.init()
        self.settings = ViewSettings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.paddle_ui = PaddleUI(
            paddle_image= self.settings.paddle_image,
        )
        self.ball_ui = BallUI(
            ball_image= self.settings.ball_image,
        )
        self.background = Background(
            background_image= self.settings.background_image,
            position= self.settings.background_position
        )
        self.clock = pygame.time.Clock()
        self.score = ScoreUI(
            text=self.settings.score_text,
            score=scorepoint,
        )
        self.instructions = []
        

    def show_instruction(self, text:str, position:tuple, font_size:int):
        instruction = Instructions(
            text=text,
            position=position,
            size=font_size
        )
        self.instructions.append(instruction)
        

    def clear_instructions(self):
        self.instructions = []


    def refresh_screen(self, ball:object, paddle:object, targets:dict):
        self.screen.blit(self.background.background, self.background.position)
        self.screen.blit(self.ball_ui.image, ball)
        self.screen.blit(self.paddle_ui.image, paddle)
        self.screen.blit(self.score.score_text, self.settings.score_position)
        for image in targets:
            self.screen.blit(image.image, targets[image].target)
        for instruction in self.instructions:
            self.screen.blit(instruction.instruction, instruction.pos)
        pygame.display.update()
        self.clock.tick(self.settings.framerate)


    def quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


