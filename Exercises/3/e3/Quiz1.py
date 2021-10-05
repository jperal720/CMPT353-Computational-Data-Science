import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


populations = pd.DataFrame({
    'province': ['bc', 'ab', 'sk', 'on', 'pq'],
    'population': [51, 44, 11, 14, 85],
    'region': ['W', 'W', 'W', 'C', 'C']
})

covid = pd.DataFrame({
    'province': ['bc', 'ab', 'sk', 'on', 'pq'],
    'cases': [14, 22, 4, 53, 37],
    'active': [21, 47, 11, 73, 24]
})

all_data = pd.DataFrame({})
# all_data.set_index([
#     'province',
#     'population',
#     'region',
#     'cases',
#     'active'
# ])

all_data = all_data.append(populations)
all_data = all_data.append(covid)


all_data = all_data.set_index('province')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


populations = pd.DataFrame({
    'province': ['bc', 'ab', 'sk', 'on', 'pq'],
    'population': [51, 44, 11, 14, 85],
    'region': ['W', 'W', 'W', 'C', 'C']
})

covid = pd.DataFrame({
    'province': ['bc', 'ab', 'sk', 'on', 'pq'],
    'cases': [14, 22, 4, 53, 37],
    'active': [21, 47, 11, 73, 24]
})

all_data = pd.DataFrame({})
# all_data.set_index([
#     'province',
#     'population',
#     'region',
#     'cases',
#     'active'
# ])

all_data = all_data.append(populations)
all_data = all_data.append(covid)


all_data = all_data.set_index('province')

grouped = pd.DataFrame()


print(all_data)
print(all_data)