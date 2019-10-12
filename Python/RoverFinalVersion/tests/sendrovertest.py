from systemrovertest import Rover
from loadcommandstest import Commands
import unittest

def main():

	commandsRover = Commands.loadInstructions('rovercommands.input')
	
	roverOne = Rover(commandsRover[0])
	roverOne.getRoverCleanLocalization(commandsRover[1].split())
	roverOne.positionRover(commandsRover[2])
	
	roverTwo = Rover()
	roverTwo.getRoverCleanLocalization(commandsRover[3].split())
	roverTwo.positionRover(commandsRover[4])

class MainTest(unittest.TestCase):

	def testMain(self):
		commandsRover = Commands.loadInstructions('rovercommands.input')
		self.assertEqual(['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM'], commandsRover)

		roverOne = Rover(commandsRover[0])
		roverOne.getRoverCleanLocalization(commandsRover[1].split())
		roverOne.positionRover(commandsRover[2])

		self.assertEqual('5 5', commandsRover[0])
		self.assertEqual('1 2 N'.split(), commandsRover[1].split())
		self.assertEqual('LMLMLMLMM', commandsRover[2])

		roverTwo = Rover()
		roverTwo.getRoverCleanLocalization(commandsRover[3].split())
		roverTwo.positionRover(commandsRover[4])

		self.assertEqual('3 3 E'.split(), commandsRover[3].split())
		self.assertEqual('MMRMMRMRRM', commandsRover[4])


if __name__ == '__main__':
	unittest.main()