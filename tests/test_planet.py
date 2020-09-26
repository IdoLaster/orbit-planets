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
		mock_planet1 = Planet("Test1", (0,0,0), 5, 1, (0,0))

		self.assertRaises(ValueError, mock_planet1.get_gravity_force, None),
		self.assertRaises(ZeroDivisionError, mock_planet1.get_gravity_force, mock_planet1)

if __name__ == "__main__":
	unittest.main()