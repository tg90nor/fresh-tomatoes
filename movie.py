class Movie:
  title = ""
  poster_url = ""
  trailer_url = ""
  imdb_id = ""

  def __init__(self, title, poster_url, trailer_url, imdb_id):
    self.title = title
    self.poster_url = poster_url
    self.trailer_url = trailer_url
    self.imdb_id = imdb_id
