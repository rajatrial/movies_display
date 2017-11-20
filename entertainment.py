import media
import fresh_tomatoes as ft
def main():
	#Define instances of type movie for three movies
	toy_story = media.Movie("Toy Story","Story of a boy",
		"https://resizing.flixster.com/OD2Yrbt-xldV7SH2i90XkjcNUoY=/206x305/v1.bTsxMTIwNzIwNztqOzE3NTg5OzEyMDA7MjE5MDsyOTIw",
		"https://www.youtube.com/watch?v=KYz2wyBy3kc")
	rounders = media.Movie("Rounders","Man plays poker and has an up and down ride",
		"https://images-na.ssl-images-amazon.com/images/I/51HC0HRKYJL.jpg",
		"https://www.youtube.com/watch?v=-Qv4K-4-FZM")
	home_alone = media.Movie("Home Alone",
		"Story of a boy","https://resizing.flixster.com/aOlnRywehj7SnyZzUn6MnsswmG4=/300x300/v1.bjsyMjM0MTA7ajsxNzUwNzsxMjAwOzMyODs0Mzc",
		"https://www.youtube.com/watch?v=CK2Btk6Ybm0")
	# Define an array movies and append all three instances
	movies=[]
	movies.append(toy_story)
	movies.append(rounders)
	movies.append(home_alone)
	# Use fresh_tomatoes to open the movie pages
	ft.open_movies_page(movies)

if __name__ == "__main__":
	main()