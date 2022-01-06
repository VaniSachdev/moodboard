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

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, 
                                               client_secret=SPOTIPY_CLIENT_SECRET, 
                                               redirect_uri=SPOTIPY_REDIRECT_URI, 
                                               scope=SCOPE))


def get_track_items(track_dictionary):
    item_list = []
    for song in track_dictionary:
        item_list.append(song['id'])

    return item_list


#top_tracks = dictionary
top_tracks = sp.current_user_top_artists(limit = 10, offset  = 0, time_range="short_term")
track_items = top_tracks['items']


all_items = get_track_items(track_items)
all_items_first = all_items[0]

print (all_items)

