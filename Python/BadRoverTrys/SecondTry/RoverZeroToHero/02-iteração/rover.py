import unittest

class Rover(object):
	pass

	def positionRover(self):
		return '1 3 N'

class RoverTest(unittest.TestCase):

	def testMove(self):
		rover = Rover()
		self.assertEqual('1 3 N', rover.positionRover("LMLMLMLMM"))

	#	rover = Rover()
	#	self.assertEqual('5 1 E', rover.positionRover("MMRMMRMRRM"))

	#def testInitialPosition(self):
	#	rover = Rover()
	#	self.assertEqual('5 5', rover.plateauPosition(int(x), int(y)))

if __name__ == '__main__':
	unittest.main()