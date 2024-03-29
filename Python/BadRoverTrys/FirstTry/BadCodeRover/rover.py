from spaceShip import SpaceShip

possibleDirections = "NESW"
possibleCardinal = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Rover(SpaceShip):

	def __init__(self, sizeX, sizeY):
		self

	@classmethod
	def positionRover(self):
		while 1:
			try:
				positionX, positionY, dir = input().split()
				initialPosition = (int(positionX), int(positionY), possibleDirections.find(dir))

				self.moveRover(self, initialPosition)
			except:
				print('Invalid position. Try again!')
				return

	def moveRover(self, initialPosition):
		try:
			roverMovement = input().lower()

			r = lambda x, y, a: (x, y, (a+1) % 4)
			l = lambda x, y, a: (x, y, (a-1 + 4) % 4)
			m = lambda x, y, a: (x+possibleCardinal[a][0], y+possibleCardinal[a][1], a)

			for i in roverMovement:
				initialPosition = eval('%s%s' % (i, str(initialPosition)))
			print(initialPosition[0], initialPosition[1], possibleDirections[initialPosition[2]])
		except:
			print('Invalid move! Try again!')
			return

def main():
	rover = Rover.getPlateauSize()
	rover.positionRover()

if __name__ == "__main__": main()

