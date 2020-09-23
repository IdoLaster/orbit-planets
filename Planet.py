import numpy as np

class Planet():
    G = 100 # Gravitional constant
    def __init__(self, name, color, radius, mass, pos):
        self.name = name
        self.color = color
        self.radius = radius # This is not used in any of the calculation, but for the graphics
        self.mass = mass
        self.pos = np.array(pos)

        self.velocty = np.array((0,0))
        self.acceleration = np.array((0,0))

    def update(self):
        self.velocty = self.velocty + self.acceleration
        
        self.pos = self.pos + self.velocty

        self.acceleration = self.acceleration * 0

    def get_gravity_force(self, planet_other):
        dir = self.pos - planet_other.pos
        distance = np.linalg.norm(dir) # In this case the distance is equals to the vector magnitue
        dir = dir / np.linalg.norm(dir)
        strength = (self.G * self.mass * planet_other.mass) / distance ** 2
        force = dir * strength

        return force

    def apply_force(self, force):
        f = force / self.mass
        self.acceleration = self.acceleration + f