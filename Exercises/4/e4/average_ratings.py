import pandas as pd
import numpy as np
import difflib
import re

movie_list = pd.read_csv('movie_list.txt', names=['movies'], delimiter="\n")
movie_ratings_raw = pd.read_csv('movie_ratings.csv')

movie_ratings_raw['title'] = movie_ratings_raw.apply(lambda x: difflib.get_close_matches(x['title'], movie_list['movies'], n=1), axis=1)
print(movie_ratings_raw['title'][3] == [])
movie_ratings_raw.drop(movie_ratings_raw[movie_ratings_raw['title'].astype(bool) != True].index, inplace=True)

# movie_ratings_raw['num_of_ratings'] = 1
movie_ratings_raw['rating'] = movie_ratings_raw['rating'].astype(int)
movie_ratings_raw['title'] = movie_ratings_raw['title'].astype(str)

print(movie_ratings_raw.groupby(['title']).agg(
    {'rating': ['mean']}
).reset_index().round(2))

