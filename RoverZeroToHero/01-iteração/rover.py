import unittest

class Rover(object):
	pass

class RoverTest(unittest.TestCase):

	def testMove(self):
		rover = Rover()
		self.assertEqual(1, 1)

if __name__ == '__main__':
	unittest.main()