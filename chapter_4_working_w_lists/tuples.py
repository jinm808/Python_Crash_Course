'''
4-13: Buffet
A buffet-style restaurant offers only five basic foods. 
'''

# Think of five simple foods, and store them in a tuple.
menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

# Use a for loop to print each food the restaurant offers.
for food in menu_items:
  print(food)

# Try to modify one of the items, and make sure that Python rejects the change.
# menu_items[0] = 'avocado'
# print(menu_items)

# The restaurant changes its menu, replacing two of the items with different foods. 
# Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )
for food in menu_items:
  print(food)