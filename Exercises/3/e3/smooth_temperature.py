from matplotlib import pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
import pandas as pd
import numpy as np
import sys

dataset_location = 'sysinfo.csv'

cpu_data = pd.read_csv(dataset_location)

cpu_data['timestamp'] = cpu_data['timestamp'].map(lambda x: x.replace('-','').replace(':', ''))
cpu_data['temperature'] = cpu_data['temperature'].astype(float)
cpu_data['timestamp'] = pd.to_datetime(cpu_data['timestamp'], format='%Y%m%d %H:%M:%S')

pd.set_option('display.width', 2000)

loess_smoothed = lowess(cpu_data['temperature'], cpu_data['timestamp'], frac=0.015) #LOWESS function

#Kalman Smoothing

kalman_data = cpu_data[['temperature', 'cpu_percent', 'sys_load_1', 'fan_rpm']]
print(kalman_data)




plt.figure(figsize=(12, 4))
plt.plot(cpu_data['timestamp'], cpu_data['temperature'], 'b.', alpha=0.5)
plt.plot(cpu_data['timestamp'], loess_smoothed[:, 1], 'r-')
# plt.show() # maybe easier for testing
plt.savefig('cpu.svg') # for final submission