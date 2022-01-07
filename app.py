from flask import Flask, request, url_for, session, redirect 
from analysis import SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
# app.secret_key = "bruhidkforrn"
# app.config['SESSION_COOKIE_NAME'] = 'Vanis Cookie'

@app.route('/')
def login():
    pass

def button():
    spot_oauth = create_spotify_oauth()
    auth_url = spot_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect_page():
    return 'redirect'

def create_spotify_oauth():
    return SpotifyOAuth(
            client_id= SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=url_for('redirect_page', _external=True),
            scope="user-library-read") 