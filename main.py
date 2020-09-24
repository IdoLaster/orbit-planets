import pygame
from pygame.locals import *
import numpy as np

import sys

from Planet import Planet

width, height = 1920, 1080
SCALE = 10000
def create_planets():
	planets = []
	earth = Planet("Earth", (0, 0, 255), 10, 1, (width // 2, 200))
	earth.velocty = np.array((1,0))
	sun = Planet("Sun", (255, 255, 0), int(696340 // SCALE), 1000, (width // 2, height // 2))
	mars = Planet("MARS", (255, 0, 0), int(300000 // SCALE), 10, (width // 3, height // 2))
	mars.velocty = np.array((0, 1))
	planets.append(earth)
	planets.append(mars)
	planets.append(sun)
	return planets

def main():
	pygame.init()
	
	fps = 60
	fpsClock = pygame.time.Clock()
	font = pygame.font.SysFont("Arial", 32)
	
	
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
		
		for i, planet in enumerate(planets):
			pygame.draw.circle(screen, planet.color, planet.pos.astype(int), planet.radius)
			textsurf = font.render(f"{planet.name}: {planet.pos[0], planet.pos[1]}", False, (255,255,255))
			screen.blit(textsurf, (0, 34 * i))

		pygame.display.flip()
		fpsClock.tick(fps)

if __name__ == "__main__":
	main()