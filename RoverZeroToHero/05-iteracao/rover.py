import unittest

class Rover(object):

	def __init__(self):
		self.x = 0
		self.y = 0
		#0 north, 1 east, 2 south, 3 weast
		self.pointingTo = 0
		self.plateauPosition = (5, 5)


	def roverCoordinate(self, command=''):
		for c in command:
			if c == 'R':
				self.rightRotate()
			elif c == 'L':
				self.leftRotate()
			elif c == 'M':
				self.moveRover()

		direction = ['N', 'E', 'S', 'W'][self.pointingTo]
		return f'{self.x} {self.y} {direction}'

	def moveRover(self):

		if(self.pointingTo == 0): #North
			self.y += 1

		if(self.pointingTo == 2): #South
			self.y -= 1

		if(self.pointingTo == 1): #East
			self.x += 1

		if(self.pointingTo == 3): #Weast
			self.x -= 1

		return True

	def rightRotate(self):
		self.pointingTo = 0 if self.pointingTo == 3 else self.pointingTo + 1
		return self.pointingTo

	def leftRotate(self):
		self.pointingTo = 3 if self.pointingTo == 0 else self.pointingTo - 1
		return self.pointingTo

class RoverTest(unittest.TestCase):

	#def testRoverCoordinate(self):
	#	rover = Rover()
	#	self.assertEqual('1 3 N', rover.roverCoordinate("LMLMLMLM"))

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

	def testPositionNorth(self):
		rover = Rover()
		rover.pointingTo = 0

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(1, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(2, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(3, rover.y)

	def testPositionSouth(self):
		rover = Rover()
		rover.pointingTo = 2

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(-1, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(-2, rover.y)

		rover.moveRover()
		self.assertEqual(0, rover.x)
		self.assertEqual(-3, rover.y)

	def testPositionEast(self):
		rover = Rover()
		rover.pointingTo = 1

		rover.moveRover()
		self.assertEqual(1, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(2, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(3, rover.x)
		self.assertEqual(0, rover.y)

	def testPositionWeast(self):
		rover = Rover()
		rover.pointingTo = 3

		rover.moveRover()
		self.assertEqual(-1, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(-2, rover.x)
		self.assertEqual(0, rover.y)

		rover.moveRover()
		self.assertEqual(-3, rover.x)
		self.assertEqual(0, rover.y)

if __name__ == '__main__':
	unittest.main()