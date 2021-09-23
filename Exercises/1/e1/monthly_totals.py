import pandas as pd
import numpy as np
import math as m

data = pd.read_csv('/Users/jonathanperalgort/Documents/CMPT353-Computational-Data-Science/Exercises/1/e1/precipitation.csv')

data

totals = pd.DataFrame(data['precipitation'], index=data['name'], columns=data['date'])
counts = pd.DataFrame(data['precipitation'], index=data['name'], columns=data['date'])

totals = totals.groupby(totals.index, axis=0).sum()

totals

def date_to_month(d):
    # You may need to modify this function, depending on your data types.
    return '%04i-%02i' % (d.year, d.month)