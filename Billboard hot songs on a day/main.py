from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=url)
site_content = response.text
soup = BeautifulSoup(site_content, "html.parser")

song_names = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
song_list = [song.getText().strip() for song in song_names]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
year = date.split("-")[0]
song_uris = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)