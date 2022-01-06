import spotipy
from spotipy.oauth2 import SpotifyOAuth

#gets list of tracks (necessary for a lot of spotipy data analysis)
def get_track_ids(track_dictionary):
    id_list = []
    for song in track_dictionary:
        id_list.append(song['id'])

    return id_list

#extracts metadata + audio features (valence) using track-ids
def metadata(sp, track_id):
    feature_dict = sp.audio_features(track_id)[0]
    valence = feature_dict['valence']
    song_md = sp.track(track_id)
    title = song_md['name']
    artists = song_md['artists'][0]['name']
    url = song_md['external_urls']['spotify']
    album_cover =  song_md['album']['images'][0]['url']

    return [title, artists, valence, url, album_cover]

#metadata (list_of_ids = list of track ids)
def pre_df(sp, list_of_ids):
    song_data = []

    for song in list_of_ids:
        song_data.append(metadata(sp, song))

    return song_data