import numpy as np

class Planet():
    G = 10000 # Gravitional constant
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
        print(f"Earth {self.pos=}")

        self.acceleration = self.acceleration * 0

    def get_gravity_force(self, planet_other):
        dir = self.pos - planet_other.pos
        print(f"{dir=}")
        distance = np.linalg.norm(dir) # In this case the distance is equals to the vector magnitue
        dir = dir / np.linalg.norm(dir)
        print(f"{dir=}")
        print(f"{distance=}")
        strength = (self.G * self.mass * planet_other.mass) / distance ** 2
        print(f"{strength=}")
        force = dir * strength
        print(f"{force=}")
        return force

    def apply_force(self, force):
        f = force / self.mass
        self.acceleration = self.acceleration + f
        print(f"{self.acceleration=}")