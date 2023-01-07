from turtle import Turtle


class Target(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=4.2, stretch_wid=0.8)


class Targets:

    def __init__(self):
        self.white_tgt = []
        self.green_tgt = []
        self.red_tgt = []
        self.purple_tgt = []
        self.targets = [self.purple_tgt, self.red_tgt, self.green_tgt, self.white_tgt]
        self.colors = ['purple', 'red', 'green', 'white']
        self.n_targets = 8
        self.row_counter = 0
        self.x = -350
        self.y = 220
        self.generate_targets()
        self.current_hit_color = 3

    def generate_targets(self):
        for item in self.targets:
            idx = self.targets.index(item)
            color = self.colors[idx]

            match color:
                case 'red':
                    self.n_targets = 16
                case 'green': 
                    self.n_targets = 16
                case 'white':
                    self.n_targets = 24

            for i in range(0, self.n_targets):
                target = Target()
                self.targets[idx].append(target)

            for obj in self.targets[idx]:
                if self.row_counter == 8:
                    self.x = -350
                    self.y -= 25
                    self.row_counter = 0
                obj.color(color)
                obj.goto(self.x, self.y)
                self.row_counter += 1
                self.x += 99
            self.x = -350

    def target_hit(self, ball):
        for target_list in self.targets:
            for target in target_list:
                if target.distance(ball) <= 64 and (target.ycor() - ball.ycor()) < 20 and (target.ycor() - ball.ycor()) > -20:
                    target.goto(1000,1000)
                    self.current_hit_color = self.targets.index(target_list)
                    return True

    def hit_color(self):
        return self.current_hit_color








































