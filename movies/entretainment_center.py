import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
fight_club = media.Movie("Figth Club",
                         "A man that found the Fight Club",
                         "http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")
#avatar.show_trailer()
#fight_club.show_trailer()
avengers = media.Movie("Avengers",
                       "Super Hero save the wolrd",
                       "http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")
insidious = media.Movie("Insidious",
                        "Horror film of bad guy",
                        "http://upload.wikimedia.org/wikipedia/en/2/2d/Insidious_poster.jpg",
                        "https://www.youtube.com/watch?v=zuZnRUcoWos")
saw = media.Movie("Saw",
                  "Games of death",
                  "http://upload.wikimedia.org/wikipedia/en/5/56/Saw_official_poster.jpg",
                  "https://www.youtube.com/watch?v=S-1QgOMQ-ls")

movies = [toy_story, avatar, fight_club, avengers, insidious, saw]
#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print("Doc")
print(media.Movie.__doc__)
print("Dict")
print(media.Movie.__dict__)
print("Name")
print(media.Movie.__name__)
print("Bases")
print(media.Movie.__bases__)
print("Module")
print(media.Movie.__module__)


		
			
			
				
		







