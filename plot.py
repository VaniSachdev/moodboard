from matplotlib.pyplot import title
import plotly.graph_objects as go
import numpy as np 

from analysis import song_df

def plot_graph():
    print ("hi")
    song_df['complete']  = song_df['title'] + "<br>" + song_df['artists']

    title_col = ((np.asarray(song_df['complete'])).reshape(7,7))
    valence_col = ((np.asarray(song_df['valence'])).reshape(7,7))


    fig = go.Figure(data=go.Heatmap(
                        z= valence_col,
                        text=title_col,
                        colorscale = "YlGn_r", 
                        showlegend = False,
                        hovertemplate = '%{text}<extra></extra>'
                        ))

    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.update_traces(showscale=False)

    fig.write_html('templates/moodboard.html', auto_open=False)
