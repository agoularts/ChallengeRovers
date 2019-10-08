import sys

class SpaceShip:

	def __init__(self, sizeX, sizeY):
		self.sizeX = int(sizeX)
		self.sizeY = int(sizeY)
	
	@classmethod
	def getPlateauSize(self):
		while 1:
			try:
				sizeX, sizeY = input().split()
				return self(sizeX, sizeY)
			except:
				print('Invalid input')
				continue

	def confirmPlateauSize(self):
		print('Plateau confirmed!')

