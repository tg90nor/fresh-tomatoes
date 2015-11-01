import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 30px;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .jumbotron {
          background-color: rgba(0,0,0,0.85);
          color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Start playing the video when the title is clicked
        $(document).on('click', '.movie-tile', function (event) {
            $('#trailer').show();
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            var imdbId = $(this).attr('data-imdb-id');
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            var resturl = "http://www.omdbapi.com/?i="+imdbId+"&plot=short&r=json";
            $.ajax({
              url: resturl,
                dataType: 'json',
                success: function(data){
                  var title  = data.Title;
                  var genre  = data.Genre;
                  var plot   = data.Plot;
                  var relYear = data.Year;
                  var actors = data.Actors;
                  
                  $('#imdb').html(
                    "<h2>"+title+"</h2>" +
                    "<p><i>"+genre+" - first aired in "+relYear+"</i></p>" +
                    "<p>"+plot+"</p>" +
                    "<p>Actors: "+actors+"</p>" +
                    "<p><small>source: <a href=\\"http://www.imdb.com/title/"+imdbId+"/\\">IMDB</a></small></p>" +
                    "<p><a href=\\"#\\" id=\\"jumbo-hide\\"><span class=\\"glyphicon glyphicon-chevron-up\\"></span> Hide trailer</a></p>"
                  );
                }
            });
        });

        // Hide the trailer jumbotron when the hide button is clicked
        $(document).on('click', '#jumbo-hide', function (event) {
          $("#trailer-video-container").empty();
          $('#trailer').hide();
        });

        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
          $('#trailer').hide();
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <div class="jumbotron">
      <div class="container">
        <h1>Fresh Tomatoes!</h1>
      </div>
    </div>
    <div class="jumbotron" id="trailer">
      <div class="row">
        <div class="col-lg-8">
          <div class="embed-responsive embed-responsive-16by9" id="trailer-video-container">
          </div>
        </div>
        <div class="col-lg-4" id="imdb">
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-imdb-id="{imdb_id}" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_url,
            trailer_youtube_id=trailer_youtube_id,
            imdb_id=movie.imdb_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
