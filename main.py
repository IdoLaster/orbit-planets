import pygame
from pygame.locals import *
import numpy as np

import sys

from Planet import Planet


SCALE = 10000
def create_planets():
	planets = []
	earth = Planet("Earth", (0, 0, 255), 10, 1, (1280 // 3, 720 - 200))
	#earth.velocty = np.array((1,0))
	sun = Planet("Sun", (255, 255, 0), int(696340 // SCALE), 1000, (1280 // 2, 720 // 2))
	planets.append(earth)
	planets.append(sun)
	return planets

def main():
	pygame.init()
	
	fps = 60
	fpsClock = pygame.time.Clock()
	
	width, height = 1280, 720
	screen = pygame.display.set_mode((width, height))
	planets = create_planets()
	# Game loop.
	while True:
		screen.fill((0, 0, 0))
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		for planet in planets:
			tmp_planets = planets.copy()
			tmp_planets.remove(planet)

			forces = list(map(planet.get_gravity_force, tmp_planets))
			for force in forces:
				planet.apply_force(force)
				planet.update()
				
		# Draw.
		
		for planet in planets:
			pygame.draw.circle(screen, planet.color, planet.pos.astype(int), planet.radius)

		pygame.display.flip()
		fpsClock.tick(fps)

if __name__ == "__main__":
	main()