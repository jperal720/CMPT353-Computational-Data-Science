from matplotlib import pyplot as plt
import statsmodels.nonparametric.smoothers_lowess as lowess
import pandas as pd
import numpy as np
import sys

dataset_location = 'sysinfo.csv'

cpu_data = pd.read_csv(dataset_location)

# filtered = lowess(cpu_data['timestamp'], cpu_data['temperature'], frac=0.05)

cpu_data['timestamp'] = cpu_data['timestamp'].map(lambda x: x.replace('-','').replace(':', ''))
cpu_data['temperature'] = cpu_data['temperature'].astype(float)
cpu_data['timestamp'] = pd.to_datetime(cpu_data['timestamp'], format='%Y%m%d %H:%M:%S')

# pd.set_option("display.max_rows", 4501, "display.max_columns", 1)
pd.set_option('display.width', 2000)

print(cpu_data)
print(cpu_data['timestamp'][2])



plt.figure(figsize=(12, 4))
plt.plot(cpu_data['timestamp'], cpu_data['temperature'], 'b.', alpha=0.5)
plt.show() # maybe easier for testing
# plt.savefig('cpu.svg') # for final submission