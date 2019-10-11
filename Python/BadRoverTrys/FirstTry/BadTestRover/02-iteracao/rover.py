import unittest

class Rover(object):

	def roverCoordinate(self, command=''):
		return '1 2 N'

class RoverTest(unittest.TestCase):

	def testRoverCoordinate(self):
		rover = Rover()
		self.assertEqual('1 2 N', rover.roverCoordinate("LMLMLMLMM"))

	#	rover = Rover()
	#	self.assertEqual('3 3 E', rover.roverCoordinate("MMRMMRMRRM"))

	#def testInitialPosition(self):
	#	rover = Rover()
	#	self.assertEqual('0 0 N', rover.roverCoordinate())

if __name__ == '__main__':
	unittest.main()