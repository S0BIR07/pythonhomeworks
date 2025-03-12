import json
import requests
from random import randint
url = "https://api.themoviedb.org/3/genre/movie/list"
params = {
    "api_key": "361d3262a6908875a49a2d5a1fa42004"
}
response = requests.get(url, params=params)

# GET movie genres from response:

if response.status_code == 200:
    genres = response.json()["genres"]
else: 
    raise Exception(response.status_code)

# create a new dictionary of genre names as keys and ids as values
genres_dict = {genre["name"].lower():genre["id"] for genre in genres}

get_genre = input("Enter a genre: ").lower()
if get_genre not in genres_dict.keys():
    get_genre = input("Genre not found!Enter again: ")
if get_genre not in genres_dict.keys():
    raise ValueError("Movie genre not found!")
# get ID of movie genre to pull request
id = genres_dict[get_genre]

# Base url to get movies according to genre
Base_url = "https://api.themoviedb.org/3/discover/movie"
parameters = {
    "api_key": "361d3262a6908875a49a2d5a1fa42004",
    "with_genre": id,
    "sort_by": "popularity.desc"
}
# ----------
# PULL GET REQUEST for movies of chosen genre
data = requests.get(Base_url, params=parameters)

# get the list of movie names from the data
movie_names = [values["original_title"] for values in data.json()["results"]]
rand = randint(0,len(movie_names)-1)

print(movie_names[rand])