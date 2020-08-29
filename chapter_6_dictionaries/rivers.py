# 6-5: Rivers
# Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'.
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for k, v in rivers.items():
  print(f'{k.title()} runs through {v.title()}.')
print('\n')

# Use a loop to print the name of each river included in the dictionary.
for key in rivers.keys():
  print(key.title())
print('\n')

# Use a loop to print the name of each country included in the dictionary.
for value in rivers.values():
  print(value.title())
print('\n')