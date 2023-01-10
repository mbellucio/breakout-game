from turtle import Turtle


class Target(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=4.2, stretch_wid=0.5)
        self.tgt_color = ''
        # size width: 84 // size heigh: 16


class Targets:

    def __init__(self):
        self.x_pos = -354
        self.y_pos = 200
        self.targets = []
        self.xspace = 100
        self.yspace = 18
        self.tgt_colors = {
            'purple': 16,
            'red': 16,
            'green': 24,
            'white': 24, 
        }
        self.create_targets()

    def create_targets(self):
        for item in self.tgt_colors:
            counter = 0
            for i in range(0, self.tgt_colors[item]):
                target = Target()
                target.tgt_color = str(item)
                target.color(target.tgt_color)
                target.goto(self.x_pos, self.y_pos)
                self.targets.append(target)
                self.x_pos += self.xspace
                counter += 1
                if counter == 8:
                    self.y_pos -= self.yspace
                    self.x_pos = -354
                    counter = 0
            # self.y_pos -= self.yspace
            self.x_pos = -354

    def delete_target(self, target):
        target.goto(1000,1000)































