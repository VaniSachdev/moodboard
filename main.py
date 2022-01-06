import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time
import gspread

# from wrapper import get_track_items


#static variables 
SPOTIPY_CLIENT_ID = '9f2aa702ed634cf2947e19f0cbdf17c7'
SPOTIPY_CLIENT_SECRET = '0e98d396bd3a4ebdb3d96a23905cea99'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:5000'
SCOPE = "user-top-read"
DF_COLUMNS  = ["title", "artists", "valence", "spotify url", "album_cover url"]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, 
                                               client_secret=SPOTIPY_CLIENT_SECRET, 
                                               redirect_uri=SPOTIPY_REDIRECT_URI, 
                                               scope=SCOPE))


def get_track_ids(track_dictionary):
    id_list = []
    for song in track_dictionary:
        id_list.append(song['id'])

    return id_list

def metadata(track_id):
    feature_dict = sp.audio_features(track_id)[0]
    valence = feature_dict['valence']
    song_md = sp.track(track_id)
    title = song_md['name']
    artists = song_md['artists'][0]['name']
    url = song_md['external_urls']['spotify']
    album_cover =  song_md['album']['images'][0]['url']

    return [title, artists, valence, url, album_cover]



#top_tracks = dictionary
top_tracks = sp.current_user_top_tracks(limit = 10, offset  = 0, time_range="short_term")
track_items = top_tracks['items']

all_ids = get_track_ids(track_items)

song_data = []
# song_data.append(DF_COLUMNS)

for song in all_ids:
    song_data.append(metadata(song))

#df 

song_df = pd.DataFrame(song_data, columns = DF_COLUMNS)
print (song_df[["title", "artists", "valence"]])
