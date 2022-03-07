import pygame

pygame.mixer.init()

pygame.mixer.music.load('sounds/BoxCat Games - Assignment.mp3')
pygame.mixer.music.play(-1)


# Constants
class Constants:
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 670
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    COLOR_BLACK = (0, 0, 0)
    COLOR_WHITE = (255, 255, 255)

    BACKGROUND_STARS_1_SPEED = 1
    BACKGROUND_STARS_2_SPEED = 2

    FPS = 60
    FONT = 'assets/Pixeltype.ttf'

    ROLLING = 0
    PAUSED = 1


game_1 = 0

paddle_sound = pygame.mixer.Sound('sounds/paddle.wav')
wall_sound = pygame.mixer.Sound('sounds/ball.wav')
player_collided_sound = pygame.mixer.Sound('sounds/smw_coin.wav')

# Global Variables
game_loop = True

ball_speed_x = 7
ball_speed_y = 7
ball_moving_left = False
ball_moving_down = False

player_1_speed = 10
player_1_moving_up = False
player_1_moving_down = False
player_1_score = 0
player_1_status = 0

player_2_speed = 10
player_2_moving_up = False
player_2_moving_down = False
player_2_score = 0
player_2_status = 0
