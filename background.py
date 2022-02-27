import pygame
import config

class Background():
    def __init__(self, position_x):
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.stars_1_position_x = position_x
        self.stars_2_position_x = position_x
        self.stars_1_speed = config.Constants.BACKGROUND_STARS_1_SPEED
        self.stars_2_speed = config.Constants.BACKGROUND_STARS_2_SPEED
        self.background_img = pygame.image.load('img/background.png')
        self.background_stars_1_img = pygame.image.load('img/background_stars_1.png')
        self.background_stars_2_img = pygame.image.load('img/background_stars_2.png')
    
    def move(self):
        self.stars_1_position_x += self.stars_1_speed
        self.stars_2_position_x += self.stars_2_speed
    
    def render(self, surface):
        surface.blit(self.background_img,(self.position_x, 0))
        surface.blit(self.background_stars_1_img,(self.stars_1_position_x, 0))
        surface.blit(self.background_stars_2_img,(self.stars_2_position_x, 0))

        # repeating stars
        if self.stars_1_position_x >= 0:
            surface.blit(self.background_stars_1_img, \
                    (self.stars_1_position_x - config.Constants.SCREEN_WIDTH, 0))
        if self.stars_2_position_x >= 0:
            surface.blit(self.background_stars_2_img, \
                    (self.stars_2_position_x - config.Constants.SCREEN_WIDTH, 0))