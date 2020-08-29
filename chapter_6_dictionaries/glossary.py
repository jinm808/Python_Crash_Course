# 6-3: Glossary
# A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary.

# Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. 

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
  
for key, value in glossary.items():
  print(f'{key.title()}: {value}')