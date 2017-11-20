import webbrowser
#Define the class that we will use
class Movie():
	#Define global variables
	VALID_RATINGS = ['G','PG','PG13','R']
	# Constructor - define title, storyline, image, and trailer
	# Image should point to an image online
	def __init__(self,title,storyline,poster_image,trailer_youtube):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)

