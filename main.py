import pygame
from pygame.locals import *
import numpy as np

import sys

from Planet import Planet

SCALE = 10000 # Scale, still need to figure it out

#PyGame constant
LEFT = 1 # PyGame left mouse bvutton id
width, height = 1280, 720 # PyGame window size
HIGHLIGHTED_PLANET_CIRCLE_OFFSET = 5
FONT_SIZE = 32

# PyGame colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def create_planets():
	"""
	This functions creates mock planets.

	Returns:
		list: List of mock planets.
	"""
	planets = []

	earth = Planet("Earth", BLUE, 10, 1, (width // 2, 200), velocity=(1,0))
	sun = Planet("Sun", (255, 255, 0), int(696340 // SCALE), 1000, (width // 2, height // 2))
	mars = Planet("MARS", RED, int(300000 // SCALE), 10, (width // 3, height // 2), velocity=(0,1))

	planets.append(earth)
	planets.append(mars)
	planets.append(sun)

	return planets

def main():
	# Init PyGame
	pygame.init()
	
	fps = 60
	fpsClock = pygame.time.Clock()
	screen = pygame.display.set_mode((width, height))

	font = pygame.font.SysFont("Arial", FONT_SIZE)

	planets = create_planets()
	highlighted_planet = None

	# Game loop.
	while True:
		screen.fill(BLACK)
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN and event.button == LEFT:
				highlighted_planet = handle_left_click(planets)
		
		# Calculate force and apply force.
		for planet in planets:
			'''
			We are removing the current iterator planet since there's is no force 
			by a planet on himself (this is probably wrong, but I am not very smart)
			and it will lead to divion by 0.
			'''
			tmp_planets = planets.copy()
			tmp_planets.remove(planet)

			forces = map(planet.get_gravity_force, tmp_planets)
			for force in forces:
				planet.apply_force(force)
			
			planet.update()
				
		# Draw all planets and relative labels (labels are temporary).
		for planet in planets:
			pygame.draw.circle(screen, planet.color, planet.pos.astype(int), planet.radius)

			# Going to draw an highlighted circle around the highlighted planet
			# And show some information about that planet.
			if highlighted_planet == planet:
				pygame.draw.circle(screen, GREEN, planet.pos.astype(int), planet.radius + HIGHLIGHTED_PLANET_CIRCLE_OFFSET, 1)

				name_label = font.render(f"{planet.name}", False, planet.color)
				mass_label = font.render(f"Mass: {planet.mass}", False, WHITE)
				position_label = font.render(f"Position: {str(np.round(planet.pos))}", False, WHITE)
				velocity_label = font.render(f"Velocity: {str(np.round(planet.velocity, 2))}", False, WHITE)

				screen.blit(name_label, (0, 0))
				screen.blit(mass_label, (0, FONT_SIZE))
				screen.blit(position_label, (0, FONT_SIZE * 2))
				screen.blit(velocity_label, (0, FONT_SIZE * 3))

		# Draw a label for the graivitonal constant
		G_label = font.render(f"G: {Planet.G}", False, WHITE)
		screen.blit(G_label, (width - G_label.get_width(), 0))

		# Update screen.
		pygame.display.flip()
		fpsClock.tick(fps)

def handle_left_click(planets):
	"""
	This functions handles the left click button of the mouse

	Args:
		planets (List of planets): The planets list

	Returns:
		Planet: The planet we clicked on, or None if we haven't clicked on a planet.
	"""
	for planet in planets:
		if planet.clicked_on(np.array(pygame.mouse.get_pos())):
			return planet
	
if __name__ == "__main__":
	main()