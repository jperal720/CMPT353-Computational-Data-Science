from matplotlib import pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
import pandas as pd
import numpy as np
from pykalman import KalmanFilter
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

initial_state = kalman_data.iloc[0]
observation_covariance = np.diag([0.5, 0.25, 0.5, 0.25]) ** 2 # TODO: shouldn't be zero
transition_covariance = np.diag([0.2, 0.1, 0.2, 0.2]) ** 2 # TODO: shouldn't be zero
transition = [[0.97,0.5,0.2,-0.001], [0.1,0.4,2.2,0], [0,0,0.95,0], [0,0,0,1]] # TODO: shouldn't (all) be zero

kf = KalmanFilter(
    initial_state_mean=initial_state,
    initial_state_covariance=observation_covariance,
    observation_covariance=observation_covariance,
    transition_covariance=transition_covariance,
    transition_matrices=transition
)
pred_state, state_cov = kf.smooth(kalman_data)

print(transition)



plt.figure(figsize=(12, 4))
plt.plot(cpu_data['timestamp'], cpu_data['temperature'], 'b.', alpha=0.5)
plt.plot(cpu_data['timestamp'], loess_smoothed[:, 1], 'r-')
plt.plot(cpu_data['timestamp'], pred_state[:, 0], 'r-')
plt.show() # maybe easier for testing
# plt.savefig('cpu.svg') # for final submission