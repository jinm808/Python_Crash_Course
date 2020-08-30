# 7-2: Restaurant Seating
# Write a program that asks the user how many people are in their dinner group. 
prompt = "How many people are in your dinner party tonight? "
guests = int(input(prompt))

# If the answer is more than eight, print a message saying they’ll have to wait for a table. 
if guests > 8:
  print('I\'m sorry, you\'ll have to wait for a table.')
# Otherwise, report that their table is ready.
else:
  print('Your table is ready.')