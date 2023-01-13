

class ViewSettings:

    def __init__(self):
        #screen
        self.screen_size = (1000, 800)
        self.framerate = 60
        #images
        self.ball_image = 'Assets/Images/ball.png'
        self.paddle_image = 'Assets/Images/paddle.jpg'
        self.background_image = 'Assets/Images/bg_image.jpg'
        #positions
        self.background_position = (0, 0)
        #targets
        self.target_images = {
            'target_1': 'Assets/Images/purple_target.png',
            'target_2': 'Assets/Images/red_target.png',
            'target_3': 'Assets/Images/yellow_targets.png',
            'target_4': 'Assets/Images/green_target.png'
        }
        #score
        self.score_font_propperties = {
            'font_name': 'monospace',
            'font_size': 50,
            'bold': True,
            'anti_alias': True,
            'color': (255, 255, 255)
        }
        self.score_text = 'Score:'
        self.score_position = (750, 30)

        self.game_over_text = 'Game Over'
        self.game_over_pos = (350, 500)
        self.game_over_size = 60

        self.restart_text = 'Press "r" to restart'
        self.restart_pos = (385, 575)
        self.restart_size = 22

        self.start_text = 'Press "up" to start'
        self.start_pos = (385, 500)
        self.start_size = 22

        self.game_win_text = 'You Won!'
        self.game_win_pos = (350, 500)
        self.game_win_size = 60