import pygame
import config

pygame.font.init()

# Text font
game_font = pygame.font.Font(config.Constants.FONT, 60)

class Hud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        global game_font

        self.score_1 = config.player_1_score
        self.score_2 = config.player_2_score
        self.status_1 = config.player_1_status
        self.status_2 = config.player_2_status
        self.image = pygame.image.load('img/HUD.png')
        self.score_text = game_font.render(f'{self.score_1}:{self.score_2}', False, (255, 255, 255))
    
    def update_data(self):
        '''aaaaaa'''
    
    def render(self, surface):
        surface.blit(self.image,(0,0))
        surface.blit(self.score_text,(config.Constants.SCREEN_WIDTH/2,config.Constants.SCREEN_HEIGHT-35))