def make_shirt(size, text):
  """Summarize the shirt that's going to be made."""
  print(f'I\'m going to make a {size} size t-shirt. It will say, "{text}".')

# Call the function using positional arguments.
make_shirt('Large', 'I love Python!')

# Call the function using keyword arguments.
make_shirt(size = 'Medium', text = 'Readability counts')