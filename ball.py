import pygame
import config


class Ball(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = config.ball_speed_x
        self.speed_y = config.ball_speed_y
        self.image = pygame.image.load('img/ball.png')
        self.width = 20
        self.height = 20

    def move(self):
        if config.ball_moving_left:
            self.position_x -= self.speed_x
        else:
            self.position_x += self.speed_x

        if config.ball_moving_down:
            self.position_y += self.speed_y
        else:
            self.position_y -= self.speed_y

    def render(self, surface):
        surface.blit(self.image, (self.position_x, self.position_y))
