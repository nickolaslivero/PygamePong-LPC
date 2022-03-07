from config import *
from ball import *
# from player import *
from background import *
from game_hud import *
from skill_selector import *
from sys import exit

# screen
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
pygame.display.set_caption("Pong War - PyGame Edition - 2021.01.30")
pygame.display.set_icon(pygame.image.load('img/ball.png'))

# background
background = Background(0)

# menu text image
menu_text = pygame.image.load('img/menu_text.png').convert_alpha()

# Game tips
tip_1_img = pygame.image.load('img/tip_screen_1.png').convert_alpha()
tip_2_img = pygame.image.load('img/tip_screen_2.png').convert_alpha()
actual_tip = 1

# PAUSE
pause = pygame.image.load('img/pause.png').convert_alpha()
# HUD
hud = Hud()

# Player coordinates
player_1 = Player(30, 300, 'player_1')
player_2 = Player(820, 300, 'player_2')

# ball
ball = Ball(position_x=Constants.SCREEN_WIDTH / 2,
            position_y=Constants.SCREEN_HEIGHT / 2)

# skill selector
skill_selector = Skill()
clock = pygame.time.Clock()
current_time = 0
button_press_time = 0


# Players movement
def move_players():
    player_1.move()
    player_2.move()


def background_move():
    background.move()

    # background stars movement repeat
    if background.stars_1_position_x >= Constants.SCREEN_WIDTH:
        background.stars_1_position_x = 0
    if background.stars_2_position_x >= Constants.SCREEN_WIDTH:
        background.stars_2_position_x = 0

    background.render(screen)


def collision_player_1_ball():
    if ball.position_x < (player_1.position_x + player_1.width):
        if player_1.position_y < ball.position_y < (player_1.position_y + player_1.height):
            config.ball_moving_left = False
            player_collided_sound.play()


def collision_player_2_ball():
    if ball.position_x + ball.width > player_2.position_x:
        if player_2.position_y < ball.position_y < (player_2.position_y + player_2.height):
            config.ball_moving_left = True
            player_collided_sound.play()


def verify_skill():
    global skill_selector
    # skill_selector.active = True

    if config.player_1_score > 0:
        if config.player_1_score % 3 == 0:
            if skill_selector.active == False:
                skill_selector.set_image(skill_selector)

            skill_selector.active = True
            skill_selector.player = 1
            if skill_selector.name == "slow":
                config.player_2_speed = 2
            if skill_selector.name == "freeze":
                skill_freeze(1)
        else:
            config.player_2_speed = 7

    if config.player_2_score > 0:
        if config.player_2_score % 3 == 0:
            if skill_selector.active == False:
                skill_selector.set_image(skill_selector)

            skill_selector.active = True
            skill_selector.player = 2
            if skill_selector.name == "slow":
                config.player_1_speed = 2
            if skill_selector.name == "freeze":
                skill_freeze(2)
        else:
            config.player_1_speed = 7


def skill_freeze(player):
    if player == 1:
        config.player_2_moving_up = True
        config.player_2_moving_down = True

    if player == 2:
        config.player_1_moving_up = True
        config.player_1_moving_down = True


class Game:
    def __init__(self):
        self.current_screen = 'menu'

    def menu(self):
        # Players input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.current_screen = 'tips_screen'

        background_move()
        screen.blit(menu_text, (0, 0))

        # update menu screen
        pygame.display.flip()

    def tips_screen(self):
        global actual_tip, tip_1_img, tip_2_img

        # Players input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    actual_tip += 1

        background_move()

        if actual_tip == 1:
            screen.blit(tip_1_img, (0, 0))
        elif actual_tip == 2:
            screen.blit(tip_2_img, (0, 0))
        else:
            actual_tip = 1
            self.current_screen = 'main_screen'

        # update menu screen
        pygame.display.flip()

    # Game logic
    @staticmethod
    def main_screen():
        # Players input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    config.player_1_moving_up = True
                elif event.key == pygame.K_s:
                    config.player_1_moving_down = True
                elif event.key == pygame.K_UP:
                    config.player_2_moving_up = True
                elif event.key == pygame.K_DOWN:
                    config.player_2_moving_down = True
                elif event.key == pygame.K_p:
                    if config.jogo != config.Constants.PAUSED:
                        config.jogo = config.Constants.PAUSED
                    else:
                        config.jogo = config.Constants.ROLLING
                        background_move()
                elif event.key == pygame.K_e:
                    exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    config.player_1_moving_up = False
                elif event.key == pygame.K_s:
                    config.player_1_moving_down = False
                elif event.key == pygame.K_UP:
                    config.player_2_moving_up = False
                elif event.key == pygame.K_DOWN:
                    config.player_2_moving_down = False

        background_move()
        if config.jogo != config.Constants.PAUSED:
            move_players()
            ball.move()
            collision_player_1_ball()
            collision_player_2_ball()

        # player 1 collision with top wall
        if player_1.position_y <= 0:
            player_1.position_y = 0

        # player 1 collision with bottom wall
        if player_1.position_y >= Constants.SCREEN_HEIGHT - 150:
            player_1.position_y = Constants.SCREEN_HEIGHT - 150

        # player 2 collision with top wall
        if player_2.position_y <= 0:
            player_2.position_y = 0

        # player 2 collision with bottom wall
        if player_2.position_y >= Constants.SCREEN_HEIGHT - 150:
            player_2.position_y = Constants.SCREEN_HEIGHT - 150

        # Ball collision with top wall
        if ball.position_y <= 0:
            config.ball_moving_down = True
            wall_sound.play()

        # Ball collision with bottom wall
        if ball.position_y >= Constants.SCREEN_HEIGHT - 20:
            config.ball_moving_down = False
            wall_sound.play()

        # Ball collision with left wall
        if ball.position_x <= 0:
            config.ball_moving_left = False
            config.player_2_score += 1

            if skill_selector.player == 2:
                if config.player_2_score % 3 != 0:
                    skill_selector.player = 0
                    skill_selector.active = False

            wall_sound.play()

        # Ball collision with right wall
        if ball.position_x >= Constants.SCREEN_WIDTH - 20:
            config.ball_moving_left = True
            config.player_1_score += 1

            if skill_selector.player == 1:
                if config.player_1_score % 3 != 0:
                    skill_selector.player = 0
                    skill_selector.active = False
            wall_sound.play()

        verify_skill()
        # Drawing objects
        player_1.render(screen)
        player_2.render(screen)
        ball.render(screen)
        hud.render(screen)
        if config.jogo == config.Constants.PAUSED:
            screen.blit(pause, (0,0))

        if skill_selector.active == True:
            skill_selector.render(screen, skill_selector)

        # update game screen
        pygame.display.flip()
