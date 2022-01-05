from flask import Flask, request, url_for, session, redirect 
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.secret_key = "bruhidkforrn"
app.config['SESSION_COOKIE_NAME'] = 'Vanis Cookie'

@app.route('/')
def login():
    spot_oauth = create_spotify_oauth()
    auth_url = spot_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect_page():
    return 'redirect'

@app.route('/getTracks')
def getTracks():
    return 'tracks! '


def create_spotify_oauth():
    return SpotifyOAuth(
            client_id="9f2aa702ed634cf2947e19f0cbdf17c7",
            client_secret="0e98d396bd3a4ebdb3d96a23905cea99",
            redirect_uri=url_for('redirect_page', _external=True),
            scope="user-library-read")