import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import gameFunctions as gf

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Make a ship.
	ship = Ship(ai_settings, screen)
	# Make a group to store bullets in.
	bullets = Group()
	# Make an alien.
	alien = Alien(ai_settings, screen)

	# Start the main loop for the game.
	while True:

		# Watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)

		# Redraw the screen during each pass through the loop.
		gf.update_screen(ai_settings, screen, ship, alien, bullets)

		# Make the most recently drawn screen visible.
		pygame.display.flip()

run_game()