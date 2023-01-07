from turtle import Screen
from targets import Targets
from paddle import Paddle
from ball import Ball
from score import Score
from info import StartInstruction, GameOver
import time


#------------- Screen Config --------------#

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)
screen.listen()


#------------- Class Initializations --------------#

targets = Targets()
paddle = Paddle()
ball = Ball()
score = Score()
instruction = StartInstruction()
end_game = GameOver()

#------------- Event listeners --------------#

screen.onkeypress(fun=paddle.move_right, key='Right')
screen.onkeypress(fun=paddle.move_left, key='Left')
screen.onkeypress(fun=ball.start_ball, key='w')

#--------------- Set difficulty (speed) ----#

def set_difficulty():
    speed = targets.hit_color()
    match speed:
        case 3:
            return time.sleep(0.01)
        case 2: 
            return time.sleep(0.008)
        case 1: 
            return time.sleep(0.005)
        case 0:
            return time.sleep(0.002)


#------------- Game Loop --------------#

game_on = False
game_on_waiting = True

while game_on_waiting:
    time.sleep(0.01)
    screen.update()
    ball.starting_position(paddle)
    if ball.start:
        game_on = True
        game_on_waiting = False
        instruction.remove_info()

while game_on:
    score.refresh_score()
    set_difficulty()
    screen.update()
    ball.move_ball()
    if ball.horizontal_collision():
        ball.bounce_horizontal()
    if ball.vertical_collision() or ball.collision_with_paddle(paddle):
        ball.bounce_vertical()
    if targets.target_hit(ball):
        ball.bounce_vertical()
        score.point(targets.hit_color())
    if ball.ball_hit_player_side():
        end_game.end_game()
        break
    
#--------------------
screen.exitonclick()
#--------------------



