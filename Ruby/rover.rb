
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

def moveRover()
	if(initialDirection == 0)
		positionY += 1

	if(initialDirection == 2)
		positionY -= 1

	if(initialDirection == 1)
		positionX += 1

	if(initialDirection == 3)
		positionX -= 1

	return true
end 


positionRover(commands)