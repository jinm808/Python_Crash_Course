'''
4-11: My Pizzas, Your Pizzas
Start with your program from Exercise 4-1 (page 60). 
Make a copy of the list of pizzas, and call it friend_pizzas.
'''
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]


# Add a new pizza to the original list.
favorite_pizzas.append('za')

# Add a different pizza to the list friend_pizzas.
friend_pizzas.append('kalzone')

# Prove that you have two separate lists. 
# Print the message, My favorite pizzas are:, and then use a for loop to print the first list. 

print('\nMy favorite pizzas are:')
for pizza in favorite_pizzas:
  print(pizza)
  
# Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

print('\nMy friend’s favorite pizzas are:')
for pizza in friend_pizzas:
  print(pizza)

