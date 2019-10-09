directions = ['N', 'E', 'S', 'W']

class Rover(object):

	def __init__(self, positionX, positionY, roverDirection):
		self._positionX = int(positionX)
		self._positionY = int(positionY)
		self.initialDirection = directions.index(roverDirection)

	def positionRover(self, commands=''):
		for command in commands:
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
	nexus = Rover(1, 2, 'N')
	nexus.positionRover("LMLMLMLMM")

	rover = Rover(3, 3, 'E')
	rover.positionRover("MMRMMRMRRM")

if __name__ == '__main__':
	main()
