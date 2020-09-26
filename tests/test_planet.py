import numpy as np

import unittest

from Planet import Planet

class TestPlanet(unittest.TestCase):
	"""
	This class contains few basic tests for the planet class.
	"""

	def test_get_gravity_force_calc(self):
		"""
		A simple test to make sure we are calculating correctly the gravitional force
		"""
		Planet.G = 1

		"""
		F = (G * m1 * m2) / d ** 2
		Direction = (pos1 - pos2 / d) * -1
		"""
		mock_planet1 = Planet("Test1", (0,0,0), 5, 1, (0,0))
		mock_planet2 = Planet("Test1", (0,0,0), 5, 10, (0,5))
		"""
		In this case we set G = 1
		d = 5
		m1 = 1
		m2 = 10
		pos1 = (0, 0)
		pos2 = (0, 5)
		therefore
		F = (1 * 1 * 10) / 5 ** 2 = 0.4
		Direction will be = (((0, 0) - (0, 5)) / 5) * -1 = (0, 1)
		so final force should be:
		F = (0, 1) * 0.4 = (0, 0.4)
		"""
		force = mock_planet1.get_gravity_force(mock_planet2)
		fx = force[0]
		fy = force[1]
		self.assertAlmostEqual(fx, 0)
		self.assertAlmostEqual(fy, 0.4)

	def test_get_gravity_force_rasies(self):
		"""
		A simple test to see if the right excpetions rasies
		for spesific paramters
		"""
		mock_planet1 = Planet("Test1", (0,0,0), 5, 1, (0,0))

		self.assertRaises(ValueError, mock_planet1.get_gravity_force, None),
		self.assertRaises(ZeroDivisionError, mock_planet1.get_gravity_force, mock_planet1)

	def test_apply_force_calc(self):
		"""
		A test to check we are apply force correctly
		"""
		mock_force = np.array((5, 0))
		mock_mass = 1
		inital_velocity = np.array((0,0))
		expected_vx, expected_vy = inital_velocity + (mock_force / mock_mass)

		
		mock_planet1 = Planet("Test1", (0,0,0), 5, mock_mass, (0,0), velocity=inital_velocity)
		mock_planet1.apply_force(mock_force)

		calc_vx, calc_vy = mock_planet1.velocity

		self.assertAlmostEqual(expected_vx, calc_vx)
		self.assertAlmostEqual(expected_vy, calc_vy)
	
	def test_update(self):
		"""
		A test to make sure we are updating the planet position
		correctly.
		"""
		mock_pos = np.array((0,0))
		mock_inital_velocity = np.array((0,5))
		mock_planet = Planet("Test1", (0,0,0), 1, 1, mock_pos, velocity=mock_inital_velocity)

		expected_px, expected_py = mock_pos + mock_inital_velocity
		mock_planet.update()
		calc_px, calc_py = mock_planet.pos

		self.assertAlmostEqual(expected_px, calc_px)
		self.assertAlmostEqual(expected_py, calc_py) 

if __name__ == "__main__":
	unittest.main()