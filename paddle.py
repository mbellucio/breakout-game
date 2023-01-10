from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.base_speed = 20
        self.move_speed = 20
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.scren_pos = (0, -280)
        self.goto(self.scren_pos)
        self.speed_color = {
            'purple': 1.5,
            'red': 1.3,
            'green': 1.1,
            'white': 1
        }


    def move_right(self):
        if not self.xcor() >= 320:
            new_x = self.xcor() + self.move_speed
            self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        if not self.xcor() <= -320:
            new_x = self.xcor() - self.move_speed
            self.goto(x=new_x, y=self.ycor())

    def paddle_speed(self, tgt_color):
        self.move_speed = self.base_speed * (self.speed_color[tgt_color])
    
    
