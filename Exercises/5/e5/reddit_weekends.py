import pandas as pd
import numpy as np
import datetime
import stats

counts = pd.read_json(sys.argv[1], lines=True)
updated_counts = pd.DataFrame()

def fun(row):
    if(not(row['date'] > datetime.date(2011, 12, 1) and row['date'] < datetime.date(2014, 1, 1) and row['subreddit'] == 'canada')):
        updated_counts.append(row)

# print(counts[counts['date'] > np.datetime64("2011-12-31") & counts['date'] < datetime.datetime("2014-1-1")])
print(counts.apply(lambda x: fun(x), axis=1))
# counts['date'] = counts['date'].astype(datetime.datetime)
print(updated_counts)