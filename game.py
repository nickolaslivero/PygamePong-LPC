from config import *
from ball import *
from player import *
from background import *
from sys import exit

# screen
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
pygame.display.set_caption("Pong War - PyGame Edition - 2021.01.30")
pygame.display.set_icon(pygame.image.load('img/ball.png'))

# background
background = Background(0)

# Players coordinates
player_1 = Player(30, 300, 'player_1')
player_2 = Player(820, 300, 'player_2')

# ball
ball = Ball(position_x = Constants.SCREEN_WIDTH/2, \
            position_y = Constants.SCREEN_HEIGHT/2)

# Players movement
def move_players():
    player_1.move()
    player_2.move()

class Game():
    def __init__(self):
        self.current_screen = 'main_screen'

    def main_screen(self):
        # Players input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.current_screen = 'main_screen'

        screen.blit(Background.background, Background.background_cord)
        pygame.display.flip()
    
    # Game logic
    def main_screen(self):
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
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    config.player_1_moving_up = False
                elif event.key == pygame.K_s:
                    config.player_1_moving_down = False
                elif event.key == pygame.K_UP:
                    config.player_2_moving_up = False
                elif event.key == pygame.K_DOWN:
                    config.player_2_moving_down = False
        
        background.move()
        move_players()
        ball.move()

        # background stars movement repeat
        if background.stars_1_position_x >= Constants.SCREEN_WIDTH:
            background.stars_1_position_x = 0
        if background.stars_2_position_x >= Constants.SCREEN_WIDTH:
            background.stars_2_position_x = 0

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
        
        # Ball collision with bottom wall
        if ball.position_y >= Constants.SCREEN_HEIGHT - 20:
            config.ball_moving_down = False
        
        # Ball collision with left wall
        if ball.position_x <= 0:
            config.ball_moving_left = False
        
        # Ball collision with right wall
        if ball.position_x >= Constants.SCREEN_WIDTH - 20:
            config.ball_moving_left = True

        # Drawing objects
        background.render(screen)
        player_1.render(screen)
        player_2.render(screen)
        ball.render(screen)

        # update game screen
        pygame.display.flip()