

class Target:
    def __init__(self, color:str, target_image:object):
        self.target_color = color
        self.target = target_image.get_rect()

    def target_move(self, position:tuple):
        self.target = self.target.move(position)
