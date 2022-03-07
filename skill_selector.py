import random

# from config import *
import player
from player import *


class Skill(pygame.sprite.Sprite):
    def __init__(self):
        global vector
        vector = ['img/slow_opponent.png', 'img/slow_yourself.png', 'img/bigger_opponent.png',
                  'img/bigger_yourself.png', 'img/freeze_opponent.png', 'img/freeze_yourself.png',
                  'img/invert_opponent.png', 'img/invert_yourself.png', 'img/smaller_opponent.png',
                  'img/smaller_yourself.png']
        pygame.sprite.Sprite.__init__(self)
        self.position_x = 450
        self.position_y = 300

        self.image = pygame.image.load('{}'.format(random.choice(vector)))

    def render(self, surface):
        surface.blit(self.image, (self.position_x, self.position_y))