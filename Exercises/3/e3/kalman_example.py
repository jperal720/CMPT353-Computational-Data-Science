from matplotlib import pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
from pykalman import KalmanFilter
import pandas as pd
import numpy as np

n_samples = 25

input_range = np.linspace(0, 2 * np.pi, n_samples, dtype=np.float64)

observations = pd.DataFrame()
observations['sin'] = (np.sin(input_range)) + np.random.normal(0, 0.5, n_samples)
observations['cos'] = (np.cos(input_range)) + np.random.normal(0, 0.25, n_samples)

#LOESS Smoothing
loess_smoothed = lowess(observations['sin'], input_range, 0.4)

#Kalman Smoothing
initial_value_guess = observations.iloc[0]
observation_covariance = np.diag([0.5, 0.25]) ** 2

delta_t = 2 * np.pi / n_samples
transition_matrix = [[1, delta_t] , [-1 * delta_t, 1]]
transition_covariance = np.diag([0.2, 0.2]) ** 2


kf = KalmanFilter(
    initial_state_mean=initial_value_guess,
    initial_state_covariance=observation_covariance,
    observation_covariance=observation_covariance,
    transition_covariance=transition_covariance,
    transition_matrices=transition_matrix
)
pred_state, state_cov = kf.smooth(observations)


#Plotting
plt.figure(figsize=(12, 4))
plt.plot(input_range, observations['sin'], 'b.', alpha=0.5)
# plt.plot(input_range, loess_smoothed[:, 1], 'r-', linewidth=3)
plt.plot(input_range, pred_state[:, 0], 'r-', linewidth=3)
plt.show()