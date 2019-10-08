import pygame

from settings import Settings
import game_functions as gf
from character import Character

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height)
	)
    pygame.display.set_caption("Alien Invasion")
    
    # Make a spaceship
    character = Character(screen)

    # Start the main loop for the game
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, character)

run_game()
