def make_album(artist_name, album_title, tracks = 0):
  """Build a dictionary describing a music album."""
  album_dict = {
    'artist' : artist_name.title(),
    'album' : album_title.title()
  }

  if tracks:
    album_dict['tracks'] = tracks

  return album_dict

print("Enter 'q' at any time to stop.")

while True:
    title = input('\nWhat album are you thinking of? ').lower()
    if title == 'q':
        break
    
    artist = input('Who\'s the artist? ').lower()
    if artist == 'q':
        break

    tracks = input('Enter number of tracks if you know them: ')
    if artist == 'q':
        break

    album = make_album(artist, title, tracks)
    print(album)

print("\nThanks for responding!")

