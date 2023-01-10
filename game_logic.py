from ui import GameScreen, Score, FeedbackText
from ball import Ball
from paddle import Paddle
from targets import Targets


class GameLogic:

    def __init__(self):
        self.screen = GameScreen()
        self.score = Score()
        self.feedback_text = FeedbackText()
        self.ball = Ball()
        self.paddle = Paddle()
        self.targets = Targets()
        self.screen.refresh_screen()
        self.paddle_event_listeners()
        self.game_on = False
        self.staging_area = True

    def paddle_event_listeners(self):
        self.screen.event_listeners(function=self.paddle.move_right, key='Right')
        self.screen.event_listeners(function=self.paddle.move_left, key='Left')
        self.screen.event_listeners(function=self.start_game, key='Up')
    
    def ball_collision_paddle(self):
        if self.ball.distance(self.paddle) <= 78 and (self.ball.ycor() - self.paddle.ycor()) <= 20 and self.ball.ycor() > -280:
            return True

    def ball_collision_paddle_rside(self):
        if (self.ball.xcor() - self.paddle.xcor()) > 0:
            return True

    def determine_ball_angle(self):
        dif = self.ball.xcor() - self.paddle.xcor()
        if dif < 0:
            dif *= -1
        if dif <= 80 and dif > 70:
            return self.ball.bounce_paddle_corner()
        elif dif <= 70 and dif > 50:
            return self.ball.bounce_paddle_37()
        elif dif <=50 and dif > 30:
            return self.ball.bounce_paddle_45()
        elif dif <= 30 and dif > 15:
            return self.ball.bounce_paddle_53()
        elif dif <= 15 and dif >= 0:
            return self.ball.bounce_paddle_up()

    def ball_collision_walls(self):
        if self.ball.xcor() >= 380 or self.ball.xcor() <= -380:
            return True
    
    def ball_collision_ceiling(self):
        if self.ball.ycor() > 280:
            return True

    def ball_hit_target(self):
        for target in self.targets.targets:
            if self.ball.distance(target) <= 50 and (self.ball.ycor() - target.ycor()) <= 20 and  (self.ball.ycor() - target.ycor()) >= -20:
                self.ball.invert_y()
                self.ball.ball_speed(target.tgt_color)
                self.score.score_point(target.tgt_color)
                self.paddle.paddle_speed(target.tgt_color)
                self.score.refresh_score()
                self.targets.delete_target(target)

    def ball_staging_area(self):
        self.ball.goto(x=self.paddle.xcor(), y=(self.paddle.ycor() + 20))
                
    def start_game(self):
        self.ball.bounce_paddle_up()
        self.game_on = True
        self.feedback_text.clear_feedback_text()
        self.staging_area = False

    def game_over(self):
        if self.ball.ycor() <= -280:
            return True

    def game_loop(self):
        while self.staging_area:
            self.screen.refresh_screen()
            self.ball_staging_area()
        self.up_start = None
        while self.game_on:
            self.screen.refresh_screen()
            self.ball_hit_target()
            if self.ball_collision_paddle():
                if self.ball_collision_paddle_rside():
                    self.determine_ball_angle()
                else:
                    self.determine_ball_angle()
                    self.ball.invert_x()   
            if self.ball_collision_walls():
                self.ball.invert_x()
            if self.ball_collision_ceiling():
                self.ball.invert_y()
            if self.game_over():
                self.feedback_text.game_over_text()
                break
            self.ball.move_ball()
            

    
        



