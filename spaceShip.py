import sys

class SpaceShip:

	def __init__(self, x, y):
		self._x = int(x)
		self._y = int(y)
	
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

