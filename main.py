import pygame
import game
import config


pygame.init()
game = game.Game()
clock = pygame.time.Clock()

while config.game_loop:
    game.main_screen()
    clock.tick(config.Constants.FPS)