from fresh_tomatoes import generate_movies_webpage, open_webpage_in_browser
from movie import Movie

my_favourite_movies = [
  Movie("Headhunters",
        "http://www.movie-poster-artwork-finder.com/posters/headhunters-poster-artwork-aksel-hennie-nikolaj-coster-waldau-synnove-macody-lund.jpg",  # noqa
        "https://www.youtube.com/watch?v=wkT5yzZrml8", "tt1614989"),
  Movie("Harlock: Space Pirate",
        "http://images.geeknative.com.s3.amazonaws.com/wp-content/uploads/2013/04/Space-Pirate-Captain-Harlock.jpg",  # noqa
        "https://www.youtube.com/watch?v=RvuulrGKnHI", "tt2668134"),
  Movie("The Lord of the Rings: The Return of the King",
        "http://vignette2.wikia.nocookie.net/lotr/images/b/ba/Rie.jpg/revision/latest?cb=20150203041337",  # noqa
        "https://www.youtube.com/watch?v=r5X-hFf6Bwo", "tt0167260"),
  Movie("Inception",
        "http://www.impawards.com/2010/posters/inception_ver3_xlg.jpg",
        "https://www.youtube.com/watch?v=8hP9D6kZseM", "tt1375666"),
  Movie("Pulp Fiction",
        "http://www.impawards.com/1994/posters/pulp_fiction_ver3_xxlg.jpg",
        "https://www.youtube.com/watch?v=s7EdQ4FqbhY", "tt0110912"),
  Movie("Life of Brian",
        "https://www.movieposter.com/posters/archive/main/37/MPW-18864",
        "https://www.youtube.com/watch?v=TKPmGjVFbrY", "tt0079470")
]

movie_webpage_path = generate_movies_webpage(my_favourite_movies)
open_webpage_in_browser(movie_webpage_path)
