import pygame
from pygame.locals import *
import numpy as np

import sys

from Planet import Planet


SCALE = 10000

def main():
    pygame.init()
    
    fps = 60
    fpsClock = pygame.time.Clock()
    
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    earth = Planet("Earth", (0, 0, 255), 10, 2, (1280 // 2, 720 - 200))
    earth.velocty = np.array((1,0))
    sun = Planet("Sun", (255, 255, 0), int(696340 // SCALE), 200, (1280 // 2, 720 // 2))
    # Game loop.
    while True:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        

        force = sun.get_gravity_force(earth)
        #print(force)
        earth.apply_force(force / SCALE)
        
        #print(earth.acceleration)
        earth.update()
        # Draw.
        
        pygame.draw.circle(screen, earth.color, earth.pos.astype(int), earth.radius)
        pygame.draw.circle(screen, sun.color, sun.pos.astype(int), sun.radius)

        pygame.display.flip()
        fpsClock.tick(fps)

if __name__ == "__main__":
    main()