
directions = ['N', 'E', 'S', 'W']

positionX = 1
positionY = 2
initialDirection = 'N'
commands = 'LMLMLMLMM'.chars.to_a

def positionRover(commands)
	for command in commands.each
		if command == 'R'
			puts 'Right'
		elsif command == 'L'
			puts 'Left'
		elsif command == 'M'
			puts 'MoveRover'
		end
	end
end

positionRover(commands)