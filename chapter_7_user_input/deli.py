# 7-8: Deli
# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while len(sandwich_orders) != 0:
  sandwich = sandwich_orders.pop(0).title()
  print(f'{sandwich} sandwich is prepared.')
  finished_sandwiches.append(sandwich)

print('\nToday we prepared the following sandwiches:')  
for sandwich in finished_sandwiches:
  print(f'- {sandwich} sandwich.')

