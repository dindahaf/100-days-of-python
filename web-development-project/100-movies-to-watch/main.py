import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movie_titles =[title.getText() for title in movies]
movie_titles.reverse()
    
with open("movies.txt", "w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

print("DONE")