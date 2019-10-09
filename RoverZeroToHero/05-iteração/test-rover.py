import unittest

class Rover(object):
	pass

	def __init__(self):
		self.x = 1
		self.y = 2
		#0 North, 1 east, 2 south, 3 weast
		self.initialDirection = 0

		#(1, 2, 0)
		#(1, 2, N)
		#LMLMLMLMM
		#(1, 3, N)

	def positionRover(self, commands=''):
		for c in commands:
			if c == 'R':
				self.rightRotateRover()
			elif c == 'L':
				self.leftRotateRover()
			elif c == 'M':
				self.moveRover()

		directions = ['N', 'E', 'S', 'W'][self.initialDirection]
		return f'{self.x} {self.y} {directions}'

	def moveRover(self):

		if(self.initialDirection == 0): # North
			self.y +=1

		if(self.initialDirection == 2): # South
			self.y -= 1

		if(self.initialDirection == 1): # East
			self.x += 1

		if(self.initialDirection == 3): # Weast
			self.x -= 1

		return True

	def rightRotateRover(self):
		self.initialDirection = 0 if self.initialDirection == 3 else self.initialDirection + 1
		return self.initialDirection

	def leftRotateRover(self):
		self.initialDirection = 3 if self.initialDirection == 0 else self.initialDirection - 1
		return self.initialDirection

class RoverTest(unittest.TestCase):

	def testMove(self):
		rover = Rover()
		self.assertEqual('1 3 N', rover.positionRover("LMLMLMLMM"))

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
"""
	#def testMoveRorverFront(self):
	#	rover = Rover()
	#	self.assertEqual(0, rover.movePosition)
	#	self.assertEqual(1, rover.moveRover())
	#	self.assertEqual(2, rover.moveRover())
	#	self.assertEqual(3, rover.moveRover())
	#	self.assertEqual(4, rover.moveRover())

	def testLocationPositionNorth(self):
		rover = Rover()
		rover.initialDirection = 0

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(1, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(2, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(3, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(4, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(5, rover.y)

	def testLocationPositionSouth(self):
		rover = Rover()
		rover.initialDirection = 2

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(-1, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(-2, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(-3, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(-4, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(-5, rover.y)

	def testLocationPositionEast(self):
		rover = Rover()
		rover.initialDirection = 1

		rover.moveRover()
		self.assertEqual(1, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(2, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(3, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(4, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(5, rover.x)
		self.assertEqual(0, rover.y)

	def testLocationPositionOest(self):
		rover = Rover()
		rover.initialDirection = 3

		rover.moveRover()
		self.assertEqual(-1, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(-2, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(-3, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(-4, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(-5, rover.x)
		self.assertEqual(0, rover.y)
"""

if __name__ == '__main__':
	unittest.main()