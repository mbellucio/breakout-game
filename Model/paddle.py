import pygame


class Paddle:

    def __init__(self, move_speed:int, paddle_image:object, starting_position:tuple):
        self.paddle = paddle_image.get_rect()
        self.paddle_move_speed = move_speed
        self.paddle = self.paddle.move(starting_position)
        
    def move_right(self):
        return (self.paddle_move_speed, 0)

    def move_left(self):
        return ((self.paddle_move_speed * -1), 0)

    def move_paddle(self, screen_size:tuple):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.paddle.left > 0:
            self.paddle = self.paddle.move(self.move_left())
        if keys[pygame.K_RIGHT] and self.paddle.right < screen_size[0]: 
            self.paddle = self.paddle.move(self.move_right())

