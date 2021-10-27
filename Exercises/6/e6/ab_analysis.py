import pandas as pd
from scipy import stats
import numpy as np

searches = pd.read_json('searches.json', orient='records', lines=True)


global search_count
search_count = 0

def count(row):
    global search_count
    if(row['search_count'] > 0):
        row['search_count'] = 'searched at least once'
        search_count = search_count + 1
    else:
        row['search_count'] = 'not searched'

    if(row['uid'] % 2 == 0):
        row['uid'] = 'even'
    else:
        row['uid'] = 'odd'

    return row

searches = searches.apply(lambda x: count(x), axis=1)

did_not_search_count = len(searches) - search_count
print('Users that used search:', search_count, '\nUsers that did not use search:', did_not_search_count)

contingency = []
chi2, p, dof, expected = stats.chi2_contingency(contingency )
print(p)
print(expected)

print(searches)
