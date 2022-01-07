import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 


from analysis import song_df

song_df_complete = song_df
name_col = ((np.asarray(song_df_complete['title'])).reshape(10,5))
valence_col = ((np.asarray(song_df_complete['valence'])).reshape(10,5))

pivot_table = song_df_complete.pivot(index="yrows", columns="xcols", values = "valence")

labels = (np.asarray(["{0} \n".format(title) 
for title in zip(name_col.flatten())])).reshape(10,5)

fig, ax = plt.subplots(figsize = (10,4))

ax.set_xticks([])
ax.set_yticks([])

ax.axis('off')

sns.heatmap(pivot_table,fmt = "", cmap="YlGn", linewidths = 7, ax = ax )
plt.show() 