'''
This python program is the foundation program for this package where the
class Movie is defined. The constructor has 4 instant variables movie
title, poster,you tube URL and Movie details.
 '''
import webbrowser


class Movie():

        def __init__(self, movie_title, movie_poster,
                     movie_trailer_youtube_url, movie_detials, movie_rlsedt):
            self.title = movie_title
            self.poster_image_url = movie_poster
            self.trailer_youtube_url = movie_trailer_youtube_url
            self.detials = movie_detials
            self.rlsedt = movie_rlsedt

        # The instance method show is used to open trailer in the browser
        def show(self):
            webbrowser.open(self.trailer)
