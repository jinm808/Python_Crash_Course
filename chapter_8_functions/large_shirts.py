def make_shirt(size='large', text='I love Python!'):
  """Summarize shirt that's going to be made."""
  print(f'I\'m going to make a {size} size t-shirt. \nIt will say, "{text}".')

make_shirt()
make_shirt(size = 'medium')
make_shirt('small', 'Programmers are loopy.')