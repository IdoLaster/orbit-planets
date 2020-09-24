import pygame
from pygame.locals import *
import numpy as np

import sys

from Planet import Planet

width, height = 1920, 1080 # PyGame window size
SCALE = 10000 # Scale, still need to figure it out

def create_planets():
	"""
	This functions creates mock planets.

	Returns:
		list: List of mock planets.
	"""
	planets = []

	earth = Planet("Earth", (0, 0, 255), 10, 1, (width // 2, 200), velocity=(1,0))
	sun = Planet("Sun", (255, 255, 0), int(696340 // SCALE), 1000, (width // 2, height // 2))
	mars = Planet("MARS", (255, 0, 0), int(300000 // SCALE), 10, (width // 3, height // 2), velocity=(0,1))

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

	font = pygame.font.SysFont("Arial", 32)

	planets = create_planets()

	# Game loop.
	while True:
		screen.fill((0, 0, 0))
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		# Calculate force and apply force.
		for planet in planets:
			'''
			We are removing the current iterator planet since there's is no force 
			by a planet on himself (this is probably wrong, but I am not very smart)
			and it will lead to divion by 0.
			'''
			tmp_planets = planets.copy()
			tmp_planets.remove(planet)

			forces = list(map(planet.get_gravity_force, tmp_planets))
			for force in forces:
				planet.apply_force(force)
				planet.update()
				
		# Draw all planets and relative labels (labels are temporary).
		for i, planet in enumerate(planets):
			pygame.draw.circle(screen, planet.color, planet.pos.astype(int), planet.radius)
			textsurf = font.render(f"{planet.name}: {planet.pos[0], planet.pos[1]}", False, (255,255,255))
			screen.blit(textsurf, (0, 34 * i))

		# Update screen.
		pygame.display.flip()
		fpsClock.tick(fps)

if __name__ == "__main__":
	main()