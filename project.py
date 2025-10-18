# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# start coding here
# Filter movies only, and only from the 1990s 
filter1 = (   (netflix_df["type"] == "Movie") &  
             (netflix_df["release_year"] >= 1990) & 
             (netflix_df["release_year"] < 2000)
         )
netflix_1990s = netflix_df.loc[filter1] # salvando as row,column que se encaixem no filtro
print(netflix_1990s)


# extractin duration
plt.hist(netflix_1990s['duration'])
duration = int( netflix_1990s['duration'].mode() ) 
print("most frequent movie duration in the 1990s: ",duration) 
# deixar em INT para nao ficar numero quebrado.
# se usar o .mean()[0] ele pega o primeiro valor .mode() → pega o valor mais comum. 
# .mean() pega a media.


# A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s
short_movie_count = 0
for label, row in netflix_1990s.iterrows():
    if (row["genre"] == "Action") and (row["duration"] < 90):
        short_movie_count = short_movie_count + 1
print("short action movies released in the 1990s w/ less than 90min: ", short_movie_count)
