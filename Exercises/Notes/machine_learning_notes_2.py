from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt

#Creating Linear Regression Model
model = LinearRegression(fit_intercept=False)

#Training Data
x = [15, 2, -19, 5]
y = [2, 3, 4, 3]

X = np.stack([x], axis=1)
y = np.stack([y], axis=1)

#Setting up the intercept manually
X_with = np.concatenate([np.ones(X.shape), X], axis=1)
# print(X_with, '\n')

model.fit(X_with, y)
# print(model.coef_)

#Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=3, include_bias=True)

y = [23, 32, 455]
X_poly = np.array([[2], [3], [4]])

poly.fit_transform(X)

model = LinearRegression(fit_intercept=False)
model.fit(X_poly, y)

print(model.coef_)