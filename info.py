from turtle import Turtle


class StartInstruction(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.info_start()

    def info_start(self):
        self.goto(0, -150)
        self.write(
            arg='Press "w" to start',
            align='center',
            font=('courier', 16, 'bold')
        )
    
    def remove_info(self):
        self.clear()


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()


    def end_game(self):
        self.goto(0, -120)
        self.write(
            arg='Game Over',
            align='center',
            font=('courier', 26, 'bold')
        )
