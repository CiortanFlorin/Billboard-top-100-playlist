import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = int(date.split("-")[0])

uri_list  = []
URL = f"https://www.billboard.com/charts/hot-100/{date}?rank=1"

response = requests.get(URL)
syte_html = response.text

soup = BeautifulSoup(syte_html, "html.parser")
songs = [element.getText() for element in soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")]


client_id = "YOUR CLIENT ID"
client_secret = "YOUR CLIENT SECRET"
redirect_uri = "http://example.com"
spoty = SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri=redirect_uri,
    client_id=client_id,
    client_secret=client_secret,
    show_dialog=True,
    cache_path='token.txt')
sp = spotipy.Spotify(auth_manager=spoty)

for n in songs:
    results = sp.search(q=f"track:{n} year:{year}", type='track')
    try:
         uri = results['tracks']['items'][0]['uri']
         uri_list.append(uri)
    except IndexError:
        print(f"{n} not on spotify")


playlist_name = f"{date} Bilboard 100"
user = sp.current_user()['id']
playlist = sp.user_playlist_create(user=user, name=playlist_name, public=False)


sp.playlist_add_items(playlist_id=playlist['id'], items=uri_list)
print(playlist)
