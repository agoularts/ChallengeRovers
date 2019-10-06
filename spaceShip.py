import sys

class SpaceShip:

	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)
	
	@classmethod
	def getPlateauSize(self):
		while 1:
			try:
				x, y = input().split()
				return self(x, y)
			except:
				print('Invalid input')
				continue

	def confirmPlateauSize(self):
		print('Plateau confirmed!')

