import pandas as pd
import numpy as np
import math as m

totals = pd.read_csv('/Users/jonathanperalgort/Documents/CMPT353-Computational-Data-Science/Exercises/1/e1/totals.csv').set_index(keys=['name'])


counts = pd.read_csv('/Users/jonathanperalgort/Documents/CMPT353-Computational-Data-Science/Exercises/1/e1/counts.csv').set_index(keys=['name'])

totals

counts

sum_of_precipitations = pd.DataFrame.sum(totals, axis=1)
sum_of_precipitations


pd.Series.argmin(sum_of_precipitations) #Shows the location with the minimum total precipitation


totals/counts #Shows the average precipitations per month in each location`

sum_of_counts = pd.DataFrame.sum(counts, axis=1)

sum_of_counts

#Daily average of precipitations
sum_of_precipitations/sum_of_counts