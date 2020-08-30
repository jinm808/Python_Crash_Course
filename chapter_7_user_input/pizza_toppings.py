# 7-4: Pizza Toppings
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a quit value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

active = True
while active:
  prompt = 'What topping would you like on your pizza? \nEnter \'quit\' when you are finished \n>>> '
  topping = input(prompt).lower()

  if topping != 'quit':
    print(f'\nI\'ll add {topping} to your pizza.')
  else:
    active = False

