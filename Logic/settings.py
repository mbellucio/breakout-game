

class Settings:

    def __init__(self):
        #Paddle
        self.paddle_speed = 10
        self.paddle_starting_position = (375, 778)
        self.paddle_parts = {
            "edge": 135,
            "side_middle": 95,
            "middle": 25
        }

        #ball
        self.ball_base_speed = 6
        self.ball_starting_position = (500, 755)
        self.ball_angle = {
            "edge": (1.3, 0.7),
            "side_middle": (1, 1),
            "middle": (0.3, 1.2)
        }
        
        #targets
        self.target_size = 150
        self.target_propperties = {
            'target_1': {
                'rows': 2,
                'point': 100,
                'speed': 14            
            },

            'target_2': {
                'rows': 2,
                'point': 50,
                'speed': 12            
            },

            'target_3': {
                'rows': 3,
                'point': 25,
                'speed': 10            
            },

            'target_4': {
                'rows': 3,
                'point': 10,
                'speed': 8            
            },
        }
        self.targets_starting_position = (0, 120)
        self.targets_row_distance = 20
        
        
 