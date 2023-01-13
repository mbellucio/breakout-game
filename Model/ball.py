import pygame


class Ball:

    def __init__(self, speed:int, ball_image:object, starting_position:tuple):
        self.ball = ball_image.get_rect()
        self.ball_base_speed = speed
        self.x_speed = self.ball_base_speed
        self.y_speed = self.ball_base_speed
        self.ball = self.ball.move(starting_position)
    
    def move_ball(self):
        self.ball = self.ball.move((self.x_speed, self.y_speed))

    def invert_y(self):
        self.y_speed = self.y_speed * -1

    def invert_x(self):
        self.x_speed = self.x_speed * -1

    def bounce(self, coordinates:tuple):
        self.x_speed = self.ball_base_speed * coordinates[0]
        self.y_speed = self.ball_base_speed * coordinates[1]
        self.invert_y()

    def start(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.x_speed = 0
            self.y_speed = self.ball_base_speed * -1
            return True