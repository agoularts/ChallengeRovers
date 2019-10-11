### How to use
NASA have two Rovers for this mission, start your link in /src/ with:
```
python systemrover.py
```
The command above, load the commands from 'rovercommands.input'


### Check tests
The code have three files for tests:  
test-rover-generic.py => positions (5,5) for plateau and (0, 0, N) for rover.  
test-rover-construct.py => positions (5,5) for plateau and (X, Y, ['NESW']) for rovers, check code.  
testSpaceship.py => positions (X, Y) for plateau.  

to run, enter in /tests/
```
python test-rover-generic.py
python test-rover-construct.py
python testSpaceship.py
```
