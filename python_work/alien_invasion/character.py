import pygame

class Character():
	"""Creates the spaceship"""
	
	def __init__(self, screen):
		"""Initialize the character and set its starting position"""
		self.screen = screen
		
		# Load the character image and get its rect
		self.image = pygame.image.load('images/Chief.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.bg_color
		
		# Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	
	def blitme(self):
		"""Draw the character at its current location"""
		self.screen.blit(self.image, self.rect)

