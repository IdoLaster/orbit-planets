import pygame
from pygame.locals import *
import numpy as np

import sys

from Planet import Planet

width, height = 1280, 720 # PyGame window size
SCALE = 10000 # Scale, still need to figure it out

LEFT = 1

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
	highlighted_planet = None

	# Game loop.
	while True:
		screen.fill((0, 0, 0))
		
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

			forces = list(map(planet.get_gravity_force, tmp_planets))
			for force in forces:
				planet.apply_force(force)
				planet.update()
				
		# Draw all planets and relative labels (labels are temporary).
		for planet in planets:
			pygame.draw.circle(screen, planet.color, planet.pos.astype(int), planet.radius)
			if highlighted_planet == planet:
				pygame.draw.circle(screen, (0, 255, 0), planet.pos.astype(int), planet.radius + 5, 1)

				name_label = font.render(f"{planet.name}", False, planet.color)
				mass_label = font.render(f"Mass: {planet.mass}", False, (255, 255, 255))
				position_label = font.render(f"Position: {str(np.round(planet.pos))}", False, (255, 255, 255))
				velocity_label = font.render(f"Velocity: {str(np.round(planet.velocity, 2))}", False, (255, 255, 255))

				screen.blit(name_label, (0, 0))
				screen.blit(mass_label, (0, 34))
				screen.blit(position_label, (0, 34 * 2))
				screen.blit(velocity_label, (0, 34 * 3))

		# Update screen.
		pygame.display.flip()
		fpsClock.tick(fps)

def handle_left_click(planets):
	for planet in planets:
		if planet.clicked_on(np.array(pygame.mouse.get_pos())):
			return planet
if __name__ == "__main__":
	main()