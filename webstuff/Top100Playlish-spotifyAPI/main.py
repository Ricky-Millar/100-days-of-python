from datetime import datetime
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

artist_list = []
song_list = []
CLIENT_ID = '4bca5421bcad44e1b7f4c60f41d09dcb'
CLIENT_PASS = 'a00c979835fe41fcaed044d8a9569e89'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_PASS,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

def get_date():
    global year_raw
    format_date = "%Y-%m-%d"
    year_raw = input('what year you would like to travel to in YYYY-MM-DD')
    try:
        datetime.strptime(year_raw, format_date)
        print("This is the correct date string format.")
        return f'https://www.billboard.com/charts/hot-100/{year_raw}'
    except ValueError:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        get_date()


top100_url = get_date()
year = int(year_raw.split("-")[0])
yearmin = year - 5
yearmax = year + 1


print(top100_url)
response = requests.get(top100_url)
top100_html_raw = response.text
soup = BeautifulSoup(top100_html_raw, "html.parser")

artist_list = soup.find_all(name= "span", class_="chart-element__information__artist text--truncate color--secondary")
song_list = soup.find_all(name= "span", class_="chart-element__information__song text--truncate color--primary")

artist_list = [artist.getText() for artist in artist_list]
song_list = [song.getText() for song in song_list]

print(artist_list)
print(song_list)
uri_list = []
for i in range(len(artist_list)):
    try:
        query = f"track:{song_list[i]} year:{yearmin}-{yearmax}"     #%20artist:{artist_list[i]}
        result=sp.search(query, limit=1, type='track')
        uri = result["tracks"]["items"][0]['id']
        uri_list.append(uri)
    except :
        print("poopsie")


playlist = sp.user_playlist_create(user=user_id, name=f"{year_raw} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)


#example     query="track:gold%20artist:abba              then maybe->   %20year:1980-2020"

