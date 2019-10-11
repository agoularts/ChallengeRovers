from spaceship import SpaceShip

directions = ['N', 'E', 'S', 'W']

class Rover(SpaceShip):

	def __init__(self, sizeX = 5, sizeY = 5):
		self

	@classmethod
	def getRoverCleanLocalization(self):
		self._positionX, self._positionY, self.initialDirection = input().split()
		self._positionX = int(self._positionX)
		self._positionY = int(self._positionY)
		self.initialDirection = directions.index(self.initialDirection)

	def positionRover(self):
		self.commands = input()

		for command in self.commands:
			if command == 'R':
				self.rightRotateRover()
			elif command == 'L':
				self.leftRotateRover()
			elif command == 'M':
				self.moveRover()

		directions = ['N', 'E', 'S', 'W'][self.initialDirection]
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

def main():
	roverOne = Rover.getPlateauSize()
	roverOne.getRoverCleanLocalization()
	roverOne.positionRover()

	roverTwo = Rover()
	roverTwo.getRoverCleanLocalization()
	roverTwo.positionRover()

	roverThree = Rover()
	roverThree.getRoverCleanLocalization()
	roverThree.positionRover()

if __name__ == '__main__':
	main()
