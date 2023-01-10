from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.default_speed = 3.5
        self.speed = 3.5
        self.x_move = 3.5
        self.y_move = 3.5
        self.speed_color = {
            'purple': 1.8,
            'red': 1.5,
            'green': 1.25, 
            'white': 1
        }

    def move_ball(self):
        new_x = self.x_move + self.xcor()
        new_y = self.y_move + self.ycor() 
        self.goto(x=new_x, y=new_y)
 
    def invert_x(self):
        self.x_move *= -1    

    def invert_y(self):
        self.y_move *= -1

    def bounce_paddle_53(self):
        self.x_move = self.speed * 0.75
        self.y_move = self.speed * 1.25

    def bounce_paddle_45(self):
        self.x_move = self.speed * 1
        self.y_move = self.speed * 1
        
    def bounce_paddle_37(self):
        self.x_move = self.speed * 1.25
        self.y_move = self.speed * 0.75

    def bounce_paddle_corner(self):
        self.x_move = (self.speed + 1) * 1.75
        self.y_move = (self.speed + 1) * 0.25

    def bounce_paddle_up(self):
        self.x_move = self.speed * 0.1
        self.y_move = self.speed * 1.5

    def ball_speed(self, tgt_color):
        self.speed = self.default_speed * (self.speed_color[tgt_color])
    
    


