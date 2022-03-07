import pygame
import config

# player 1
player_1 = pygame.image.load("img/player.png")
player_1_y = 300

# player 2 - robot
player_2 = pygame.image.load("img/player.png")
player_2_y = 300


class Player:
    def __init__(self, position_x, position_y, player):
        self.name = player
        self.position_x = position_x
        self.position_y = position_y
        self.width = 40
        self.height = 120

        if player == 'player_1':
            self.speed = config.player_1_speed
            self.image = pygame.image.load('img/player.png')
        else:
            self.speed = config.player_2_speed
            self.image = pygame.image.load('img/player.png')

    def move(self):
        if self.name == 'player_1':
            if config.player_1_moving_up:
                self.position_y -= config.player_1_speed
            elif config.player_1_moving_down:
                self.position_y += config.player_1_speed
        else:
            if config.player_2_moving_up:
                self.position_y -= config.player_2_speed
            elif config.player_2_moving_down:
                self.position_y += config.player_2_speed

    def render(self, surface):
        surface.blit(self.image, (self.position_x, self.position_y))
