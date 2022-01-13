## About

Moodboard is inspired by the heat-wave style maps Github uses to visualize a user's commits. It is a Flask application that uses the Spotify API and extracts metadata from a user's current music history to visualize their current mood. Specifically, I graphed the valence, which is audio feature data that measures how happy/sad a song is. (By design, this metric is quite subjective, but I thought it would be fun to visualize how a user's mood changes (or at least their song-choice) over time.)

Please note that since this project's design is not intended for production,I can't really host it on the web without explicitly giving every account explicit permission on Spotify's developer website. (Thus the (now disconnected) heroku deplpoyment history under the environment section) I didn't realize that till later, so here's a demo that shows my inital ✨vision✨: https://vanisachdev.github.io/moodboard-demo/. You can run it locally though! 

## Requirements

**Locally** 
1. In your terminal run. `> pip install -r requirements.txt`
2. Go to your [Spotify Dashboard](https://developer.spotify.com/dashboard/) & create a new project.
3. Copy/paste the Client ID + Secret ID into analysis.py.
4. Add your desired redirect URI (any link will do) to both the URI section of your Spotify project & to analysis.py. 
5.  Run your flask application by typing in  `flask run` in the terminal & view your results!

