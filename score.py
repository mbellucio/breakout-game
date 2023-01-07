from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score = 0 
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(x=260, y=260)
        self.write(
            arg=f'Score:{self.score}',
            align='center',
            font=('courier', 30, 'bold')
        )

    def point(self, target_color):
        match target_color:
            case 3:
                self.score += 10
            case 2:
                self.score += 30
            case 1: 
                self.score += 60
            case 0:
                self.score += 100
            