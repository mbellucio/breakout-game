from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.start = False
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = 7
        self.y_move = 7

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def start_ball(self):
        self.start = True

    def starting_position(self, paddle_pos):
        self.goto(paddle_pos.xcor(), (paddle_pos.ycor() + 22))

    def horizontal_collision(self):
        if self.xcor() > 385 or self.xcor() < -385:
            return True

    def vertical_collision(self):
        if self.ycor() > 285:
            return True
        
    def ball_hit_player_side(self):
        if self.ycor() < -285:
            return True

    def bounce_horizontal(self):
        self.x_move *= -1

    def bounce_vertical(self):
        self.y_move *= -1

    def collision_with_paddle(self, paddle):
        if self.distance(paddle) <= 90 and self.ycor() < -258:
            return True


