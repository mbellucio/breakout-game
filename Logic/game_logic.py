from Model.ball import Ball
from Model.paddle import Paddle
from Model.target import Target
from Model.score import Score
from GUI.targetsUI import TargetUI
from GUI.view import View
from Logic.settings import Settings
from Mixer.mixer import Mixer
from math import floor
import pygame


class GameLogic:

    def __init__(self):
        self.mixer = Mixer()
        self.score = Score()
        self.view = View(self.score.score)
        self.settings = Settings()
        self.ball = Ball(
            speed= self.settings.ball_base_speed,
            ball_image= self.view.ball_ui.image,
            starting_position= self.settings.ball_starting_position,
        )
        self.paddle = Paddle(
            move_speed= self.settings.paddle_speed,
            paddle_image= self.view.paddle_ui.image,
            starting_position= self.settings.paddle_starting_position
        )
        self.targets = {}
        self.create_targets()
        self.game_start = False
        self.staging_area = True
        self.staging_instruction = False
        self.game_over = False
        self.game_win = False


    def create_targets(self):
        target_posx = self.settings.targets_starting_position[0]
        target_posy = self.settings.targets_starting_position[1]
        screen_width = self.view.settings.screen_size[0]
        n_targets = floor(screen_width / self.settings.target_size)
        space_between_targets = (screen_width - (self.settings.target_size * n_targets))/(n_targets - 1)
        for color in self.settings.target_propperties:
            for row in range(0, self.settings.target_propperties[color]['rows']):
                for target_creator in range(0, n_targets):
                    image = TargetUI(target_image=self.view.settings.target_images[color])
                    target = Target(
                        color=color,
                        target_image=image.image
                    )
                    target.target_move((target_posx, target_posy))
                    target_posx += (space_between_targets + self.settings.target_size)
                    self.targets[image] = target
                target_posy += self.settings.targets_row_distance
                target_posx = self.settings.targets_starting_position[0]


    def move_paddle_event(self):
         self.paddle.move_paddle(screen_size=self.view.settings.screen_size)


    def wall_collision(self):
        if self.ball.ball.left <= 0 or self.ball.ball.right >= self.view.settings.screen_size[0]:
            self.ball.invert_x()
            self.mixer.play_sf(self.mixer.ball.sound)
        if self.ball.ball.top < 0:
            self.ball.invert_y()
            self.mixer.play_sf(self.mixer.ball.sound)
        

    def handle_bounce(self, hit_part:tuple):
        self.ball.bounce(hit_part)
        if self.ball.ball.midbottom[0] - self.paddle.paddle.midtop[0] < 0: 
            self.ball.invert_x()
        

    def add_points(self, target:str):
        self.score.add_score(points=self.settings.target_propperties[target]['point']) 
        self.view.score.score = self.score.score


    def ball_speed(self, target:str):
        self.ball.ball_base_speed = self.settings.target_propperties[target]['speed']


    def ball_collide_target(self):
        for item in self.targets:
            target = self.targets[item]
            if self.ball.ball.colliderect(target.target):
                self.ball.invert_y()
                target.target_move((2000,2000))
                self.add_points(target.target_color)
                self.ball_speed(target.target_color)
                self.mixer.play_sf(self.mixer.target.sound)
                self.view.score.refresh_score()


    def ball_collide_paddle(self):
        if self.ball.ball.colliderect(self.paddle.paddle):
            self.mixer.play_sf(self.mixer.ball.sound)
            hit_point = self.ball.ball.midbottom[0] - self.paddle.paddle.midtop[0]
            hit_side = self.settings.paddle_parts
            ball_angles = self.settings.ball_angle
            if hit_point < 0:
                hit_point *= -1
            if hit_point <= hit_side['edge'] and hit_point > hit_side['side_middle']:
                self.handle_bounce(ball_angles['edge'])
            elif hit_point <= hit_side['side_middle'] and hit_point > hit_side['middle']:
                self.handle_bounce(ball_angles['side_middle'])
            else:
                self.handle_bounce(ball_angles['middle'])


    def handle_game_over(self):
        if self.ball.ball.bottom >= self.view.settings.screen_size[1]:
            if self.staging_area == False:
                self.game_start = False
                self.game_over = True
                self.view.show_instruction(
                    text=self.view.settings.game_over_text,
                    position=self.view.settings.game_over_pos,
                    font_size=self.view.settings.game_over_size
                )
                self.view.show_instruction(
                    text=self.view.settings.restart_text,
                    position=self.view.settings.restart_pos,
                    font_size=self.view.settings.restart_size
                )

    def handle_game_win(self):
        if self.score.score == 2430:
            if self.staging_area == False:
                self.game_win = True
                self.game_start = False
                self.view.show_instruction(
                    text=self.view.settings.game_win_text,
                    position=self.view.settings.game_win_pos,
                    font_size=self.view.settings.game_win_size
                )
                self.view.show_instruction(
                    text=self.view.settings.restart_text,
                    position=self.view.settings.restart_pos,
                    font_size=self.view.settings.restart_size
                )


    def handle_staging_area(self):
        self.ball.ball.x = (self.paddle.paddle.x + (self.settings.target_size - 30))
        self.ball.ball.y = self.settings.ball_starting_position[1]
        if self.ball.start():
            self.game_start = True
            self.staging_area = False
        if self.staging_instruction == False:
            self.view.show_instruction(
                text=self.view.settings.start_text,
                position=self.view.settings.start_pos,
                font_size=self.view.settings.start_size
            )
            self.staging_instruction = True

    def restart_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.__init__()


    def game_loop(self):
        self.view.refresh_screen(
            ball=self.ball.ball, 
            paddle=self.paddle.paddle,
            targets=self.targets,
        )
        self.handle_game_over()
        self.handle_game_win()
        if self.game_start:
            self.view.clear_instructions()
            self.wall_collision()
            self.ball_collide_paddle()
            self.ball_collide_target()
            self.ball.move_ball()
            self.move_paddle_event()
        elif self.staging_area:
            self.move_paddle_event()
            self.handle_staging_area()
        elif self.game_over:
            self.restart_event()
        elif self.game_win:
            self.restart_event()

       
    def game(self):
        self.mixer.play_music(sound=self.mixer.music.sound)
        while True:
            self.view.quit_event()
            self.game_loop()
            

 