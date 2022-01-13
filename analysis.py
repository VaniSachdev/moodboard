import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from wrapper import get_track_ids, pre_df

#static variables 
SPOTIPY_CLIENT_ID = 'SPOTIFY_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'SPOTIFY_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'REDIRECT_URI'
SCOPE = "user-read-recently-played"
DF_COLUMNS  = ["title", "artists", "valence", "spotify url", "album_cover url", "yrows", "xcols"]

#spotipy object 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, 
                                               client_secret=SPOTIPY_CLIENT_SECRET, 
                                               redirect_uri=SPOTIPY_REDIRECT_URI, 
                                               scope=SCOPE))


#use spotipy to find ids for top 30 songs 
top_tracks = sp.current_user_recently_played(limit = 49, after=None, before=None)
# top_tracks = sp.current_user_top_tracks(limit = 50, offset  = 0, time_range="medium_term")
track_items = top_tracks['items']



#get list of all ids 
all_ids = get_track_ids(track_items)




#metadata for all songs 
song_data = pre_df(sp, all_ids)



#panda times 
song_df = pd.DataFrame(song_data, columns = DF_COLUMNS)
# print(song_df[['title', 'valence']])

#find max, min, and average valencey !!!
# min_valence =  song_df.loc[song_df['valence'].idxmin()]
# max_valence =  song_df.loc[song_df['valence'].idxmax()]
# average_valence = round(song_df['valence'].mean(), 2)





