import unittest

class Rover(object):
	pass

	def __init__(self):
		#0 North, 1 east, 2 south, 3 weast
		self.initialDirection = 0
		self.movePosition = 0

		#(1, 2, 0)
		#(1, 2, N)
		#LMLMLMLMM
		#(1, 3, N)

	def positionRover(self):
		return '1 3 N'

	def rightRotateRover(self):
		self.initialDirection = 0 if self.initialDirection == 3 else self.initialDirection + 1
		return self.initialDirection

	def leftRotateRover(self):
		self.initialDirection = 3 if self.initialDirection == 0 else self.initialDirection - 1
		return self.initialDirection

	def moveRover(self):
		self.movePosition = self.movePosition + 1
		return self.movePosition

class RoverTest(unittest.TestCase):

	#def testMove(self):
	#	rover = Rover()
	#	self.assertEqual('1 3 N', rover.positionRover("LMLMLMLMM"))

	#	rover = Rover()
	#	self.assertEqual('5 1 E', rover.positionRover("MMRMMRMRRM"))

	#def testInitialPosition(self):
	#	rover = Rover()
	#	self.assertEqual('5 5', rover.plateauPosition(int(x), int(y)))

	def testRoverPOsition(self):
		rover = Rover()
		self.assertEqual(0, rover.initialDirection)
		print('North = 0')
		self.assertEqual(3, rover.leftRotateRover())
		print('Weast = 3')
		self.assertEqual(0, rover.rightRotateRover())
		print('North = 0')
		self.assertEqual(1, rover.rightRotateRover())
		print('East = 1')
		self.assertEqual(2, rover.rightRotateRover())
		print('South = 2')

	def testMoveRorverFront(self):
		rover = Rover()
		self.assertEqual(0, rover.movePosition)
		self.assertEqual(1, rover.moveRover())
		self.assertEqual(2, rover.moveRover())
		self.assertEqual(3, rover.moveRover())
		self.assertEqual(4, rover.moveRover())

if __name__ == '__main__':
	unittest.main()