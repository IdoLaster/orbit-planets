import numpy as np
import math

class Planet():
	G = 1 # Gravitional constant
	def __init__(self, name, color, radius, mass, pos):
		self.name = name
		self.color = color
		self.radius = radius # This is not used in any of the calculation, but for the graphics
		self.mass = mass
		self.pos = np.array(pos)

		self.velocty = np.array((0,0))

		self.acceleration = np.array((0,0))

	def update(self):
		self.pos = self.pos + self.velocty
		#self.velocty = self.velocty * 0

	def get_gravity_force(self, planet_other):
		direction = (self.pos - planet_other.pos ) * -1
		
		distance = np.linalg.norm(direction)
		direction = direction / np.linalg.norm(direction)
		
		strength = (self.G * self.mass * planet_other.mass) / (distance ** 2)
		
		force = direction * strength
		
		return force # [fx, fy]

	def apply_force(self, force):
		f = force / self.mass
		self.velocty = self.velocty + f