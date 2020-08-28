'''
5-3: Alien Colors #1
Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
'''
alien_color = 'green'

''''
Write an if statement to test whether the alien’s color is green. 
If it is, print a message that the player just earned 5 points.
'''
if alien_color.lower() == 'green':
  print('You earned 5 points!')

'''
Write one version of this program that passes the if test and another tha fails. 
(The version that fails will have no output.)
'''
if alien_color.lower() != 'green':
  print(f'Beware, {alien_color} alliens attack!')


'''
5-4: Alien Colors #2
Choose a color for an alien as you did in Exercise 5-3.

If the alien’s coor isn’t green, print a statement that the player just earned 10 points.
Write one version of this program that runs the if block and another that runs the else block.
'''
alien_color = 'yellow'
if alien_color.lower() == 'green':
  print('You earned 5 points!')
else:
  print('You earned 10 points!')

'''
5-5: Alien Colors #3
Turn your if-else chain from Exercise 5-4 into an if-elif-else cahin.
If the alien is green, print a message that the player earned 5 points.
If the alien is yellow, print a message that the player earned 10 points.
If the alien is red, print a message that the player earned 15 points.
Write three versions of this program, making sure each message is printed for the appropriate color alien.
'''
alien_color = 'red'
if alien_color.lower() == 'green':
  print('You earned 5 points!')
elif alien_color.lower() == 'yellow':
  print('You earned 10 points!')
else:
  print('You earned 15 points!')