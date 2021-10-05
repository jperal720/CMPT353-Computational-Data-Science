from matplotlib import pyplot as plt
import pykalman as pyk
import pandas as pd
import numpy as np

n_samples = 25

input_range = np.linspace(0, 2 * np.pi, n_samples, dtype=np.float64)

observations = pd.DataFrame()
observations['sin'] = (np.sin(input_range)) + np.random.normal(0, 0.5, n_samples)
observations['cos'] = (np.cos(input_range)) + np.random.normal(0, 0.25, n_samples)

#Plotting
plt.figure(figsize=(12, 4))
plt.plot(input_range, observations['sin'], 'b.', alpha=0.5)
plt.show()