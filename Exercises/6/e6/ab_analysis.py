import pandas as pd
import statsmodels
import numpy as np

searches = pd.read_json('searches.json', orient='records', lines=True)

print(searches)