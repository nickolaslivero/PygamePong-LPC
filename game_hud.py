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
    
    def update_data(self):
        '''aaaaaa'''
    
    def render(self, surface):
        surface.blit(self.image,(0,0))
        score_text = game_font.render(f'{config.player_1_score}:{config.player_2_score}', False, (255, 255, 255))
        surface.blit(score_text,(config.Constants.SCREEN_WIDTH/2,config.Constants.SCREEN_HEIGHT-35))