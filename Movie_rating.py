class MovieReview :
    
    
    def __init__(self, movie , story  ,actors , music):
            self.movie_name = movie

            self.story_rating = story
            self.actors_rating = actors
            self.music_rating = music

            self.avg = int((self.story_rating + self.actors_rating + self.music_rating)/3)

            self.myrating = {
                  "Movie Name" : self.movie_name,
                  "Story Rating" : self.story_rating,
                  "Actor Rating" : self.actors_rating,
                  "Music Rating" : self.music_rating,
                  "AvgRating" : self.avg,
            }
            review2 = MovieReview("Beautiful Sound", 5, 5 , 5)
            movie_list.append(self.myrating)

moviereviews = []

def avg_star_rating(self, movie_list):
     for movie in movie_list:
         if(movie["Avg Rating"] == 1 ):
             print("Thanks for the response, You rated movie with  *")  
             print(movie)

         elif(movie["Avg Rating"] == 2):
              review2 = MovieReview("Beautiful Sound", 5, 5, 5)
              review2.add_movie_ratings(moviereviews)
              review2.avg_star_ratings(moviereviews) 
   
    