from config import *
from ball import *
from player import *

def verify_score():
    global ball_x, ball_y, ball_dx, ball_dy, score_1, score_2

    if ball_x < -50:
        ball_x = 640
        ball_y = 360
        ball_dy *= -1
        ball_dx *= -1
        score_2 += 1
    elif ball_x > 1320:
        ball_x = 640
        ball_y = 360
        ball_dy *= -1
        ball_dx *= -1
        score_1 += 1


def collision_player_wall(player_y):
    # player collides with upper wall
    if player_y <= 0:
        return  0

    # player collides with lower wall
    elif player_y >= 570:
        return 570
    
    return player_y
    