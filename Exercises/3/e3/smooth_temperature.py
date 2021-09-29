from matplotlib import pyplot as plt
import statsmodels.nonparametric.smoothers_lowess as lowess
import pandas as pd
import numpy as np
import sys

dataset_location = 'sysinfo.csv'
cpu_data = pd.read_csv(dataset_location, sep=' ', header=None,
                       names=['timestamp', 'temperature', 'sys_load_1', 'cpu_percentage', 'cpu_frequency', 'fan_rpm'])

### LOWESS function, must input list of measurements (independent values),
### the input_range (dependent/calculated values), and frac (size of "local neighborhood")

# filtered = lowess(measurements, input_range, frac=0.05)

plt.figure(figsize=(12, 4))
plt.plot(cpu_data['timestamp'], cpu_data['temperature'], 'b.', alpha=0.5)
plt.show() # maybe easier for testing
# plt.savefig('cpu.svg') # for final submission