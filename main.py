import pygame
import game
import config


pygame.init()
game = game.Game()
clock = pygame.time.Clock()

while config.game_loop:
    if game.current_screen == 'menu':
        game.menu()
    elif game.current_screen == 'tips_screen':
        game.tips_screen()
    else:
        game.main_screen()
    clock.tick(config.Constants.FPS)