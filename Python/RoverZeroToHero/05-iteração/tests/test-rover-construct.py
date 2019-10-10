from testSpaceship import SpaceShip
import unittest

directions = ['N', 'E', 'S', 'W']

class Rover(SpaceShip):
	pass

	def __init__(self, positionX, positionY, roverDirection):
		self._positionX = int(positionX)
		self._positionY = int(positionY)
		#0 North, 1 east, 2 south, 3 weast
		self.initialDirection = directions.index(roverDirection)

		#(1, 2, 0)
		#(1, 2, N)
		#LMLMLMLMM
		#(1, 3, N)

	def positionRover(self, commands=''):
		for command in commands:
			if command == 'R':
				self.rightRotateRover()
			elif command == 'L':
				self.leftRotateRover()
			elif command == 'M':
				self.moveRover()

		directions = ['N', 'E', 'S', 'W'][self.initialDirection]
		return f'{self._positionX} {self._positionY} {directions}'
		print(f'{self._positionX} {self._positionY} {directions}')

	def moveRover(self):

		if(self.initialDirection == 0): # North
			self._positionY +=1

		if(self.initialDirection == 2): # South
			self._positionY -= 1

		if(self.initialDirection == 1): # East
			self._positionX += 1

		if(self.initialDirection == 3): # Weast
			self._positionX -= 1

		return True

	def rightRotateRover(self):
		self.initialDirection = 0 if self.initialDirection == 3 else self.initialDirection + 1
		return self.initialDirection

	def leftRotateRover(self):
		self.initialDirection = 3 if self.initialDirection == 0 else self.initialDirection - 1
		return self.initialDirection

class RoverTest(unittest.TestCase):

	def testMove(self):
		roverSubOne = Rover(1, 2, 'N')
		self.assertEqual('1 3 N', roverSubOne.positionRover("LMLMLMLMM"))

		roverSubTwo = Rover(3, 3, 'E')
		self.assertEqual('5 1 E', roverSubTwo.positionRover("MMRMMRMRRM"))

	#def testInitialPosition(self):
	#	rover = Rover(1, 2, 'E')
	#	self.assertEqual('5 5', rover.plateauPosition(int(x), int(y)))


	def testRoverPosition(self):
		roverOne = Rover(1, 2, 'N')
		self.assertEqual(0, roverOne.initialDirection)
		print('North = 0')
		self.assertEqual(3, roverOne.leftRotateRover())
		print('Weast = 3')
		self.assertEqual(0, roverOne.rightRotateRover())
		print('North = 0')
		self.assertEqual(1, roverOne.rightRotateRover())
		print('East = 1')
		self.assertEqual(2, roverOne.rightRotateRover())
		print('South = 2')

	def testMoveRorverFront(self):
		roverOne = Rover(1, 2, 'N')
		self.assertEqual(1, roverOne.moveRover())

	def testLocationPositionNorth(self):
		roverOne = Rover(1, 2, 'N')
		roverOne.positionRover("LMLMLMLMM")

		roverOne.moveRover()
		self.assertEqual(1, roverOne._positionX)
		self.assertEqual(4, roverOne._positionY)

		roverOne.moveRover()
		self.assertEqual(1, roverOne._positionX)
		self.assertEqual(5, roverOne._positionY)

		roverOne.moveRover()
		self.assertEqual(1, roverOne._positionX)
		self.assertEqual(6, roverOne._positionY)

		roverOne.moveRover()
		self.assertEqual(1, roverOne._positionX)
		self.assertEqual(7, roverOne._positionY)

		roverOne.moveRover()
		self.assertEqual(1, roverOne._positionX)
		self.assertEqual(8, roverOne._positionY)

	def testLocationPositionSouth(self):
		rovertTwo = Rover(2, 0, 'S')
		rovertTwo.positionRover("MMMM")

		rovertTwo.moveRover()
		self.assertEqual(2, rovertTwo._positionX)
		self.assertEqual(-5, rovertTwo._positionY)

		rovertTwo.moveRover()
		self.assertEqual(2, rovertTwo._positionX)
		self.assertEqual(-6, rovertTwo._positionY)

		rovertTwo.moveRover()
		self.assertEqual(2, rovertTwo._positionX)
		self.assertEqual(-7, rovertTwo._positionY)

		rovertTwo.moveRover()
		self.assertEqual(2, rovertTwo._positionX)
		self.assertEqual(-8, rovertTwo._positionY)

		rovertTwo.moveRover()
		self.assertEqual(2, rovertTwo._positionX)
		self.assertEqual(-9, rovertTwo._positionY)

	def testLocationPositionEast(self):
		roverThree = Rover(3, 3, 'E')
		roverThree.positionRover("MMRMMRMRRM")

		roverThree.moveRover()
		self.assertEqual(6, roverThree._positionX)
		self.assertEqual(1, roverThree._positionY)

		roverThree.moveRover()
		self.assertEqual(7, roverThree._positionX)
		self.assertEqual(1, roverThree._positionY)

		roverThree.moveRover()
		self.assertEqual(8, roverThree._positionX)
		self.assertEqual(1, roverThree._positionY)

		roverThree.moveRover()
		self.assertEqual(9, roverThree._positionX)
		self.assertEqual(1, roverThree._positionY)

		roverThree.moveRover()
		self.assertEqual(10, roverThree._positionX)
		self.assertEqual(1, roverThree._positionY)

	def testLocationPositionOest(self):
		roverFour = Rover(4, 4, 'W')
		roverFour.positionRover('LMLMLMLMMMM')

		roverFour.moveRover()
		self.assertEqual(0, roverFour._positionX)
		self.assertEqual(4, roverFour._positionY)

		roverFour.moveRover()
		self.assertEqual(-1, roverFour._positionX)
		self.assertEqual(4, roverFour._positionY)

		roverFour.moveRover()
		self.assertEqual(-2, roverFour._positionX)
		self.assertEqual(4, roverFour._positionY)

		roverFour.moveRover()
		self.assertEqual(-3, roverFour._positionX)
		self.assertEqual(4, roverFour._positionY)

		roverFour.moveRover()
		self.assertEqual(-4, roverFour._positionX)
		self.assertEqual(4, roverFour._positionY)

if __name__ == '__main__':
	unittest.main()