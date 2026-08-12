import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic


URL = "https://appbrewery.github.io/bakeboard-hot-100/"


date =input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
response = requests.get(url=f"{URL}{date}")
response.raise_for_status()
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
song_names = [tag.getText().strip() for tag in soup.select("h3.chart-entry__title")]

yt = YTMusic("browser.json")

playlist_id = None
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

for p in playlists:
    if p["title"] == f"{date} Billboard 100":
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print(f"Playlist for {date} already exists with ID: {playlist_id}")

else:
    playlist_id = yt.create_playlist(
        f"{date} Billboard 100",
        f"Top 100 songs from {date} according to Billboard",
        "PRIVATE"
    )
    print("Playlist created.")

for song in song_names:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Error occurred while adding {song}: {e}")

