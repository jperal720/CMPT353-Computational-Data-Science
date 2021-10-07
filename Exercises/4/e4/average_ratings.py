import pandas as pd
import numpy as np
import difflib
import re

movie_list = pd.read_csv('movie_list.txt', names=['Movies'], delimiter="\n")
movie_ratings_raw = pd.read_csv('movie_ratings.csv')

movie_list = movie_list.set_index('Movies')
movie_list['Num. of ratings'] = 'NaN'
movie_list['Sum of ratings'] = 'NaN'

# print(movie_list)
print(movie_list.loc['A Time to Kill'])