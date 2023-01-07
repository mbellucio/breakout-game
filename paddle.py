from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.speed = 18
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.goto(0, -280)
        self.color('white')

    def move_right(self):
        if not self.xcor() > 313:
            new_x = self.xcor() + self.speed
            self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        if not self.xcor() < -320:
            new_x = self.xcor() - self.speed
            self.goto(x=new_x, y=self.ycor())

