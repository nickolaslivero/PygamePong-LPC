import pygame

# Constants
class Constants:
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 670
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    COLOR_BLACK = (0, 0, 0)
    COLOR_WHITE = (255, 255, 255)

    BACKGROUND_STARS_1_SPEED = 2
    BACKGROUND_STARS_2_SPEED = 3

    FPS = 60
    FONT = 'assets/PressStart2P.ttf'

# Global Variables
game_loop = True

ball_speed_x = 7
ball_speed_y = 7
ball_moving_left = False
ball_moving_down = False

player_1_speed = 10
player_1_moving_up = False
player_1_moving_down = False

player_2_speed = 10
player_2_moving_up = False
player_2_moving_down = False