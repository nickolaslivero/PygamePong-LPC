import random
 
# from config import *
import player
from player import *
from config import *
 
 
class Skill(pygame.sprite.Sprite):
    def __init__(self):
        global vector
        vector = ['img/slow_opponent.png', 
                  'img/freeze_opponent.png', 
                 ]
        pygame.sprite.Sprite.__init__(self)
        self.position_x = 450
        self.position_y = 300
        self.active = False
        self.name = ""
        self.player = 0
 
        self.image = pygame.image.load('{}'.format(random.choice(vector)))
 
    def render(self, surface, skill):
        surface.blit(skill.image, (self.position_x, self.position_y))
    
    def set_image(self, skill):
        string_vetor = random.choice(vector)
        if string_vetor == 'img/slow_opponent.png':
           skill.name = "slow"
        else:
            skill.name = "freeze"
        skill.image = pygame.image.load('{}'.format(string_vetor))
 
