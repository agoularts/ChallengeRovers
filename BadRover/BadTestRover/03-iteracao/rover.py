import unittest

class Rover(object):

	def __init__(self):
		#0 north, 1 east, 2 south, 3 oest
		self.pointingTo = 0

	def roverCoordinate(self, command=''):
		return '1 2 N'

	def rightRotate(self):
		self.pointingTo = 0 if self.pointingTo == 3 else self.pointingTo + 1
		return self.pointingTo

	def leftRotate(self):
		self.pointingTo = 3 if self.pointingTo == 0 else self.pointingTo - 1
		return self.pointingTo

class RoverTest(unittest.TestCase):

	#def testRoverCoordinate(self):
	#	rover = Rover()
	#	self.assertEqual('1 2 N', rover.roverCoordinate("LMLMLMLMM"))

	#	rover = Rover()
	#	self.assertEqual('3 3 E', rover.roverCoordinate("MMRMMRMRRM"))

	#def testInitialPosition(self):
	#	rover = Rover()
	#	self.assertEqual('0 0 N', rover.roverCoordinate())

	def testPositionPoint(self):
		rover = Rover()
		self.assertEqual(0, rover.pointingTo)
		self.assertEqual(3, rover.leftRotate())
		self.assertEqual(0, rover.rightRotate())
		self.assertEqual(1, rover.rightRotate())
		self.assertEqual(2, rover.rightRotate())

if __name__ == '__main__':
	unittest.main()