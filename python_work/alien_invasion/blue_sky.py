import pygame

from settings import Settings
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height)
	)
    pygame.display.set_caption("Blue Sky")
    
    # Start the main loop for the game
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen)

run_game()
