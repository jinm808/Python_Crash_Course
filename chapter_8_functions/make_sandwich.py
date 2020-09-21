def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print('\nI\'ll make you a great sandwich:')
    for item in items:
        print(f'\t...adding {item} to your sandwich.')
    print('Your sandwich is ready!')

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')