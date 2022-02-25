import pygame
from pygame.locals import *
from sys import exit
from config import *
from ball import *
from player import *
from game import *

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MyPong - PyGame Edition - 2021.01.30")

# sound effects
bounce_sound_effect = pygame.mixer.Sound('sounds/bounce.wav')

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)


# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

def command_keys():
    global player_1_y
    global player_2_y
   #  keystroke events
    keys = pygame.key.get_pressed()
    
    if keys[K_w]:
        player_1_y -= 5    
    if keys[K_s]:
        player_1_y += 5
    if keys[K_UP]:
        player_2_y -= 5    
    if keys[K_DOWN]:
        player_2_y += 5


def draw_screen_victory(screen):
    screen.fill(COLOR_BACKGROUNG)
    screen.blit(score_text, score_text_rect)
    screen.blit(victory_text, victory_text_rect)

def draw_objects(screen):
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(player_1, (50, player_1_y))
    screen.blit(player_2, (1180, player_2_y))
    screen.blit(score_text, score_text_rect)


def collision_ball_wall():
    global ball_dy

    if ball_y > 700:
        ball_dy *= -1
        bounce_sound_effect.play()
    elif ball_y <= 0:
        ball_dy *= -1
        bounce_sound_effect.play()

def collision_player_one():
    global ball_dx

    # ball collision with the player 2 's paddle
    if ball_x > 1160:
        if player_2_y < ball_y + 25:
            if player_2_y + 150 > ball_y:
                ball_dx *= -1
                bounce_sound_effect.play()


def collision_player_two():
    global ball_dx

     # ball collision with the player 1 's paddle
    if ball_x < 100:
        if player_1_y < ball_y + 25:
            if player_1_y + 150 > ball_y:
                ball_dx *= -1
                bounce_sound_effect.play()
    

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
     
    command_keys()
    
    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:
        # clear screen
        screen.fill(COLOR_BACKGROUNG)

        collision_ball_wall()

        collision_player_one()
        collision_player_two()
        
        
        verify_score()

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy


        player_1_y = collision_player_wall(player_1_y)
        player_2_y = collision_player_wall(player_2_y)

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE)

        # drawing objects
        draw_objects(screen)
    else:
       draw_screen_victory(screen)

    # update screen
    pygame.display.flip()
    game_clock.tick(FPS)

pygame.quit()