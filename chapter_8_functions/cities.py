def describe_city(city, country = 'Iceland'):
  """Describe a city."""
  print(f'{city.title()} is in {country.title()}.')

describe_city('Reykjavik')
describe_city(city = 'Akureyri')
describe_city(city = 'Seattle', country = 'the United states')