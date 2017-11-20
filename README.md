# Overview
This package opens a website containing three movies. Each associated movie has an image, and links to a youtube trailer video.

# Usage 

The main program is entertainment.py. The only dependencies are *media.py* and *fresh_tomatoes.py*. This version runs on python 2.7.

# Modification

If you want to add your own movies do the following:
Declare a new Movie `new_movie` as follows : 
`new_movie = media.Movie("name","description","Image Link","Youtube Link")`
Add to the array movies with `movies.append(new_movie)`