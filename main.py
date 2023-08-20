import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
website_html = response.text
soup = BeautifulSoup(website_html, "lxml")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("./movies.txt", mode="w",encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

all_movies_description = soup.select(selector="div.descriptionWrapper")


movies_description = [movie.getText() for movie in all_movies_description]
print(movies_description)
movies_descriptions = movies_description[::-1]

with open("./MoviesDesc.txt", mode="w",encoding="utf-8") as file:
    for movie in movies_descriptions:
        file.write(f"{movie}\n")