'''
Importing the media python program which has movie definition and dynamic_page_genarator python
program that generates the dynamic HTML page. Multiple movie instances are
created using this program.
'''
import media
import dynamic_page_genarator

Angry_Birds_Movie = media.Movie("The Angry Birds Movie",
                                "angry-birds-movie-poster.jpg",
                                "https://www.youtube.com/watch?v=1U2DKKqxHgE",
                                "Voice of birds by Jason Sudeikis, Josh Gad",
                                "Release date- 5/20/2016")
M_Impssble_5 = media.Movie("Mission Impossible 5",
                           "mission-impossible-5.jpg",
                           "https://www.youtube.com/watch?v=pXwaKB7YOjw",
                           "Star cast: Tom Cruise, Rebecca Ferguson",
                           "Release date- 7/31/2016")
Kfu_Panda_3 = media.Movie("Kungfu Panda 3",
                          "kung-fu-panda-3.jpg",
                          "https://www.youtube.com/watch?v=UgBWSPD6MUU",
                          "Voice by Bryan Cranston, Jack Black, J.K. Simmons",
                          "Release date 1/29/2016")
The_Good_Dinosaur = media.Movie("The Good Dinosaur",
                                "the-good-dinosaur-poster.jpg",
                                "https://www.youtube.com/watch?v=Dbgqz2WU0_s",
                                "Voice by Raymond Ochoa, Sam elliot",
                                " Release date 1/29/2016")
The_God_Father = media.Movie("The God Father",
                             "the-godfather.jpg",
                             "https://www.youtube.com/watch?v=sY1S34973zA",
                             "Star cast: Marlon Branda, Al Pacino",
                             "Release date 3/15/1972")
Maze_Runner2 = media.Movie("Maze Runner: The Scorch Trials",
                           "maze-runner-2.jpg",
                           "https://www.youtube.com/watch?v=-44_igsZtgU",
                           "Star cast:Dylan O'Brien, Kaya Scodelario",
                           "Release date 9/18/2015")
# Creating array movie with all the movie class elements
movies = [Angry_Birds_Movie, M_Impssble_5, Kfu_Panda_3,
          The_Good_Dinosaur, The_God_Father, Maze_Runner2]
dynamic_page_genarator.open_movies_page(movies)
