def make_car(manufacturer, model, **features):
  """Store information about a car in a dictionary."""
  profile = {
    'manufacturer' : manufacturer,
    'model' : model
  }

  for key, value in features.items():
    profile[key] = value

  return profile

my_outback = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(my_outback)

my_accord = make_car('honda', 'accord', year = 1991,color = 'white', headlights = 'popup')
print(my_accord)
