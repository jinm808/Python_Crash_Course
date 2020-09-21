def make_album(artist_name, album_title, tracks=0):
  """Build a dictionary describing a music album."""
  album_dict = {
    'artist' : artist_name.title(),
    'album' : album_title.title()
  }

  if tracks:
    album_dict['tracks'] = tracks

  return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony', tracks = 10)
print(album)

album = make_album('willie nelson', 'red-headed stranger', 7)
print(album)
