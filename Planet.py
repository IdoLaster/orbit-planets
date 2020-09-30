import numpy as np
import math

class Planet():
	G = 1 # Gravitional constant

	def __init__(self, name, color, radius, mass, pos, velocity=(0,0)):
		"""
		Inits a new planet object.
		The name, color, radius not effect the calculations, they are for displaying reasons.

		Args:
			name (String): The name of the planet.
			color (tuple): (R, G, B) values of the planet color
			radius (Integer): The radius of the planet.
			mass (Float): The mass of the planet.
			pos (tuple): (Px, Py) the position of the planet
		"""
		self.name = name
		self.color = color
		self.radius = radius 

		self.mass = mass
		self.pos = np.array(pos)
		self.velocity = np.array(velocity)


	def update(self):
		"""
		Updates self position by the current velocity
		"""
		self.pos = self.pos + self.velocity

	def get_gravity_force(self, planet_other):
		"""
		Calculates the graivitonal force that planet_other effects self 

		Args:
			planet_other (Planet): The planet we are calculating the graivtonal force from.

		Returns:
			np.array: [Fx, Fy] The graivitonal force that applies to self.
		"""
		if planet_other == None:
			raise ValueError("planet_other cannot be None")

		if np.array_equal(self.pos, planet_other.pos):
			raise ZeroDivisionError("Planets collision!")

		direction = (self.pos - planet_other.pos ) * -1
		
		distance = np.linalg.norm(direction)
		direction = direction / np.linalg.norm(direction)
		
		strength = (self.G * self.mass * planet_other.mass) / (distance ** 2)
		
		force = direction * strength
		
		return force # [fx, fy]

	def apply_force(self, force):
		"""
		Applies force to self

		Args:
			force (np.array): [Fx, Fy] The force to apply to self.
		"""
		if force is None:
			raise ValueError("Force can't be None!")
		f = force / self.mass
		self.velocity = self.velocity + f

	def clicked_on(self, pos):
		"""
		Takes in a position and returns true if the position is inside
		the planet radius.

		Args:
			pos (np.array): The position we would like to check

		Returns:
			Boolean: True if we are inside the planet radius.
		"""
		d = np.sqrt(np.sum(np.power(pos - self.pos, 2)))

		return d < self.radius