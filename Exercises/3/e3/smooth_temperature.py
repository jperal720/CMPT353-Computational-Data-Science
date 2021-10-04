from matplotlib import pyplot as plt
import statsmodels.nonparametric.smoothers_lowess as lowess
import pandas as pd
import numpy as np
import sys

dataset_location = 'sysinfo.csv'
# cpu_data = pd.read_csv(dataset_location, sep=' ', header=None, index_col=0,
#                        names=['timestamp', 'temperature', 'sys_load_1', 'cpu_percentage', 'cpu_frequency', 'fan_rpm'])

cpu_data = pd.read_csv(dataset_location)

### LOWESS function, must input list of measurements (independent values),
### the input_range (dependent/calculated values), and frac (size of "local neighborhood")

# filtered = lowess(cpu_data['timestamp'], cpu_data['temperature'], frac=0.05)

cpu_data['timestamp'] = cpu_data['timestamp'].map(lambda x: x.replace('-','').replace(':', '').replace(' ', '').replace('.', ''))
cpu_data['timestamp'] = pd.to_datetime(cpu_data['timestamp'], format='%Y%m%d %H:%M:%S')
# cpu_data['timestamp'] = pd.to_datetime(cpu_data['timestamp'], format='%d%m%Y')

# pd.set_option("display.max_rows", 4501, "display.max_columns", 1)
pd.set_option('display.width', 2000)
print(cpu_data)
print(cpu_data['timestamp'][2])

plt.figure(figsize=(12, 4))
# plt.plot(cpu_data['temperature'], input_range, 'b.', alpha=0.5)
# plt.show() # maybe easier for testing
# plt.savefig('cpu.svg') # for final submission