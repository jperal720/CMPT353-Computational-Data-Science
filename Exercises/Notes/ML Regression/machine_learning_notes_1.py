from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt

model = LinearRegression(fit_intercept=True)

#Training Data
x = [15, 2, -19, 5]
y = [2, 3, 4, 3]

X = np.stack([x], axis=1)
y = np.stack([y], axis=1)

#Fitting training data to model
model.fit(X, y)

#Predicting output, given X_fit to the trained model
X_fit = [[15], [-19]]
y_fit = model.predict(X_fit)

#Will print close to [2] and [4] since the values used to train the model
#showed that an ouput of 2 and 4, corresponded to an input of 15 and -19, respectively.
print(y_fit)

#Plotting data
plt.plot(x, y, 'b.')
plt.plot(X_fit, y_fit, 'g.', markersize=25)
plt.plot(x, model.predict(X), 'r-')
plt.legend(['training data', 'specfici predictions from previous slide', 'predicted line'])

plt.show()