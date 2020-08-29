# 5-10: Checking Usernames
# Do the following to create a program that simulates how websites ensure that everyone has a unique username.

# Make a list of five or more usernames called current_users. 
current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']

# Make another list of five usernames called new_users. 
# Make sure one or two of the new usernames are also in the current_users list.
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

# Loop through the new_users list to see if each new username has already been used. 
# If it has, print a message that the person will need to enter a new username. 
# If a username has not been used, print a message saying that the username is available.
for user in new_users:
  # Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
  if user.lower() in current_users:
    print(f'Username {user} already taken.\nEnter new username.')
  else:
    print(f'Username {user} is available.')

