import unittest

class Rover(object):
	pass

class RoverTest(unittest.TestCase):

	def testFoo(self):
		rover = Rover()
		self.assertEqual(1, 1)
		self.assertEqual(2, 2)

if __name__ == '__main__':
	unittest.main()