from turtle import Screen, Turtle
from time import sleep


class GameScreen:

    def __init__(self):
        self.refresh_rate = 0.000000001
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Breakout')
        self.screen.tracer(0)
        self.screen.listen()

    def exit_on_click(self):
        self.screen.exitonclick()

    def refresh_screen(self):
        sleep(self.refresh_rate)
        self.screen.update()

    def event_listeners(self, function, key):
        self.screen.onkeypress(fun=function, key=key)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()   
        self.score = 0
        self.screen_pos = (240, 250)
        self.goto(self.screen_pos)
        self.point_table = {
            'purple': 100,
            'red': 50,
            'green': 25,
            'white': 10
        }
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(
            arg=f'Score:{self.score}',
            align='center',
            font=('courier', 30, 'bold')
        )
    
    def score_point(self, target_color):
        self.score += self.point_table[target_color]


class FeedbackText(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.screen_pos = (0, -150)
        self.goto(self.screen_pos)
        self.start_instruction()

    def start_instruction(self):
        self.write(
            arg='Press "up" to start',
            align='center',
            font=('courier', 16, 'bold')
        )

    def game_over_text(self):
        self.write(
            arg='Game Over',
            align='center',
            font=('courier', 26, 'bold')
        )

    def clear_feedback_text(self):
        self.clear()

    

