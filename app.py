from flask import Flask, request, url_for, session, redirect, render_template
from matplotlib.pyplot import plot
from analysis import SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID
from spotipy.oauth2 import SpotifyOAuth
from plot import plot_graph 

app = Flask(__name__)
# app.secret_key = "bruhidkforrn"
# app.config['SESSION_COOKIE_NAME'] = 'Vanis Cookie'

@app.route('/')
def login():
    picture_link = "/static/media/moodboard.png"
    spot_oauth = create_spotify_oauth()
    auth_url = spot_oauth.get_authorize_url()
    return render_template("login.html", picture_link = picture_link, auth_url = auth_url)


@app.route('/redirect')
def redirect_page():
    plot_graph() 
    return render_template("explain.html")

@app.route('/moodboard')
def moodboard():
    return render_template("moodboard.html")

def create_spotify_oauth():
    return SpotifyOAuth(
            client_id= SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=url_for('redirect_page', _external=True),
            scope="user-library-read") 
